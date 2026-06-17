# 🌐 Multilingual Translation Web Application

A full-stack translation web application that translates Hindi text into **English, Tamil, and Bengali** using a **FastAPI backend** and a **Streamlit frontend**.

## 🚀 Features

* Translate Hindi text into:

  * English
  * Tamil
  * Bengali
* FastAPI REST API backend
* Interactive Streamlit user interface
* Character counter
* Loading spinner
* Clear button
* Error handling
* Health check endpoint
* Deployable on Render and Streamlit Community Cloud

---

## 📂 Project Structure

```text
TASK/
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── docs/
    └── README.md
```

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* Deep Translator

### Frontend

* Streamlit
* Requests

---

# ⚙️ Backend Setup

## 1. Navigate to backend

```bash
cd backend
```

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run FastAPI server

```bash
uvicorn main:app --reload --port 8000
```

Server:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# ⚙️ Frontend Setup

## 1. Navigate to frontend

```bash
cd frontend
```

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Streamlit

```bash
streamlit run app.py
```

Application:

```text
http://localhost:8501
```

---

# 📡 API Endpoints

## Health Check

### Endpoint

```http
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## Translate Text

### Endpoint

```http
POST /translate
```

### Request

```json
{
  "text": "हेलो"
}
```

### Response

```json
{
  "english": "Hello",
  "tamil": "ஹலோ",
  "bengali": "হ্যালো"
}
```

---

# ☁️ Deployment

## Backend Deployment (Render)

Create a new **Web Service**.

### Root Directory

```text
backend
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

After deployment:

```text
https://your-app-name.onrender.com
https://your-app-name.onrender.com/docs
```

---

## Frontend Deployment (Streamlit Community Cloud)

Set the backend URL inside `app.py`:

```python
FASTAPI_URL = "https://your-render-url.onrender.com"
```

Deploy the repository on Streamlit Community Cloud and set:

* Repository: Your GitHub repository
* Main file path:

```text
frontend/app.py
```

---

# 🧪 Example Usage

Input:

```text
मेरा नाम आर्यन है
```

Output:

```text
English : My name is Aryan
Tamil    : என் பெயர் ஆர்யன்
Bengali  : আমার নাম আর্যন
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* REST API development using FastAPI
* API consumption using Streamlit
* Request and response validation with Pydantic
* Frontend and backend separation
* Deployment of production-ready Python applications
* Integration of multilingual translation services

---

## 👨‍💻 Author

**Aryan Shukla**

B.Tech CSE (AI/ML) Student
Python • FastAPI • Machine Learning • RAG • AI Applications
