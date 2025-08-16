import os
import time
import uuid
import threading
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage, AIMessage
import streamlit as st
import uvicorn

# =========================
#       FASTAPI PART
# =========================

load_dotenv()
app = FastAPI()

class ChatResponse(BaseModel):
    answer: str

class ChatRequest(BaseModel):
    prombt: str
    session_id: str

llm = ChatCohere(
    cohere_api_key="ORpQXJdhHU93VMRqEAiwtXQqIXuxqTaZdcBEUxL8",
    model="command-a-03-2025"
)

chat_histories = {}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_cohere(request: ChatRequest):
    history = chat_histories.get(request.session_id, [])
    history.append(HumanMessage(content=request.prombt))
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))
    chat_histories[request.session_id] = history
    return ChatResponse(answer=response.content)

# =========================
#   STREAMLIT FRONTEND
# =========================

def run_streamlit():
    st.set_page_config(page_title="EMAM ChatBot", page_icon="💬", layout="centered")
    st.markdown("<h1 style='text-align: center;'>🤖 EMAM ChatBot</h1>", unsafe_allow_html=True)

    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is on your mind?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"prombt": prompt, "session_id": st.session_state.session_id}
                )

                if response.status_code == 200:
                    answer = response.json()["answer"]
                else:
                    answer = "❌ Error from API"
            except Exception as e:
                answer = f"⚠️ Could not connect to API: {e}"

            time.sleep(1)
            message_placeholder.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

# =========================
#  RUN BOTH TOGETHER
# =========================

def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # Run FastAPI in background
    threading.Thread(target=run_fastapi, daemon=True).start()

    # Run Streamlit in main thread
    run_streamlit()
