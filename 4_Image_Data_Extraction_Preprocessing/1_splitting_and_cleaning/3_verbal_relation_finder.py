
import json
import nltk
from nltk import word_tokenize
from collections import Counter


interesting = open('/home/sdg/Desktop/VG/interesting_images.json', 'w')
source = '/home/sdg/Desktop/VG/formatted_split1_scenegraph.json'

verbal_rel = []

def find_verbal_rel(file):
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
#                            if rel['synsets'] != 'Along.r.1':
                                if '.r.' not in rel['synsets']:
                                    verbal_rel.append(image['image_id'])
#                            verbal_rel.append(rel['synsets'])
    json.dump(Counter(verbal_rel), interesting)

find_verbal_rel(source)




