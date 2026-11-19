import numpy as np
import torch
import pickle
import time
import os
# %matplotlib inline
import matplotlib.pyplot as plt
import pickle
from torch_geometric.datasets import ZINC

from data.molecules import MoleculeDatasetDGL 
from data.data import LoadData
from torch.utils.data import DataLoader
from data.molecules import MoleculeDataset



# zinc_obj = ZINC(root='data/molecules/ZINC/', subset=True, split= 'train', transform = None, pre_transform = None, pre_filter = None, force_reload = False)
# print(zinc_obj)


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



DATASET_NAME = 'ZINC'
dataset = MoleculeDatasetDGL(DATASET_NAME) 


print(len(dataset.train))
print(len(dataset.val))
print(len(dataset.test))

# print(dataset.train[0])
# print(dataset.val[0])
# print(dataset.test[0])


num_atom_type = 28
num_bond_type = 4

start = time.time()
with open('data/molecules/ZINC.pkl','wb') as f:
        pickle.dump([dataset.train,dataset.val,dataset.test,num_atom_type,num_bond_type],f)
print('Time (sec):',time.time() - start)


DATASET_NAME = 'ZINC'
dataset = LoadData(DATASET_NAME)
trainset, valset, testset = dataset.train, dataset.val, dataset.test



batch_size = 10
collate = MoleculeDataset.collate
print(MoleculeDataset)
train_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True, collate_fn=collate)




    