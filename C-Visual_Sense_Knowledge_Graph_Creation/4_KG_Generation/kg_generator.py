import re
import os
import json
import string
from rdflib import Graph, Literal, Namespace, RDF, URIRef, RDFS
from rdflib.namespace import XSD
from image_source_maker import get_all_image_sources, load_data

def format_synset(synset):
    # These replace numbers with "0" before in numbers without
    synset = str(synset).replace("01", "1")
    synset = str(synset).replace("02", "2")
    synset = str(synset).replace("03", "3")
    synset = str(synset).replace("04", "4")
    synset = str(synset).replace("05", "5")
    synset = str(synset).replace("06", "6")
    synset = str(synset).replace("07", "7")
    synset = str(synset).replace("08", "8")
    synset = str(synset).replace("09", "9")
    # Lowercase the synset (some of them are in caps lock for no reason)
    synset = str(synset).lower()
    # Capitalize only the first character of the string
    synset = string.capwords(synset)
    # Replace the squared brackets and the apostrophe
    synset = str(synset).replace('[', '')
    synset = str(synset).replace(']', '')
    synset = str(synset).replace("'", "")
    synset = re.sub(r"\([^()]*\)", "", synset)
    return synset

def format_frame_URI(frame_uri):
    # Define a dictionary to map the input strings to the corresponding full URLs
    url_dict = {
        'mft:': 'https://w3id.org/spice/SON/HaidtValues#',
        'bhv:': 'https://w3id.org/spice/SON/SchwartzValues#',
        'folk:': 'http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#',
        'fs:': 'https://w3id.org/framester/data/framestercore/',
        'folk:': 'http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#',
        'be:': 'http://www.ontologydesignpatterns.org/ont/emotions/BasicEmotions.owl#'
    }
    # Iterate over the dictionary keys and check if the frame URI starts with any of them
    for prefix in url_dict.keys():
        if frame_uri.startswith(prefix):
            # Replace the prefix with the corresponding URL
            frame_uri = url_dict[prefix] + frame_uri[len(prefix):]
            frame_uri = URIRef(frame_uri)
            return frame_uri
    # If the frame URI does not start with any known prefix, return None
    return None

