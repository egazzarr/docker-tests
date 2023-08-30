import json
import os
import subprocess

client_id = os.environ['CLIENT_ID']
client_secret  = os.environ['CLIENT_SECRET']  
reana_admin_token = os.environ['REANA_ADMIN_TOKEN']
print(reana_admin_token)

with open('/home/emails.json', 'r') as file:
    j = json.load(file)
for i in j:
    try:
        # subprocess.check_output([f'kubectl -n reana exec deployment/reana-server -c rest-api -- flask reana-admin user-create --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8')
        # subprocess.check_output([f'kubectl -n reana exec deployment/reana-server -c rest-api -- flask reana-admin user-list --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8')
        subprocess.check_output([f'flask reana-admin user-create --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8') 
    except subprocess.CalledProcessError as e:
        print(e.stderr)
