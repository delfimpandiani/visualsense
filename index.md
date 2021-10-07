# Visual Sense: Automatically Making Multimodal Sense of the Visual World
### By Delfina S. M. Pandiani, Stefano De Giorgis and Fiorela Ciroku 

This project aims at integrating the annotated image dataset Visual Genome (VG) with the knowledge graph resource Framester, in order to produce a linked data knowledge graph that contains multimodal (factual, linguistic, and visual) knowledge. Our goal was to develop a full flow that allows, for a VG image of choice, the automatic modelling, implementation and publication of a semantic web knowledge graph (RDF) containing multimodal data. To do so, we first analyzed the relevant datasets, and completed design and modeling tasks following the eXtreme Design Methodology in order to extract the schema of Visual Genome as an ontology TBox and create the Visual Sense Ontology. We then developed a pipeline [Fig. 1] to shape the data (ABox) accordingly, with four major stages: 1. Image Data Extraction, 2. Data Preprocessing, 3. Frame Evocation, 4. KG Construction.


![Image](https://delfimpandiani.github.io/visualsense/images/pipeline.jpg)
Fig 1. General pipeline of the Visual Sense project. Starting from the data and knowledge provided by the Visual Genome project in JSON format, our pipeline selects allows for the automatic creation of semantic web knowledge graphs containing visual, factual and linguistic data.


## Datasets

### Visual Genome

[Visual Genome (VG)](https://visualgenome.org/) is an annotated image dataset containing over 108K images where each image is annotated with an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects. Regarding relationships and attributes as first-class citizens of the annotation space, in addition to the traditional focus on objects, VG’s annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs. The Visual Genome dataset is among the first to provide a detailed labeling of object interactions and attributes, providing a first step of grounding visual concepts to language by canonicalizing the objects, attributes, relationships, noun phrases in region descriptions, and question & answer pairs to WordNet synsets.

### Framester
Framester is a frame-based ontological resource acting as a hub between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create an interoperable predicate space formalized according to frame semantics and semiotics principles. Framester uses WordNet and FrameNet at its core, expanding to other resources transitively, and represents them in a formal version of frame semantics. Framester has a freely available dedicated SPARQL endpoint and an API. The schema of Framester is also available as an ontology.

### Relevant links
[Visual Genome](https://visualgenome.org/)

[Visual Genome JSON datasets](https://visualgenome.org/api/v0/api_home.html)

[Visual Genome API](https://visualgenome.org/api/v0/api_endpoint_reference.html)

[Framester](https://github.com/framester/Framester)

[Framester SPARQL Endpoint](http://etna.istc.cnr.it/framester2/sparql)

[Framester API](http://etna.istc.cnr.it/framester_web/)


## Visual Genome’s Data Model

The Visual Genome team provides two ways of accessing the data (always in JSON format):
1. Using the provided API to access the data directly from their server, without the need to keep any local data available.
2. Downloading all the data and use local methods to parse and work with the visual genome data.

We decided to use the second option, as it was more reliable. As a preliminary task, we did a manual exploration of the JSON files in order to further understand the way that the data was structured. As a result of this process, the original schema behind Visual Genome was detected [Fig. 2]. Certain issues became apparent, such as the use of different keys for the same conceptual instances in different JSON files (e.g., “id”, “image_id”), so before designing our ontology, we proposed an intermediary data model that took care of the detected duplications [Fig. 3].

![Image](https://delfimpandiani.github.io/visualsense/images/VG_orig.png)
Fig 2. Original data model of Visual Genome, reconstructed by manual inspection of the publicly available JSON files.
![Image](https://delfimpandiani.github.io/visualsense/images/VG_new.png)
Fig 3. Slimmer data model of Visual Genome, proposed to deal with duplicated information.


## Knowledge Engineering Methodology: eXtreme Design 

This knowledge engineering project has followed the eXtreme Design (XD) methodology proposed by Bloomqvist. eXtreme Design (XD) is an ontology design methodology whose core principle is ontology design patterns (ODP) reuse, as an explicit activity. ODPs are small ontologies which, ideally, form the bigger ontology with the correct alignment. They mediate between use cases (problem types) and design solutions. 

### Competency Questions

The general XD methodology first requires a focus on stories and Competency Questions (CQs). To do so, the ontology engineers get in close and frequent contact with domain experts, so as to collect the requirements for the ontology in the form of stories. The key information that a story should contain is the goal/objective of the story and questions that need to be answered in order to reach that goal. Once the stories are collected, they are prioritized and then broken down by the ontology engineers. They identify the main concepts and the possible general constraints from the user stories to create Competency Questions (CQs). A complete list of competency questions for this ontology can be found [here](https://docs.google.com/document/d/1f12wkdOa-a24GMtxxS5N_OKMapnWtygOdGr5gI7P3DU/edit?usp=sharing). They were extracted from the story below. 

>"When surfing the Visual Genome dataset, I want to search images that contain objects in them. It is great to know if the objects have attributes associated with them. If there is more than one object in the image, I need to know about the relation that exists between these objects. Regarding the regions of the objects and the regions of relations, I want to identify the region that they are included in. I need to investigate if the image evokes any conceptual frames and if the frames are involved in these regions. I am also keen to find out the bounding boxes that cover the objects, relations and regions and the location and surface of the bounding boxes in the image. I would like to know the size of the image to understand which percentage of the image the object (bounding box of the object) and relation occupy. An interesting aspect is to search about the synsets that are related to objects, regions, relations and frames."

## The Visual Sense Ontology

Visual Sense ontology is an ontology that aims to formally represent Visual Genome’s annotation components and their interrelationships, and to connect these components to the Framester schema, so as to further ground visual data to language. The ontology was developed following the XD ontology design methodology. Below we present how the Visual Sense ontology has reused ontology design patterns (ODPs) and been aligned to and reused other ontologies while presenting its T-Box [Fig. 4], with explanations of its crucial classes and properties. Further details of all classes and properties are available in LODE-Powered Visual Sense Ontology Documentation. LODE is a tool for producing human-readable documentation of the ontologies. The Visual Sense ontology has been published at the following permanent IRI: https://w3id.org/visualsense.

The Visual Sense Ontology can be further explored via the WebVOWL tool:

[![Image](https://delfimpandiani.github.io/visualsense/images/webvowl.png)](http://www.visualdataweb.de/webvowl/#opts=editorMode=true;#iri=https://w3id.org/visualsense)

### Ontology and Ontology Design Pattern (ODP) Alignment and Reuse

The Visual Sense Ontology is aligned to DOLCE Ultra Lite (DUL) foundational ontology and reuses classes and properties from the Framester schema. Furthermore, certain Ontology Design Patterns (ODPs) were reused in the design and modeling of the Visual Sense Ontology.

### Alignment to DUL and ODP Reuse

The alignment to DUL was due to the cognitive nature of the Visual Sense ontology, as the task of representing and improving formal knowledge in the visual sensemaking process is particularly coherent to the human cognitive and socio-cultural aspects covered by DUL. What the Visual Genome model considers simply an “image”, is considered in the Visual Sense Ontology as something that semantically is spread into two different classes, reusing the Content ODP Information Realization, by being spread onto two different classes, `:ImageObject` and `:ImageRegion`. `:ImageObject` is modeled as a subclass of `dul:InformationObject`, since the focus of expressiveness of this class is on the meaning that is conveyed in and by the Image itself.

<img width="1041" alt="Screenshot 2021-09-24 at 14 05 20" src="https://user-images.githubusercontent.com/12375920/135294449-598f3278-cbf2-444a-984b-05cd1cd11d06.png">
Figure 4. T-Box of the Visual Sense ontology. The ontology is aligned to Dolce Ultra Light and the Framester Schema, and reuses Ontology Design Patterns.

This class of `:ImageObject` is furthermore axiomatized as having a realization through a location in some `:ImageRegion`. The class `:ImageRegion` is in fact a subclass of `dul:SpaceRegion` and it represents the physical extension of the image, the spatial area occupied by the image measured in terms of pixels. 

This conceptual duality is coherently kept with all the other classes in the ontology: a mereological relation exists between `:ImageRegion` and any other subpart of the image, with the possibility to query the ontology based on the spatial area of interest. In particular, these physical subparts of an `:ImageRegion` are the areas, bound by coordinates, which are recognised in the Visual Genome dataset as areas of location for Regions and Objects. They are modeled as `:BoundingBoxes`, which are subclasses of `dul:SpaceRegion`, they are explicitly `dul:partOf` some `:ImageRegion`, and they are also the `dul:locationOf` some `:DepictedObject` or `:DepictedRegion`. 

The `:DepictedRegion` class applies the Situation Content Ontology Design Pattern, whose intent is to represent contexts or situations, and the things that are contextualized. This pattern itself reifies the N-ary Relation Logical Ontology Design Pattern, and it allows the contextualization of things that have something in common, or are associated: a same place, time, view, causal link, systemic dependence, etc. In the case of Visual Sense, `:DepictedRegion` is modeled as a subclass of the class `dul:Situation`,in the sense that a depicted region provides a context and is the setting for a variety of things (depicted objects, relationships between depicted objects, evoked conceptual frames) that share a same informational space.

### Alignment to Framester Schema

The other ontology reused in Visual Sense is the Framester schema, in particular the fschema:Frame and fschema:ConceptualFrame classes are reused both for the frames evoked by some `:DepictedObject`, located in some `:BoundingBox`, and the frames recognised as evoked by the FRED tool, while the `fschema:WnSynsetFrame` is reused for the frames evoked by some specific Wordnet Synset.

##  Frame Evocation Experiments

The usage of WordNet synsets to disambiguate object annotations in the Visual Genome repository allows the exploration of frame evocation via querying of the Framester hub. Specifically, Framester querying can be performed in order to retrieve Conceptual Frames evoked by synsets used as labels for some Image Region, DepictedObject, or ObjectRelationship. Additionally, it is possible to extract formal frame knowledge from the natural language provided in the Visual Genome annotations, by automatically generating Knowledge Graphs (KG) with the FRED tool, using sentences (images’ scene descriptions) as input. Since WordNet synsets are related to Depicted Objects, region descriptions are related to Depicted Regions, and each Depicted Object and Depicted Region is localized by a bounding box in an image, this in turn allows the localization of evoked frames to a specific set of pixels. As such, the integration of lexical resources such as Framester and FRED allows for sophisticated grounding of visual data to language.

### Experiments, Lessons, and Refinements

The first frame evocation attempt was driven by the principle of maximizing the amount of frame knowledge extraction, using each lexical unit (LU) of each bounding box in an image as input variable for a SPARQL query to Framester, in order to retrieve all the frames potentially evoked by all the synset of the LU in input. It is worth mentioning that each Image in Visual Genome has an average of 50 Regions, and for each region there is a minimum of one object (but often more than one), some relationships between objects, and some attributes for each object. The result of this first attempt was a massive amount of evoked frames (in the order of magnitude of hundreds of frames per image) which was not useful in extracting real knowledge about the semantic content of the analyzed image, since it was just the set of frames potentially evoked by each sense of each LU.

Since the interest was not on the potential frame evocation but on the most likely knowledge contained in each image, an improvement was performed by applying the following heuristic, with the purpose to decrease noise and increase meaningfulness and precision of frame evocation: instead of using the LU from annotations, since Visual Genome already provides WordNet synsets to disambiguate annotations, those synsets were used to query Framester. The result was a considerable amount of evoked frames, but because of the structure of each image JSON file, the frame evocation was still related mainly to the presence or absence of some object in an image. This meant that the frame evocation was mainly answering the implicit question “what is there” instead of “what is happening”. 

For this reason, as we were interested conceptually more in the second question, a further restriction was applied. The heuristic was to focus on Regions having at least two objects and a relation between them, and to be sure, via NLP techniques, that this relation was a verb (and not e.g. a preposition). A first confirmation of this intuition’s rightfulness comes directly from the data: regions with verbal relations between objects are the ones in which there is the highest "semantic concentration", in terms of number of relations to and from entities.


### Frame Evocation Pipeline

![frame_evocation_pipeline.png](https://github.com/delfimpandiani/visualsense/blob/main/5_Frame_Evocation/frame_evocation_pipeline.png)

A summary of the final pipeline is presented here, step by step, while the full code is available [here](https://github.com/delfimpandiani/visualsense/blob/main/5_Frame_Evocation/pipeline_cleaned.py).

1. From a Visual Genome image scenegraph.json and regiongraph.json extract the list of relationships whose predicate is a verb.
2. Extract the Region_ID and Region Description (of region having a verb as predicate).
3. Generate the knowledge graph from natural language via FRED tool, taking as input each Region Description.
4. Extract and store in a file all the frames evoked and all the synsets retrieved in each triple of the FRED graphs.
5. Extract the WordNet synsets used in the json file as annotations (from the regions having a verb as a predicate).
6. Clean the WordNet synsets data extracted from Visual Genome json file, in order to have the iri of corresponding FramesterSyn entities, ready to be used to query Framester.
7. Clean the WordNet synsets data extracted from FRED graphs, in order to have the iri of corresponding FramesterSyn entities, ready to be used to query Framester.
8. Merge the two lists of synsets from FRED and Visual Genome json file.
9. For each synset, launch a SPARQL query to Framester in order to retrieve all the evoked frames.
10. Collect all the frames evoked keeping track of the amount of evocations of each frame.
11. Produce the final json file showing: name of the frame evoked, number of evocation occurrences and image ID.



## RML Mapping and KG Construction

The next step in our pipeline was the definition of mapping rules for transforming input data into semantic web knowledge graphs, according to the developed Visual Sense ontology.

### RML and PyRML

For this purpose, we used the RML generic mapping language, based on and extending R2RML. The RDF Mapping language (RML) is a mapping language defined to express customized mapping rules from heterogeneous data structures and serializations to the RDF data model. RML is defined as a superset of the W3C-standardized mapping language, aiming to extend its applicability and broaden its scope, adding support for data in other structured formats.

In order to process the RML files, we utilized pyRML, a Python based engine tool developed by Andrea Nuzzolese. It is possible to use pyRML either by means of its API or the command line tool that is provided along with the source package.

### PyRML Mapping Rules

The mapping rules (in turtle format) can be accessed here. The mapping rules utilize three preprocessed JSON files specific to an image (image_data.json, scenegraphs.json, and regions.json) as sources. From these, logical sources are used to create multiple triple maps. In this first iteration of the pipeline, issues were identified with mapping nested structures. Therefore, one subset of data had to be converted from a JSON into tabular CSV data. Further refinements for the mapping rules are envisioned.

Some example mapping rules and declaration of sources:
```markdown

:ImageObjectTriplesMap 
    rml:logicalSource :ImageSource ;
    rr:subjectMap [
        rr:template "http://w3id.org/visualsense/resource/ImageObject/image_object_{image_id}";
        rr:class visualsense:ImageObject
    ] ;

    rr:predicateObjectMap [
        rr:predicate visualsense:hasLocation;
        rr:objectMap [
            rr:template "http://w3id.org/visualsense/resource/ImageRegion/image_region_{image_id}"  
        ]
    ] .

:DepictedObjectTriplesMap 
    rml:logicalSource :DepictedObjectSource ;
    rr:subjectMap [
        rr:template "https://w3id.org/visualsense/resource/DepictedObject/depicted_object_{object_id}";
        rr:class visualsense:DepictedObject
    ] ;

    rr:predicateObjectMap [
        rr:predicate visualsense:hasLocation;
        rr:objectMap [
            rr:template "https://w3id.org/visualsense/resource/BoundingBox/bb_dep_object_{object_id}"
        ]
    ] ;

    rr:predicateObjectMap [
        rr:predicate visualsense:isTypedBy;
        rr:objectMap [
            rr:template "http://etna.istc.cnr.it/framester2/data/framestersyn/{synsets}"
        ]
    ] ;

    rr:predicateObjectMap [
        rr:predicate rdfs:label;
        rr:objectMap [
            rml:reference "names";
            rr:datatype xs:string;
        ]
    ] ;

    rr:predicateObjectMap [
        rr:predicate visualsense:hasObjAttribute;
        rr:objectMap [
            rml:reference "attributes";
            rr:datatype xs:string;
        ]
    ] ;


    rr:predicateObjectMap [
        rr:predicate visualsense:isDepictedIn;
        rr:objectMap [
            rr:constant "http://w3id.org/visualsense/resource/ImageObject/image_object_2384656"
        ]
    ] .

:ImageSource rml:source "./sources/image_data.json";
    rml:referenceFormulation ql:JSONPath ;
    rml:iterator "$" .
    
:DepictedObjectSource rml:source "./sources/scenegraphs.json";
    rml:referenceFormulation ql:JSONPath ;
    rml:iterator "$.objects[*]" .
```

### KG Publication
The Knowledge Graph of one image (ID 2384656) was automatically created with our pipeline, and is available here. There were a few minor syntax issues, so post-processing was performed. The manually cleaned Knowledge Graph has been published here. This KG instantiates all classes defined by the Visual Sense ontology. As such, it contains knowledge about one image (Visual Genome ID 2384656) including co-occurent depicted objects, depicted relationships, attributes, pixel data, evoked WordNet synsets, and Conceptual Frames evoked by specific regions.

![Image](https://delfimpandiani.github.io/visualsense/images/kg.png)

### Ontology Testing

The eXtreme Design provides a precise methodology for testing which includes three types of tests that need to be conducted: (1) Competency question verification, (2) Inference verification, and (3) Error provocation. Competency question verification consists in the reformulation of the competency questions from natural language to SPARQL queries and running them against the ontology using a toy dataset which is supposed to include the expected result of the query. Inference verification tests are used to understand how the information needs to be produced, i.e. entered explicitly as assertions or derived from other facts through inferencing. Lastly, error provocation is a stress test of the ontology to verify how the ontology reacts when it is fed with erroneous facts or boundary data. The protocol that we have followed for each of the tests is the following. 

1. Gather requirements
2. Select requirement to be tested
3. Formulate test procedure
4. Create test case
5. Add test data
6. Determine expected result
7. Run test
8. Compare result
9. Analyze unexpected result
10. Document test
11. Iterate is necessary

## SPARQL Endpoint Publication

A SPARQL endpoint was created with Docker… available at...
