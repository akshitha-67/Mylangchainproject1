from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
import streamlit as st

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

openai_key = os.getenv("OPENAI_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")

if not openai_key:
    raise RuntimeError(
        "OPENAI_API_KEY is missing. Check the .env file in the chatbot folder."
    )

if not langchain_key:
    raise RuntimeError(
        "LANGCHAIN_API_KEY is missing. Check the .env file in the chatbot folder."
    )

os.environ["OPENAI_API_KEY"] = openai_key

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_key

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}"),
    ]
)

## streamlit framework

st.title("Meenakshi's Langchain Demo With OPENAI API")
input_text = st.text_input("Search the topic u want")

# openAI LLm
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
