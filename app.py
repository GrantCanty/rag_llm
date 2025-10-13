import streamlit as st
import time

from backend.llm_query import answer_user
from backend.process_document import process_documents
from backend.util import get_available_text_and_files

process_documents(get_available_text_and_files())


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask me about Ferrari's financial information"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


def response_generator(response: str):
    #response = f"this is a response for prompt: {prompt}"
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

with st.chat_message("assistant"):
    if prompt is not None:
        answer = answer_user(prompt)
        response = st.write_stream(response_generator(answer))
        st.session_state.messages.append({"role": "assistant", "content": response})
# Add assistant response to chat history
#st.session_state.messages.append({"role": "assistant", "content": response})
#p = answer_user(prompt)
#print(p)