import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(

    page_title="Chatbot",
    page_icon="",
    layout="centered"
)

st.title("Generative AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY"),
    temperature = 0.1
)

user_prompt = st.chat_input("Ask Anything")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})

    response = llm.invoke(
        input=[{"role":"system", "content":"You are a helpful Chatbot Assistant"}, *st.session_state.chat_history]
    )

    assistance_response = response.content

    st.session_state.chat_history.append({"role":"assistant", "content":assistance_response})

    with st.chat_message("assistant"):
        st.markdown(assistance_response)