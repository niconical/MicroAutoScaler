import torch
import numpy as np
import datetime
from metrics_fetch import save_all_fetch_data
from prepareData import read_and_generate_dataset

# 收集数据

services = ["adservice", "cartservice", "checkoutservice","currencyservice", "emailservice","frontend","paymentservice","productcatalogservice","recommendationservice","shippingservice"]
metrics = ['req','cpu','res','pod','mem']

times_train = [
    ('2024-04-06 11:30:00', '2024-04-08 12:30:00')
]#

save_all_fetch_data(times_train, 1, root_dir='./data/boutique/train/', interval=30, services=services,metrics=metrics)#interval 间隔

###req
# "adservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[0],metrics[0])
adservice_req=np.genfromtxt(file, dtype=np.double)
adservice_req = adservice_req[:,np.newaxis]
# "cartservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[1],metrics[0])
cartservice_req=np.genfromtxt(file, dtype=np.double)
cartservice_req = cartservice_req[:,np.newaxis]
# "checkoutservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[2],metrics[0])
checkoutservice_req=np.genfromtxt(file, dtype=np.double)
checkoutservice_req = checkoutservice_req[:,np.newaxis]
# "currencyservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[3],metrics[0])
currencyservice_req=np.genfromtxt(file, dtype=np.double)
currencyservice_req = currencyservice_req[:,np.newaxis]
# "emailservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[4],metrics[0])
emailservice_req=np.genfromtxt(file, dtype=np.double)
emailservice_req = emailservice_req[:,np.newaxis]
# "frontend"
file = './data/boutique/train/1_{}_{}.log'.format(services[5],metrics[0])
frontend_req=np.genfromtxt(file, dtype=np.double)
frontend_req = frontend_req[:,np.newaxis]
# "paymentservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[6],metrics[0])
paymentservice_req=np.genfromtxt(file, dtype=np.double)
paymentservice_req = paymentservice_req[:,np.newaxis]
# "productcatalogservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[7],metrics[0])
productcatalogservice_req=np.genfromtxt(file, dtype=np.double)
productcatalogservice_req = productcatalogservice_req[:,np.newaxis]
# "recommendationservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[8],metrics[0])
recommendationservice_req=np.genfromtxt(file, dtype=np.double)
recommendationservice_req = recommendationservice_req[:,np.newaxis]
# "shippingservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[9],metrics[0])
shippingservice_req=np.genfromtxt(file, dtype=np.double)
shippingservice_req = shippingservice_req[:,np.newaxis]

#####################################################################################################
####cpu
file = './data/boutique/train/1_{}_{}.log'.format(services[0],metrics[1])
adservice_cpu=np.genfromtxt(file, dtype=np.double)
adservice_cpu = adservice_cpu[:,np.newaxis]
# "cartservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[1],metrics[1])
cartservice_cpu=np.genfromtxt(file, dtype=np.double)
cartservice_cpu = cartservice_cpu[:,np.newaxis]
# "checkoutservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[2],metrics[1])
checkoutservice_cpu=np.genfromtxt(file, dtype=np.double)
checkoutservice_cpu = checkoutservice_cpu[:,np.newaxis]
# "currencyservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[3],metrics[1])
currencyservice_cpu=np.genfromtxt(file, dtype=np.double)
currencyservice_cpu = currencyservice_cpu[:,np.newaxis]
# "emailservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[4],metrics[1])
emailservice_cpu=np.genfromtxt(file, dtype=np.double)
emailservice_cpu = emailservice_cpu[:,np.newaxis]
# "frontend"
file = './data/boutique/train/1_{}_{}.log'.format(services[5],metrics[1])
frontend_cpu=np.genfromtxt(file, dtype=np.double)
frontend_cpu = frontend_cpu[:,np.newaxis]
# "paymentservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[6],metrics[1])
paymentservice_cpu=np.genfromtxt(file, dtype=np.double)
paymentservice_cpu = paymentservice_cpu[:,np.newaxis]
# "productcatalogservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[7],metrics[1])
productcatalogservice_cpu=np.genfromtxt(file, dtype=np.double)
productcatalogservice_cpu = productcatalogservice_cpu[:,np.newaxis]
# "recommendationservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[8],metrics[1])
recommendationservice_cpu=np.genfromtxt(file, dtype=np.double)
recommendationservice_cpu = recommendationservice_cpu[:,np.newaxis]
# "shippingservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[9],metrics[1])
shippingservice_cpu=np.genfromtxt(file, dtype=np.double)
shippingservice_cpu = shippingservice_cpu[:,np.newaxis]

