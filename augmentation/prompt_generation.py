from langchain_core.prompts import PromptTemplate


def build_prompt():
    return PromptTemplate(
        template="""
          You are a helpful assistant.
          Answer ONLY from the provided transcript context.
          If the context is insufficient, just say you don't know.

          {context}
          Question: {question}
        """,
        input_variables=['context', 'question']
    )

def prepare_prompt(prompt, docs, question):
    context_text = "\n\n".join(doc.page_content for doc in docs)
    return prompt.invoke({"context": context_text, "question": question})