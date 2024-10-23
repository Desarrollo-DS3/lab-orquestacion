k3d cluster create mycluster -p "8082:30080@agent:0" --agents 7
kubectl taint nodes k3d-mycluster-server-0 dedicated=server:NoSchedule
kubectl label nodes k3d-mycluster-agent-0 gateway=true

kubectl apply -f gateway/gateway-deployment.yaml
kubectl apply -f samuel/samuel-deployment.yaml
kubectl apply -f juan/juan-deployment.yaml
kubectl apply -f john/john-deployment.yaml
kubectl apply -f duque/duque-deployment.yaml
kubectl apply -f julian/julian-deployment.yaml
kubectl apply -f sebastian/sebastian-deployment.yaml

kubectl get pods