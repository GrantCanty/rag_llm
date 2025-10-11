import requests
from typing import List
import os
from util import logger
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2") 
model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str) -> List[float]:
    try:
        embedding = model.encode(text)
        print(embedding)
        return embedding
    except Exception as e:
        logger.error(f'error getting embeddings: {e}')
        raise ValueError('failed to get embedding')


