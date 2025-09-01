# 🤖 EMAM ChatBot 💬

A chatbot built with **FastAPI** + **Streamlit**, powered by **LangChain Cohere**.  
The backend (FastAPI) handles chat requests, while the frontend (Streamlit) provides a chat UI.  
Both run together from a single script using Python threading.

---

## 📂 Project Structure
```

├── main.py         # Combined FastAPI + Streamlit chatbot
├── requirements.txt
└── README.md

````

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
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API key

Create a `.env` file in the project root:

```ini
TOGETHER_API_KEY=your_api_key_here
```

⚠️ Never commit `.env` to GitHub.
On **Streamlit Cloud**, set this in **App Settings → Secrets**.

---

## ▶️ Running the Chatbot

Simply run:

```bash
streamlit run app.py
```

* FastAPI backend starts at → `http://127.0.0.1:8000/chat`
* Streamlit frontend starts in your browser

The app will launch a **chat interface** where you can talk to the Cohere-powered assistant.

---

## 🌐 Deployment

* **Streamlit Cloud** → Deploy the file directly. Use Secrets Manager for your API key.
* **Railway / Render / Heroku** → Can also run this file since it starts both backend and frontend.
* For production, consider **splitting backend & frontend** into separate services.

---

## 📜 License

This project is for learning/demo purposes.
Feel free to fork, extend, and improve!
