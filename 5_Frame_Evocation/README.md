# Frame Evocation Experiments

The usage of WordNet synsets to disambiguate object annotations in the Visual Genome repository allows the exploration of frame evocation via querying of the Framester hub. Specifically, Framester querying can be performed in order to retrieve Conceptual Frames evoked by synsets used in an Image Region. Additionally, Knowledge Graphs (KG) can be automatically generated with the FRED tool using sentences (images’ scene descriptions) as input, and thus it is possible to extract formal knowledge from the natural language provided in the Visual Genome annotations. Since WordNet synsets are related to VG depicted objects, and each depicted object is localized by a bounding box in an image, this in turn allows the localization of evoked frames to a specific set of pixels. As such, the use of lexical resources such as Framester and FRED allows for sophisticated grounding of visual data to language.

## Experiments, Lessons, and Refinements

The first frame evocation attempt was driven by the principle of maximizing the amount of knowledge extraction, using each lexical unit (LU) of each bounding box in an image as input for a SPARQL query to Framester in order to retrieve all the frames potentially evoked by all the synset of the LU in input. It is worth mentioning that each Image in Visual Genome has an average of 50 Regions, and for each region there is a minimum of one object (but often more than one), some relationships between objects, and some attributes for each object. The result of this first attempt was a massive amount of evoked frames (in the order of magnitude of hundreds of frames per image) which was not useful in extracting real knowledge about the semantic content of the analyzed image, since it was just the set of frames potentially evoked by each sense of each LU.

Since the interest was not on the potential frame evocation but on the actual knowledge contained in each image, an improvement was performed by applying the following heuristic, with the purpose to decrease noise and increase meaningfulness and precision of frame evocation: instead of using the LU from annotations, since Visual Genome already provides WordNet synsets to disambiguate annotations, those synsets were used to query Framester. The result was still a considerable amount of evoked frames, but because of the structure of each image json file, the frame evocation was still related mainly to the presence or absence of some entity in an image, meaning, the frame evocation was in percentage mainly a consequence of the implicit question “what is there” instead of “what is happening”. For this reason, being interested conceptually more in the second question, a further restriction was applied.

The final heuristic was then to focus on those Regions having at least two objects and a relation between them, and to be sure, via NLP techniques, that this relation was a verb (and not e.g. a preposition). A first confirmation of a rightful intuition comes from looking at the data: those regions are the ones in which there is the highest "semantic concentration", in terms of number of relations to and from objects.

## Frame Evocation Pipeline

The final pipeline is composed by the following steps, and it’s available at ### put github ###

From a Visual Genome image extract the list of relationships whose predicate is a verb.
Extract the Region_ID and Region Description (of region having a verb as predicate).
Generate the knowledge graph from natural language via FRED tool, taking as input each Region Description.
Extract and store in a file all the frames evoked and all the synsets retrieved in each triple of the FRED graphs.
Extract the WordNet synsets used in the json file as annotations (from the regions having as predicate a verb).
Clean the WordNet synsets data extracted from Visual Genome json file, in order to have the iri of corresponding FramesterSyn entities, ready to be used to query Framester.
Clean the WordNet synsets data extracted from FRED graphs, in order to have the iri of corresponding FramesterSyn entities, ready to be used to query Framester.
Merge the two lists of synsets from FRED and Visual Genome json file.
For each synset, launch a SPARQL query to Framester in order to retrieve all the evoked frames.
Collect all the frames evoked keeping track of the amount of evocations of each frame.
Produce the final json file showing name of the frame evoked, number of evocation occurrences and image ID.


This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.
