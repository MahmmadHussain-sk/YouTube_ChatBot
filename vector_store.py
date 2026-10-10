# vector_store.py
# This file turns raw transcript text into a searchable FAISS vector
# database. This is the "vector database" + "RAG" part of the project.

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Free, local embedding model - runs on your machine, no API key needed.
# This is what converts text chunks into numeric vectors.
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def build_vector_store(transcript_text):
    """
    Takes the full transcript text and returns a ready-to-search
    FAISS vector store built from it.
    """

    # Step 1: split the long transcript into overlapping chunks.
    # Overlap keeps sentences from being cut in half between chunks.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,     # roughly how many characters per chunk
        chunk_overlap=200    # characters shared between neighboring chunks
    )
    text_chunks = splitter.split_text(transcript_text)

    # Step 2: load the embedding model
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Step 3: embed every chunk and store the vectors inside FAISS
    vector_store = FAISS.from_texts(text_chunks, embeddings)

    return vector_store
