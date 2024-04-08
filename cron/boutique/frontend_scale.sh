#!/bin/bash

# Set the KUBECONFIG environment variable
export KUBECONFIG=/etc/kubernetes/admin.conf

# Generate a random number between 1 and 10
REPLICAS=$((RANDOM % 10 + 1))

# Scale the deployment
kubectl scale deployment frontend --replicas=$REPLICAS -n app
