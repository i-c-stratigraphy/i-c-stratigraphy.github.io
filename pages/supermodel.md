---
layout: page
title: "Stratigraphy Data Model"
permalink: /supermodel
---
# ICS Supermodel

> WARNING
> 
> This page and all the information about the ICS Supermodel is in an early phase of development.
> 
> This work was formally unveiled at the [STRATI 2026](https://strati2026.org/) conference in July 2026.
{: .warning}

Last updated: 2026-07-01 by [Nicholas Car](https://orcid.org/0000-0002-8742-7730)

1. [Abstract](#abstract)
2. [Motivation](#motivation)
3. [Modelling System](#modelling-system)
4. [Integrative Model](#integrative-model)
5. [Foreground Models](#foreground-models)
   1. [GTS Model](#gts-model)
   2. [Stratigraphy Model](#strat-model)
   3. [Visual Chart Model](#vc-model) 
   4. [GSSP Model](#gssp-model)
6. [Background Models](#background-models)
   1. [RDF](#rdf-model)
   2. [OWL](#owl-model)
   3. [OWL](#time-model)
   4. [THORS](#thors-model)
   5. [GeoSPARQL](#geosparql-model)
   6. [schema.org](#schema-model)
   7. [SKOS](#skos-model)
7. [Datasets](#datasets)
   1. [Geological Timescale  Dataset](#gts-dataset)
   2. [Visual Chart Dataset](#vc-dataset)
   3. [GSSP Dataset](#gssps-dataset)
8. [References](#references)

![](/images/supermodel/domains.svg){: width="50%"}

<a id="abstract"></a>
## 1. Abstract

The ICS Stratigraphy 'Supermodel' is an information model covering many aspects of
the stratigraphy domain as characterised by the International Commission on Stratigraphy (ICS).

It is made to allow for the growth of formal data definitions within the stratigraphy domain with the side benefits of
allowing for the integration of data both across distinct aspects of the domain and also for
data outside the domain, such as broader geological data, to be joined with it.

<a id="motivation"></a>
## 2. Motivation

Geology and resource sector science and engineering have long used large volumes of sophisticated data however many 
projects have to re-implement data associations related to stratigraphy due to a lack of standardised models and datasets
in that subdomain.

The [International Commission on Stratigraphy (ICS)](https://stratigraphy.org/), as the international authority responsible 
for establishing the fundamental scale used to represent the history of the Earth, has long published the [Chronostratigraphic Chart](https://stratigraphy.org/chart) as the principal reference 
resource within the field. Since 2026, this Chart has been made available as data, rather than solely as a document. 
The ICS is now undertaking efforts to define additional stratigraphic domain elements through the suite of standardised resources 
encompassed by this Supermodel, to enable projects to maximise reuse of stratigraphic information and to minimise redundant reimplementation.

By improving the consistency and authority of stratigraphy domain data, automated agents that on-deliver and otherwise
reuse ICS data, such as AI and web search systems, will have a greater likelyhood of doing so faithfully.

<a id="modelling-system"></a>
## 3. Modelling System
### 3.1. Semantic Web

The [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web) as a technical methodology and specific set of data models 
used widely for machine-readable content often, but not always, available on the Internet. Semantic Web approaches are used for 
this Supermodel to ensure its elements both reuse existing resources in this sector, such as international geological models,
and so that they can be maximally reused by others. Semantic Web resources are generally considered to exhibit interoperable and
open data best practices.

Specific reasons for the use of Semantic Web for this Supermodel are:

1. Semantic Web models can reuse other model's elements to a degree other modelling systems can't
   * this allows for maximal interoperability through shared model elements and modelling patterns
2. A large body of Semantic Web models in relevant domains already exist that can be reused
   * for example, the [SWEET Ontology](https://earthportal.eu/ontologies/SWEET), the [GeoSciML and similar vocabularies](https://cgi.vocabs.ga.gov.au/vocab)
     and other geology-domain Supermodels such as the [Supermodel for the Geological Survey of Western Australia](https://geological-survey-of-western-australia.github.io/GSWA-Supermodel/) 
3. Semantic Web models are "AI ready" 
   * they present their data and definitions in ways that Large Language Models and other technologies can readily use 

The two fundamental models within the Semantic Web that are used here are:

1. [RDF - Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework)
   * a technical, structural model for associating data elements
2. [OWL - Web Ontology Language](https://en.wikipedia.org/wiki/Web_Ontology_Language)
   * a set theory-based modelling language that represents conceptual classes of things and their properties 

RDF provides the data structure and OWL the general-purpose information model which these Supermodel models use to represent
things such as stratigraphic unit types, time periods, GSSP locations and so on.
### 3.2. The Supermodel

![](/images/supermodel/layers.svg){: width="40%"}

As with all things within this Supermodel's remit, the [Supermodel itself has a formal OWL model](https://linked.data.gov.au/def/supermodel). Its description says it is "...an enterprise data model that provides a structure for the creation of models for specialised datasets that allow for their uniqueness to be preserved but also provide for their deep integration."

The main elements of the Supermodel that matter in this case are the _Foreground_ and _Background_ models:

![](/images/supermodel/models-by-type.svg){: width="90%"}

Several specialised Foreground Models are already defined for obvious aspects of the stratigraphy domain and a number of 
pre-existing Background models covering generic domains relevant to stratigraphy such as spatiality, temporality, 
conceptual relations and scientific referencing, have been selected for Foreground Model alignment.

More Foreground and Background models are expected as scope grows.
### 3.3. Modelling Patterns
#### 3.3.1 Introducing Patterns

A modelling pattern is a reusable approach for modelling a recurring information scenario. For example, the [Time Ontology in OWL](#time-model)
provides a pattern for the expression of instances in time and periods of time that the various _foreground models_ use when
they wish to represent time objects.

A more fundamental pattern is the [_qualified relation_](https://patterns.dataincubator.org/book/qualified-relation.html) which
is a basic graph data model pattern used to link one object to another with qualifying information, such as the beginning of 
an _Age_ in the chronostratigraphic chart being liked to a time representation of it in _millions of years ago_ (MYA) 
qualified with an uncertainty. An example:

![](/images/supermodel/pattern-qualified.svg){: width="75%"}
#### 3.3.2 List of Patterns

It is not possible to make a comprehensive listing of patterns used by models as they overlap, however here are some 
significant ones used in this Supermodel:

<style>
   .display th,
   .display td {padding:3px}
   .display th {background: #eee}
   .display th {font-weight: bold}
   .display tr:nth-child(even) {background: #eee}
   .display tr:nth-child(odd) {background: #fff}
</style>

| Pattern                      | Purpose                                                                                                    | Defined By                          | Used In                                                       |
|------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------|
| Universal object identifiers | To ensure all data objects, both definitional and class instances, are identified uniquely and universally | [RDF Model](#rdf-model)             | all                                                           |
| Feature/Geometry Linking     | To associate an object with a geospatial location on Earth                                                 | [GeoSPARQL](#geosparql-model)       | [Stratigraphy Model](#strat-model), [GSSP Model](#gssp-model) |
| Indicating Temporality       | To associate an object with a temporal location                                                            | [Time Ontology in OWL](#time-model) | [GTS Model](#gts-model)                                       |
| Literature referencing by ID | To provide certainty in referencing scientific literature                                                  | [schema.org](#schema-model)         | [GSSP Model](#gssp-model)                                     |
| _more coming..._             |                                                                                                            |                                     |                                                               |
{: .display }
## 4. Integrative Model

![](/images/supermodel/integrative.svg){: width="75%"}

This Supermodel's integrative model is a skeleton model that joins the various foreground models together via relations 
between classes and them in other models.

Here the Stratigraphic Model is joined to the Geological Timescale model by means of instances of the former's 
`Stratigraphic Unit` class indicating related instances of the latter's `Geocronological Era` by the predicate `has age`.

This model is created entirely from elements within the Foreground and Background Models but is presented as a stand-alone
model also, to be used as a Supermodel high-level view.

<a id="foreground-models"></a>
## 5. Foreground Models

The Foreground Models in this Supermodel are the main, specialised, domain models developed specifically for this situation.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="gts-model"></a>
### 5.1. Geologic Timescale (GTS) Model

[http://resource.geosciml.org/ontology/gts](/pages/models/gts.html)

This model was originally developed in 2011 by Cox & Richards in 2012 [ref](#ref-gts) as a sophisticated _Time Ontology in OWL_ 
[ref](#ref-time)-based timescale dataset.

This model contains specialised forms of a `Geocronologic Era` class to represent the various Chronostratigraphic Chart 
time objects, such as `Period`, `Age`, `Super-Eon` and so on. It also has a specialised time instant class called 
`Geocrhonologic Boundary` used to contain the starting and finishing details of `Geocronologic Era` instances.

It also contains a `Stratigraphic Point` class which is used to associate `Geocrhonologic Boundary` objects with 
some GSSP information.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="strat-model"></a>
### 5.2. Stratigraphy Model

[http://resource.geosciml.org/ontology/stratigraphy](/pages/models/strat.html)

This model is developing alongside this Supermodel and will be published soon - mid-2026. 

It contains detailed stratigraphic domain information.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="vc-model"></a>
### 5.3. ICS Visual Chart Model

[http://resource.geosciml.org/ontology/isc-visual-chart](/pages/models/vis.html)

This is a [SKOS](#ref-skos) vocabulary representation of the instances of `Geocronologic Era` class instances - the 
Chronostratigraphic Chart's elements - with some time information taken from the _Geologic Timescale Model_ and additions
such as colours created to allow for the generation of the Chronostratigraphic Chart in traditional visual form from data,
as it is displayed at <https://stratigraphy.org/chart>.

When generated from parts, this model contains multilingual and alternate chronometric and stratigraphic labels as well.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="gssp-model"></a>
### 5.4. GSSP Model

[http://resource.geosciml.org/ontology/gssp](/pages/models/gssp.html)

This model is developing alongside this Supermodel and will be published soon - mid-2026. 

It contains a Semantic Web representation of the Global Boundary Stratotype Section and Points (GSSP) information
online at <https://stratigraphy.org/gssps> and will eventually be used to generate that web page, just as the Visual 
ICS Chart Model already generates the online Chart at <https://stratigraphy.org/chart>.
### Other Foreground Models

<a id="background-models"></a>
_More coming..._
## 6. Background Models

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="rdf-model"></a>
### 6.1. RDF Model

<https://www.w3.org/TR/rdf12-concepts/>

The Semantic Web's fundamental data structure model. [ref](#ref-rdf)

The model defines the low-level data structure used by all other models within the Supermodel and data created according to those models.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="owl-model"></a>
### 6.2. OWL Model

<https://www.w3.org/TR/owl2-overview/>

A data modelling, model built on RDF and widely used within the Semantic Web. [ref](#ref-owl)

OWL provides us with mathematical set theory-based mechanisms for modelling classes of objects. 

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="time-model"></a> 
### 6.3. Time Ontology in OWL

<https://www.w3.org/TR/owl-time/>

A fundamental domain ontology of temporal concepts, for describing the temporal properties of resources. [ref](#ref-time)

This ontology provides us with the basic temporal objects we need for geological time periods and for the expression
of relationsips between them, such as `Jurrasic` being _before_ `Cretaceous`. 

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="thors-model"></a>
### 6.4. Temporal Hierarchical Ordinal Reference System (THORS) Model

<http://resource.geosciml.org/ontology/timescale/thors>

This model, created in 2005 [ref](#ref-thors), provides a Semantic Web representation of the _Temporal Hierarchical Ordinal Reference Systems_
defined in GeoSciML [ref](#ref-gcml) using mostly _Time Ontology in OWL_ [ref](#ref-time) and [SKOS](#ref-skos) elements.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="geosparql-model"></a>
### 6.5. GeoSPARQL

<http://www.opengis.net/doc/IS/geosparql/1.1>

GeoSPARQL contains a small spatial domain OWL ontology that allow literal representations of geometries to be associated 
with spatial features and for features to be associated with other features using spatial relations.

GeoSPARQL `Feature` instances are used in this Supermodel to represent both GSSP locations and stratigraphic units that 
GSSPs are indicated within. 

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="schema-model"></a>
### 6.6. schema.org Model

<https://schema.org>

"Schema.org is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured 
data on the Internet" - <https://schema.org>.

schema.org provide a large number of general-purpose classes and predicates use to represent non-specialist information 
objects and relations, such as names (`schema:name`) and descriptions for things.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}


<a id="skos-model"></a>
### 6.7. Simple Knowledge Organization System (SKOS) Model

<https://www.w3.org/TR/skos-reference/>

A common data model for sharing and linking knowledge organization systems via the Web [ref](#ref-skos)

SKOS is widely used for modelling vocabularies of concepts.


<a id="datasets"></a>
## 7. Datasets

This section contains datasets that have been created according to the models in the previous section.

<a id="gts-dataset"></a>
### 7.1 Geological Timescale Dataset

<http://resource.geosciml.org/vocabulary/timescale/gts2020>

An RDF/OWL representation of the GeoSciML Geologic Timescale according to the [Geologic Timescale Model](#gts-model).

Data online at <https://github.com/i-c-stratigraphy/chart/blob/main/supermodel/datasets/gts2020.ttl>.

<a id="vc-dataset"></a>
### 7.2 ICS Visual Chart Dataset

<https://stratigraphy.org/chart>

A representation of the ICS' Chronostratigraphic Chart in RDF/OWL according to the [SKOS vocabulary model](#ref-skos).

Data online at <https://github.com/i-c-stratigraphy/chart/blob/main/chart.ttl>

<a id="gssps-dataset"></a>
### 7.3 GSSPs Dataset

<p style="color:red; font-style: italic;">TODO</p>

<a id="references"></a>
## 8. References

1. <a id="ref-rdf"></a> World Wide Web Consortium, _RDF 1.2 Concepts and Abstract Data Model_. W3C Candidate Recommendation (2026). <https://www.w3.org/TR/rdf12-concepts/>
1. <a id="ref-owl"></a> World Wide Web Consortium, _OWL 2 Web Ontology Language Document Overview (Second Edition)_. W3C Recommendation (2012). <https://www.w3.org/TR/owl2-overview/>
1. <a id="ref-thors"></a> Cox, S.J.D.,Richard, S.M. _A formal model for the geologic time scale and global stratotype section and point, compatible with geospatial information transfer standards_. Geosphere, 1, 119-137 (2005). <https://doi.org/10.1130/GES00022.1>
1. <a id="ref-gts"></a> Cox, S.J.D., Richard, S.M. _A geologic timescale ontology and service_. Earth Sci Inform 8, 5–19 (2015). <https://doi.org/10.1007/s12145-014-0170-6>
1. <a id="ref-gsml"></a> Open Geospatial Consortium, _OGC Geoscience Markup Language 4.1 (GeoSciML)_. OGC Implementation Standard (2017). <http://www.opengis.net/doc/geosciml/4.1>
1. <a id="ref-skos"></a> World Wide Web Consortium, _SKOS Simple Knowledge Organization System Reference_. W3C Recommendation (2009). <https://www.w3.org/TR/skos-reference/>
1. <a id="ref-time"></a> World Wide Web Consortium, _Time Ontology in OWL_. W3C Recommendation (2022). <https://www.w3.org/TR/owl-time/>

<!-- 1. <a id="ref-turtle"></a> World Wide Web Consortium, _RDF 1.1 Turtle_ W3C Recommendation (2014). <https://www.w3.org/TR/turtle/> -->

<!--

### 3.3 Data Syntax

The RDF data model used for the technical structure of all these models can be expressed in multiple data formats or
syntaxes which are equivalent regarding the information contained but have different tooling, compression and readability
values.

Most of the examples used here are implemented using the [Turtle](https://en.wikipedia.org/wiki/Turtle_(syntax)) [ref](#ref-turtle) syntax which is generally considered to be the, or one of the, most human-readable formats. Several examples are given 
in the [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) format to indicate use of a different format and one that may be
more acceptable to software developers.

The declaration of the Jurassic time period as a GTS `Geochronologic Era` objects with several properties in Turtle:

```turtle
PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>
PREFIX ischart: <http://resource.geosciml.org/classifier/ics/ischart/>
PREFIX schema: <https://schjema.org>

ischart:Jurassic
  a gts:GeochronologicEra ;
  schema:name "Jurassic" ;
.
```

...and in JSON-LD:

```json
{
  "@graph": [
    {
      "@id": "http://resource.geosciml.org/classifier/ics/ischart/Jurassic",
      "@type": "http://resource.geosciml.org/ontology/timescale/gts#GeochronologicEra",
      "https://schjema.orgname": "Jurassic"
    }
  ]
}
```

### Namespaces

Short prefixes are used in place of long, URL-like identifiers for namespace in this document within diagrams, example 
code (see above section) and within text. This allows the association of the data object for `Jurassic` to be associated 
with the word "Jurassic" which can be represented like this:

```turtle
<http://resource.geosciml.org/classifier/ics/ischart/Jurassic>
   <https://schema.org/name> "Jurassic" ;
.
```

to be represented like this:

```turtle
ischart:Jurassic
   schema:name "Jurassic" ;
.
```

The following table contains the commonly used ones:

**Prefix** | **Namespace**                                            | **Description**                             
--- |----------------------------------------------------------|---------------------------------------------
`ex` | `http://example.com/` | An examples namespace
`geo` | `http://www.opengis.net/ont/geosparql#`                  | GeoSPARQL namespace                         
`gts` | `http://resource.geosciml.org/ontology/timescale/gts#`   | Geologic Timescale Model namespace          
`gssp` | `http://resource.geosciml.org/vocabulary/gssp/`          | GSSP Model namespace                        
`gssps` | `http://resource.geosciml.org/vocabulary/gssps/`         | GSSPs Dataset namespace                     
`ischart` | `http://resource.geosciml.org/classifier/ics/ischart/`   | Chronostratigraphic Chart dataset namespace 
`owl` | `http://www.w3.org/2002/07/owl#`                         | OWL Ontology namespace                      
`rdfs` | `http://www.w3.org/2000/01/rdf-schema#`                  | RDFS Model namespace                        
`schema` | `https://schema.org/`                                    | schema.org model                            
`strat` | `http://resource.geosciml.org/ontology/stratigraphy/`    | Stratigraphy Model namespace                
`thors` | `http://resource.geosciml.org/ontology/timescale/thors#` | THORS Model namespace                       
`time` | `http://www.w3.org/2006/time#`                           | Time Ontology in OWL namespace              
`skos` | `http://www.w3.org/2004/02/skos/core#` | SKOS Ontology namespace
`sweetrg` | `http://sweetontology.net/realmGeol/`                    | SWEET Ontology Realm Geologic namespace
`xsd` | `http://www.w3.org/2001/XMLSchema#` | XSD Datatypes namespace
{: .alt}

<a id="integrative-model"></a>

-->