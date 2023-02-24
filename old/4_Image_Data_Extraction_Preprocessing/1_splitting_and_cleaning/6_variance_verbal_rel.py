
import json
import nltk
from nltk import word_tokenize
from collections import Counter


variance_verbal_rel = open('/home/sdg/Desktop/VG/variance_verbal_rel.json', 'w')
source = '/home/sdg/Desktop/VG/formatted_split1_scenegraph.json'
#out2 = open('/home/sdg/Desktop/VG/retry_var_spot.json', 'w')

d2 = {}

def spot_var(file):
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
#    json.load(d2)
    json.dump(d2, variance_verbal_rel)                            
    print(d2)


spot_var(source)


