# 💬 AI Chatbot (Streamlit + LangChain)

An interactive conversational AI chatbot built using **Streamlit**, **LangChain**, and your preferred **LLM API (OpenAI / Groq / Gemini / etc.)**.  
The app features persistent chat history, LangChain-compatible message formatting, and automatic removal of reasoning text (`<think>` blocks) for a clean user experience.

---

## 🚀 Features
- 🔁 Persistent conversation history using `st.session_state`
- 🧠 LangChain-based message handling with `HumanMessage` and `AIMessage`
- ✨ Automatic removal of `<think>...</think>` reasoning content
- 🎨 Clean, simple chat UI powered by **Streamlit**
- ⚙️ Easily switch between different LLM providers (OpenAI, Groq, Gemini, etc.)

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Streamlit** – for the web UI  
- **LangChain** – for message structuring and LLM integration  
- **Dotenv** – for secure environment variable management  
- **Any LLM Provider API** – e.g. OpenAI GPT, Groq, Anthropic Claude, Gemini, etc.

---

## 📦 Project Structure
- ├── main.py # Contains model setup and LangChain model initialization
- ├── chatbot_ui.py # Streamlit-based chat interface
- ├── .env # Stores your API key (not committed)
- ├── requirements.txt # Python dependencies
- └── README.md # Documentation


## Create Venv
```
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Create a .env file in the root directory and paste your API KEY in .env file:
```
touch .env

GROQ_API_KEY=your_groq_api_key_here
# or
ANTHROPIC_API_KEY=your_anthropic_api_key_here

```

## Run app from streamlit:
```
streamlit run chatbot_ui.py

```
