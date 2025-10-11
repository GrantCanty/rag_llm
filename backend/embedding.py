import requests
from typing import List
import os
from util import logger
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb


load_dotenv()

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="docs")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/distilbert-base-nli-mean-tokens") 
model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str) -> List[float]:
    try:
        embedding = model.encode(text)
        print(embedding)
        return embedding
    except Exception as e:
        logger.error(f'error getting embeddings: {e}')
        raise ValueError('failed to get embedding')


