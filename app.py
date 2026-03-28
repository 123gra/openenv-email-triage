from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    text: str

@app.get("/")
def home():
    return FileResponse("index.html")

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