def generate_image_KG(image_data, region_graphs, scene_graphs, frame_data):
    # Define namespaces
    VS = Namespace('https://w3id.org/visualsense#')
    CPV = Namespace('https://w3id.org/italia/onto/CPV/')
    FSCHEMA = Namespace('https://w3id.org/framester/schema/')
    FS = Namespace('https://w3id.org/framester/data/framestercore/')
    MFT = Namespace('https://w3id.org/spice/SON/HaidtValues#')
    BHV = Namespace('https://w3id.org/spice/SON/SchwartzValues#')
    FOLK = Namespace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#')
    BE = Namespace('http://www.ontologydesignpatterns.org/ont/emotions/BasicEmotions.owl#')

    # Create graph
    g = Graph()

    for image in image_data:
        # Add ImageObject triples
        image_id = image["image_id"]
        image_object_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}")
        physical_image_uri = URIRef(image["url"])
        g.add((image_object_uri, RDF.type, VS.ImageObject))
        g.add((image_object_uri, VS.hasPathURL, Literal(image["url"], datatype=XSD.decimal)))
        g.add((image_object_uri, VS.hasLocation,
               URIRef(f"http://w3id.org/visualsense/resource/ImageBox/image_box_{image_id}")))
        # Add ImageBox triples
        image_id = image["image_id"]
        image_box_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageBox/image_box_{image_id}")
        g.add((image_box_uri, RDF.type, VS.ImageBox))
        g.add((image_box_uri, VS.isLocationOf,
               URIRef(f"http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}")))
        g.add((image_box_uri, VS.hasHeight, Literal(image["height"], datatype=XSD.decimal)))
        g.add((image_box_uri, VS.hasWidth, Literal(image["width"], datatype=XSD.decimal)))

    for image_regions in region_graphs:
        # Add DepictedRegion triples
        image_id = image_regions["image_id"]
        image_box_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageBox/image_box_{image_id}")
        image_object_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}")
        regions = image_regions["regions"]
        for region in regions:
            region_id = region["region_id"]
            depicted_region_uri = URIRef(f'https://w3id.org/visualsense/resource/DepictedRegion/depicted_region_{region_id}')
            region_bb_uri = URIRef(f'https://w3id.org/visualsense/resource/BoundingBox/bb_region_{region_id}')
            g.add((depicted_region_uri, RDF.type, VS.DepictedRegion))
            g.add((depicted_region_uri, VS.hasLocation, image_box_uri))
            g.add((depicted_region_uri, RDFS.label, Literal(region["phrase"], datatype=XSD.string)))
            g.add((depicted_region_uri, VS.isDepictedIn, image_object_uri))
            for object in region["objects"]:
                object_id = object["object_id"]
                depicted_object_uri = URIRef(f'https://w3id.org/visualsense/resource/DepictedObject/depicted_object_{object_id}')
                g.add((depicted_region_uri, VS.includesDepictedObject, depicted_object_uri))
                g.add((depicted_object_uri, VS.isDepictedObjectIncludedIn, depicted_region_uri))
            for relationship in region["relationships"]:
                relationship_id = relationship["relationship_id"]
                object_relationship_uri = URIRef(f'https://w3id.org/visualsense/resource/ObjectRelationship/object_relationship_{relationship_id}')
                g.add((depicted_region_uri, VS.includesObjectRel, object_relationship_uri))

            # Add (Region) BoundingBox triples
            g.add((region_bb_uri, RDF.type, VS.BoundingBox))
            g.add((region_bb_uri, VS.hasHeight, Literal(region["height"], datatype=XSD.decimal)))
            g.add((region_bb_uri, VS.hasWidth, Literal(region["width"], datatype=XSD.decimal)))
            g.add((region_bb_uri, VS.hasXCoordinate, Literal(region["x"], datatype=XSD.decimal)))
            g.add((region_bb_uri, VS.hasYCoordinate, Literal(region["y"], datatype=XSD.decimal)))
            g.add((region_bb_uri, VS.isLocationOf, depicted_region_uri))
            g.add((region_bb_uri, VS.isPartOf, depicted_region_uri))

    for image in scene_graphs:
        image_id = image["image_id"]
        image_object_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}")
        image_box_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageBox/image_box_{image_id}")

        # Add DepictedObject triples
        for depicted_object in image["objects"]:
            depicted_object_id = depicted_object["object_id"]
            depicted_object_uri = URIRef(f"http://w3id.org/visualsense/resource/DepictedObject/depicted_object_{depicted_object_id}")
            bb_dep_object_uri = URIRef(f'https://w3id.org/visualsense/resource/BoundingBox/bb_dep_object_{depicted_object_id}')
            g.add((depicted_object_uri, RDF.type, VS.DepictedObject))
            g.add((depicted_object_uri, VS.hasLocation, bb_dep_object_uri))
            g.add((depicted_object_uri, VS.isDepictedIn, image_object_uri))
            # Add Synset to DepictedObject triples
            try:
                synset = depicted_object["synsets"][0]
                synset = format_synset(synset)
                synset_URI = URIRef(f'https://w3id.org/framester/data/framestersyn/{synset}')
                g.add((depicted_object_uri, VS.isTypedBy, synset_URI))
            except:
                continue
            # Add label to DepictedObject triples
            label = depicted_object["names"][0]
            g.add((depicted_object_uri, RDFS.label,  Literal(label, datatype=XSD.string)))
            # Add attributes to DepictedObject triples
            try:
                for attribute in depicted_object["attributes"]:
                    g.add((depicted_object_uri, VS.hasObjAttribute, Literal(attribute, datatype=XSD.string)))
            except:
                continue
            # Add (DepictedObject) Bounding Box triples
            g.add((bb_dep_object_uri, RDF.type, VS.BoundingBox))
            g.add((bb_dep_object_uri, VS.isLocationOf, depicted_object_uri))
            g.add((bb_dep_object_uri, VS.isPartOf, image_box_uri))

            g.add((bb_dep_object_uri, VS.hasHeight, Literal(depicted_object["h"], datatype=XSD.decimal)))
            g.add((bb_dep_object_uri, VS.hasWidth, Literal(depicted_object["w"], datatype=XSD.decimal)))
            g.add((bb_dep_object_uri, VS.hasXCoordinate, Literal(depicted_object["x"], datatype=XSD.decimal)))
            g.add((bb_dep_object_uri, VS.hasYCoordinate, Literal(depicted_object["y"], datatype=XSD.decimal)))

            # Add ObjectRelationship triples
        for relationship in image["relationships"]:
            relationship_id = relationship["relationship_id"]
            relationship_uri = URIRef(
                f"http://w3id.org/visualsense/resource/ObjectRelationship/object_relationship_{relationship_id}")
            g.add((relationship_uri, RDF.type, VS.ObjectRelationship))
            g.add((relationship_uri, VS.isDepictedIn, image_object_uri))

            # Add Synset to ObjectRelationship triples
            try:
                synset = relationship["synsets"][0]
                synset = format_synset(synset)
                synset_URI = URIRef(f'https://w3id.org/framester/data/framestersyn/{synset}')
                g.add((relationship_uri, VS.isTypedBy, synset_URI))
            except:
                continue
            # Add label to ObjectRelationship triples
            label = relationship["predicate"]
            g.add((relationship_uri, RDFS.label, Literal(label, datatype=XSD.string)))

            # Add subject and object to ObjectRelationship triples
            rel_subject_id = relationship["subject_id"]
            rel_object_id = relationship["object_id"]
            rel_subject_uri = URIRef(f'https://w3id.org/visualsense/resource/DepictedObject/depicted_object_{rel_subject_id}')
            rel_object_uri = URIRef(f'https://w3id.org/visualsense/resource/DepictedObject/depicted_object_{rel_object_id}')
            g.add((relationship_uri, VS.hasRelSubject, rel_subject_uri))
            g.add((relationship_uri, VS.hasRelObject, rel_object_uri))

    for frame in frame_data:
        image_id = frame["image_id"]
        image_object_uri = URIRef(f"http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}")
        region_id = frame["region_id"]
        depicted_region_uri = URIRef(f'https://w3id.org/visualsense/resource/DepictedRegion/depicted_region_{region_id}')
        frame_uri = frame["frame"]
        frame_uri = format_frame_URI(frame_uri)
        g.add((frame_uri, RDF.type, VS.ConceptualFrame))
        g.add((frame_uri, VS.isFrameOfType, Literal(frame["type"], datatype=XSD.string)))
        g.add((frame_uri, VS.isEvokedBy, image_object_uri))
        g.add((frame_uri, VS.isEvokedBy, depicted_region_uri))
        g.add((image_object_uri, VS.evokes, frame_uri))
        g.add((depicted_region_uri, VS.evokes, frame_uri))

    # # Serialize RDF graph to file
    g.serialize('output_KG/visualsense.ttl', format='turtle')

    count = 0
    for s, p, o in g:
        print(s, p, o)
        count += 1
    print(count, " number of triples")
    return g

