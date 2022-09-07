from flask import *
import requests

app = Flask(__name__)

# global
data = {
    "endpoint" : "",
    "http_method" : "",
    "payload" : {},
    "headers" : {}
}

def get_call(data):
    endpoint = data["endpoint"]
    headers = data["headers"]
    response = requests.get(endpoint, headers=headers)
    return [response.status_code, response.text,]

def post_call(data):
    endpoint = data["endpoint"]
    payload = data["payload"]
    headers = data["headers"]
    response = requests.post(f'{endpoint} / post', data = payload, headers=headers)
    return [response.status_code, response.text]


@app.route("/", methods=["GET", "POST"])
def p():
    response = ""
    response_code = ""
    if request.method == "POST":
        data["endpoint"] = str(request.form.get("endpoint"))
        data["http_method"] = str(request.form.get("http_method"))
        data["payload"] = str(request.form.get("payload"))
        data["payload"] = str(request.form.get("headers"))
    
        print(data["payload"])
        if data["http_method"].lower() == "get":
            output = get_call(data)
            response_code += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(response)
            
        elif data["http_method"].lower() == "post":
            output = post_call(data)
            response_code += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(response)
        
        else:
            response = ""

    return render_template("index.html", response=response, response_code=response_code)



app.run(debug = True, host = "0.0.0.0", port = 3333)