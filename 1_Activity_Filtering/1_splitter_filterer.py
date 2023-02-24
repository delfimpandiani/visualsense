import json
import nltk
from nltk import word_tokenize
from collections import Counter
import os

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def create_split_paths(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(1, 11):
        split_path = os.path.join(directory, f'split{i}_scenegraph.json')
        if not os.path.exists(split_path):
            with open(split_path, 'w') as split_file:
                pass  # do nothing, file is created with no content

def split_maker(directory, original_data_source):
    create_split_paths(directory)
    split1 = open('../VG_data/VG_data_splits/split1_scenegraph.json', 'w')
    split2 = open('../VG_data/VG_data_splits/split2_scenegraph.json', 'w')
    split3 = open('../VG_data/VG_data_splits/split3_scenegraph.json', 'w')
    split4 = open('../VG_data/VG_data_splits/split4_scenegraph.json', 'w')
    split5 = open('../VG_data/VG_data_splits/split5_scenegraph.json', 'w')
    split6 = open('../VG_data/VG_data_splits/split6_scenegraph.json', 'w')
    split7 = open('../VG_data/VG_data_splits/split7_scenegraph.json', 'w')
    split8 = open('../VG_data/VG_data_splits/split8_scenegraph.json', 'w')
    split9 = open('../VG_data/VG_data_splits/split9_scenegraph.json', 'w')
    split10 = open('../VG_data/VG_data_splits/split10_scenegraph.json', 'w')

    with open(original_data_source) as f:
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
    print("splits created!")

    return

def filter_non_verbal_imgs(split_name):
    split_path = 'VG_data/VG_data_splits/' + split_name + '_scenegraph.json'
    verbal_rel = []
    verbal_imgs_path = 'VG_data/VG_data_verbal_imgs/' + split_name + "_verbal_images.json"
    if not os.path.exists(verbal_imgs_path):
        with open(verbal_imgs_path, 'w') as verbal_imgs:
            pass
    else:
        with open(verbal_imgs_path, 'w') as verbal_imgs:
            with open(split_path) as f:
                split_object = json.load(f)
                for image in split_object:
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
                                if s[1] in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
                                    if '.r.' not in rel['synsets']:
                                        verbal_rel.append(image['image_id'])
            #                            verbal_rel.append(rel['synsets'])
            verbal_imgs_dict = Counter(verbal_rel)
            json.dump(Counter(verbal_rel), verbal_imgs)
    print("finished the verbal investigation for split", split_name)
    return verbal_imgs_dict


#########################################################
####################### Execution #######################
#########################################################
# split_maker("VG_data/VG_data_splits", "VG_data/scene_graphs.json")

# for x in range(1, 11):
#     split_name = "split" + str(x)
#     filter_non_verbal_imgs(split_name)

