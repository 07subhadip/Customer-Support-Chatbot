# Dynamic Customer Support Chatbot

An intelligent, console-based customer support assistant powered by **Llama-3.1-8B-Instruct** (via Hugging Face). This chatbot features persistent memory, maintaining context across conversations, and uses a rich terminal interface for a polished user experience.

## 🚀 Features

- **Advanced LLM Integration**: Leverages the Meta Llama 3.1 model for high-quality, natural language responses.
- **Persistent Memory**: Conversational history is saved locally (`chat_history.txt`), allowing the bot to remember previous context even after restarting the script.
- **Rich Terminal UI**: Utilizes the `rich` library to render Markdown and formatted text directly in the console.
- **Environment Secure**: API keys are managed securely via `.env` files.

## 🛠️ Prerequisites

Before running the chatbot, ensure you have **Python 3.8+** installed. You will also need a Hugging Face Access Token.

### Required Python Packages

Install the necessary dependencies using pip:

```bash
pip install streamlit langchain-huggingface python-dotenv rich
```

_(Note: `streamlit` is imported but the current script runs primarily in the console. Ensure all imports in the script are satisfied.)_

### API Configuration

1.  Get your API token from [Hugging Face](https://huggingface.co/settings/tokens).
2.  Create a `.env` file in the same directory as the script.
3.  Add your token to the `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

## 💻 Usage

To start the chatbot, simply run the Python script:

```bash
python fll_dynamic_customer_support_chatbot.py
```

- **Interact**: Type your query at the `You :` prompt.
- **Exit**: Type `exit`, `end`, or `quit` to terminate the session.

## ⚠️ Cautions and Limitations

Please be aware of the following usage limits and design constraints:

1.  **Local File Storage**:

    - **Privacy Warning**: Conversation history is stored in plain text in `chat_history.txt` within the same directory. **Do not share this file** if your conversations contain sensitive information.
    - **Concurrency**: This script is designed for a single local user. Running multiple instances simultaneously may cause conflicts when writing to the history file.

2.  **API Rate Limits**:

    - This application uses the free Hugging Face Inference API. You may encounter rate limits or slower response times during peak usage hours.
    - **Token Limit**: The model is configured with a `max_new_tokens` limit of 2048. Extremely long responses may be truncated.

3.  **Model Hallucinations**:

    - As with all Large Language Models (LLMs), Llama 3.1 can make mistakes or "hallucinate" facts. Always verify critical information provided by the chatbot, especially for technical or financial support scenarios.

4.  **Memory Management**:
    - The `chat_history.txt` file grows indefinitely. If the file becomes too large, it may exceed the model's context window, causing errors. It is recommended to manually archive or delete `chat_history.txt` periodically to reset the context.
