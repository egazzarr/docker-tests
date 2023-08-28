import requests, json, os
import configparser
import pandas as pd


config = configparser.ConfigParser()
path=os.path.join(os.getcwd(),'/home/iam.ini')
config.read(path)
client_id = config['IAM']['client_id']
client_secret = config['IAM']['client_secret']

print(client_id)
token_resp = requests.post(
    "https://iam-escape.cloud.cnaf.infn.it/token",
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "scim:read"
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"},
)

token_json = token_resp.json()
token = token_json['access_token']
headers = {"Authorization": "Bearer %s" % token}
list_url = "https://iam-escape.cloud.cnaf.infn.it/scim/Users"

startIndex = 1
results = []
resp = requests.get(list_url, headers=headers, params={"startIndex": startIndex})
data = resp.json()
response = json.loads(resp.text)

# need to do this as iam return sonly first 100 results 

while startIndex < response['totalResults']:
    resp = requests.get(list_url, headers=headers, params={"startIndex": startIndex})
    data = resp.json()
    response = json.loads(resp.text)
    for user in data['Resources']:
        for email in user['emails']:
            results.append(email['value'])
            print(email['value'])
        startIndex+=1
    print(startIndex)

with open('emails.json', 'w+') as fp:
    fp.write(json.dumps(results))