# Image Data Extraction and Preprocessing

**Smaller files**

Due to the considerable size of the JSON files, we started by doing some data pre-processing, in particular the first step was to parse the scenegraph.json and regiongraph.json files provided by VG into smaller files via the built in methodology:

![split1_scenegraph.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/split1_scenegraph.png)

The following steps are, for this reason, meant to be applied to each single split.

**Data polishing**

In order to facilitate the subsequent operations (see Frame Evocation pipeline for further information), the next step was to change the syntax of WordNet synsets. This was because the syntax used in the original Visual Genome file did not correspond either to the original one in WordNet, nor to the one used in Framester hub for any synset. As such, we applied a transformation so that the syntax of synsets matches the one used for the Framestersyn class in Framester, which is the one used in the frame evocation pipeline. In detail, the syntax for both objects’ and relationships’ synsets was changed from:<br/>

{<br/>
‘synsets’ : [ ‘backpack.n.01’ ]<br/>
}<br/>
To:<br/>
{<br/>
‘synsets’ : ‘Backpack.n.1’<br/>
}<br/>

That is, we stripped off squared brackets (turning the value from a list into a string), capitalized the first letter, and replaced the double digit with a single one. 

**Creating a Subset of Action-Oriented Images**

In order to populate our Knowledge Graph (KG) with meaningful information, we decided that for the time being we were more interested in populating the graph with “action-oriented” images -- images where some agent/s (e.g. humans, animals) are depicted in some sort of action, as opposed to images depicting static landscapes. This was due to the assumption that frame evocation would be higher and/or more varied with action-oriented images. Therefore, it was decided that, for the time being, only images that are associated with at least one verbal (non-prepositional) relationship would be used to populate the Visual Sense KG. This decision is reflected in the definition of image region in the ontology T-Box, which must contain a verbal relationship between two objects in order to be included into the Knowledge Graph. 

To perform the image subset creation, a function was defined to iterate through the (split) scenegraph JSON file’s relations in order to apply to each relationship label a part of speech (POS) tag. Then, only relationships whose labels had been tagged as verbs were selected, pruning instead the data of prepositional relations (OF, ON, WITH etc). Subsequently, images found to have verbal relations were counted and appended to a list, and a dictionary was created, the image_id’s as keys, and each image’s number of occurrences of verbal relations as values:

![find_verbal_rel.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/find_verbal_rel.png)


**Ranking Images by "Actionness"**

In order to populate our KG in an orderly manner, we decided to rank the images in the VG dataset, in order to decide which images to introduce to the Visual Sense Knowledge Base first. The first criterion adopted was to rank images by the total number of occurrences of verbal (non-prepositional) relationships depicted in them. The dictionary created in the precedent step was used for this task. To visually explore the distribution of the ranked images, the matplotlib Python library was used to plot the distribution of images according to the number of occurrences of verbal relations per image.

![verb_occurr_plot.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/verb_occurr_plot.png)


As shown in figure, the vast majority of images lie in the span between 1 to 40 occurrences per image of verbal relations, with some peculiar graph outliers, namely the two dots showing images with about 90 and 150 verbal relation occurrences each. This quantitative analysis step was fundamental to a second layer: the qualitative analysis of data.

**Ranking Images by Verbal Relation Variance**

This first criterion (number of total occurrences of verbal per image) to rank images was based, in linguistics terms, on the number of verbal token occurrences per image. However, we hypothesized that another interesting metric would be ranking images by their number of unique verbal types, i.e. by the number of unique verbal relationships present in each image. Since conceptually we were more interested in e.g. a scene with less occurrences of the same action but more types of different actions, a script was developed to count the amount of unique verbal relations per image. The results were plotted using matplotlib Python library:

![types_verb_rel_plot.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/types_verb_rel_plot.png)


As shown in figure, the vast majority of images include only 1-4 unique verbal relations types. The most common verbs are auxiliary verbs like “Have.v.1” and “Be.v.1”, while some other most commonly used verbs are those to describe images, like “Wear.v.1” or “Stand.v.1”.

**Final Ranking and Possible Approaches**

A final remark is worth to be mentioned: albeit the final ranking of images adopted was the one based on unique verbal relations per image, a combination of the two rankings methodologies above mentioned, and the consequent proposal of a unified approach, is also possible. Conceptually it seemed more adherent to the modeling approach chosen to evaluate variance as more relevant than frequency, but e.g. once also the prepositional relations will be taken into account, a plausible approach could be a weighted score combining local frequency (namely the number of occurrences per image), local variance (the number of unique relations per image) with global frequency and variance (freq. and var. considering all relations of all images taken into account.)






This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.
