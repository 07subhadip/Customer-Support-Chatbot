import os
import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

# -------------------- Setup --------------------
load_dotenv()
st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬")

st.title("💬 Customer Support Chatbot")
st.caption("Powered by LLaMA 3.1 + HuggingFace")

# -------------------- Load Model (CACHED) --------------------
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        temperature=0.5,
        max_new_tokens=512,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    return ChatHuggingFace(llm=llm)

llama = load_model()

# -------------------- Prompt Template --------------------
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a helpful gentle Customer Support Assistant ChatBot"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
    ]
)

# -------------------- Session State --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------- Display Chat --------------------
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    else:
        st.chat_message("assistant").write(msg.content)

# -------------------- User Input --------------------
query = st.chat_input("Type your message...")

if query:
    st.chat_message("user").write(query)

    prompt = chat_template.invoke(
        {
            "chat_history": st.session_state.chat_history,
            "query": query
        }
    )

    response = llama.invoke(prompt)

    st.chat_message("assistant").write(response.content)

    st.session_state.chat_history.append(HumanMessage(content=query))
    st.session_state.chat_history.append(AIMessage(content=response.content))
