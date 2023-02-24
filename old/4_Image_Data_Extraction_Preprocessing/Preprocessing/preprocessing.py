import json
import string
import re
import matplotlib.pyplot as plt
from collections import defaultdict
import nltk
from nltk import word_tokenize
from collections import Counter
from os import stat



def format_obj_syn():
    out = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/correct_syn_scenegraph1.json', 'w')
    scenes_file = "/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/out_scenegraph1.json"
     # put the path of the file
    with open(scenes_file) as f:
        scenegraph = json.load(f)
        for jsonObj in scenegraph:
            for obj in jsonObj['objects']:
                for syn in obj['synsets']:
                    for v in syn:
                        # These replace numbers with "0" before in numbers without
                        obj['synsets'] = str(obj['synsets']).replace("01", "1")
                        obj['synsets'] = str(obj['synsets']).replace("02", "2")
                        obj['synsets'] = str(obj['synsets']).replace("03", "3")
                        obj['synsets'] = str(obj['synsets']).replace("04", "4")
                        obj['synsets'] = str(obj['synsets']).replace("05", "5")
                        obj['synsets'] = str(obj['synsets']).replace("06", "6")
                        obj['synsets'] = str(obj['synsets']).replace("07", "7")
                        obj['synsets'] = str(obj['synsets']).replace("08", "8")
                        obj['synsets'] = str(obj['synsets']).replace("09", "9")
                        # This lowercase all the synsets (some of them are in caps lock for no reason)
                        obj['synsets'] = str(obj['synsets']).lower()
                        # These replace the squared brackets and the apostrophe
                        obj['synsets'] = str(obj['synsets']).replace('[', '')
                        obj['synsets'] = str(obj['synsets']).replace(']', '')
                        obj['synsets'] = str(obj['synsets']).replace("'", "")
                        # This capitalize only the first character of the string
                        obj['synsets'] = string.capwords(obj['synsets'])
                        # Honestly? I don't remember what this was for, it was used in the frame extraction pipeline
                        obj['synsets'] = re.sub(r"\([^()]*\)", "", obj['synsets'])
            # Finally we dump everything in the main file           
        json.dump(scenegraph, out)
        return

def format_rel_syns():
    out = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/correct_syn_scenegraph1.json', 'w')
    scenes_file = "/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/out_scenegraph1.json"
    # put the path of the file
    with open(scenes_file) as f:
        scenegraph = json.load(f)
        for jsonObj in scenegraph:
            for rel in jsonObj['relationships']:
                for syn in rel['synsets']:
                    # These replace numbers with "0" before in numbers without
                    rel['synsets'] = str(rel['synsets']).replace("01", "1")
                    rel['synsets'] = str(rel['synsets']).replace("02", "2")
                    rel['synsets'] = str(rel['synsets']).replace("03", "3")
                    rel['synsets'] = str(rel['synsets']).replace("04", "4")
                    rel['synsets'] = str(rel['synsets']).replace("05", "5")
                    rel['synsets'] = str(rel['synsets']).replace("06", "6")
                    rel['synsets'] = str(rel['synsets']).replace("07", "7")
                    rel['synsets'] = str(rel['synsets']).replace("08", "8")
                    rel['synsets'] = str(rel['synsets']).replace("09", "9")
                    # This lowercase all the synsets (some of them are in caps lock for no reason)
                    rel['synsets'] = str(rel['synsets']).lower()
                    # These replace the squared brackets and the apostrophe
                    rel['synsets'] = str(rel['synsets']).replace('[', '')
                    rel['synsets'] = str(rel['synsets']).replace(']', '')
                    rel['synsets'] = str(rel['synsets']).replace("'", "")
                    # This capitalize only the first character of the string
                    rel['synsets'] = string.capwords(rel['synsets'])
                    # Honestly? I don't remember what this was for, it was used in the frame extraction pipeline
                    rel['synsets'] = re.sub(r"\([^()]*\)", "", rel['synsets'])
    # Finally we dump everything in the main file           
    json.dump(scenegraph, out)
    return

