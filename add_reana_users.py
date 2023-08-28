import json
import os
import subprocess
import configparser


config = configparser.ConfigParser()
path=os.path.join(os.getcwd(),'/home/iam.ini')
config.read(path)
client_id = config['IAM']['client_id']
client_secret = config['IAM']['client_secret']
reana_admin_token = config['REANA']['reana_admin_token']

with open('emails.json', 'r') as file:
    j = json.load(file)
    print(j)
for i in j:
    print (i)
    output = subprocess.check_output([f'kubectl exec -i -t deployment/reana-server -n reana -- flask reana-admin user-create --email {i} --admin-access-token ZnUBqNhGkZ0_h3uSsp0Uxw'], shell=True, encoding='utf-8')
    print(output)
   