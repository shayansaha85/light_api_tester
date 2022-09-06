from flask import *
import requests

app = Flask(__name__)

# global
data = {
    "endpoint" : "",
    "http_method" : "",
    "payload" : {}
}


def get_call(data):
    endpoint = data["endpoint"]
    response = requests.get(endpoint)
    return [response.status_code, response.text,]

def post_call(data):
    endpoint = data["endpoint"]
    payload = data["payload"]
    response = requests.post(f'{endpoint} / post', data = payload)
    return [response.status_code, response.text]


@app.route("/", methods=["GET", "POST"])
def p():
    response = ""
    if request.method == "POST":
        data["endpoint"] = str(request.form.get("endpoint"))
        data["http_method"] = str(request.form.get("http_method"))
        data["payload"] = str(request.form.get("payload"))
    
        print(data["payload"])
        if data["http_method"].lower() == "get":
            output = get_call(data)
            response += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(response)
            
        elif data["http_method"].lower() == "post":
            output = post_call(data)
            response += "Response code : " + str(output[0]) + "\n"
            response += str(output[1]) + "\n"
            print(response)
        
        else:
            response = ""

    return render_template("index.html", response=response)



app.run(debug = True, host = "0.0.0.0", port = 3333)