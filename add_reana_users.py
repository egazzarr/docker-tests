import json
import os
import subprocess
# import configparser


# config = configparser.ConfigParser()
# path=os.path.join(os.getcwd(),'/home/iam.ini')
# config.read(path)
# client_id = config['IAM']['client_id']
# client_secret = config['IAM']['client_secret']
client_id = os.environ['CLIENT_ID']
client_secret  = os.environ['CLIENT_SECRET']  
reana_admin_token = os.environ['REANA_ADMIN_TOKEN']
print(reana_admin_token)

with open('/home/emails.json', 'r') as file:
    j = json.load(file)
    # print(j)
for i in j:
    # print (i)
    # output = subprocess.check_output([f'kubectl exec -i -t deployment/reana-server -n reana -- flask reana-admin user-create --email {i} --admin-access-token ${REANA_ADMIN_TOKEN}'], shell=True, encoding='utf-8')
    output = subprocess.check_output([f'flask reana-admin user-create --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8')
    # output = subprocess.check_output([f'echo {i} {reana_admin_token}'], shell=True, encoding='utf-8')
    
    print(output)
   