###############################################################################################
### res
# "adservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[0],metrics[2])
adservice_res=np.genfromtxt(file, dtype=np.double)
adservice_res = adservice_res[:,np.newaxis]
# "cartservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[1],metrics[2])
cartservice_res=np.genfromtxt(file, dtype=np.double)
cartservice_res = cartservice_res[:,np.newaxis]
# "checkoutservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[2],metrics[2])
checkoutservice_res=np.genfromtxt(file, dtype=np.double)
checkoutservice_res = checkoutservice_res[:,np.newaxis]
# "currencyservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[3],metrics[2])
currencyservice_res=np.genfromtxt(file, dtype=np.double)
currencyservice_res = currencyservice_res[:,np.newaxis]
# "emailservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[4],metrics[2])
emailservice_res=np.genfromtxt(file, dtype=np.double)
emailservice_res = emailservice_res[:,np.newaxis]
# "frontend"
file = './data/boutique/train/1_{}_{}.log'.format(services[5],metrics[2])
frontend_res=np.genfromtxt(file, dtype=np.double)
frontend_res = frontend_res[:,np.newaxis]
# "paymentservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[6],metrics[2])
paymentservice_res=np.genfromtxt(file, dtype=np.double)
paymentservice_res = paymentservice_res[:,np.newaxis]
# "productcatalogservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[7],metrics[2])
productcatalogservice_res=np.genfromtxt(file, dtype=np.double)
productcatalogservice_res = productcatalogservice_res[:,np.newaxis]
# "recommendationservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[8],metrics[2])
recommendationservice_res=np.genfromtxt(file, dtype=np.double)
recommendationservice_res = recommendationservice_res[:,np.newaxis]
# "shippingservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[9],metrics[2])
shippingservice_res=np.genfromtxt(file, dtype=np.double)
shippingservice_res = shippingservice_res[:,np.newaxis]

###########################################################################################

### pod
# "adservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[0],metrics[3])
adservice_pod=np.genfromtxt(file, dtype=np.double)
adservice_pod = adservice_pod[:,np.newaxis]
# "cartservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[1],metrics[3])
cartservice_pod=np.genfromtxt(file, dtype=np.double)
cartservice_pod = cartservice_pod[:,np.newaxis]
# "checkoutservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[2],metrics[3])
checkoutservice_pod=np.genfromtxt(file, dtype=np.double)
checkoutservice_pod = checkoutservice_pod[:,np.newaxis]
# "currencyservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[3],metrics[3])
currencyservice_pod=np.genfromtxt(file, dtype=np.double)
currencyservice_pod = currencyservice_pod[:,np.newaxis]
# "emailservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[4],metrics[3])
emailservice_pod=np.genfromtxt(file, dtype=np.double)
emailservice_pod = emailservice_pod[:,np.newaxis]
# "frontend"
file = './data/boutique/train/1_{}_{}.log'.format(services[5],metrics[3])
frontend_pod=np.genfromtxt(file, dtype=np.double)
frontend_pod = frontend_pod[:,np.newaxis]
# "paymentservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[6],metrics[3])
paymentservice_pod=np.genfromtxt(file, dtype=np.double)
paymentservice_pod = paymentservice_pod[:,np.newaxis]
# "productcatalogservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[7],metrics[3])
productcatalogservice_pod=np.genfromtxt(file, dtype=np.double)
productcatalogservice_pod = productcatalogservice_pod[:,np.newaxis]
# "recommendationservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[8],metrics[3])
recommendationservice_pod=np.genfromtxt(file, dtype=np.double)
recommendationservice_pod = recommendationservice_pod[:,np.newaxis]
# "shippingservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[9],metrics[3])
shippingservice_pod=np.genfromtxt(file, dtype=np.double)
shippingservice_pod = shippingservice_pod[:,np.newaxis]

