cat emails.txt | while read line 
do
#    echo -e "\033[1;33m$line"
   kubectl exec -i -t deployment/reana-server -n reana -- flask reana-admin user-create --email $line --admin-access-token $REANA_ACCESS_TOKEN
   echo -e "\033[1;33m added user $line"
#    kubectl exec -i -t deployment/reana-server -n reana -- flask reana-admin token-grant -e $line --admin-access-token $REANA_ACCESS_TOKEN
#    echo -e "\033[1;33m granting TOKEN for user $line"
done