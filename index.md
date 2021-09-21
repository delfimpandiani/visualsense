# Visual Sense: Automatically Making Multimodal Sense of the Visual World
### By Delfina S. M. Pandiani, Stefano De Giorgis and Fiorela Ciroku 

This project aims at integrating the annotated image dataset Visual Genome (VG) with the knowledge graph resource Framester, in order to produce a linked data knowledge graph that contains multimodal (factual, linguistic, and visual) knowledge. Our goal was to develop a full flow that allows, for a VG image of choice, the automatic modelling, implementation and publication of a semantic web knowledge graph (RDF) containing multimodal data. To do so, we first analyzed the relevant datasets, and completed design and modeling tasks following the eXtreme Design Methodology in order to extract the schema of Visual Genome as an ontology TBox and create the Visual Sense Ontology. We then developed a pipeline [Fig. 1] to shape the data (ABox) accordingly, with four major stages: 1. Image Data Extraction, 2. Data Preprocessing, 3. Frame Evocation, 4. KG Construction.


![Image](https://delfimpandiani.github.io/visualsense/images/pipeline.jpg)
Fig 1. General pipeline of the Visual Sense project. Starting from the data and knowledge provided by the Visual Genome project in JSON format, our pipeline selects allows for the automatic creation of semantic web knowledge graphs containing visual, factual and linguistic data.


## Datasets

[Visual Genome (VG)](https://visualgenome.org/) is an annotated image dataset containing over 108K images where each image is annotated with an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects. Regarding relationships and attributes as first-class citizens of the annotation space, in addition to the traditional focus on objects, VG’s annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs. The Visual Genome dataset is among the first to provide a detailed labeling of object interactions and attributes, providing a first step of grounding visual concepts to language by canonicalizing the objects, attributes, relationships, noun phrases in region descriptions, and question & answer pairs to WordNet synsets.

Framester is a frame-based ontological resource acting as a hub between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create an interoperable predicate space formalized according to frame semantics and semiotics principles. Framester uses WordNet and FrameNet at its core, expanding to other resources transitively, and represents them in a formal version of frame semantics. Framester has a freely available dedicated SPARQL endpoint and an API. The schema of Framester is also available as an ontology.

### Relevant links
Visual Genome: https://visualgenome.org/

Visual Genome JSON datasets: https://visualgenome.org/api/v0/api_home.html

Visual Genome API: https://visualgenome.org/api/v0/api_endpoint_reference.html

Framester: https://github.com/framester/Framester

Framester SPARQL Endpoint: http://etna.istc.cnr.it/framester2/sparql

Framester API: http://etna.istc.cnr.it/framester_web/


## Visual Genome’s Data Model

The Visual Genome team provides two ways of accessing the data (always in JSON format):
Using the provided API to access the data directly from their server, without the need to keep any local data available.
Downloading all the data and use local methods to parse and work with the visual genome data.
We decided to use the second option, as it was more reliable. As a preliminary task, we did a manual exploration of the JSON files in order to further understand the way that the data was structured. As a result of this process, the original schema behind Visual Genome was detected [Fig. 2]. Certain issues became apparent, such as the use of different keys for the same conceptual instances in different JSON files (e.g., “id”, “image_id”), so before designing our ontology, we proposed an intermediary data model that took care of the detected duplications [Fig. 3].

![Image](https://delfimpandiani.github.io/visualsense/images/VG_orig.png)
Fig 2. Original data model of Visual Genome, reconstructed by manual inspection of the publicly available JSON files.
![Image](https://delfimpandiani.github.io/visualsense/images/VG_new.png)
Fig 3. Slimmer data model of Visual Genome, proposed to deal with duplicated information.


## Knowledge Engineering Methodology: eXtreme Design 

This knowledge engineering project has followed the eXtreme Design (XD) methodology proposed by Bloomqvist. eXtreme Design (XD) is an ontology design methodology whose core principle is ontology design patterns (ODP) reuse, as an explicit activity. ODPs are small ontologies which, ideally, form the bigger ontology with the correct alignment. They mediate between use cases (problem types) and design solutions. 

The general XD methodology first requires a focus on stories and Competency Questions (CQs), without going into much detail about ODPs. To do so, the ontology engineers (the so called customer team) get in close and frequent contact with domain experts, so as to collect the requirements for the ontology in the form of stories by using Google Forms or Github issues. In both cases, the key information that a story should contain is the goal/objective of the story and questions that need to be answered in order to reach that goal. Once the stories are collected, they are prioritized and then broken down by the ontology engineers. They identify the main concepts and the possible general constraints from the user stories to create CQs. Competency questions are the means to collect requirements in the XD methodology. Each story has a table of requirements (competency questions) that need to be fulfilled and later tested. The testing of the CQs is one of the main tests that are executed in the XD methodology. The practice is to create a test case for each competency question which contains information such as requirement (CQ), test category, test case description, test, input test data, expected result, actual result, executed by, execution date, environment, execution result and execution comment. 


## The Visual Sense Ontology

Visual Sense ontology is an ontology that aims to formally represent Visual Genome’s annotation components and their interrelationships, and to connect these components to the Framester schema, so as to further ground visual data to language. The ontology was developed following the XD ontology design methodology. Below we present how the Visual Sense ontology has reused ontology design patterns (ODPs) and been aligned to and reused other ontologies while presenting its T-Box [Fig. 4], with explanations of its crucial classes and properties. Further details of all classes and properties are available in LODE-Powered Visual Sense Ontology Documentation. LODE is a tool for producing human-readable documentation of the ontologies. The Visual Sense ontology has been published at the following permanent IRI: https://w3id.org/visualsense.

![Image](https://delfimpandiani.github.io/visualsense/images/vsontology.png)
Figure 4. T-Box of the Visual Sense ontology. The ontology is aligned to Dolce Ultra Light and the Framester Schema, and reuses Ontology Design Patterns.


### Ontology and Ontology Design Pattern (ODP) Alignment and Reuse

The Visual Sense Ontology is aligned to DOLCE Ultra Lite (DUL) foundational ontology and reuses classes and properties from the Framester schema. Furthermore, certain Ontology Design Patterns (ODPs) were reused in the design and modeling of the Visual Sense Ontology.

### Alignment to DUL and ODP Reuse

The alignment to DUL was due to the cognitive nature of the Visual Sense ontology, as the task of representing and improving formal knowledge in the visual sensemaking process is particularly coherent to the human cognitive and socio-cultural aspects covered by DUL. What the Visual Genome model considers simply an “image”, is considered in the Visual Sense Ontology as something that semantically is spread into two different classes, reusing the Content ODP Information Realization, by being spread onto two different classes, :ImageObject and :ImageRegion. :ImageObject is modeled as a subclass of dul:InformationObject, since the focus of expressiveness of this class is on the meaning that is conveyed in and by the Image itself.This class of :ImageObject is furthermore axiomatized as having a realization through a location in some :ImageRegion. The class :ImageRegion is in fact a subclass of dul:SpaceRegion and it represents the physical extension of the image, the spatial area occupied by the image measured in terms of pixels. 

This conceptual duality is coherently kept with all the other classes in the ontology: a mereological relation exists between :ImageRegion and any other subpart of the image, with the possibility to query the ontology based on the spatial area of interest. In particular, these physical subparts of an :ImageRegion are the areas, bound by coordinates, which are recognised in the Visual Genome dataset as areas of location for Regions and Objects. They are modeled as :BoundingBoxes, which are subclasses of dul:SpaceRegion, they are explicitly dul:partOf some :ImageRegion, and they are also the dul:locationOf some :DepictedObject or :DepictedRegion. 

The :DepictedRegion class applies the Situation Content Ontology Design Pattern, whose intent is to represent contexts or situations, and the things that are contextualized. This pattern itself reifies the N-ary Relation Logical Ontology Design Pattern, and it allows the contextualization of things that have something in common, or are associated: a same place, time, view, causal link, systemic dependence, etc. In the case of Visual Sense, :DepictedRegion is modeled as a subclass of the class dul:Situation,in the sense that a depicted region provides a context and is the setting for a variety of things (depicted objects, relationships between depicted objects, evoked conceptual frames) that share a same informational space.

### Alignment to Framester Schema

The other ontology reused in Visual Sense is the Framester schema, in particular the fschema:Frame and fschema:ConceptualFrame classes are reused both for the frames evoked by some :DepictedObject, located in some :BoundingBox, and the frames recognised as evoked by the FRED tool, while the fschema:WnSynsetFrame is reused for the frames evoked by some specific Wordnet Synset.

##  Frame Evocation Experiments

The usage of WordNet synsets to disambiguate object annotations in the Visual Genome repository allows the exploration of frame evocation via querying the Framester hub. Specifically, Framester querying can be performed in order to retrieve Conceptual Frames evoked by synsets used as labels for some Image Region. Additionally, Knowledge Graphs (KG) can be automatically generated with FRED tool using sentences (images’ scene descriptions) as input, and thus it is possible to extract formal knowledge from the natural language provided in the Visual Genome annotations. Since WordNet synsets are related to VG depicted objects, and each depicted object is localized by a bounding box in an image, this in turn allows the localization of evoked frames to a specific set of pixels. As such, the use of lexical resources such as Framester and FRED allows for sophisticated grounding of visual data to language.

### Experiments, Lessons, and Refinements
The first frame evocation attempt was driven by the principle of maximizing the amount of knowledge extraction, using each lexical unit (LU) of each bounding box in an image as input variable for a SPARQL query to Framester, in order to retrieve all the frames potentially evoked by all the synset of the LU in input. It is worth mentioning that each Image in Visual Genome has an average of 50 Regions, and for each region there is a minimum of one object (but often more than one), some relationships between objects, and some attributes for each object. The result of this first attempt was a massive amount of evoked frames (in the order of magnitude of hundreds of frames per image) which was not useful in extracting real knowledge about the semantic content of the analyzed image, since it was just the set of frames potentially evoked by each sense of each LU.

Since the interest was not on the potential frame evocation but on the actual knowledge contained in each image, an improvement was performed by applying the following heuristic, with the purpose to decrease noise and increase meaningfulness and precision of frame evocation: instead of using the LU from annotations, since Visual Genome already provides WordNet synsets to disambiguate annotations, those synsets were used to query Framester. The result was a considerable amount of evoked frames, but because of the structure of each image json file, the frame evocation was still related mainly to the presence or absence of some entity in an image, meaning, the frame evocation was in percentage mainly a consequence of the implicit question “what is there” instead of “what is happening”. For this reason, being interested conceptually more in the second question, a further restriction was applied.

The final heuristic was then to focus on those Regions having at least two objects and a relation between them, and to be sure, via NLP techniques, that this relation was a verb (and not e.g. a preposition). A first confirmation of this intuition’s rightfulness comes directly from the data: regions with verbal relations between objects are the ones in which there is the highest "semantic concentration", in terms of number of relations to and from entities.

### Frame Evocation Pipeline

![Image](https://delfimpandiani.github.io/visualsense/images/evocation_pipeline.png)

```markdown
Frame evocation some code of the pipeline

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

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

## SPARQL Endpoint Publication

A SPARQL endpoint was created with Docker… available at...
