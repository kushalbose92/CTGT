import numpy as np
import torch
import time
import os
# %matplotlib inline
import matplotlib.pyplot as plt
import pickle
from torch_geometric.datasets import GNNBenchmarkDataset

from data.SBMs import SBMsDatasetDGL 
from data.data import LoadData
from torch.utils.data import DataLoader
from data.SBMs import SBMsDataset


class DotDict(dict):
    def __init__(self, **kwds):
        self.update(kwds)
        self.__dict__ = self

# sbm_obj = GNNBenchmarkDataset(root='data/SBMs/', name='PATTERN')
# print(sbm_obj)


# if not os.path.isfile('molecules_zinc_full.zip'):
#     print('downloading..')
#     curl https://www.dropbox.com/s/grhitgnuuixoxwl/molecules_zinc_full.zip?dl=1 -o molecules_zinc_full.zip -J -L -k
#     unzip molecules_zinc_full.zip -d ../
#     # !tar -xvf molecules_zinc_full.zip -C ../
# else:
#     print('File already downloaded')
    
    
# import os
# os.chdir('../../') # go to root folder of the project
# print(os.getcwd())



DATASET_NAME = 'SBM_PATTERN'
dataset = SBMsDatasetDGL(DATASET_NAME) 


print(len(dataset.train))
print(len(dataset.val))
print(len(dataset.test))

# print(dataset.train[0])
# print(dataset.val[0])
# print(dataset.test[0])


start = time.time()
with open('data/SBMs/SBM_PATTERN.pkl','wb') as f:
        pickle.dump([dataset.train,dataset.val,dataset.test],f)
print('Time (sec):',time.time() - start)



DATASET_NAME = 'SBM_PATTERN'
dataset = LoadData(DATASET_NAME)
trainset, valset, testset = dataset.train, dataset.val, dataset.test


batch_size = 10
collate = SBMsDataset.collate
print(SBMsDataset)
train_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True, collate_fn=collate)




    