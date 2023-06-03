#import requests
import json
import functions as f
from fastapi import FastAPI


f.hello_world()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World How are you?"}

@app.get("/time")
async def time():
    t = f.return_time()
    t_json = json.dumps(t, indent=4, default=str)
    print ("returning :\n" + t_json)
    return t_json
