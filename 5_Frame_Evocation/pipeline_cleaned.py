import json
import rdflib
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from collections import Counter
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint
import requests
import json
import nltk
from nltk.corpus import brown
from nltk import word_tokenize
from nltk.corpus import stopwords
import re


#--------------------------------------------------------------------------
# STEP 0
# the id variable is necessary to the final json file, and it is
# useful to remember which image the extracted json files are related to.
# the "f" file is extracted from VG dataset file scene_graph.json
# the "f1" file is extracted from VG dataset file regions.json
#--------------------------------------------------------------------------

id = 861
f = open("/home/sdg/Desktop/VG/final_syn_regiongraph1 - $.[860].json")
f1 = open('/home/sdg/Desktop/VG/correct_syn_scenegraph1 - $.[860].json')
regions = json.load(f)
scenegraph = json.load(f1)

relationships_id = []


#--------------------------------------------------------------------------
# STEP 1 : define function to populate the relationships_id list 
# with id of relationships whose predicate is a verb.
#--------------------------------------------------------------------------


def find_verb_relations_id(file):
    for rel in file["relationships"]:
        if '.r.' not in rel['synsets']:
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
                    if s[1] in ('VB' ,'VBD' ,'VBG' ,'VBN' ,'VBP' ,'VBZ'):
                            relationships_id.append(rel['relationship_id'])
                        # list all the region_id for regions having a relation that is a verb
    print("These are the relationships IDs you could be interested in:\n", relationships_id)
                            

find_verb_relations_id(scenegraph)


#--------------------------------------------------------------------------
# STEP 2 : define a function to extract the regions_id and the region description 
# of the regions having as predicate a verb. 
# Store those the IDs and region descriptions in 2 .txt files.
#--------------------------------------------------------------------------


def regions_of_interest(regions):
    with open('regions_of_interest.txt', 'w') as roi:
        with open('description_of_interest.txt', 'w') as doi:
            print('These are the Regions IDs you could be interested in:')
            for reg in regions['regions']:
                for rel in reg['relationships']:
                    for el in relationships_id:
                        if el == rel['relationship_id']:
                            print(reg['region_id'])
                            roi.write(str(reg['region_id'])+'\n')
                            doi.write(str(reg['phrase'])+'\n')
    return doi, roi
            

regions_of_interest(regions)

doi = open('description_of_interest.txt', 'r+')
roi = open('regions_of_interest.txt', 'r+')



#--------------------------------------------------------------------------
# STEP 3 : define a function to pass the description region to FRED tool, via
# a call to online service. Store the graphs generated in a single .ttl file.
#--------------------------------------------------------------------------



def generate_FRED_graphs(doi):
    headers = {
        'accept': 'text/turtle',
        'Authorization': 'insert key',
    }
    with open('FRED.ttl', "w") as FRED_ttl:
        for line in doi:
            stripped_line = line.strip()
            params = (
                ('text', stripped_line),
                ('wfd_profile', 'b'),
                ('textannotation', 'earmark'),
                ('wfd', True),
                ('roles', False),
                ('alignToFramester', True),
                ('semantic-subgraph', True)
            )
            response = requests.get('http://wit.istc.cnr.it/stlab-tools/fred', headers=headers, params=params)
            FRED_ttl.write("#")
            FRED_ttl.write("FRED graph for Visual Genome Region Description: ")
            FRED_ttl.write(stripped_line)
            FRED_ttl.write("\n")
            FRED_ttl.write(response.text)
            FRED_ttl.write("\n")
            FRED_ttl.write("#")
            FRED_ttl.write("----------------------------------------------")
            FRED_ttl.write("\n")
            return FRED_ttl


generate_FRED_graphs(doi)

FRED_ttl = open('FRED.ttl', 'r+')

#--------------------------------------------------------------------------
# STEP 4 : define a function to extract the frames recognised by FRED tool as being
# evoked in the .ttl file. Also extract and store all the synsets retrieved by FRED.
#--------------------------------------------------------------------------


