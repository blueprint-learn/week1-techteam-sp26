from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


# TODO: implement /health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: implement /items/{item_id} endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
