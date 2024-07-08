from fastapi import FastAPI
import db

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/ping")
def ping():
    return {"_": "pong"}