import requests, json, os
import configparser

config = configparser.ConfigParser()
path=os.path.join(os.getcwd(),'iam.ini')
config.read(path)
client_id = config['IAM']['client_id']
client_secret = config['IAM']['client_secret']

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

results = []

list_url = "https://iam-escape.cloud.cnaf.infn.it/scim/Users"
resp = requests.get(list_url, headers=headers)
data = resp.json()
for user in data['Resources']:
    for email in user['emails']:
            results.append(email['value'])
with open('emails.json', 'w+') as fp:
    fp.write(json.dumps(results))

for user in results:
    flask reana-admin token-grant -e user --admin-access-token $REANA_ACCESS_TOKEN