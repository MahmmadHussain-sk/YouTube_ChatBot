# chatbot.py
# This file is the "brain" of the RAG pipeline:
# 1. retrieve the most relevant transcript chunks from FAISS
# 2. hand those chunks + the user's question to Groq's LLM
# 3. return the LLM's answer

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# ChatGroq replaces ChatOpenAI here - same LangChain interface,
# just pointed at Groq's much faster (and free-tier) LLM hosting.
# llama-3.3-70b-versatile is a strong general-purpose model on Groq.
llm = ChatGroq(
     model="qwen-3.8-27b",
    api_key=os.getenv("GROQ_API_KEY") 
    
)

# The prompt template tells the LLM to answer ONLY from the video
# context, which keeps it from making things up (hallucinating).
prompt = ChatPromptTemplate.from_template(
    """
    You are an assistant that answers questions about a YouTube video.
    Use ONLY the transcript context below to answer the question.
    If the answer is not in the context, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """
)


def ask_question(vector_store, question):
    """
    Runs one full RAG cycle: retrieve relevant chunks, build the
    prompt, and return the LLM's answer as plain text.
    """

    # Step 1: turn the vector store into a retriever and fetch the
    # top 4 chunks that are most similar to the question
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    relevant_docs = retriever.invoke(question)

    # Step 2: combine the retrieved chunks into one context string
    context_text = "\n\n".join([doc.page_content for doc in relevant_docs])

    # Step 3: fill in the prompt template with the context and question
    final_prompt = prompt.format(context=context_text, question=question)

    # Step 4: send the finished prompt to Groq's LLM
    response = llm.invoke(final_prompt)

    return response.content
