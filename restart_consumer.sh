echo "update code in all node"
fab -f update_code.py init_tasker
echo "delete old rc"
echo "create new rc"
kubectl delete -f consumer.json
kubectl create -f consumer.json
