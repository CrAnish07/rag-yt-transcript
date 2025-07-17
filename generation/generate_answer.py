from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature=0.5,
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=pipe)
model = ChatHuggingFace(llm=llm)

def generate_answer(prompt):
    return model.invoke(prompt).content