# Visual Sense: Automatically Making Multimodal Sense of the Visual World

This project aims at integrating the annotated image dataset Visual Genome (VG) with the knowledge graph resource Framester, in order to produce a linked data knowledge graph that contains multimodal (factual, linguistic, and visual) knowledge. Our goal was to develop a full flow that allows, for a VG image of choice, the automatic modelling, implementation and publication of a semantic web knowledge graph (RDF) containing multimodal data. To do so, we first analyzed the relevant datasets, and completed design and modeling tasks following the eXtreme Design Methodology in order to extract the schema of Visual Genome as an ontology TBox and create the Visual Sense Ontology. We then developed a pipeline [Fig. 1] to shape the data (ABox) accordingly, with four major stages: 1. Image Data Extraction, 2. Data Preprocessing, 3. Frame Evocation, 4. KG Construction.



Fig 1. General pipeline of the Visual Sense project. Starting from the data and knowledge provided by the Visual Genome project in JSON format, our pipeline selects allows for the automatic creation of semantic web knowledge graphs containing visual, factual and linguistic data.


## Datasets

Visual Genome (VG) is an annotated image dataset containing over 108K images where each image is annotated with an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects. Regarding relationships and attributes as first-class citizens of the annotation space, in addition to the traditional focus on objects, VG’s annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs. The Visual Genome dataset is among the first to provide a detailed labeling of object interactions and attributes, providing a first step of grounding visual concepts to language by canonicalizing the objects, attributes, relationships, noun phrases in region descriptions, and question & answer pairs to WordNet synsets.

Framester is a frame-based ontological resource acting as a hub between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create an interoperable predicate space formalized according to frame semantics and semiotics principles. Framester uses WordNet and FrameNet at its core, expanding to other resources transitively, and represents them in a formal version of frame semantics. Framester has a freely available dedicated SPARQL endpoint and an API. The schema of Framester is also available as an ontology.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Relevant links
Visual Genome: https://visualgenome.org/

Visual Genome JSON datasets: https://visualgenome.org/api/v0/api_home.html

Visual Genome API: https://visualgenome.org/api/v0/api_endpoint_reference.html

Framester: https://github.com/framester/Framester

Framester SPARQL Endpoint: http://etna.istc.cnr.it/framester2/sparql

Framester API: http://etna.istc.cnr.it/framester_web/




## Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

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

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/delfimpandiani/visualsense/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
