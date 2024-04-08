# MicroAutoScaler

<!-- ![Static Badge](https://img.shields.io/badge/python-3.6-blue) ![Static Badge](https://img.shields.io/badge/PyTorch-red)  -->
- [Overview](#overview)
- [I. Machine Prerequis](#i-machine-prerequis)
- [II. Installation](#ii-installation)
  - [1. Setup Required Packages](#1-setup-required-packages)
  - [2. Setup Docker](#2-setup-docker)
  - [3. Setup Kubernetes Cluster](#3-setup-kubernetes-cluster)
  - [4. Setup Longhorn](#4-setup-longhorn)
  - [5. Setup Prometheus](#5-setup-prometheus)
  - [6. Setup Istio](#6-setup-istio)
  - [7. Setup Locust](#7-setup-locust)
- [III. Deploy Benchmark Microservices](#iii-deploye-benchmark-microservices)
  - [1. Bookinfo](#1-bookinfo)
  - [2. Online-boutique](#2-online-boutique)
  - [3. Train-ticket](#3-train-ticket)
- [IV. Workload Generation](#iv-workload-generation)
- [V. Train and Test](#v-train-and-test)
  - [1. Model Configuration](#1-model-configuration)
  - [2. Collect the original dataset](#2-collect-the-original-dataset)
  - [3. Process the dataset](#3-process-the-dataset)
  - [4. Export the well-trained model](#4-export-the-well-trained-model)
- [VI. Autoscaling](#vi-autoscaling)
- [VII. Evaluation](#vii-evaluation)
  - [1. Analyze the similarity between the original graph relationship and od, cc.](#1-analyze-the-similarity-between-the-original-graph-relationship-and-od--cc)
  - [2. Compute relevant metrics.](#2-compute-relevant-metrics)
- [VIII. Thanks](#thanks)

## Overview

This repository contains a prototyped version of DeepScaler described in our ASE '23 paper "DeepScaler: Holistic Autoscaling for Microservices Based on Spatiotemporal GNN with Adaptive Graph Learning".

## I. Machine Prerequisite

| **Aspect**                  | **Details**                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Operating System            | Ubuntu 18.04 LTS                                                                                                    |
| Kernel Version              | 4.15.0                                                                                                              |
| VM Specifications           | 4 with 12-core 2.2 GHz CPU, 24 GB memory, 100GB disk<br>4 with 24-core 2.2 GHz CPU, 32 GB memory, 500 GB disk |
| Network | ... |

## II. Installation

### 1. Setup Required Packages

- Python 3.6

- numpy == 1.21.5
- pandas == 1.4.4
- torch == 1.13.1

 ```pip3 install -r requirement.txt```

### 2. Setup Docker

```bash
apt update && apt upgrade
apt-cache madison docker.io

apt install docker.io=$YOUR_DOCKER_VERSION #like 20.10.21-0ubuntu1~20.04.2
systemctl enable docker
```

You can use some image acceleration configurations if you are in a region with limited access to DockerHub. For example, you can use the Aliyun image acceleration service:

```bash
cd /etc/docker

sudo tee /etc/docker/daemon.json << -'EOF' { "registry-mirrors": ["https://xxx.mirror.aliyuncs.com"] }
  "exec-opts": ["native.cgroupdriver=systemd"]
EOF

sudo systemctl daemon-reload sudo systemctl restart docker
```

### 3. Setup Kubernetes Cluster

A running Kubernetes cluster is required before deploying DeepScaler. The following instructions are tested with Kubernetes v1.23.4. For set-up instructions, refer to [this](setUp-k8s.md).

```bash
# Update the apt package list and install https transport, curl tool
apt-get update && apt-get install -y apt-transport-https curl

# Add the Kubernetes apt source to the apt source list
sudo tee /etc/apt/sources.list.d/kubernetes.list <<-'EOF' 
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main 
EOF

# Add the Kubernetes apt source key for secure package download
curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

# Set the Kubernetes version
KUBE_VERSION=1.23.4-00

# Install kubectl, kubeadm, kubelet
apt install kubectl=$KUBE_VERSION kubeadm=$KUBE_VERSION kubelet=$KUBE_VERSION

# Pull the Kubernetes images from Aliyun repository
kubeadm config images pull --image-repository registry.aliyuncs.com/google_containers

# Initialize the Kubernetes master node with a specified pod network CIDR and image repository
sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --image-repository registry.aliyuncs.com/google_containers

# Export the KUBECONFIG environment variable
export KUBECONFIG=/etc/kubernetes/admin.conf

# Taint the Kubernetes master node to prevent scheduling of pods
kubectl taint nodes <your-node-name> node-role.kubernetes.io/master:NoSchedule-

# Install the Calico network plugin
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.2/manifests/tigera-operator.yaml
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.2/manifests/custom-resources.yaml

```

### 4. Setup Longhorn

Before this, you may need to install Helm:

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
bash get_helm.sh
```

Then execute:

```bash
apt install open-iscsi jq nfs-common
helm repo add longhorn https://charts.longhorn.io
curl -sSfL https://raw.githubusercontent.com/longhorn/longhorn/v1.6.0/scripts/environment_check.sh | bash
helm repo update && helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace --version 1.6.0
```

### 5. Setup Prometheus

Prometheus is an open-source monitoring and alerting toolkit used for collecting and storing metrics from various systems.

This project has prepared the necessary yaml for you to install Prometheus, you just need to execute:

```bash
kubectl apply --server-side -f env/kube-prometheus/manifest/setup
kubectl apply -f env/kube-prometheus/manifest/
```

### 6. Setup Istio

Istio is an open-source service mesh platform that enhances the management and security of microservices in a distributed application. After having a cluster running a supported version of Kubernetes, installing Istio is needed.

```bash
$ curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.17.4 TARGET_ARCH=x86_64 sh -
$ cd istio-1.21.1
$ export PATH=$PWD/bin:$PATH

istioctlinstall --set profile=demo -y
kubernetes create ns app
kubectl label namespace app istio-injection=enabled
```

### 7. Setup Locust

We utilize the [Locust](https://locust.io/) load testing tool, an open-source tool that employs Python code to define user behaviors and simulate millions of users.

```bash
pip install locust
```

## III. Deploy Benchmark Microservices

### 1. Bookinfo

```bash
(1) kubectl create -f <(istioctl kube-inject -f /benchmarks/bookinfo/bookinfo.yaml)
(2) kubectl apply  -f /benchmarks/bookinfo/bookinfo-gateway.yaml)
```

### 2. Online-boutique

```bash
(1) kubectl create -f <(istioctl kube-inject -f ./benchmarks/boutique/boutique.yaml) -n app
(2) kubectl apply  -f ./benchmarks/boutique/boutique-gateway.yaml -n app
```

### 3. Train-ticket

Deploy the Train-Ticket system on K8S with istio.

```bash
(1) kubectl create -f <(istioctl kube-inject -f ./benchmarks/train-ticket/ts-deployment-part1.yml)
(2) kubectl create -f <(istioctl kube-inject -f ./benchmarks/train-ticket/ts-deployment-part2.yml)
(3) kubectl create -f <(istioctl kube-inject -f ./benchmarks/train-ticket/ts-deployment-part3.yml)
(4) kubectl apply  -f ./benchmarks/train-ticket/trainticket-gateway.yaml
```

## IV. Workload Generation

The generated workload intensity varied over time, emulating typical characteristics of microservice workloads, including slight increases, slight decreases, sharp increases, sharp decreases, and continuous fluctuations. The flow data simulation script is collected from FIFA World Cup access datasets and stored in the [file](https://github.com/SYSU-Workflow-Administrator/DeepScaler/blob/main/sendFlow/random-100max.req).

The script [load_generator.py](https://github.com/SYSU-Workflow-Administrator/DeepScaler/blob/main/sendFlow/load_generator.py) is for simulating user behavior for both "Bookinfo" and "Online-Boutique" and [load_generator_train.py](https://github.com/SYSU-Workflow-Administrator/DeepScaler/blob/main/sendFlow/load_generator_train.py) is for simulating user behavior for "Train-Ticket."

Simulate the workload generator:

```bash
sh sendFlow/sendLoop.sh
```

You can refer to this [webpage](https://blog.techbridge.cc/2019/05/29/how-to-use-python-locust-to-do-load-testing/) for customized usage.

## V. Train and Test

### 1. Model Configuration

The information that needs to be configured before model training is stored in [config/train_config.yaml](https://github.com/SYSU-Workflow-Administrator/DeepScaler/blob/main/config/train_config.yaml), and the processed data sets and various model configuration information are stored in [config/train_dataset_speed.yaml](https://github.com/SYSU-Workflow-Administrator/DeepScaler/blob/main/config/train_dataset_speed.yaml). You can modify the tuning parameters yourself.

### 2. Collect the original dataset

```python
template = {
    "cpu":"sum(irate(container_cpu_usage_seconds_total{{container=~'{1}',namespace=~'{0}'}}[1m]))/sum(container_spec_cpu_quota{{container=~'{1}',namespace=~'{0}'}}/container_spec_cpu_period{{container=~'{1}',namespace=~'{0}'}})",
    "mem": "sum(container_memory_usage_bytes{{namespace='{0}',container='{1}'}}) / sum(container_spec_memory_limit_bytes{{namespace='{0}',container='{1}'}})",
    "res": "sum(rate(istio_request_duration_milliseconds_sum{{reporter='destination',destination_workload_namespace='{0}',destination_workload='{1}'}}[{2}]))/sum(rate(istio_request_duration_milliseconds_count{{reporter='destination',destination_workload_namespace='{0}',destination_workload='{1}'}}[{2}]))/1000",
    "req": "sum(rate(istio_requests_total{{destination_workload_namespace='{0}',destination_workload='{1}'}}[{2}]))",
    "pod": "count(container_spec_cpu_period{{namespace='{0}',container='{1}'}})"
}
```

Run this code, and the data will be stored in the folder location you have set.

```bash
python metrics_fetch.py
```

```python
#Here's "Online-Boutique" example:
prefix_api = "http://localhost:30090/api/v1/query?query="
namespace = 'boutiquessj'
interval = 120
services = ["adservice", "cartservice", "checkoutservice","currencyservice","emailservice","frontend","paymentservice","productcatalogservice","recommendationservice","shippingservice"]
metrics = ['cpu','res','req','mem','pod']
```

### 3. Process the dataset

Transform the raw dataset into a time-sliced dataset for model training and learning.

```bash
python data_process.py
```

### 4. Export the well-trained model

We provide a more detailed and complete command description for training and testing the model:

```bash
python -u main.py
--model_config_path <model_config_path>
--train_config_path <train_config_path>
--model_name <model_name>
--num_epoch <num_epoch>
--num_iter <num_iter>
--model_save_path <model_save_path>
--max_graph_num <max_graph_num>
```

| Parameter name    | Description of parameter       |
|-------------------|--------------------------------|
| model_config_path | Config path of models          |
| train_config_path | Config path of Trainer         |
| model_name        | Model name to train            |
| num_epoch         | Training times per epoch       |
| num_iter          | Maximum value for iteration    |
| model_save_path   | Model save path                |
| max_graph_num     | Volume of adjacency matrix set |

More parameter information please refer to main.py.
The models exported after running the file are stored in the [model_states](https://github.com/SYSU-Workflow-Administrator/DeepScaler/tree/main/model_states).

## VI. Autoscaling

Utilizing well-trained and tested models to enable automatic scaling of various microservices.

```bash
python predict_scale.py
```

## VII. Evaluation

### 1. Analyze the similarity between the original graph relationship and od, cc

```bash
python similarity.py
 ```

### 2. Compute relevant metrics

```bash
python calculate.py
```

## VIII. Thanks

This repository was inspired by the work of  Shijie Song or Chunyang Meng (<songshj6@mail2.sysu.edu.cn>, <mengchy3@mail2.sysu.edu.cn>) on their [DeepScaler](https://github.com/SYSU-Workflow-Lab/DeepScaler). I am grateful for the ideas and insights I gained from their project.
