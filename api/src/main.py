from fastapi import FastAPI
from src.modules import routers

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
for router in routers:
    app.include_router(router)

@app.get("/ping")
def ping():
    return {"_": "pong"}