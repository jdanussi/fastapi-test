from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, you accessed the root"}

@app.get("/route1")
def create_item():
    return {"message": "You accessed /route1"}

@app.get("/route2")
def update_item(item_id: int):
    return {"message": "You accessed /route2"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
