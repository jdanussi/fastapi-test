from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, you accessed the root using GET method"}

@app.post("/items")
def create_item():
    return {"message": "Hello, you accessed /items using POST method"}

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"Hello, you accessed /items/{item_id} using PUT method"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
