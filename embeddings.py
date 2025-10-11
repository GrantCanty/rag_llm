import requests
from typing import List
import os
import logging
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

load_dotenv()

headers = {
    'Authorization': f'Bearer {os.getenv("HUGGINGFACE_API_KEY")}',
    'Content-Type': 'application/json'
}

logger = logging.getLogger(__name__)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/distilbert-base-nli-mean-tokens")    

def get_embedding(text: str) -> List[float]:
    try:
        embedding = model.encode(text)
        print(embedding)
        return embedding
    except Exception as e:
        logger.error(f'error getting embeddings: {e}')
        raise ValueError('failed to get embedding')

get_embedding("testing")