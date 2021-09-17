import visual_genome
import json
import rdflib
from rdflib import Graph, Literal, RDF, URIRef, Namespace
import collections
from collections import Counter
from visual_genome import api
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint
import requests
import xlrd
import json
import nltk
from nltk.corpus import brown
from nltk import word_tokenize
from nltk.corpus import stopwords
import titlecase
import re


#--------------------------------------------------------------------------
# STEP 0
# the id variable is useful to remember which image the extracted json files are related to.
# the "f" file is extracted from VG dataset file scene_graph.json
# the "f1" file is extracted from VG dataset file regions.json
#--------------------------------------------------------------------------

id = 2384656
f = open("examples/regions_json/regions.json")
f1 = open('examples/regions_json/scenegraphs.json')
regions = json.load(f)
scenegraph = json.load(f1)

relationships_id = []

