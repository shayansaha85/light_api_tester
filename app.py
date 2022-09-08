from flask import *
import requests
import json

app = Flask(__name__)

# global
data = {
    "endpoint" : "",
    "http_method" : "",
    "payload" : "",
    "headers" : ""
}

def filter_json(payload):
    s = ""
    for x in payload.split():
        s += x
    return s

def get_call(data):
    endpoint = data["endpoint"].strip()
    headers = data["headers"].strip()
    if len(headers) != 0:
        response = requests.get(endpoint, headers=json.loads(filter_json(headers)))
    else:
        response = requests.get(endpoint)

    return [response.status_code, response.text]

def post_call(data):
    endpoint = data["endpoint"].strip()
    payload = data["payload"].strip()
    headers = data["headers"].strip()
    if len(headers) != 0:
        response = requests.post(f'{endpoint} / post', data = json.loads(filter_json(payload)), headers=json.loads(filter_json(headers)))
    else:
        response = requests.post(f'{endpoint} / post', data = json.loads(filter_json(payload)))

    return [response.status_code, response.text]


@app.route("/", methods=["GET", "POST"])
def p():
    response = ""
    response_code = ""
    if request.method == "POST":
        data["endpoint"] = str(request.form.get("endpoint"))
        data["http_method"] = str(request.form.get("http_method"))
        data["payload"] = request.form.get("payload")
        data["headers"] = request.form.get("headers")
        print(len(data["headers"].strip()))

        if data["http_method"] == "post" and len(data["payload"].strip()) == 0:
            response = "Please add payload"
            response_code = "Response code : FATAL"
    
        elif data["http_method"].lower() == "get":
            output = get_call(data)
            response_code += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(response)
            
        elif data["http_method"].lower() == "post":
            output = post_call(data)
            response_code += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(data["payload"].strip().replace("\n", ""))
            print(response)
        
        else:
            response = ""

    return render_template("index.html", response=response, response_code=response_code)



app.run(debug = True, host = "0.0.0.0", port = 3333)