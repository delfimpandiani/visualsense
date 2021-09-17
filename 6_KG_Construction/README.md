# RML Mapping and KG Construction

The next step in our pipeline was the definition of mapping rules for transforming input data into semantic web knowledge graphs, according to the developed Visual Sense ontology.

## RML and PyRML

For this purpose, we used the RML generic mapping language, based on and extending R2RML. The RDF Mapping language (RML) is a mapping language defined to express customized mapping rules from heterogeneous data structures and serializations to the RDF data model. RML is defined as a superset of the W3C-standardized mapping language, aiming to extend its applicability and broaden its scope, adding support for data in other structured formats.

In order to process the RML files, we utilized pyRML, a Python based engine tool developed by Andrea Nuzzolese. It is possible to use pyRML either by means of its API or the command line tool that is provided along with the source package.

## PyRML Mapping Rules

The mapping rules (in turtle format) can be accessed here. The mapping rules utilize three preprocessed JSON files specific to an image (image_data.json, scenegraphs.json, and regions.json) as sources. From these, logical sources are used to create multiple triple maps. In this first iteration of the pipeline, issues were identified with mapping nested structures. Therefore, one subset of data had to be converted from a JSON into tabular CSV data. Further refinements for the mapping rules are envisioned.

## KG Publication
The Knowledge Graph of one image (ID 2384656) was automatically created with our pipeline, and is available (image_2384656_graph.ttl). There were a few minor syntax issues, so post-processing was performed. The manually cleaned Knowledge Graph has been published (manually_cleaned_KG_1_image.ttl). This KG instantiates all classes defined by the Visual Sense ontology. As such, it contains knowledge about one image (Visual Genome ID 2384656) including co-occurent depicted objects, depicted relationships, attributes, pixel data, evoked WordNet synsets, and Conceptual Frames evoked by specific regions.
