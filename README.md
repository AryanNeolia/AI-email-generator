# AI Email Generator ✉️🤖

An AI-powered email rewriting assistant built using **FastAPI** and **OpenAI API**.  
It converts rough, informal messages into structured, professional emails with customizable tone.

---

## 🚀 Features

- Tone customization (Polite, Professional, Assertive, Friendly)
- REST API built with FastAPI
- Structured request validation using Pydantic
- Prompt-engineered responses
- Secure API key handling using environment variables

---

## 🛠 Tech Stack

- Python
- FastAPI
- OpenAI API
- Uvicorn
- Pydantic

---

## 📌 How It Works

1. User sends rough message + tone.
2. Backend validates input.
3. Dynamic prompt is generated.
4. OpenAI model rewrites message into a professional email.
5. Response returned as structured JSON.

---

## 🧪 Example Request

```json
POST /generate-email

{
  "message": "hey sir i cant send report today will send tomorrow",
  "tone": "professional"
}
