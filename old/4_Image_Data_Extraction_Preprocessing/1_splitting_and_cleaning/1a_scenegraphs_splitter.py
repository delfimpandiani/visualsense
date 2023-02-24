import json


split1 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split1_scenegraphs.json', 'w')
split2 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split2_scenegraph.json', 'w')
split3 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split3_scenegraph.json', 'w')
split4 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split4_scenegraph.json', 'w')
split5 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split5_scenegraph.json', 'w')
split6 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split6_scenegraph.json', 'w')
split7 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split7_scenegraph.json', 'w')
split8 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split8_scenegraph.json', 'w')
split9 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split9_scenegraph.json', 'w')
split10 = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/results_files/split10_scenegraph.json', 'w')


with open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/scenegraphs.json') as f:
    scene_graphs = json.load(f)
    json.dump(scene_graphs[0:10000], split1)
    json.dump(scene_graphs[10000:20000], split2)
    json.dump(scene_graphs[20000:30000], split3)
    json.dump(scene_graphs[30000:40000], split4)
    json.dump(scene_graphs[40000:50000], split5)
    json.dump(scene_graphs[50000:60000], split6)
    json.dump(scene_graphs[60000:70000], split7)
    json.dump(scene_graphs[70000:80000], split8)
    json.dump(scene_graphs[80000:90000], split9)
    json.dump(scene_graphs[90000:], split10)


