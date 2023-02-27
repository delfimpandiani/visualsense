import requests
import rdflib
from rdflib import Literal, URIRef, Namespace
import json
import os
import pandas as pd
import csv
import time

def initialize_globals():
    global headers
    headers = {
        'accept': 'text/turtle',
        'Authorization': 'insert FRED key', # if you don't have one, please contact stefano.de.giorgis@gmail.com
    }
    global all_names
    all_names = [Namespace("https://w3id.org/framester/wn/wn30/"), Namespace("https://w3id.org/framester/vn/vn31/data/"), Namespace("<http://dbpedia.org/resource/"), Namespace("https://w3id.org/framester/data/framestercore/"), Namespace("https://w3id.org/framester/pb/pbdata/"), Namespace("https://w3id.org/framester/framenet/abox/gfe/"), Namespace("https://w3id.org/framester/pb/pbschema/"), Namespace("https://w3id.org/framester/wn/wn30/wordnet-verbnountropes/"), Namespace("https://w3id.org/framester/data/framesterrole/"), Namespace("http://babelnet.org/rdf/"), Namespace("https://w3id.org/framester/framenet/abox/fe/"), Namespace("https://w3id.org/framester/framenet/abox/frame/"), Namespace("https://w3id.org/framester/data/framestersyn/") ]
    global generic_emo_frames
    generic_emo_frames = ['https://w3id.org/framester/data/framestercore/EmotionActive', 'https://w3id.org/framester/data/framestercore/EmotionsByStimulus', 'https://w3id.org/framester/data/framestercore/EmotionsSuccessOrFailure', 'https://w3id.org/framester/data/framestercore/EmotionDirected', 'https://w3id.org/framester/data/framestercore/EmotionHeat', 'https://w3id.org/framester/data/framestercore/CauseEmotion', 'https://w3id.org/framester/data/framestercore/EmotionsOfMentalActivity']
    global generic_value_frames
    generic_value_frames = ['https://w3id.org/framester/data/framestercore/MoralityEvaluation', 'https://w3id.org/framester/data/framestercore/PeopleByMorality']
    global valuefile
    valuefile = "knowledge_extraction_sources/mftriggers_dictionary.csv"
    global emofile
    emofile = "knowledge_extraction_sources/BE_emotion_dictionary.csv"
    global bhvfile
    bhvfile = 'knowledge_extraction_sources/bhv_dictionary.csv'
    global folkfile
    folkfile = 'knowledge_extraction_sources/taf_dictionary.csv'
    global isaac
    isaac = URIRef('http://www.ontologydesignpatterns.org/ont/is/isaac_vanilla.owl#')
    global haidt
    haidt = URIRef('https://w3id.org/spice/SON/HaidtValues#')
    global valuetriggers
    valuetriggers = URIRef('http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl#triggers')
    global emotriggers
    emotriggers = URIRef('http://www.ontologydesignpatterns.org/ont/emotions/EmoCore.owl#triggers')
    global istriggers
    istriggers = URIRef('http://www.ontologydesignpatterns.org/ont/is/isnet.owl#activates')
    global graphFor
    graphFor = URIRef('https://w3id.org/sdg/meta#graphFor')
    return

def output_as_csv(df, path, out_file_path, header):
    # This function is to write the output in a new file
    if not os.path.isfile(out_file_path):
        df.to_csv(out_file_path, index=False, header=header, sep="\t")
    else:
        df.to_csv(out_file_path, mode='a', index=False, header=False, sep="\t")
    return

def build_dict(file):
    # This function is to create (and return) a dictionary out of the desired csv file, in this script are Values, but it could be anything
    with open(file) as ttl_file:
        input_file = csv.DictReader(open(file))
        for row in input_file:
            return {row['s'] :row['o'] for row in input_file}