###########################################################################################
###mem
# "adservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[0],metrics[4])
adservice_mem=np.genfromtxt(file, dtype=np.double)
adservice_mem = adservice_mem[:,np.newaxis]
# "cartservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[1],metrics[4])
cartservice_mem=np.genfromtxt(file, dtype=np.double)
cartservice_mem = cartservice_mem[:,np.newaxis]
# "checkoutservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[2],metrics[4])
checkoutservice_mem=np.genfromtxt(file, dtype=np.double)
checkoutservice_mem = checkoutservice_mem[:,np.newaxis]
# "currencyservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[3],metrics[4])
currencyservice_mem=np.genfromtxt(file, dtype=np.double)
currencyservice_mem = currencyservice_mem[:,np.newaxis]
# "emailservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[4],metrics[4])
emailservice_mem=np.genfromtxt(file, dtype=np.double)
emailservice_mem = emailservice_mem[:,np.newaxis]
# "frontend"
file = './data/boutique/train/1_{}_{}.log'.format(services[5],metrics[4])
frontend_mem=np.genfromtxt(file, dtype=np.double)
frontend_mem = frontend_mem[:,np.newaxis]
# "paymentservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[6],metrics[4])
paymentservice_mem=np.genfromtxt(file, dtype=np.double)
paymentservice_mem = paymentservice_mem[:,np.newaxis]
# "productcatalogservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[7],metrics[4])
productcatalogservice_mem=np.genfromtxt(file, dtype=np.double)
productcatalogservice_mem = productcatalogservice_mem[:,np.newaxis]
# "recommendationservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[8],metrics[4])
recommendationservice_mem=np.genfromtxt(file, dtype=np.double)
recommendationservice_mem = recommendationservice_mem[:,np.newaxis]
# "shippingservice"
file = './data/boutique/train/1_{}_{}.log'.format(services[9],metrics[4])
shippingservice_mem=np.genfromtxt(file, dtype=np.double)
shippingservice_mem = shippingservice_mem[:,np.newaxis]

timeLen = len(adservice_cpu)
xx = torch.tensor([])
for i in range(timeLen):
    listreq = np.vstack((adservice_req[i], cartservice_req[i], checkoutservice_req[i], currencyservice_req[i], emailservice_req[i], frontend_req[i], paymentservice_req[i], productcatalogservice_req[i], recommendationservice_req[i], shippingservice_req[i]))
    listcpu = np.vstack((adservice_cpu[i], cartservice_cpu[i], checkoutservice_cpu[i], currencyservice_cpu[i], emailservice_cpu[i], frontend_cpu[i], paymentservice_cpu[i], productcatalogservice_cpu[i], recommendationservice_cpu[i], shippingservice_cpu[i]))
    listres = np.vstack((adservice_res[i], cartservice_res[i], checkoutservice_res[i], currencyservice_res[i], emailservice_res[i], frontend_res[i], paymentservice_res[i], productcatalogservice_res[i], recommendationservice_res[i], shippingservice_res[i]))
    listpod = np.vstack((adservice_pod[i], cartservice_pod[i], checkoutservice_pod[i], currencyservice_pod[i], emailservice_pod[i], frontend_pod[i], paymentservice_pod[i], productcatalogservice_pod[i], recommendationservice_pod[i], shippingservice_pod[i]))
    listmem = np.vstack((adservice_mem[i], cartservice_mem[i], checkoutservice_mem[i], currencyservice_mem[i], emailservice_mem[i], frontend_mem[i], paymentservice_mem[i], productcatalogservice_mem[i], recommendationservice_mem[i], shippingservice_mem[i]))

    listreq = torch.tensor(listreq, dtype=torch.float32).clone().detach()
    listcpu = torch.tensor(listcpu, dtype=torch.float32).clone().detach()
    listres = torch.tensor(listres, dtype=torch.float32).clone().detach()
    listpod = torch.tensor(listpod, dtype=torch.float32).clone().detach()
    listmem = torch.tensor(listmem, dtype=torch.float32).clone().detach()
    
    listt = torch.cat((listreq, listcpu, listres, listpod, listmem), dim=1)
    
    yy = torch.unsqueeze(listt, dim=0)
    xx = torch.cat((xx, yy), dim=0)

xx = xx.numpy()
print(xx.shape)
np.savez("./data/boutique/train", xx)  # 生成原始的序列数据

## for train 
all_data = read_and_generate_dataset(graph_signal_matrix_filename='./data/boutique/train.npz', 
                                        num_of_hours=24, 
                                        num_for_predict=120*24, 
                                        points_per_hour=120, 
                                        save=True)

