import os
from rich.console import Console
from rich.markdown import Markdown

import streamlit as st

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# -------------------- Setup -----------------------
load_dotenv()

console = Console()

hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize the model

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    temperature = 0.5,
    max_new_tokens = 2048,
    huggingfacehub_api_token = hf_api_key
)

llama = ChatHuggingFace(
    llm = llm
) 

print("Llama Initialization completed.")

# -------------------- Model Template -----------------------

chat_template = ChatPromptTemplate(
    [
        ('system', "You're a helpful gentle Customer Support Assistent ChatBot"),
        MessagesPlaceholder(variable_name = "chat_history"),
        ("human", "{query}")
    ],
    input_variables = ["query"]
)

# -------------------- Memory -----------------------

chat_history = []

if os.path.exists("chat_history.txt"):
    with open("chat_history.txt", "r", encoding = "utf-8") as f:
        for line in f:
            chat_history.append(HumanMessage(content = line.strip()))

console.print(Markdown("""## Your Customer Support Chatbot is ready to assist you"""))
print("-" * 50)

# -------------------- Chat Loop -----------------------

while True:
    query = input("You : ")

    if query.lower() in ["exit", "end", "quit"]:
        print("Thanks for chatting. Have a good day!")
        break

    prompt = chat_template.invoke(
        {
            "chat_history" : chat_history,
            "query" : query
        }
    )
    
    result = llama.invoke(prompt)

    print("-" * 50)
    console.print(Markdown(result.content))
    print("-" * 50)

    chat_history.append(HumanMessage(content = query))
    chat_history.append(AIMessage(content = result.content))

    with open("chat_history.txt", "a", encoding = "utf-8") as f:
        f.write(f"User : {query}\nAI : {result.content}")