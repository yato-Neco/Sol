'''
Copyright [2021] [x64neco]
Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''



import time
from flask import Flask, jsonify, request, render_template
import concurrent.futures
import json



app = Flask(__name__)
     
     




sec = 0


def time_sol():

    

    while True:

        global sec


        time.sleep(0.1)

        

        sec = time.perf_counter()



@app.route('/') 
def sol_api():



    sec2 = 0

    min = 0

    hour = 0

    sol = 0

    sec_round = round(sec)




    sec2 = sec_round % 60

    min = (sec_round // 60) % 60

    hour = (sec_round // 3600) % 24

    sol = sec_round // 88775

    

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