def frames_from_FRED(FRED_ttl):
    g = rdflib.Graph()
    g.parse(FRED_ttl, format="ttl")
    fscore = URIRef("https://w3id.org/framester/data/framestercore/")
    wnsyn = URIRef("http://www.w3.org/2006/03/wn/wn30/instances/synset")
    frames = []
    synsets = []
    frames_file = open('frames_retrieved_by_FRED.txt', 'w')
    synsets_file = open('synsets_retrieved_by_FRED.txt', 'w')
    for s,p,o in g:
        if fscore in str(s):
            frames.append(s)
        if fscore in str(o):
            frames.append(o)
#    print(Counter(frames), len(frames))
    for s,p,o in g:
        if wnsyn in str(s):
            synsets.append(s)
        if wnsyn in str(o):
            synsets.append(o)
#    print(Counter(synsets), len(synsets))
    frames_set = set(frames)
    synsets_set = set(synsets)
    for el in frames_set:
        frames_file.write(el)
        frames_file.write('\n')
    for el in synsets_set:
        synsets_file.write(el)
        synsets_file.write('\n')


frames_from_FRED(FRED_ttl)

FRED_syns = open('synsets_retrieved_by_FRED.txt', 'r+')

#--------------------------------------------------------------------------
# STEP 5 : define a function to extract all the wordnet synsets used as annotation
# in VG dataset.
#--------------------------------------------------------------------------

objsyn = []
relsyn = []

def extract_explicit_synsets_dict(regions):
    with open('synsets_file.txt', 'w') as synsets_file:
        print("These are the Relations synsets you could be interested in:")
        for region in regions['regions']:
            if len(region['relationships']) > 0:
                for rel in region["relationships"]:
                    if len(rel['synsets']) > 0:
                        if '.r.' not in rel['synsets']:
#                        for synocc in rel["synsets"]:
                            print(rel['synsets'])
                            relsyn.append(rel['synsets'])
            for obj in region["objects"]:
                for objocc in obj["synsets"]:
                    objsyn.append(obj['synsets'])
        objset = set(objsyn)
        relset = set(relsyn)
        for el in objset:
            synsets_file.write(el+"\n")
        for el in relset:
            synsets_file.write(el+"\n")

        print('These are the Objects synsets in the VG dataset:\n', Counter(objsyn), len(objsyn))
        print('These are the Relations synsets in the VG dataset:\n', Counter(relsyn), len(relsyn))


extract_explicit_synsets_dict(regions)


synset_file = open('synsets_file.txt', 'r+')


#--------------------------------------------------------------------------
# STEP 6 : change the syntax for wn synsets from the VG dataset in order to 
# make them ready for being passed to Framester.
#--------------------------------------------------------------------------


def clean_VG_synsets(synset_file):
    out = open("synsets_for_framester.txt", "w")
    print('These are the corresponding synset Frames in Framester:')
    for line in synset_file:
        line = line.replace("01", "1")
        line = line.replace("02", "2")
        line = line.replace("03", "3")
        line = line.replace("04", "4")
        line = line.replace("05", "5")
        line = line.replace("06", "6")
        line = line.replace("07", "7")
        line = line.replace("08", "8")
        line = line.replace("09", "9")
        line = line.capitalize()
        secondline = re.sub(r"\([^()]*\)", "", line)
        print(secondline)
        out.write(secondline)


clean_VG_synsets(synset_file)

syns_for_Framester = open('synsets_for_framester.txt', 'r+')

#--------------------------------------------------------------------------
# STEP 6.1 : change the syntax for wn synsets retrieved by FRED in order to 
# make them ready for being passed to Framester.
#--------------------------------------------------------------------------


def clean_FRED_synsets(FRED_syns):
    out = open("FRED_synsets_cleaned.txt", "w")
    for line in FRED_syns:
        line = line.replace("01", "1")
        line = line.replace("02", "2")
        line = line.replace("03", "3")
        line = line.replace("04", "4")
        line = line.replace("05", "5")
        line = line.replace("06", "6")
        line = line.replace("07", "7")
        line = line.replace("08", "8")
        line = line.replace("09", "9")
        line = line.replace('http://www.w3.org/2006/03/wn/wn30/instances/synset-', '')
        line = line.replace('-noun-', '.n.')
        line = line.replace('-verb-', '.v.')
        line = line.capitalize()
        secondline = re.sub(r"\([^()]*\)", "", line)
