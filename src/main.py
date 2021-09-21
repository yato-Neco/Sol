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
import json


app = Flask(__name__)


@app.route('/mars_api/') 
def mars_api_home():


    mars_time = "<h1>mars_api<h1>"


  

    return mars_time

@app.route('/mars_api/<req>') 
def mars_api(req):

    print(req)

    mars_time = "Home"


    if req == "sol":
        mars_time = sol_api()
   
  

    return jsonify(mars_time)




def sol_api():


    sec = 0

    min = 0

    hour = 0

    sol = 0

    sec_round = round(time.perf_counter())


    sec = sec_round % 60

    min = (sec_round // 60) % 60

    hour = (sec_round // 3600) % 24

    sol = sec_round // 88775

    

    mars_time = {
        "Sol": sol,
        "hour": hour,
        "min": min,
        "sec": sec,
    }


    return mars_time

   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)




    
        