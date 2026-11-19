import matplotlib.pyplot as plt
import numpy as np
import os

layers = [1,2,3,4,5,6]

zinc_1 = [0.1547, 0.1540, 0.1553, 0.1543]
zinc_2 = [0.1404, 0.1445, 0.1445, 0.1437]
zinc_3 = [0.1500, 0.1496, 0.1510, 0.1504]
zinc_4 = [1.5473, 1.5444, 1.5461, 1.5460]
zinc_5 = [1.5455, 1.5424, 1.5457, 1.5463]
zinc_6 = [1.5461, 1.5451, 1.5446, 1.5459]



# zinc = [0.1547, 0.1404, 0.1500, 1.5473, 1.5455, 1.5461]
# pattern = [86.3437, 85.4177, 84.7457, 85.3353, 84.0029, 76.4241]
# cluster = [77.1934, 16.8132, 77.8009, 77.9582, 75.4408, 73.4174]
# molhiv = [0.7754, 0.801, 0.7497, 0.6983, 0.7458, 0.76]


# Generate some example data
data = [zinc_1, zinc_2, zinc_3, zinc_4, zinc_5, zinc_6]
     

# Create a figure and axis object
# fig, ax = plt.subplots()

# Create the box plot with a red box and whiskers
boxplot = plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='red'), showfliers=False)

# Set the color of the median line to blue
# for median in boxplot['medians']:
#     median.set(color='black')

# # Set the color of the whiskers and caps to green
# for whisker, cap in zip(boxplot['whiskers'], boxplot['caps']):
#     whisker.set(color='black')
#     cap.set(color='black')

# # Set the x-axis labels
# ax.set_xticklabels(['1', '2', '3', '4', '5', '6'])

# # Set the y-axis label
# ax.set_ylabel('MAE')

# plt.savefig(os.getcwd() + "/zinc_box.png")

# # Show the plot
# plt.show()

plt.xlabel("Number of layers", fontsize=23)
plt.ylabel("MAE", fontsize=23)
plt.yticks([0.0, 0.4, 0.8, 1.2, 1.6], [r'$0.0$', r'$0.4$', r'$0.8$', r'$1.2$', r'$1.6$'], fontsize=17)
plt.xticks([1,2,3,4,5,6], fontsize=17)
plt.savefig(os.getcwd() + "/zinc.png", bbox_inches='tight', pad_inches=0.2)
plt.tight_layout()
plt.close()