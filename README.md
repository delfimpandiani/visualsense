# Visual Sense: Automatically Making Multimodal Sense of the Visual World

This repository holds all data and resources arising from the development of Visual Sense, which aims to integrate the Visual Genome image dataset with the linguistic resource Framester. Visual Sense is a knowledge engineering project designing, implementing and publicating semantic web knowledge graphs (RDF) by applying methods and tools learned during the Knowledge Engineering course taught by Prof. Valentina Presutti and Prof. Andrea Nuzzolese (2021, University of Bologna).

This project aims at integrating the annotated image dataset Visual Genome (VG) with the knowledge graph resource Framester, in order to produce a linked data knowledge graph that contains multimodal (factual, linguistic, and visual) knowledge. Our goal was to develop a full flow that allows, for a VG image of choice, the automatic modelling, implementation and publication of a semantic web knowledge graph (RDF) containing multimodal data. To do so, we first analyzed the relevant datasets, and completed design and modeling tasks following the eXtreme Design Methodology in order to extract the schema of Visual Genome as an ontology TBox and create the Visual Sense Ontology. We then developed a pipeline [Fig. 1] to shape the data (ABox) accordingly, with four major stages: 1. Image Data Extraction, 2. Data Preprocessing, 3. Frame Evocation, 4. KG Construction.


![photo_2021-09-14 15 40 49](https://user-images.githubusercontent.com/44606644/133268469-8b77821d-af7e-466c-88f7-ff9a221e3ada.jpeg)
Fig 1. General pipeline of the Visual Sense project. Starting from the data and knowledge provided by the Visual Genome project in JSON format, our pipeline selects allows for the automatic creation of semantic web knowledge graphs containing visual, factual and linguistic data.


## Datasets

Visual Genome (VG) is an annotated image dataset containing over 108K images where each image is annotated with an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects. Regarding relationships and attributes as first-class citizens of the annotation space, in addition to the traditional focus on objects, VG’s annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs. The Visual Genome dataset is among the first to provide a detailed labeling of object interactions and attributes, providing a first step of grounding visual concepts to language by canonicalizing the objects, attributes, relationships, noun phrases in region descriptions, and question & answer pairs to WordNet synsets.

Framester is a frame-based ontological resource acting as a hub between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create an interoperable predicate space formalized according to frame semantics and semiotics principles. Framester uses WordNet and FrameNet at its core, expanding to other resources transitively, and represents them in a formal version of frame semantics. Framester has a freely available dedicated SPARQL endpoint and an API. The schema of Framester is also available as an ontology.

## Relevant links
Visual Genome: https://visualgenome.org/

Visual Genome JSON datasets: https://visualgenome.org/api/v0/api_home.html

Visual Genome API: https://visualgenome.org/api/v0/api_endpoint_reference.html

Framester: https://github.com/framester/Framester

Framester SPARQL Endpoint: http://etna.istc.cnr.it/framester2/sparql

Framester API: http://etna.istc.cnr.it/framester_web/

Framester schema: https://raw.githubusercontent.com/framester/schema/master/ontology.owl


Contents of the repository so far:
- **1 VG Reconstruction**: Contains information about VG, the reconstructed ("old") underlying model of Visual Genome, based on the JSON files to be queried, images of the kinds of repetitions/complications found in the model, and a "cleaner" version ("new") underlying model of VG, that attempts to take care of the repetitive situations.
- **2 eXtreme Design** Methodology: This knowledge engineering project has followed the eXtreme Design (XD) methodology proposed by Bloomqvist. eXtreme Design (XD) is an ontology design methodology whose core principle is ontology design patterns (ODP) reuse, as an explicit activity. This folder contains information about our XD methodolofy (stories, competency questions, SPARQL test queries)
- **3 Visual Sense Ontology**: contains the visual sense ontology (in owl format), information about ontology alignment, ontology design pattern (ODP) reuse, graphs of the TBox, and documentation.
- **4 Image Data Extraction and Preprocessing**: Contains scripts to split big json files in smaller, more processable files, as well as the preprocessing pipeline with salience criteria and some stats about semantics information distribution in Visual Genome images.
- **5 Frame Evocation** Experiments: Information, code, and instructions about how we tested the evocation of Framester frames from the VG data.
- **6 KG Construction**: Contains the RML mapping rules to convert the data into KGs using the Visual Sense ontology, as well as the published first version of the KG.
- **7 Ontology Testing**: This folder contains the test cases for ontology testing.


This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.
