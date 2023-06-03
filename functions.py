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
    #time_obj_json = json.dumps(time_obj, indent=2)
    #time_obj_html = "<html><body><pre>" + time_obj_json + "</pre></body</html>"
    #print ("returning this string: \n" + time_obj_html)
    return time_obj


