import torch 
import torch.nn as nn 
import pickle
import time 
from torch_geometric.datasets import LRGBDataset
import dgl 
import os 
from tqdm import tqdm 
from scipy import sparse as sp
import numpy as np 


# data_obj = LRGBDataset(root = 'lrgb/', name = 'COCO-SP',  split = 'train')
# print(data_obj[0])

# data = data_obj[0]
# print(data.x.shape)
# print(data.edge_index.shape)
# print(data.y)

class load_LRGBDataSetDGL(torch.utils.data.Dataset):
    
    def __init__(self,
                 data_dir,
                 name,
                 split):

        self.split = split
        self.is_test = split.lower() in ['test', 'val'] 
        if name == 'Peptides-struct' or name == 'Peptides-func':
            with open(os.path.join(data_dir, name + '/%s.pt' % self.split), 'rb') as f:
                self.dataset = torch.load(f)
        else:    
            with open(os.path.join(data_dir, name + '/%s.pickle' % self.split), 'rb') as f:
                self.dataset = pickle.load(f)
        self.node_labels = []
        self.graph_lists = []
        self.n_samples = len(self.dataset)
        self._prepare()
    

    def _prepare(self):

        print("preparing %d graphs for the %s set..." % (self.n_samples, self.split.upper()))

        for data in tqdm(self.dataset):
            # print(data)
            # print("node features ", data[0].shape)
            # print("edge features ", data[1].shape)
            # print("edge index ", data[2].shape)
            # print("node labels ", data[3].shape)
           
            node_features = data[0]
            edge_list = data[2]
            # Create the DGL Graph
            g = dgl.graph((edge_list[0], edge_list[1]), num_nodes=node_features.shape[0])
            g.ndata['feat'] = node_features.long()
            g.edata['feat'] = data[1]

            self.graph_lists.append(g)
            self.node_labels.append(data[3])
            # print(g)


    def __len__(self):
        """Return the number of graphs in the dataset."""
        return self.n_samples

    def __getitem__(self, idx):
        """
            Get the idx^th sample.
            Parameters
            ---------
            idx : int
                The sample index.
            Returns
            -------
            (dgl.DGLGraph, int)
                DGLGraph with node feature stored in `feat` field
                And its label.
        """
        return self.graph_lists[idx], self.node_labels[idx]


class LRGBDatasetDGL(torch.utils.data.Dataset):

    def __init__(self, name):
        """
            TODO
        """
        start = time.time()
        print("[I] Loading data ...")
        self.name = name
        data_dir = 'data/LRGB'
        self.train = load_LRGBDataSetDGL(data_dir, name, split='train')
        self.test = load_LRGBDataSetDGL(data_dir, name, split='test')
        self.val = load_LRGBDataSetDGL(data_dir, name, split='val')
        print("[I] Finished loading.")
        print("[I] Data load time: {:.4f}s".format(time.time()-start))


def laplacian_positional_encoding(g, pos_enc_dim):
    """
        Graph positional encoding v/ Laplacian eigenvectors
    """

    # Laplacian
    #A = g.adjacency_matrix_scipy(return_edge_ids=False).astype(float)
    A = g.adj_external(scipy_fmt="csr")
    N = sp.diags(dgl.backend.asnumpy(g.in_degrees()).clip(1) ** -0.5, dtype=float)
    L = sp.eye(g.number_of_nodes()) - N * A * N

    # Eigenvectors with scipy
    #EigVal, EigVec = sp.linalg.eigs(L, k=pos_enc_dim+1, which='SR')
    EigVal, EigVec = sp.linalg.eigs(L, k=pos_enc_dim+1, which='SR', tol=1e-2) # for 40 PEs
    EigVec = EigVec[:, EigVal.argsort()] # increasing order
    g.ndata['lap_pos_enc'] = torch.from_numpy(EigVec[:,1:pos_enc_dim+1]).float() 

    return g

