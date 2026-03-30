from fastapi import FastAPI 
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse("index.html")



@app.post("/reset")
def reset():
    return {
        "state": "email_received"
    }


@app.post("/step")
def step(action: dict):
    return {
        "state": "processed",
        "reward": 1.0,
        "done": True,
        "info": {"message": "Email classified"}
    }



@app.post("/predict")
def predict(data: Input):
    text = data.text.lower()

    if "urgent" in text:
        label = "urgent"
    elif "offer" in text:
        label = "spam"
    else:
        label = "normal"

    return {"prediction": label}
