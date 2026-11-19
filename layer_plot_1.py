import matplotlib.pyplot as plt
import numpy as np
import os

layers = [1,2,3,4,5]

mnist = [97.99, 97.94, 97.93, 98.14, 97.95]
mnist_error = [0.0434, 0.1079, 0.1106, 0.1150, 0.1027]

cifar = [69.73, 70.35, 69.74, 68.90, 68.41]
cifar_error = [0.4065, 0.8049, 1.0306, 0.6105, 0.4132]

pattern = [86.5934, 72.1319, 71.7307, 49.7398, 50.6224]
pattern_error = [1.1089, 2.0838, 1.5490, 1.0454, 0.0263]

cluster = [76.7499, 23.5413, 24.2993, 28.6753, 21.5919]
cluster_error = [2.1176, 2.0666, 1.0775, 2.0782, 1.0367]

molhiv = [0.7762, 0.7893, 0.7604, 0.7295, 0.7535]
molhiv_error = [0.0089, 0.0051, 0.0032, 0.0092, 0.0056]


# mnist
plt.errorbar(layers, mnist, yerr = mnist_error, color = 'darkcyan', marker = 'o', linewidth=3, markersize = 6)
# plt.plot(layers, mnist, color = 'darkcyan', marker='o', linewidth=3, markersize=12)
# plt.fill_between(layers, zinc - zinc_error, zinc + zinc_error, alpha=0.2)
plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("Accuracy", fontsize=23)
plt.yticks([95.0, 96.0, 97.0, 98.0, 99.0, 100.0], [r'$95.0$', r'$96.0$', r'$97.0$', r'$98.0$', r'$99.0$', r'$100.0$'], fontsize=17)
plt.xticks([1,2,3,4,5], fontsize=17)
plt.savefig(os.getcwd() + "/mnist.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()

# cifar10
plt.errorbar(layers, cifar, yerr = cifar_error, color = 'darkorange', linewidth=3)
# plt.fill_between(layers, zinc - zinc_error, zinc + zinc_error, alpha=0.2)
plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("Accuracy", fontsize=23)
plt.yticks([60.0, 65.0, 70.0, 75.0, 80.0], [r'$60.0$', r'$65.0$', r'$70.0$', r'$75.0$', r'$80.0$'], fontsize=17)
plt.xticks([1,2,3,4,5], fontsize=17)
plt.savefig(os.getcwd() + "/cifar10.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()

# # pattern
plt.errorbar(layers, pattern, yerr = pattern_error,  color = 'firebrick', linewidth=3)
plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("Accuracy", fontsize=23)
plt.yticks([0.0, 20.0, 40.0, 60.0, 80.0, 100.0], [r'$0.0$', r'$20.0$', r'$40.0$', r'$60.0$', r'$80.0$', r'$100.0$'], fontsize=17)
plt.xticks([1,2,3,4,5], fontsize=17)
plt.savefig(os.getcwd() + "/pattern.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()

# cluster
plt.errorbar(layers, cluster, yerr=cluster_error, color = 'darkgoldenrod', linewidth=3)
plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("Accuracy", fontsize=23)
plt.yticks([0.0, 20.0, 40.0, 60.0, 80.0, 100.0], [r'$0.0$', r'$20.0$', r'$40.0$', r'$60.0$', r'$80.0$', r'$100.0$'], fontsize=17)
plt.xticks([1,2,3,4,5], fontsize=17)
plt.savefig(os.getcwd() + "/cluster.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()

# molhiv
plt.errorbar(layers, molhiv, yerr=molhiv_error, color = 'steelblue', linewidth=3)
plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("ROC-AUC", fontsize=23)
plt.yticks([0.65, 0.70, 0.75, 0.80, 0.85], [r'$0.65$', r'$0.70$', r'$0.75$', r'$0.80$', r'$0.85$'], fontsize=17)
plt.xticks([1,2,3,4,5], fontsize=17)
plt.savefig(os.getcwd() + "/molhiv.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()


