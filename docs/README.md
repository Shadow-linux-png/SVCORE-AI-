# Multilingual Translation Web Application

This project provides a web application for translating Hindi text into English, Tamil, and Bengali. It consists of a FastAPI backend and a Streamlit frontend.

## Project Structure

\`\`\`
.
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
└── docs/
    └── README.md
\`\`\`

## Setup and Installation

### Backend (FastAPI)

1.  **Navigate to the backend directory:**
    \`\`\`bash
    cd backend
    \`\`\`
2.  **Create a virtual environment (recommended):**
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows use \`venv\\Scripts\\activate\`
    \`\`\`
3.  **Install dependencies:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
4.  **Run the FastAPI server:**
    \`\`\`bash
    uvicorn main:app --reload --port 8000
    \`\`\`
    The API will be available at \`http://localhost:8000\`.

### Frontend (Streamlit)

1.  **Navigate to the frontend directory:**
    \`\`\`bash
    cd ../frontend
    \`\`\`
2.  **Create a virtual environment (recommended):**
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows use \`venv\\Scripts\\activate\`
    \`\`\`
3.  **Install dependencies:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
4.  **Run the Streamlit application:**
    \`\`\`bash
    streamlit run app.py
    \`\`\`
    The application will be available at \`http://localhost:8501\`.

    **Note:** Ensure the FastAPI backend is running before starting the Streamlit app, or update the \`FASTAPI_URL\` in \`frontend/app.py\` to your deployed backend URL.

## Deployment

### FastAPI on Render

1.  Create a new web service on Render.
2.  Connect your Git repository.
3.  Configure the build command: \`pip install -r backend/requirements.txt\`
4.  Configure the start command: \`uvicorn backend.main:app --host 0.0.0.0 --port $PORT\`
5.  Set environment variables as needed (e.g., for API keys if you switch translation services).

### Streamlit on Streamlit Community Cloud

1.  Ensure your \`frontend/requirements.txt\` is complete.
2.  Add a \`secrets.toml\` file in a \`.streamlit/\` directory within your frontend code for sensitive information like the FastAPI URL.
    \`\`\`toml
    # .streamlit/secrets.toml
    FASTAPI_URL = "YOUR_RENDER_DEPLOYMENT_URL"
    \`\`\`
3.  Deploy your Streamlit app to a Git repository (e.g., GitHub).
4.  Connect Streamlit Community Cloud to your repository.
5.  Configure the app settings, pointing to your Streamlit code.

## Code Quality and Features

-   **Modular Structure:** Backend and frontend are separated into distinct directories.
-   **Pydantic Schemas:** Used for request and response validation in the FastAPI backend.
-   **Type Hints:** Used throughout the Python code for better readability and maintainability.
-   **Error Handling:** Basic error handling is implemented in both backend and frontend.
-   **Requirements Files:** \`requirements.txt\` included for both backend and frontend.
-   **README:** This file provides setup and deployment instructions.
-   **Comments and Docstrings:** Basic comments are included; further docstrings can be added.
-   **Production-Ready Code Quality:** Code follows standard Python practices. The backend uses \`uvicorn\` for production deployment, and the frontend leverages Streamlit's deployment options.
-   **Streamlit Features:** Includes text area, translate button, output cards, loading spinner, error handling, character counter, and clear button.
-   **FastAPI Endpoints:** \`/health\` and \`/translate\` endpoints are implemented.
