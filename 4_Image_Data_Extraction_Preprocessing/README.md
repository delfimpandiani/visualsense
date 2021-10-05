# Image Data Extraction and Preprocessing

**Smaller files**

Due to the considerable size of json files we started by doing some data pre processing, in particular the first step was to parse the scenegraph.json and regiongraph.json files in smaller files via this methodology:

![split1_scenegraph.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/split1_scenegraph.png)

The following steps are, for this reason, meant to be applied to each single split.

**Data polishing**

In order to facilitate following operations (see Frame Evocation pipeline for further information), the very first step was to change the syntax of WordNet synsets, for both objects and relationships, from this:<br/>
{<br/>
‘synsets’ : [ ‘backpack.n.01’ ]<br/>
}<br/>
To this:<br/>
{<br/>
‘synsets’ : ‘Backpack.n.1’<br/>
}<br/>

Stripping off squared brackets, capitalizing the first letter and replacing the double digit with a single one. The syntax used in the original Visual Genome file in fact was not corresponding to the original one in WordNet, nor to the one used in Framester hub for any synset; the new one applied by us matches the syntax used for Framestersyn class in Framester, used in the frame evocation pipeline.

**Creating a Subset of Action-Oriented Images**

In order to test our ontology with meaningful information we decided to rank the data in our dataset. The first criterion adopted was to introduce in the knowledge base images with the highest amount of relationships, according to our definition of image region in the ontology T-Box, namely verbal relationships.
As shown in the following figure:

![find_verbal_rel.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/find_verbal_rel.png)


A function was defined to iterate through the scenegraph split json file’s relations in order to apply to each label a pos (part of speech) tag, and select only those tagged as verbs, pruning data from prepositional relations (OF, ON, WITH etc). 
Then, images found having verbal relations were counted and appended to a separate list, while a new python dictionary was created, taking as key the image_id and as value the number of verbal relations in the image.

**Ranking Interesting Images**

To explore filtered data a script to rank images according to the mentioned criterion was applied, and the results are show in the following image (obtained via a separate script plotting data with matplotlib python library):

![verb_occurr_plot.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/verb_occurr_plot.png)


As shown in the image the vast majority of images is included in the span between 1 to 40 occurrences per image of verbal relations, with some peculiar graph outliers, namely the two dots showing images with about 90 and 150 verbal relation occurrences each.
This quantitative analysis step was fundamental to a second layer: the qualitative analysis of data.

**Qualitative analysis: Verbal Relation Variance**

The number of occurrences was the first way to filter images, but was not enough since images were ranked, to use linguistics categories, for the number of tokens per relation shown, but not for the number of types of relation per image, namely for the number of unique relations present in each image. Since conceptually we were more interested in e.g. a scene with less occurrences of the same action but more types of different actions, a script was developed to count the amount of unique relations per image.
The results were plotted via a separate script using matplotlib python library:

![types_verb_rel_plot.png](https://raw.githubusercontent.com/delfimpandiani/visualsense/main/4_Image_Data_Extraction_Preprocessing/types_verb_rel_plot.png)


As shown in Figure X the vast majority of images is presenting only 1-4 types of verbal relations per scene. The most common verbs are auxiliary verbs like “Have.v.1” and “Be.v.1”, while some other most commonly used verbs are those to describe images, like “Wear.v.1” or “Stand.v.1”.

**Final Data**

The final list of interesting images was realized combining these two approaches, and the final rank is available here, as well as all the scripts, available here. 






This project was authored by Delfina S. M. Pandiani, Stefano De Giorgis, and Fiorela Ciroku.
