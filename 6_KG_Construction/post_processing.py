with open('n_image_2384656_graph.ttl') as a: 
    lines = a.read().splitlines()

delete_next = "no"
with open("cleaned_image_2384656_graph.ttl", "w") as f:
    for line in lines:
        n_line = line.replace("ns1", "visualsense")
        n_line = n_line.replace("['", "")
        n_line = n_line.replace("']", "")
        n_line = n_line.replace("']", "")
        if delete_next == "yes":
            delete_next = "no"
            continue
        if n_line == "<http://etna.istc.cnr.it/framester2/data/framestersyn/[]> a visualsense:WnSynsetFrame ;":
            delete_next = "yes"
            continue
        if 'ObjectRelationship/object_relationship_" ;' in n_line:
            continue
        if 'DepictedObject/depicted_object_" ;' in n_line:
            continue
        else: 
            if 'DepictedObject/depicted_object_",' in n_line:
                n_line = "    visualsense:includesDepictedObject"
            elif 'ObjectRelationship/object_relationship_",' in n_line:
                n_line = "    visualsense:includesObjectRel"
            print(n_line, file=f)
        # if n_line != "<http://etna.istc.cnr.it/framester2/data/framestersyn/[]> a visualsense:WnSynsetFrame ;":
        #     print(n_line, file=f)
        if n_line == "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .":
            print("", file=f)
            print("[ rdf:type owl:Ontology ;", file=f)
            print("   owl:imports <https://w3id.org/visualsense>", file=f)
            print("] .", file=f)



# textt = open('image_2384656_graph.ttl', 'r')

# with open("new_cleaned_image_2384656_graph.ttl", "w") as f:
#     textt = textt.replace("ns1", "visualsense")
#     print(textt, file=f)