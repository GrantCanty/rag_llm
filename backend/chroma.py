import chromadb
import logging
from util import logger  
from embedding import get_embedding
from dotenv import load_dotenv
from util import get_available_text_files


load_dotenv()

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="docs")

def add_documents_to_vector_store(docs: list[str], ids: list[str], filename: str) -> None:
    try:
        vectors = [get_embedding(text) for text in docs]
        collection.add(
            documents=docs, 
            embeddings=vectors, 
            ids=ids,
            metadatas=[{"filename": filename} for _ in docs]
        )

    except Exception as e:
        logger.error(f"Error adding documents to vector store: {e}")
        raise ValueError(f"Failed to add documents to vector store: {e}")
    

def query_similar_documents(query: str, top_k: int = 3) -> list[str]:
    try:
        context_files = get_available_text_files()
        print(f"Context files available: {context_files}")
        if len(context_files) == 0:
            return []
        query_vector = get_embedding(query)
        results = collection.query(
            query_embeddings=[query_vector], 
            n_results=top_k,
            where={"filename": {"$in": context_files}}
        )
        return results["documents"][0]
    except Exception as e:
        logger.error(f"Error querying similar documents: {e}")
        raise ValueError(f"Failed to query similar documents: {e}")