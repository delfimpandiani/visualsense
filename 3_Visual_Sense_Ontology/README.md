# The Visual Sense Ontology

Visual Sense ontology is an ontology that aims to formally represent Visual Genome’s annotation components and their interrelationships, and to connect these components to the Framester schema, so as to further ground visual data to language. The ontology was developed following the XD ontology design methodology. Below we present how the Visual Sense ontology has reused ontology design patterns (ODPs) and been aligned to and reused other ontologies while presenting its T-Box [Fig. 3], with explanations of its crucial classes and properties. Further details of all classes and properties are available in LODE-Powered Visual Sense Ontology Documentation. LODE is a tool for producing human-readable documentation of the ontologies. The Visual Sense ontology has been published at the following permanent IRI: https://w3id.org/visualsense.

![TBox_Visual_Sense](https://user-images.githubusercontent.com/44606644/133809023-6306e23e-1465-4c68-ac21-a413f44fd9ff.png)
Figure 4. T-Box of the Visual Sense ontology. The ontology is aligned to Dolce Ultra Light and the Framester Schema, and reuses Ontology Design Patterns.

## Ontology and Ontology Design Pattern (ODP) Alignment and Reuse

The Visual Sense Ontology is aligned to DOLCE Ultra Lite (DUL) foundational ontology and reuses classes and properties from the Framester schema. Furthermore, certain Ontology Design Patterns (ODPs) were reused in the design and modeling of the Visual Sense Ontology.

### Alignment to DUL and ODP Reuse

The alignment to DUL was due to the cognitive nature of the Visual Sense ontology, as the task of representing and improving formal knowledge in the visual sensemaking process is particularly coherent to the human cognitive and socio-cultural aspects covered by DUL. What the Visual Genome model considers simply an “image”, is considered in the Visual Sense Ontology as something that semantically is spread into two different classes, reusing the Content ODP Information Realization, by being spread onto two different classes, :ImageObject and :ImageRegion. :ImageObject is modeled as a subclass of dul:InformationObject, since the focus of expressiveness of this class is on the meaning that is conveyed in and by the Image itself.This class of :ImageObject is furthermore axiomatized as having a realization through a location in some :ImageRegion. The class :ImageRegion is in fact a subclass of dul:SpaceRegion and it represents the physical extension of the image, the spatial area occupied by the image measured in terms of pixels. 

This conceptual duality is coherently kept with all the other classes in the ontology: a mereological relation exists between :ImageRegion and any other subpart of the image, with the possibility to query the ontology based on the spatial area of interest. In particular, these physical subparts of an :ImageRegion are the areas, bound by coordinates, which are recognised in the Visual Genome dataset as areas of location for Regions and Objects. They are modeled as :BoundingBoxes, which are subclasses of dul:SpaceRegion, they are explicitly dul:partOf some :ImageRegion, and they are also the dul:locationOf some :DepictedObject or :DepictedRegion. 

The :DepictedRegion class applies the Situation Content Ontology Design Pattern, whose intent is to represent contexts or situations, and the things that are contextualized. This pattern itself reifies the N-ary Relation Logical Ontology Design Pattern, and it allows the contextualization of things that have something in common, or are associated: a same place, time, view, causal link, systemic dependence, etc. In the case of Visual Sense, :DepictedRegion is modeled as a subclass of the class dul:Situation,in the sense that a depicted region provides a context and is the setting for a variety of things (depicted objects, relationships between depicted objects, evoked conceptual frames) that share a same informational space.

### Alignment to Framester Schema

The other ontology reused in Visual Sense is the Framester schema, in particular the fschema:Frame and fschema:ConceptualFrame classes are reused both for the frames evoked by some :DepictedObject, located in some :BoundingBox, and the frames recognised as evoked by the FRED tool, while the fschema:WnSynsetFrame is reused for the frames evoked by some specific Wordnet Synset.

This project was authored by Delfina S. M. Pandiani, Stefano Di Giorgis, and Fiorela Ciroku.
