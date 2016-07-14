echo "update code in all node"
fab -f update_code.py init_tasker
echo "delete old rc"
kubectl delete -f center.json
echo "create new rc"
kubectl create -f center.json
