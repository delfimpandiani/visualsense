# Frame Evocation Experiments

The usage of WordNet synsets to disambiguate object annotations in the Visual Genome repository allows the exploration of frame evocation via querying of the Framester hub. Specifically, Framester querying can be performed in order to retrieve Conceptual Frames evoked by synsets used as labels for some Image Region, DepictedObject, or ObjectRelationship. Additionally, it is possible to extract formal frame knowledge from the natural language provided in the Visual Genome annotations, by automatically generating Knowledge Graphs (KG) with the FRED tool, using sentences (images’ scene descriptions) as input. Since WordNet synsets are related to Depicted Objects, region descriptions are related to Depicted Regions, and each Depicted Object and Depicted Region is localized by a bounding box in an image, this in turn allows the localization of evoked frames to a specific set of pixels. As such, the integration of lexical resources such as Framester and FRED allows for sophisticated grounding of visual data to language.

## Experiments, Lessons, and Refinements

The first frame evocation attempt was driven by the principle of maximizing the amount of frame knowledge extraction, using each lexical unit (LU) of each bounding box in an image as input variable for a SPARQL query to Framester, in order to retrieve all the frames potentially evoked by all the synset of the LU in input. It is worth mentioning that each Image in Visual Genome has an average of 50 Regions, and for each region there is a minimum of one object (but often more than one), some relationships between objects, and some attributes for each object. The result of this first attempt was a massive amount of evoked frames (in the order of magnitude of hundreds of frames per image) which was not useful in extracting real knowledge about the semantic content of the analyzed image, since it was just the set of frames potentially evoked by each sense of each LU.

Since the interest was not on the potential frame evocation but on the most likely knowledge contained in each image, an improvement was performed by applying the following heuristic, with the purpose to decrease noise and increase meaningfulness and precision of frame evocation: instead of using the LU from annotations, since Visual Genome already provides WordNet synsets to disambiguate annotations, those synsets were used to query Framester. The result was a considerable amount of evoked frames, but because of the structure of each image JSON file, the frame evocation was still related mainly to the presence or absence of some object in an image. This meant that the frame evocation was mainly answering the implicit question “what is there” instead of “what is happening”. 

For this reason, as we were interested conceptually more in the second question, a further restriction was applied. The heuristic was to focus on Regions having at least two objects and a relation between them, and to be sure, via NLP techniques, that this relation was a verb (and not e.g. a preposition). A first confirmation of this intuition’s rightfulness comes directly from the data: regions with verbal relations between objects are the ones in which there is the highest "semantic concentration", in terms of number of relations to and from entities.



## Frame Evocation Pipeline

![frame_evocation_pipeline.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/5_Frame_Evocation/frame_evocation_pipeline.png)

A summary of the final pipeline is presented here, step by step, while the full code is available [here](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/5_Frame_Evocation/pipeline_cleaned.py).

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


## Final Output

The final output is a json file organized as follows:

```
{
    "frames_evoked": [
        {
            "frame": "https://w3id.org/framester/data/framestercore/Buildings",
            "frequency": "4",
            "imageID": "861"
        } ]
}

```



This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.