# random walk positional encodings
def rand_walk_positional_encoding(g, pos_enc_dim):
    """
        Initializing positional encoding with RWPE
    """
    
    n = g.number_of_nodes()

    # Geometric diffusion features with Random Walk
    #A = g.adjacency_matrix(scipy_fmt="csr")
    A = g.adj_external(scipy_fmt="csr")
    Dinv = sp.diags(dgl.backend.asnumpy(g.in_degrees()).clip(1) ** -1.0, dtype=float) # D^-1
    RW = A * Dinv  
    M = RW
    
    # Iterate
    nb_pos_enc = pos_enc_dim
    PE = [torch.from_numpy(M.diagonal()).float()]
    M_power = M
    for _ in range(nb_pos_enc-1):
        M_power = M_power * M
        PE.append(torch.from_numpy(M_power.diagonal()).float())
    PE = torch.stack(PE,dim=-1)
    g.ndata['rw_pos_enc'] = PE  
    
    return g


class LRGBDataset(torch.utils.data.Dataset):

    def __init__(self, name):
        """
            Loading LRGB datasets
        """
        start = time.time()
        print("[I] Loading dataset %s..." % (name))
        self.name = name
        data_dir = 'data/LRGB/'
        with open(data_dir+name+'.pkl',"rb") as f:
            f = pickle.load(f)
            self.train = f[0]
            self.val = f[1]
            self.test = f[2]
        print('train, test, val sizes :',len(self.train),len(self.test),len(self.val))
        print("[I] Finished loading.")
        print("[I] Data load time: {:.4f}s".format(time.time()-start))


    # form a mini batch from a given list of samples = [(graph, label) pairs]
    def collate(self, samples):
        # The input samples is a list of pairs (graph, label).
        graphs, labels = map(list, zip(*samples))
        for c in range(len(labels)):
            labels[c] = torch.tensor(np.array(labels[c], dtype=np.float32))
        # labels = torch.from_numpy(np.array(labels))
        labels = torch.cat(labels).long()
        for idx, graph in enumerate(graphs):
            graphs[idx].ndata['feat'] = graph.ndata['feat'].float()
            graphs[idx].edata['feat'] = graph.edata['feat'].float()
        batched_graph = dgl.batch(graphs)
    
        return batched_graph, labels
    
    # def _add_self_loops(self):
        
        # function for adding self loops
        # this function will be called only if self_loop flag is True
            
        # self.train.graph_lists = [self_loop(g) for g in self.train.graph_lists]
        # self.val.graph_lists = [self_loop(g) for g in self.val.graph_lists]
        # self.test.graph_lists = [self_loop(g) for g in self.test.graph_lists]
        
    # def _make_full_graph(self):
        
        # function for converting graphs to full graphs
        # this function will be called only if full_graph flag is True
    #     self.train.graph_lists = [make_full_graph(g) for g in self.train.graph_lists]
    #     self.val.graph_lists = [make_full_graph(g) for g in self.val.graph_lists]
    #     self.test.graph_lists = [make_full_graph(g) for g in self.test.graph_lists]


    def _add_laplacian_positional_encodings(self, pos_enc_dim):
        
        # Graph positional encoding v/ Laplacian eigenvectors
        self.train.graph_lists = [laplacian_positional_encoding(g, pos_enc_dim) for g in tqdm(self.train.graph_lists)]
        self.val.graph_lists = [laplacian_positional_encoding(g, pos_enc_dim) for g in tqdm(self.val.graph_lists)]
        self.test.graph_lists = [laplacian_positional_encoding(g, pos_enc_dim) for g in tqdm(self.test.graph_lists)]

    def _add_rand_walk_positional_encodings(self, pos_enc_dim):
        
        # Graph positional encoding v/ Laplacian eigenvectors
        self.train.graph_lists = [rand_walk_positional_encoding(g, pos_enc_dim) for g in tqdm(self.train.graph_lists)]
        self.val.graph_lists = [rand_walk_positional_encoding(g, pos_enc_dim) for g in tqdm(self.val.graph_lists)]
        self.test.graph_lists = [rand_walk_positional_encoding(g, pos_enc_dim) for g in tqdm(self.test.graph_lists)]

    # def _add_wl_positional_encodings(self):
        
    #     # WL positional encoding from Graph-Bert, Zhang et al 2020.
    #     self.train.graph_lists = [wl_positional_encoding(g) for g in self.train.graph_lists]
    #     self.val.graph_lists = [wl_positional_encoding(g) for g in self.val.graph_lists]
    #     self.test.graph_lists = [wl_positional_encoding(g) for g in self.test.graph_lists]




