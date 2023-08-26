import datetime
import json

def hello_world():
    print("Hello World from functions.py!")

def return_time():
    time = datetime.datetime.now()
    time_obj = {
        "day": time.strftime("%A"),
        "date": time.strftime("%d %B %Y"),
        "time": time.strftime("%H:%M:%S"),
        "ap": time.strftime("%p")
    }
    return time_obj



