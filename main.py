import json
from fastapi import FastAPI
import functions as f
import fx as fx


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

@app.get("/money")
async def money():
    f = fx.getSharePrice
    print ("returning :\n" + f)
    return f



print ("ending main.py")