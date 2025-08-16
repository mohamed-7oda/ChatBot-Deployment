# 🤖 EMAM ChatBot 💬

A chatbot built with **FastAPI** + **Streamlit**, powered by **LangChain Cohere**.  
The backend (FastAPI) handles chat requests, while the frontend (Streamlit) provides a chat UI.  
Both run together from a single script using Python threading.

---

## 📂 Project Structure
├── main.py # Combined FastAPI + Streamlit chatbot
├── requirements.txt
├── .gitignore
└── README.md


---

## 🚀 Features
- ✅ **FastAPI backend** with `/chat` endpoint  
- ✅ **Streamlit frontend** with modern chat UI  
- ✅ **Session-based memory** for conversations  
- ✅ **Cohere model (`command-a-03-2025`)** integrated via LangChain  
- ✅ Runs both backend & frontend in **one Python process**  

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chatbot-deployment.git
cd chatbot-deployment

pip install -r requirements.txt

TOGETHER_API_KEY=your_api_key_here

python main.py
