## From Visual to Multimodal Sensemaking

This project aims at integrating a (part of a) resource of annotated images (Visual Genome) in Framester, a linked data knowledge graph that contains factual, linguistic, and visual knowledge.

Firstly, we will extract the schema of Visual Genome as an ontology TBox, and shape its data (ABox) accordingly.

Secondly, we will align the TBox and the ABox to Framester, by using the proximal entities that are contained in both Visual Genome and Framester (mostly, WordNet synsets).

Thirdly, we will generate a "scene ontology" out of Visual Genome, e.g. by exploiting existing relations and frames from Framester, which can be associated with the links existing in the clusters of annotations from Visual Genome.

Visual Genome: https://visualgenome.org/

Visual Genome JSON datasets: https://visualgenome.org/api/v0/api_home.html

Visual Genome API: https://visualgenome.org/api/v0/api_endpoint_reference.html

Framester: https://github.com/framester/Framester

Framester SPARQL Endpoint: http://etna.istc.cnr.it/framester2/sparql

Framester API: http://etna.istc.cnr.it/framester_web/

Framester schema: https://raw.githubusercontent.com/framester/schema/master/ontology.owl

Contents of the repository so far:

VG Reconstruction folder:
"Old" model: an image and a graph.ml of the reconstructed ("old") underlying model of VG, based on the JSON files to be queried. It also contains three images of the kinds of repetitions/complications found in the model (e.g., depending on which jkson file is queried, the same conceptual entity (eg., image id) has different names/dict values ("id" and "image_id")
"New" model: an image and a graph.ml of a cleaner version ("new") underlying model of VG, that attempts to take care of the repetitive situations (basically, trying to replace two different names referring to the same entity with just one entity)




You can use the [editor on GitHub](https://github.com/delfimpandiani/visualsense/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

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
