import json
import os
import subprocess

client_id = os.environ['CLIENT_ID']
client_secret  = os.environ['CLIENT_SECRET']  
reana_admin_token = os.environ['REANA_ADMIN_TOKEN']
print(reana_admin_token)
# Export existing reana users
# The output is formated in csv style: "user-id","email","","","" and 3 empty fields
try:
    subprocess.check_output(
        [
            f"""flask reana-admin user-export --admin-access-token {reana_admin_token} | cut -f2 -d "," | sed 's/"//g' > /home/reana_users.txt """
        ],
        shell=True,
        encoding="utf-8",
    )
except subprocess.CalledProcessError as e:
    print(f"Command: {e.cmd} failed with return code: {e.returncode} and error: {e.returncode}")

# Open file and load emails in a list
with open("/home/reana_users.txt") as f:
    raw_users_reana = f.readlines()

# clean carriage return
reana_emails = []
for email in raw_users_reana:
    reana_emails.append(email.replace("\n", ""))

# Compare both list and add new users if any 
with open("/home/emails.json", "r") as file:
    new_users = json.load(file)
for email in new_users:
    if email not in reana_emails:
        try:
            subprocess.check_output(
                [
                    f"flask reana-admin user-create --email {email} --admin-access-token {reana_admin_token}"
                ],
                shell=True,
                encoding="utf-8",
            )
        except subprocess.CalledProcessError as e:
            print(e.stderr)


# with open('/home/emails.json', 'r') as file:
#     j = json.load(file)
# for i in j: 
#     try:
#         # subprocess.check_output([f'kubectl -n reana exec deployment/reana-server -c rest-api -- flask reana-admin user-create --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8')
#         # subprocess.check_output([f'kubectl -n reana exec deployment/reana-server -c rest-api -- flask reana-admin user-list --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8')
#         subprocess.check_output([f'flask reana-admin user-create --email {i} --admin-access-token {reana_admin_token}'], shell=True, encoding='utf-8') 
#     except subprocess.CalledProcessError as e:
#         print(e.stderr)
