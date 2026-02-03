from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# TODO: implement /health endpoint
# TODO: implement /items/{item_id} endpoint