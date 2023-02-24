import json

split1 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split1_regiongraphs.json', 'w')
split2 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split2_regiongraphs.json', 'w')
split3 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split3_regiongraphs.json', 'w')
split4 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split4_regiongraphs.json', 'w')
split5 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split5_regiongraphs.json', 'w')
split6 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split6_regiongraphs.json', 'w')
split7 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split7_regiongraphs.json', 'w')
split8 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split8_regiongraphs.json', 'w')
split9 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split9_regiongraphs.json', 'w')
split10 = open('/home/sdg/Desktop/VG/regiongraphs_splits/split10_regiongraphs.json', 'w')


with open('/home/sdg/Desktop/VG/region_graphs.json') as f:
    region_graphs = json.load(f)
    json.dump(region_graphs[0:10000], split1)
    json.dump(region_graphs[10000:20000], split2)
    json.dump(region_graphs[20000:30000], split3)
    json.dump(region_graphs[30000:40000], split4)
    json.dump(region_graphs[40000:50000], split5)
    json.dump(region_graphs[50000:60000], split6)
    json.dump(region_graphs[60000:70000], split7)
    json.dump(region_graphs[70000:80000], split8)
    json.dump(region_graphs[80000:90000], split9)
    json.dump(region_graphs[90000:], split10)