def find_verbal_rel():
    interesting = open('/home/sdg/Desktop/VG/interesting_images.json', 'w')
    file = '/home/sdg/Desktop/VG/formatted_split1_scenegraph.json'
    verbal_rel = []
    with open(file) as f:
        split1 = json.load(f)
        for image in split1:
            for rel in image['relationships']:
                preds = rel["predicate"]
            # since some of the relationships are written in caps lock the pos_tag label them as NN, while they are VB,
            # next step is necessary to lowercase them and allow pos_tag to correctly tag them.
                if isinstance(preds, str):
                    preds = preds.lower()
                    tok = word_tokenize(preds)
                # tag the part of speech for each value
                    verbs = nltk.pos_tag(tok)
                    for s in verbs:
                # checks the PoS, all the acronyms are forms of flexed verbs
                        if s[1] in ('VB','VBD' ,'VBG', 'VBN' ,'VBP' ,'VBZ'):
                            # if rel['synsets'] != 'Along.r.1':
                            if '.r.' not in rel['synsets']:
                                verbal_rel.append(image['image_id'])
                                # verbal_rel.append(rel['synsets'])
    json.dump(Counter(verbal_rel), interesting)
    return

def img_rank_1():
    file = '/home/sdg/Desktop/VG/interesting_images.json'
    out = open('/home/sdg/Desktop/VG/quant_ranked_rel_split1.json', 'w')
    ranked_img = dict()
    with open(file) as f:
        imgs = json.load(f)
        imgs_sorted = sorted(imgs.items(), key=lambda x:x[1], reverse=True)
        # print(imgs_sorted)
        for img_id, occurr_numb in imgs_sorted:
            ranked_img.setdefault(img_id, []).append(occurr_numb)
    json.dump(ranked_img, out)
    print(ranked_img)
    return

def img_rank_1_plotter():
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
    return

def spot_variance():
    variance_verbal_rel = open('/home/sdg/Desktop/VG/variance_verbal_rel.json', 'w')
    file = '/home/sdg/Desktop/VG/formatted_split1_scenegraph.json'
    # out2 = open('/home/sdg/Desktop/VG/retry_var_spot.json', 'w')
    d2 = {}
    with open(file) as f:
        split1 = json.load(f)
        for image in split1:
            for rel in image['relationships']:
                preds = rel["predicate"]
                if isinstance(preds, str):
                    preds = preds.lower()
                    tok = word_tokenize(preds)
                    verbs = nltk.pos_tag(tok)
                    for s in verbs:
                        if s[1] in ('VB' ,'VBD' ,'VBG' ,'VBN' ,'VBP' ,'VBZ'):
                            if '.r.' not in rel['synsets']:
                                if len(rel['synsets']) > 0:
                                    d2.setdefault(image['image_id'], []).append(rel['synsets'])
    # json.load(d2)
    json.dump(d2, variance_verbal_rel)                            
    print(d2)
    return

def img_rank_2():
    file = '/home/sdg/Desktop/VG/variance_verbal_rel.json'
    out = open('/home/sdg/Desktop/VG/variance_ranked_split1.json', 'w')
    d1 = {}
    d2 = {}
    d3 = {}
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
    json.dump(d3, out)
    # print(d3)
    d4 = {key1:val1 for key1,val1 in sorted(d3.items(), key = lambda item: item[1])}
    d5 = sorted(d4, key=d4.get, reverse=True)[:100]
    # to better find all interesting images we are also creating a dictionary for the location of these image_id,
    # in order to be able to retrieve them in the frame evocation pipeline and later steps
    d6 = {'Split_1': d5}
    print(d6)
    return

def img_rank_2_plotter():
    file = '/home/sdg/Desktop/VG/variance_ranked_split1.json'
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
    return


f = open("split1_regions.json")
f1 = open('split1_scenegraphs.json')
split1_regions = json.load(f)
split1_scenegraphs = json.load(f1)

# format_obj_syn()
# format_rel_syns()
# find_verbal_rel()
# img_rank_1()
# img_rank_1_plotter()
# spot_variance()
# img_rank_2()
# img_rank_2_plotter()

