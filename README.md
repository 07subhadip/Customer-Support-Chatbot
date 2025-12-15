# Dynamic Customer Support Chatbot

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://customer-support-chatbot-kxhkv5bmfd427xkd9zefbn.streamlit.app/)

An intelligent customer support assistant powered by **Llama-3.1-8B-Instruct** (via Hugging Face). This chatbot features persistent memory, maintaining context across conversations, and offers a clean, interactive user interface built with **Streamlit**.

## 🚀 Features

- **Advanced LLM Integration**: Leverages the Meta Llama 3.1 model for high-quality, natural language responses.
- **Interactive Web UI**: Built with Streamlit for a responsive and user-friendly chat interface.
- **Persistent Session Memory**: Maintains conversation context within the active session.
- **Environment Secure**: API keys are managed securely via `.env` files.

## 🛠️ Prerequisites

Before running the chatbot, ensure you have **Python 3.8+** installed. You will also need a Hugging Face Access Token.

### Required Python Packages

Install the necessary dependencies using pip:

```bash
pip install streamlit langchain-huggingface python-dotenv
```

### API Configuration

1.  Get your API token from [Hugging Face](https://huggingface.co/settings/tokens).
2.  Create a `.env` file in the same directory as the script.
3.  Add your token to the `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

## 💻 Usage

To start the chatbot locally, use the Streamlit CLI:

```bash
streamlit run full_dynamic_customer_support_chatbot.py
```

- **Interact**: Type your query in the chat input box.
- **Exit**: Close the browser tab to end the session.

## ⚠️ Cautions and Limitations

Please be aware of the following usage limits and design constraints:

1.  **Llama Open Source Limitations**:

    - **Inherited Constraints**: As this application is built on top of Llama 3.1, it has the same limitations as the base open-source Llama models. This includes potential bias, knowledge cutoffs, and the possibility of generating incorrect or nonsensical information (hallucinations).

2.  **API Rate Limits**:

    - This application uses the free Hugging Face Inference API. You may encounter rate limits or slower response times during peak usage hours.
    - **Token Limit**: The model is configured with a `max_new_tokens` limit. Extremely long responses may be truncated.

3.  **Data Privacy**:

    - **Session Storage**: While this demo runs in the browser, always be cautious when sharing sensitive personal information with any AI chatbot.

4.  **Memory Management**:
    - Conversation history is held in the session state. Refreshing the page will reset the conversation.
