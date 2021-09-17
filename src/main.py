import time
from flask import Flask, jsonify, request, render_template
import concurrent.futures
import json



app = Flask(__name__)
     
     
sol = 0

hour = 0

min = 0

sec2 = 0

sec = 88760


 

def time_sol():

    

    while True:

        global sec

        time.sleep(1)

        sec = sec + 1

       

@app.route('/') # 'http://127.0.0.1:8888/'
def get_store():



    sec2 = sec % 60

    min = (sec // 60) % 60

    hour = (sec // 3600) % 60

    sol = sec // 88775

    

    mars_time = {
        "Sol": sol,
        "hour": hour,
        "min": min,
        "sec": sec2,
    }


    return jsonify(mars_time)
    



   
if __name__ == "__main__":

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(time_sol)
    executor.submit(app.run(host='0.0.0.0', port=8888, debug=True))

