# 🌐 Multilingual Translation Web Application

A full-stack web application that translates Hindi text into **English, Tamil, and Bengali** using a **FastAPI backend** and an **interactive Streamlit frontend**.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Deployed-success)

---

# 🚀 Live Demo

### 🌐 Frontend

https://hdbcqj9nrnpwk8qpzdvzkr.streamlit.app/

### ⚡ Backend API

https://svcore-ai-translation-api.onrender.com

### 📖 API Documentation (Swagger UI)

https://svcore-ai-translation-api.onrender.com/docs

---

# ✨ Features

* Translate Hindi text into:

  * English
  * Tamil
  * Bengali
* FastAPI REST API backend
* Interactive Streamlit user interface
* Real-time translation requests
* Character counter
* Loading spinner
* Clear button
* Error handling
* Modular project structure
* Render deployment support
* Streamlit Community Cloud deployment
* Responsive multi-column translation display

---

# 📂 Project Structure

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

# 🛠 Tech Stack

## Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* Deep Translator

## Frontend

* Streamlit
* Requests

---

# ⚙️ Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/Shadow-linux-png/SVCORE-AI-.git
cd SVCORE-AI-
```

---

## 2. Navigate to Backend

```bash
cd backend
```

---

## 3. Create Virtual Environment

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

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run FastAPI Server

```bash
uvicorn main:app --reload --port 8000
```

Backend runs on:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# ⚙️ Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

---

## 2. Create Virtual Environment

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

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Streamlit Application

```bash
streamlit run app.py
```

Application runs on:

```text
http://localhost:8501
```

---

# 📡 API Endpoint

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

# 🧪 Example Usage

### Input

```text
मेरा नाम आर्यन है
```

### Output

```text
English : My name is Aryan
Tamil    : என் பெயர் ஆர்யன்
Bengali  : আমার নাম আর্যন
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

Update the backend URL inside `app.py`:

```python
FASTAPI_URL = "https://your-render-url.onrender.com"
```

Deploy using:

* Repository: GitHub Repository
* Branch: main
* Main File Path:

```text
frontend/app.py
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* REST API development using FastAPI
* API integration using Requests
* Frontend development using Streamlit
* Request and response handling
* Backend and frontend separation
* Deployment of Python applications
* Cloud deployment using Render and Streamlit
* Integration of multilingual translation services
* Building production-ready AI-powered web applications

---

# 👨‍💻 Author

**Aryan Shukla**
B.Tech CSE (AI/ML) Student

### Skills

* Python
* FastAPI
* Machine Learning
* Retrieval-Augmented Generation (RAG)
* AI Applications
* Backend Development

### GitHub

https://github.com/Shadow-linux-png

### LinkedIn

https://www.linkedin.com/in/aryan-shukla-3821b135a/

### Portfolio

https://auto-repo-shine.lovable.app/

---

⭐ If you found this project useful, consider giving the repository a star.
