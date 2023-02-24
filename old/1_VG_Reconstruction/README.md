# Visual Genome Model Reconstruction

Visual Genome (VG) is an annotated image dataset containing over 108K images where each image is annotated with an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects. Regarding relationships and attributes as first-class citizens of the annotation space, in addition to the traditional focus on objects, VG’s annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs. The Visual Genome dataset is among the first to provide a detailed labeling of object interactions and attributes, providing a first step of grounding visual concepts to language by canonicalizing the objects, attributes, relationships, noun phrases in region descriptions, and question & answer pairs to WordNet synsets.

## Visual Genome Components

According to its documentation, the schema behind VG has seven main components: region descriptions, objects, attributes, relationships, region graphs, scene graphs, and question answer pairs. More details about each of these components is hereby provided:

- Region descriptions 
-- are human generated and localized in a region of an image with a bounding box. They are allowed to have a high degree of overlap with each other. Noun phrases in region descriptions are canonicalized to WordNet synsets.
- Objects 
-- are delineated by a tight bounding box. The authors do not provide any explicit definition of what counts as objects, but their requirement to be covered by a bounding box points towards its semantics being of physical, depicted objects. The authors canonicalize them by mapping them to their most frequent matching synset in WordNet according to WordNet lexeme counts. They then refine this simple heuristic by hand-crafting mapping rules for the 30 most common failure cases.
- Attributes -- predicate something about an Object, most commonly regarding color (e.g., yellow), states/continuous actions (e.g., standing), sizes (e.g. tall), and materials (e.g. plastic). They are also canonicalized: the authors normalize each attribute based on morphology (so called “stemming”) and map them to WordNet adjectives. As with object canonicalization, the authors include 15 hand-crafted rules to address common failure cases, which typically occur when the concrete or spatial sense of the word seen in an image is not the most common overall sense. The most common attributes describing people are intransitive verbs describing their states of motion. Certain sports (e.g. skiing, surfboarding) are over- represented due to an image bias towards these sports in the original image dataset.
- Relationships -- are connections between Object, and are directed from “subject” to “object”, and most commonly regard actions (e.g. jumping over), spatial relations (e.g. is behind), descriptive verbs (e.g. wear), prepositions (e.g. with), comparative relations (e.g. taller than), and prepositional phrases (e.g. drive on). For canonicalization of relationships, the authors ignore all prepositions, as they are not recognized by WordNet. Since the meanings of verbs are highly dependent upon their morphology and syntacting placement, the authors try to find WordNet synsets whose sentence frames (formalized syntactic frames in which a certain sense of a word may appear) match with the context of the relationship. For each verb-synset pair, the authors then consider the root hypernym of that synset to reduce potential noise from WN’s fine-grained sense distinctions. They also include 20 hand-mapped rules to correct for WN’s lower representation of concrete or spatial senses. The authors sent all their mappings along with the top four alternative synsets for each term to AMT.
- Region graphs -- are structured representations of a part of the image. Each region graph is a  directed graph representation of a region localized in an image.  The nodes in the graph represent objects, attributes, and relationships. Objects are linked to their respective attributes while relationships link one object to another.
- Scene graphs -- are the union of all region graphs for an image, and contain all objects, attributes, and relationships from each region description.
- Question and answer pairs -- are pairs of collected questions (6 different types of questions per image: what, where, how, when, who, and why) and answers. They include both freeform QAs, based on the entire image, and region-based QAs, based on selected regions of the image.  Noun phrases in region descriptions are canonicalized to WordNet synsets.


## Visual Genome’s Data Model

The Visual Genome team provides two ways of accessing the data (always in JSON format):
Using the provided API to access the data directly from their server, without the need to keep any local data available.

Downloading all the data and use local methods to parse and work with the visual genome data.
We decided to use the second option, as it was more reliable. As a preliminary task, we did a manual exploration of the JSON files in order to further understand the way that the data was structured. As a result of this process, the original schema behind Visual Genome was detected [Fig. 2]. Certain issues became apparent, such as the use of different keys for the same conceptual instances in different JSON files (e.g., “id”, “image_id”), so before designing our ontology, we proposed an intermediary data model that took care of the detected duplications [Fig. 3].

![VG_orig](https://user-images.githubusercontent.com/44606644/133807179-328c20ad-601f-40c1-9f09-4ee0eb9e06ed.png)
Fig 2. Original data model of Visual Genome, reconstructed by manual inspection of the publicly available JSON files.

![VG_new](https://user-images.githubusercontent.com/44606644/133807196-538f9109-a650-4978-ad76-29f13a9d431e.png)
Fig 3. Slimmer data model of Visual Genome, proposed to deal with duplicated information.

This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.
