def get_retriever(vector_store, k=2):
    return vector_store.as_retriever(search_type="mmr", search_kwargs={"k": k})