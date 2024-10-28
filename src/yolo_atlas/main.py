from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {
        "title": "Yolo Atlas",
        "description": "Best app on Earth!"
    }
