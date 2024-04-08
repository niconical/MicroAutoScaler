import os
import sys
import yaml
import torch
import argparse
import trainer
from utils import scaler
from models import AdapGL
from dataset import TPDataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt


def load_config(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def main(args):
    model_config = load_config(args.model_config_path)
    train_config = load_config(args.train_config_path)
    torch.manual_seed(train_config['seed'])
    # ----------------------- Load data ------------------------
    Scaler = getattr(sys.modules['utils.scaler'], train_config['scaler'])
    data_scaler = Scaler(axis=(0, 1, 2))

    data_config = model_config['dataset']
    data_names = ('train_r6ssj.npz', 'valid_r6ssj.npz', 'test_r6ssj.npz')
    data_loaders = []
    for data_name in data_names:
        dataset = TPDataset(os.path.join(data_config['train_data_dir'], data_name))
        if data_name == 'train_r6ssj.npz':
            data_scaler.fit(dataset.data['x'])
        dataset.fit(data_scaler)
        data_loader = DataLoader(dataset, batch_size=data_config['batch_size'])
        data_loaders.append(data_loader)

    # --------------------- Trainer setting --------------------
    net_name = args.model_name
    net_config = model_config[net_name]
    net_config.update(data_config)

    Model = getattr(AdapGL, net_name, None)
    if Model is None:
        raise ValueError('Model {} is not right!'.format(net_name))
    net_pred = Model(**net_config)

    net_graph = AdapGL.GraphLearn(net_config['num_nodes'], net_config['init_feature_num'])

    optimizer_pred = torch.optim.Adam(
        net_pred.parameters(),
        lr=train_config['learning_rate'],
        weight_decay=train_config['weight_decay']
    )
    optimizer_graph = torch.optim.Adam(net_graph.parameters(), lr=train_config['learning_rate'])

    sc = train_config.get('lr_scheduler', None)
    if sc is None:
        scheduler_pred, scheduler_graph = None, None
    else:
        Scheduler = getattr(sys.modules['torch.optim.lr_scheduler'], sc.pop('name'))
        scheduler_pred = Scheduler(optimizer_pred, **sc)
        scheduler_graph = None

    # --------------------------- Train -------------------------
    net_trainer = trainer.AdapGLTrainer(
        net_config['adj_mx_path'], net_pred, net_graph, optimizer_pred, optimizer_graph,
        scheduler_pred, scheduler_graph, args.num_epoch, args.num_iter,
        args.max_graph_num, data_scaler, args.model_save_path
    )
    net_trainer.train(data_loaders[0], data_loaders[1])
    y_pred, y_true = net_trainer.test(data_loaders[-1])    
    plot_results(y_true,y_pred)

def plot_results(y_true, y_pred, node_index=5, dpi=300, save_path='compare_frontend.png'):
    y_true = y_true[:, :, node_index].flatten()  # 选择第node_index个节点的真实值，并将其转换为一维数组
    y_pred = y_pred[:, :, node_index].flatten()  # 选择第node_index个节点的预测值，并将其转换为一维数组
    plt.figure(figsize=(10, 6))  # 创建一个新的图形，设置图形的大小
    plt.plot(y_true, label='True', linestyle='-', color='b')  # 绘制真实值的线
    plt.plot(y_pred, label='Predicted', linestyle='--', color='r')  # 绘制预测值的线
    plt.title('True vs Predicted')  # 设置标题
    plt.xlabel('Time Step')  # 设置x轴标签
    plt.ylabel('Value')  # 设置y轴标签
    plt.legend(loc='upper right')  # 设置图例位置
    plt.grid(True)  # 显示网格
    plt.savefig(save_path, dpi=dpi)  # 保存图形到指定路径，设置dpi为300
    plt.close()  # 关闭图形

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_config_path', type=str, default='config/train_dataset_speed.yaml',
                        help='Config path of models')
    parser.add_argument('--train_config_path', type=str, default='config/train_config.yaml',
                        help='Config path of Trainer')
    parser.add_argument('--model_name', type=str, default='AdapGLA', help='Model name to train')
    parser.add_argument('--num_epoch', type=int, default=200, help='Training times per epoch')
    parser.add_argument('--num_iter', type=int, default=30, help='Maximum value for iteration')
    parser.add_argument('--model_save_path', type=str, default='model_states/AdapGLA_boutique/AdapGLA_boutique.pkl',
                        help='Model save path')                 
    parser.add_argument('--max_graph_num', type=int, default=1, help='Volume of adjacency matrix set')
    args = parser.parse_args()

    main(args)