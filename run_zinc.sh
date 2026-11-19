# python main_molecules_graph_regression.py --config 'ZINC_LapPE_BN.json' --seed 41 --full_graph 'False' --ctgt_flag 'False' | tee output/ZINC/zinc1.txt
# python main_molecules_graph_regression.py --config 'ZINC_LapPE_BN.json' --seed 41 --full_graph 'False' --ctgt_flag 'True' | tee output/ZINC/zinc2.txt
# python main_molecules_graph_regression.py --config 'ZINC_LapPE_BN.json' --seed 41 --full_graph 'True' --ctgt_flag 'False' | tee output/ZINC/zinc3.txt
python main_molecules_graph_regression.py --config 'ZINC_LapPE_BN.json' --seed 41 --full_graph 'True' --ctgt_flag 'True' | tee output/ZINC/zinc4.txt


# python main_molecules_graph_regression.py --config 'ZINC_LapPE_LN.json' --seed 41 --full_graph 'False' --ctgt_flag 'False' | tee output/ZINC/zinc5.txt
# python main_molecules_graph_regression.py --config 'ZINC_LapPE_LN.json' --seed 41 --full_graph 'False' --ctgt_flag 'True' | tee output/ZINC/zinc6.txt
# python main_molecules_graph_regression.py --config 'ZINC_LapPE_LN.json' --seed 41 --full_graph 'True' --ctgt_flag 'False' | tee output/ZINC/zinc7.txt
# python main_molecules_graph_regression.py --config 'ZINC_LapPE_LN.json' --seed 41 --full_graph 'True' --ctgt_flag 'True' | tee output/ZINC/zinc8.txt






# =======================================


# python main_molecules_graph_regression.py --config 'ZINC_LapPE_BN.json' --seed 41 --full_graph 'False' --ctgt_flag 'True' | tee output/ZINC/zinc1.txt