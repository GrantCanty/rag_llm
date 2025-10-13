import streamlit as st
from pathlib import Path

from backend.llm_query import answer_user
from backend.process_document import process_documents
from backend.util import get_available_text_and_files

print(f'available text and files: {get_available_text_and_files()}')
process_documents(get_available_text_and_files())

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


p = answer_user(prompt)
print(p)