def img_knowledge_extraction(split_name, split_region_graphs, image_id):
    # This function takes as input a certain split and some image_id, then it generates the knowledge graphs from FRED,
    # checks for value, emotions and general frame activation, and give as output a turtle file for each image region and
    # a general csv file with knowledge extracted
    valuedict = build_dict(valuefile)
    emodict = build_dict(emofile)
    isdict = build_dict(isfile)
    bhvdict = build_dict(bhvfile)
    folkdict = build_dict(folkfile)
    i = 1
    for image in split_region_graphs:
        # print(image['image_id'])
        if image['image_id'] == image_id:
            print('found!')
            for reg in image['regions']:
                try:
                    reg['phrase'] = str(reg['phrase'].lower())
                    g = rdflib.Graph()
                    defg = rdflib.Graph()
                    obj_value_graph = rdflib.Graph()
                    obj_emo_graph = rdflib.Graph()
                    obj_is_graph = rdflib.Graph()
                    obj = []
                    usefulobj = []
                    values_list = []
                    value_trigs_list = []
                    emotions_list = []
                    emo_trigs_list = []
                    is_list = []
                    is_trigs_list = []
                    frame_list = []
                    print(reg['phrase'])
                    # try:
                    params = (
                        ('text', str(reg['phrase'])),
                        ('wfd_profile', 'b'),
                        ('textannotation', 'earmark'),
                        ('wfd', True),
                        ('roles', False),
                        ('alignToFramester', True),
                        ('semantic-subgraph', True)
                    )
                    response = requests.get('http://wit.istc.cnr.it/stlab-tools/fred', headers=headers, params=params)
                    fredg = g.parse(data=response.text, format='ttl')

                    for s ,p ,o in fredg:
                        s = str(s).replace("http://www.w3.org/2006/03/wn/wn30/instances", "https://w3id.org/framester/wn/wn30/instances")
                        o = str(o).replace("http://www.w3.org/2006/03/wn/wn30/instances", "https://w3id.org/framester/wn/wn30/instances")
                        s = str(s).replace("http://www.ontologydesignpatterns.org/ont/vn/data", "https://w3id.org/framester/vn/vn31/data")
                        o = str(o).replace("http://www.ontologydesignpatterns.org/ont/vn/data", "https://w3id.org/framester/vn/vn31/data")
                        obj.append(o)
                        defg = defg.add((URIRef(s), URIRef(p), URIRef(o)))
                        for x in obj:
                            if 'dbpedia' in str(x):
                                usefulobj.append(x)
                            if 'synset' in str(x):
                                usefulobj.append(x)
                            if 'framestercore' in str(x):
                                usefulobj.append(x)
                            if 'vn31' in str(x):
                                usefulobj.append(x)
                            if 'pbdata' in str(x):
                                usefulobj.append(x)
                        for n in set(usefulobj):
                            for valuekey1 in valuedict.keys():
                                if n == valuekey1:
                                    obj_value_graph.add((URIRef(n) ,valuetriggers ,URIRef(valuedict[valuekey1])))
                            for valuekey2 in bhvdict.keys():
                                if n == valuekey2:
                                    obj_value_graph.add((URIRef(n) ,valuetriggers ,URIRef(bhvdict[valuekey2])))
                            for valuekey3 in folkdict.keys():
                                if n == valuekey3:
                                    obj_value_graph.add((URIRef(n) ,valuetriggers ,URIRef(folkdict[valuekey3])))
                            for emokey in emodict.keys():
                                if n == emokey:
                                    obj_emo_graph.add((URIRef(n) ,emotriggers ,URIRef(emodict[emokey])))
                            for iskey in isdict.keys():
                                if n == iskey:
                                    obj_is_graph.add((URIRef(n), istriggers, URIRef(isdict[iskey])))
                        finalg = defg + obj_value_graph + obj_emo_graph + obj_is_graph
                        template = ('https://template/sdg/graph_ ' + str(reg['image_id']) + '_ ' + str(reg['region_id']))
                        finalg.add((URIRef(template), graphFor, Literal(reg['phrase'])))

                        finalg.serialize(destination=('knowledge_extraction_outputs/'+ split_name + '/region_ttls/' + str
                            (reg['image_id']) + '_' + str(reg['region_id']) + '.ttl'))
                        for s ,p ,o in finalg:
                            if valuetriggers in p:
                                values_list.append(o)
                                value_trigs_list.append(s)
                            if emotriggers in p:
                                emotions_list.append(o)
                                emo_trigs_list.append(s)
                            if istriggers in p:
                                is_list.append(o)
                                is_trigs_list.append(s)
                            if 'https://w3id.org/framester/data/framestercore/' in o:
                                frame_list.append(o)
                        values_set = set(v.replace('https://w3id.org/spice/SON/HaidtValues#' ,'mft:').replace
                            ('https://w3id.org/spice/SON/SchwartzValues#' ,'bhv:').replace
                            ('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#' ,'folk:').strip() for v in values_list)
                        values_trigs_set = set(value_trigs_list)
                        emo_set = set(e.replace('http://www.ontologydesignpatterns.org/ont/emotions/BasicEmotions.owl#'
                                                ,'be:').strip() for e in emotions_list)
                        emo_trigs_set = set(emo_trigs_list)
                        is_set = set(imsch.replace('http://www.ontologydesignpatterns.org/ont/is/isaac_vanilla.owl#'
                                                   ,'is:').strip() for imsch in is_list)
                        is_trigs_set = set(is_trigs_list)
                        frames_set = set \
                            (frame.replace('https://w3id.org/framester/data/framestercore/', 'fs:').strip() for frame in frame_list)
                        # gen_val_set = set(gen_val_list)
                        # gen_emo_set = set(gen_em_list)
                        out = {
                            'image_id': str(reg['image_id']),
                            'region_id' :str(reg['region_id']),
                            'phrase' :str(reg['phrase']),
                            'Emotions' :[', '.join(emo_set)],
                            'Emotions Triggers' :[', '.join(emo_trigs_set)],
                            'Values' :[', '.join(values_set)],
                            'Values Triggers' :[', '.join(values_trigs_set)],
                            'Frames' :[','.join(frames_set)]
                            # 'Image Schemas':[', '.join(is_set)],
                            # 'Image Schemas Triggers':[', '.join(is_trigs_set)]
                        }
                    print(out)
                    # print(frame_list)
                    df = pd.DataFrame(out)
                    output_as_csv(df, '', 'knowledge_extraction_outputs/' + split_name + '/img_tsvs/' + 'img_ ' + str(image_id) + '.tsv', [k for k in out.keys()])
                    if \
                    (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                        time.sleep(7)
                except Exception:
                    continue
                i = i + 1
    return

def split_knowledge_extractor(split_name):
    initialize_globals()
    split_region_graphs_path = open(str('VG_data/VG_data_splits/' + split_name + '_regiongraphs.json'))
    split_region_graphs = json.load(split_region_graphs_path)
    split_ranked_verbal_imgs_path = open(str('VG_data/VG_data_ranked/composite_ranked/' + split_name + '_verbal_images_ranked_c.json'))
    split_ranked_verbal_imgs = json.load(split_ranked_verbal_imgs_path)
    for x in split_ranked_verbal_imgs:
        for item in x:
            img_knowledge_extraction(split_name, split_region_graphs, int(item))
    return

#########################################################
####################### Execution #######################
#########################################################
# split_knowledge_extractor('split2')



