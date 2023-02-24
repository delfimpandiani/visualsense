import matplotlib.pyplot as plt
import json
from collections import defaultdict


ranked_imgs = '/home/sdg/Desktop/VG/quant_ranked_rel_split1.json'


with open(ranked_imgs) as f:
    dict_img = json.load(f)
    keys = dict_img.keys()
    values = dict_img.values()
 #   print(imgs_id)
    plt.plot(values, keys, linestyle="", marker="o", color='orange')
    ax = plt.gca()
    ax.axes.yaxis.set_ticks([])
#    ax.axes.xaxis.set_ticks([])
    plt.ylabel('Images')
    plt.xlabel('Number of occurrences of verbal relations per image')
    plt.title('Distribution of occurrences of verbal relations'+'\n'+'per image in scenegraph_split1.json')
    plt.show()
