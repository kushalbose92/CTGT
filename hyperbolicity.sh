python main_molecules_graph_regression.py --config 'ZINC_LapPE_Hyperboloid_HGCN.json' | tee zinc.txt
python main_SBMs_node_classification.py --config 'PATTERN_LapPE_Hyperboloid_HGCN.json' | tee pattern.txt
python main_SBMs_node_classification.py --config 'CLUSTER_LapPE_Hyperboloid_HGCN.json' | tee cluster.txt
python main_superpixels_graph_classification.py --config 'MNIST_LapPE_Hyperboloid_HGCN.json' | tee mnist.txt
python main_superpixels_graph_classification.py --config 'CIFAR_LapPE_Hyperboloid_HGCN.json' | tee cifar.txt
