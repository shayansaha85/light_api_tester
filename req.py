import requests, json

payload = """
            {
    "name": "morpheus",
    "job": "leader"
}
"""
headers = ""

endpoint = "https://reqres.in/api/users"
response = requests.post(f'{endpoint} / post', data = json.loads(payload), headers = json.loads(headers))
print(response.text)
# s = ""
# for x in payload.split():
#     s += x
# print(json.loads(s))
