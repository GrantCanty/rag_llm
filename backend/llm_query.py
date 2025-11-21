from .chroma import query_similar_documents
from .util import logger
from transformers import AutoModelForCausalLM, AutoTokenizer


LLM_MODEL = "/app/qwen_model"

print("Starting tokenizer load...")
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
print("Tokenizer loaded. Starting model load...")

print("Starting model load...")
model = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    dtype="auto",
    device_map="auto"
)
print("Model loaded successfully!")

def prompt_llm(prompt: str):
    SYSTEM_PROMPT = "You are a Personal assistant specialized in providing a well formated answer from the context being provided by the user."
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': prompt}
    ]

    try:
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        # conduct text completion
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=16384
        )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

        content = tokenizer.decode(output_ids, skip_special_tokens=True)

        try:
            # rindex finding 151668 (</think>)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            index = 0

        content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

        return content
    except Exception as e:
        logger.exception(f"Error when prompting LLM: {e}")
        return "Could not process your query"

def answer_user(query: str):
    try:
        rag_response = query_similar_documents(query)
        if len(rag_response) == 0:
            return "No relevant documents for your query"

        context = "\n".join(rag_response)
        prompt = f"Context: {context}\nAnswer the user's question concisely based off of the context provided.\nQuestion: {query}"
        llm_response = prompt_llm(prompt)
        return llm_response
    except Exception as e:
        logger.exception(f"Error answering question: {e}")
        return "Could not process your query"

