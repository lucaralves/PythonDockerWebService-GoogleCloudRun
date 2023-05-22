from fastapi import FastAPI
from env import config

MODE = config("MODE", cast=str, default=None)

workspace = FastAPI()

@workspace.get("/getJson")
def getController():
    return {"Content": "Hello World", "mode": MODE}

