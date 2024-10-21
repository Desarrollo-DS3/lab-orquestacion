#!/bin/bash

k3d cluster create mycluster -p "8082:30080@agent:0" --agents 3
kubectl taint nodes k3d-mycluster-server-0 dedicated=server:NoSchedule
kubectl label nodes k3d-mycluster-agent-0 gateway=true


kubectl apply -f gateway/gateway-deployment.yaml
kubectl apply -f samuel/samuel-deployment.yaml
kubectl apply -f juan/juan-deployment.yaml

kubectl get pods