# Meine Freund Backend

FastAPI backend scaffold built with Python 3.11.

## Setup

1. Create a virtual environment (example using `python -m venv`):
   ```bash
   python -m venv .venv
   ```
2. Activate it:
   - PowerShell: `.\.venv\Scripts\Activate`
   - bash/zsh: `source .venv/bin/activate`

3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Development Server

From the `backend` directory, run:

```bash
uvicorn app.main:app --reload
```

## Docker

- Build the container image from the `backend` directory:
  ```bash
  docker build -t meine-freund-backend .
  ```
- Run it locally and expose the API on port 8000:
  ```bash
  docker run -p 8000:8000 meine-freund-backend
  ```
- After the container starts, the app is available at:
  - `http://127.0.0.1:8000/health`
  - `http://127.0.0.1:8000/api/quote`

## Quote API

- Path: `GET /api/quote`
- Example response:
  ```json
  {
    "message": "Hello from AWS-ready backend",
    "timestamp": "2025-11-20T15:45:00.000000+00:00",
    "environment": "local"
  }
  ```

