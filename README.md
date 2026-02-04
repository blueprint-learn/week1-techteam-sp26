# Week 1 – FastAPI Basics

## Clone your repo
```bash
git clone https://github.com/blueprint-learn/week1-techteam-sp26-{username}
```

## Objective
Build your first FastAPI application and understand how APIs work.

## Requirements
Your API must include the following endpoints:

### 1. GET /
Returns:
```json
{ "message": "Hello World" }
```

### 2. GET /healt
Returns:
```json
{ "status": "ok" }
```

### 3. GET /healt
```json
{ "item_id": 3 }
```
### Running locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Submission
Push your code to GitHub. Tests will run automatically.
