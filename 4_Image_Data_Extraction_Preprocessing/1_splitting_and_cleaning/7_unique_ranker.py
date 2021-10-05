
import json
from os import stat

source = '/home/sdg/Desktop/VG/variance_verbal_rel.json'
out = open('/home/sdg/Desktop/VG/variance_ranked_split1.json', 'w')

d1 = {}
d2 = {}
d3 = {}

def f1(file):
    with open(file) as f:
        imgs = json.load(f)
        for k, v in imgs.items():
            # create a new dict with unique values
            d1[k] = list(set(v))
            # create another dict taking as value the lenght of the list of unique values
            d2[k] = len(list(set(v)))
            # create a final dict in which items are sorted by the number of items in each list of values
            unique_list = sorted(d2.items(), key=lambda x:x[1], reverse=True)
            for x in unique_list:
                d3.setdefault(x[0], x[1])

#    print(d3)

f1(source)
json.dump(d3, out)



d4 = {key1:val1 for key1,val1 in sorted(d3.items(), key = lambda item: item[1])}
d5 = sorted(d4, key=d4.get, reverse=True)[:100]


# to better find all interesting images we are also creating a dictionary for the location of these image_id,
# in order to be able to retrieve them in the frame evocation pipeline and later steps
d6 = {'Split_1': d5}
print(d6)