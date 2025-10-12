from chroma import query_similar_documents
from process_document import process_documents
from util import get_available_text_and_files
from util import logger
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv


load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
if HUGGINGFACE_API_TOKEN == None:
    raise ValueError("Missing HuggingFace API Token ")
LLM_MODEL = os.getenv("LLM_MODEL")

client = InferenceClient(model=LLM_MODEL, token=HUGGINGFACE_API_TOKEN, timeout=120)

def prompt_llm(prompt: str):
    try:
        
        SYSTEM_PROMPT = "You are a Personal assistant specialized in providing well formated answer from the context being provided."
        message = [
            {'role': 'system', 'prompt': SYSTEM_PROMPT},
            {'role': 'user',   'prompt': prompt}
        ]
        result = client.text_generation(
            message,
            temperature=0.7,
            max_new_tokens=200
        )
        text = result.choices[0].message.content
        return text
    except Exception as e:
        logger.exception(f"Error when prompting LLM: {e}")
        return "Could not process your query"


def answer_user(query: str):
    try:
        rag_response = (query_similar_documents(query))
        
        if len(rag_response) == 0:
            return "No relevant documents for your query"

        context = "\n".join(rag_response)
        prompt = f"Context: {context}\nAnswer the user's question concisely based off of the context provided.\nQuestion: {query}"
        llm_response = prompt_llm(prompt)
        return llm_response
    except Exception as e:
        logger.exception(f"Error answering question: {e}")
        return "Could not process your query"