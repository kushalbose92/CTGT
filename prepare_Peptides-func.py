# import torch 
# from torch_geometric.datasets import LRGBDataset 

# obj = LRGBDataset(root = 'LRGB/', name = 'Peptides-func', split = 'train')
# print(obj)




import numpy as np
import torch
import pickle
import time
import os

import pickle
import os


from data.lrgb import LRGBDatasetDGL
from data.data import LoadData
from torch.utils.data import DataLoader

start = time.time()

DATASET_NAME = 'Peptides-func'
dataset = LRGBDatasetDGL(DATASET_NAME) 

print('Time (sec):',time.time() - start) # 356s=6min


start = time.time()

with open('data/LRGB/Peptides-func.pkl','wb') as f:
        pickle.dump([dataset.train,dataset.val,dataset.test],f)
        
print('Time (sec):',time.time() - start) # 38s

# DATASET_NAME = 'MNIST'
# dataset = LoadData(DATASET_NAME) # 54s
# trainset, valset, testset = dataset.train, dataset.val, dataset.test

# start = time.time()

# batch_size = 10
# collate = SuperPixDataset.collate
# train_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True, collate_fn=collate)

# print('Time (sec):',time.time() - start) # 0.0003s

    