def generate_top_images_KG(split_name):
    top_images_path = '../VG_data/VG_data_ranked/composite_ranked/split2_verbal_images_ranked_c.json'
    image_ids_list = []
    with open(top_images_path, 'r') as f:
        # Load the list from the file
        original_list = json.load(f)
    new_list = [sublist[1] for sublist in original_list]
    for image_id in new_list:
        file_path = '../3_Framal_Knowledge_Extraction/knowledge_extraction_outputs/' + split_name + '/image_tsvs/' + 'img_' + image_id + '.tsv'
        if os.path.isfile(file_path):
            image_ids_list.append(image_id)
    try:
        image_data, region_graphs, scene_graphs, frame_data = load_data()
    except:
        image_data, region_graphs, scene_graphs, frame_data = get_all_image_sources(image_ids_list, split_name)
    g = generate_image_KG(image_data, region_graphs, scene_graphs, frame_data)
    return g

#########################################################
####################### Execution FOR 76 TOP IMAGES #######################
#########################################################
kg = generate_top_images_KG("split2")


####################### Execution for just 2 images #######################
# image_ids_list = ['2410077', '2402053']
# split_name = 'split2'
# # image_data, region_graphs, scene_graphs, frame_data = get_all_image_sources(image_ids_list, split_name)
# image_data, region_graphs, scene_graphs, frame_data = load_data()
# generate_image_KG(image_data, region_graphs, scene_graphs, frame_data)
