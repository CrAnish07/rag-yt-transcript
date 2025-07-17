from config import settings
from ingestion.fetch_transcripts import get_transcripts
from ingestion.text_splitter import split_text
from ingestion.embed_store import create_vector_store
from retrieval.retriever import get_retriever
from augmentation.prompt_generation import build_prompt, prepare_prompt
from generation.generate_answer import generate_answer
from langchain_huggingface import ChatHuggingFace


if __name__ == "__main__":
    video_id = "MfU27Ub-bs4"

    transcript = get_transcripts(video_id)
    chunks = split_text(transcript)
    vector_store = create_vector_store(chunks)

    retriever = get_retriever(vector_store)
    question = "is the topic of LLM discussed in this video? if yes then what was discussed"

    docs = retriever.invoke(question)
    prompt = build_prompt()
    final_prompt = prepare_prompt(prompt, docs, question)

    answer = generate_answer(final_prompt)
    print(answer)