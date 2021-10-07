import matplotlib.pyplot as plt
import json
from collections import defaultdict


ranked_imgs = '/home/sdg/Desktop/VG/variance_ranked_split1.json'

def plotter(file):
    with open(file) as f:
        img = json.load(f)
        k = img.keys()
        v = img.values()
    #   print(imgs_id)
        plt.plot(v, k, linestyle="", marker="o", color='orange')
        ax = plt.gca()
        ax.axes.yaxis.set_ticks([])
        #    ax.axes.xaxis.set_ticks([])
        plt.ylabel('Images')
        plt.xlabel('Number of unique verbal relations per image')
        plt.title('Distribution of unique verbal relations'+'\n'+'per image in scenegraph_split1.json')
        plt.show()

plotter(ranked_imgs)