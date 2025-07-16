from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
    return Chroma.from_documents(chunks, embeddings)