import requests
import json
import functions as f
from fastapi import FastAPI


f.hello_world()
app = FastAPI()

@app.get("/")

async def root():
    return {"message": "Hello World How are you?"}