#        print(secondline)
        out.write(secondline)

clean_FRED_synsets(FRED_syns)


#--------------------------------------------------------------------------
# STEP 6.2 : merge the two wn synsets files from VG and FRED in one unique file.
#--------------------------------------------------------------------------


def merge_syns(syns_for_Framester, FRED_syns):
    with open('final_syns_list.txt', 'w') as final_syns_list:
        for line in syns_for_Framester:
            final_syns_list.write(line)
    final_syns_list.close
    with open('final_syns_list.txt', 'r+') as final_syns_list:
        for line in FRED_syns:
            if line not in final_syns_list:
                final_syns_list.write(line)


merge_syns(syns_for_Framester, FRED_syns)

final_syns_list = open('final_syns_list.txt', 'r+')

#--------------------------------------------------------------------------
# STEP 7 : use the WordNet Synsets as variable for a query to check which
# frames are evoked in Framester by each synset.
#--------------------------------------------------------------------------

framestersyn = []


def evoke_frames(synset_list):
    prequery = final_syns_list.readlines()
    sparql = SPARQLWrapper('http://etna.istc.cnr.it/framester2/sparql')
    for line in prequery:
        querystring = ('''
    SELECT DISTINCT ?frame
    WHERE{
    ?frame rdf:type fschema:ConceptualFrame , owl:Class ;
        rdfs:subClassOf fschema:FrameOccurrence .
    ?frame fschema:subsumes framestersyn:'''+ line + "}")
        sparql.setQuery(querystring)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results['results']['bindings']:
            res = result['frame']
            for value in res.values():
                if value != 'uri':
                    framestersyn.append(value)
    print('These are the frames evoked in the processed image:')
    print(set(framestersyn))


evoke_frames(final_syns_list)

#frames_evoked = open('frames_evoked.txt', 'r+')


#--------------------------------------------------------------------------
# STEP 8 : produce a txt file of evoked frames with frequency and image id, 
# ready to be converted in json format.
#--------------------------------------------------------------------------

frame_dict = {}

frame_list_for_conversion = open('frames_evoked_for_conversion.txt', 'w')

def count_frames(framestersyn):
	for item in framestersyn:
		if (item in frame_dict):
			frame_dict[item] += 1
		else:
			frame_dict[item] = 1
	for key, value in frame_dict.items():
		frame_list_for_conversion.write( 'frame : %s |'%(key) + ' frequency : %d |'%(value) + ' imageID : ' + str(id) + '\n')

count_frames(framestersyn)


#--------------------------------------------------------------------------
# STEP 9 : produce the final json with evoked frames, frequency and image ID.
#--------------------------------------------------------------------------


def line_to_dict(split_Line):
    line_dict = {}
    for part in split_Line:
        key, value = part.split(" : ", maxsplit=1)
        line_dict[key] = value
    return line_dict

frame_list_for_conversion = open('frames_evoked_for_conversion.txt', 'r+')

def convert() :
#    f = open(frame_list_for_conversion)
    content = frame_list_for_conversion.read()
    splitcontent = content.splitlines()
    # Split each line by pipe
    lines = [line.split(' | ') for line in splitcontent]
    # Convert each line to dict
    lines = [line_to_dict(l) for l in lines]
    another_dict = {'frames_evoked' : lines}
    # Output JSON 
    with open("final_frames_file.json", 'w') as fout:
        json.dump(another_dict, fout, indent=4)


convert()


#--------------------------------------------------------------------------
# STEP 10 : Enjoy the end of this f***ing awesome pipeline and spend
# a couple of seconds thinking to all those non computer scientists who
# spit blood for this mediocre result. That's all folks. Thank You.
#
#                              ಥ‿ಥ
#
#--------------------------------------------------------------------------
