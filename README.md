# BE-01: Basic FastAPI Endpoint

Minimal FastAPI server with two GET endpoints, built as Week 1 setup 
assignment for FlyRank's Backend AI Engineering internship.

## Endpoints

- `GET /get_users` — returns all users (in-memory dict)
- `GET /get_user/{id}` — returns a single user by ID, 404 if not found

## Run locally

\`\`\`bash
python -m venv api_env
api_env\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn api_endpoint:app --reload
\`\`\`

Server runs at `http://127.0.0.1:8000`

## Test

\`\`\`bash
curl http://127.0.0.1:8000/get_users
curl http://127.0.0.1:8000/get_user/111
\`\`\`

Or open the endpoints directly in a browser.

## Notes

Data is hardcoded in-memory (no database) — matches the scope of this 
assignment, which is server setup and request/response fundamentals, 
not persistence.