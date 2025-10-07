import streamlit as st
from main import model
from langchain_core.messages import HumanMessage, AIMessage
import re

st.title("ChatBot ☁️")

#Chat history in langchain format
if "formatted_args" not in st.session_state:
    st.session_state.formatted_args = []

# Initialize chat history by streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.session_state.formatted_args.append(HumanMessage(content=prompt))

    ai_response = model.invoke(st.session_state.formatted_args)

    # Get the text content safely
    bot_reply = getattr(ai_response, "content", str(ai_response))
    # Remove any <think>...</think> sections
    bot_reply = re.sub(r"<think>.*?</think>", "", bot_reply, flags=re.DOTALL).strip()

    st.session_state.formatted_args.append(AIMessage(content=bot_reply))

    print(st.sesformatted_args)
    
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assitant", "content": bot_reply})