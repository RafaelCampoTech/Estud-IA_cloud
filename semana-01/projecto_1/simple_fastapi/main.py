from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Grupo Estud-IA"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/dummy")
def read_dummy(a: str = "Dummy"):
    return {"a": a, "message": "Hello from dummy_function!"}
