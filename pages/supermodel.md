---
layout: page
title: "Stratigraphy Data Model"
permalink: /supermodel
---
## ICS Supermodel

> WARNING
> 
> This page and all the information about the ICS Supermodel are in an early phase of development, as of April 2026. 
> This work is aiming to be released at the [STRATI 2026](https://strati2026.org/) conference in June 2026.
{: .warning}

Last updated: 2026-04-22 by Nicholas Car

1. [Abstract](#abstract)
2. [Motivation](#motivation)
3. [Modelling System](#modelling-system)
4. [Integrative Model](#integrative-model)
5. [Foreground Models](#foreground-models)
   1. [GTS Model](#gts-model)
   2. [THORS Model](#thors-model)
   3. [Stratigraphy Model](#strat-model)
   4. [Vis. Chart Model](#ics-vc-model)
   5. [GSSP Model](#gssp-model)
6. [Background Models](#background-models)
7. [Example Data](#example-data)
8. [References](#references)

![](/images/supermodel/domains.svg){: width="50%"}

<a id="abstract"></a>
### 1. Abstract

The ICS Stratigraphy 'Supermodel' an overarching, enterprise and integrative, formal information model covering aspects of
the stratigraphy domain as characterised by the International Commission on Stratigraphy (ICS).
It includes several specialised 'foreground models' that can be used individually or together as well as a series of 'background models' used for integration.

The Supermodel and the foreground models are implemented using Semantic Web 
techniques which includes reusing general-purpose data modelling patterns. This allows these models can be integrated 
with more general geology models and even more general resources sector, environmental, scientific and economic models.

<a id="motivation"></a>
### 2. Motivation

Geology and resource sector science and engineering have long used large volumes of sophisticated data however many 
projects have to re-implement data associations related to stratigraphy due to a lack of standardised models and datasets
in that subdomain.

The [International Commission on Stratigraphy (ICS)](https://stratigraphy.org/), as the international authority responsible 
for establishing the fundamental scale used to represent the history of the Earth, has long published the [Chronostratigraphic Chart](https://stratigraphy.org/chart) as the principal reference 
resource within the field. Since 2025, this Chart has been made available as data, rather than solely as a document. 
The ICS is now undertaking efforts to define additional stratigraphic domain elements through the suite of standardised resources 
encompassed by this Supermodel, to enable projects to maximise reuse of stratigraphic information and to minimise redundant reimplementation.

<a id="modelling-system"></a>
### 3. Modelling System

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

#### The Supermodel, model

![](/images/supermodel/layers.svg){: width="40%"}

As with all things within this Supermodel's remit, the [Supermodel itself has a formal OWL model](https://linked.data.gov.au/def/supermodel). Its description says it is "...an enterprise data model that provides a structure for the creation of models for specialised datasets that allow for their uniqueness to be preserved but also provide for their deep integration."

The main elements of the Supermodel that matter in this case are the _Foreground_ and _Background_ models:

![](/images/supermodel/models-by-type.svg){: width="90%"}

#### Modelling Patterns

<p style="color:red; font-style: italic;">TODO</p>

#### Data Syntax

<p style="color:red; font-style: italic;">TODO</p>

#### Namespaces

<p style="color:red; font-style: italic;">TODO</p>

<a id="integrative-model"></a>
### 4. Integrative Model

![](/images/supermodel/integrative.svg){: width="75%"}

This Supermodel's integrative model is a skeleton model that joins the various foreground models together via relations 
between classes and them in other models.

Here the Stratigraphic Model is joined to the Geological Timescale model by means of instances of the former's 
`Stratigraphic Unit` class indicating related instances of the latter's `Geocronological Era` by the predicate `has age`.

This model is created entirely from elements within the Foreground and Background Models but is presented as a stand-alone
model also, to be used as a Supermodel high-level view.

<a id="foreground-models"></a>
### 5. Foreground Models

The Foreground Models in this Supermodel are the main, specialised, domain models developed specifically for this situation.

![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="gts-model"></a>
#### 5.1. Geologic Timescale (GTS) Model

<http://resource.geosciml.org/ontology/timescale/gts>

This model was originally developed in 2011 by Cox & Richards in 2012 [ref](#ref-gts) as a sophisticated _Time Ontology in OWL_ 
[ref](#ref-time)-based timescale dataset.

This model contains specialised forms of a `Geocronologic Era` class to represent the various Chronostratigraphic Chart 
time objects, such as `Period`, `Age`, `Super-Eon` and so on. It also has a specialised time instant class called 
`Geocrhonologic Boundary` used to contain the starting and finishing details of `Geocronologic Era` instances.

It also contains a `Stratigraphic Point` class which is used to associate `Geocrhonologic Boundary` objects with 
some GSSP information.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="thors-model"></a>
#### 5.2. Temporal Hierarchical Ordinal Reference System (THORS) Model

<http://resource.geosciml.org/ontology/timescale/thors>

This model, created in 2005 [ref](#ref-thors), provides a Semantic Web representation of the _Temporal Hierarchical Ordinal Reference Systems_
defined in GeoSciML [ref](#ref-gcml) using mostly _Time Ontology in OWL_ [ref](#ref-time) and [SKOS](#ref-skos) elements.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="strat-model"></a>
#### 5.3. Stratigraphy Model

<http://resource.geosciml.org/ontology/stratigraphy> -- _not working yet_

This model is developing alongside this Supermodel and will be published soon - mid-2026. 

It contains detailed stratigraphic domain information.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="ics-vis-model"></a>
#### 5.4. ICS Visual Chart Model

<http://resource.geosciml.org/ontology/isc-chart> -- _not working yet_

This is a [SKOS](#ref-skos) vocabulary representation of the instances of `Geocronologic Era` class instances - the 
Chronostratigraphic Chart's elements - with some time information taken from the _Geologic Timescale Model_ and additions
such as colours created to allow for the generation of the Chronostratigraphic Chart in traditional visual form from data,
as it is displayed at <https://stratigraphy.org/chart>.

When generated from parts, this model contains multilingual and alternate chronometric and stratigraphic labels as well.


![](/images/supermodel/model-icon.svg){: width="15%" style="float: right"}

<a id="gssp-model"></a>
#### 5.5. GSSP Model

<http://resource.geosciml.org/ontology/gssp> -- _not working yet_

This model is developing alongside this Supermodel and will be published soon - mid-2026. 

It contains a Semantic Web representation of the Global Boundary Stratotype Section and Points (GSSP) information
online at <https://stratigraphy.org/gssps> and will eventually be used to generate that web page, just as the Visual 
ICS Chart Model already generates the online Chart at <https://stratigraphy.org/chart>.

#### Other Foreground Models

<a id="background-models"></a>
### 6. Background Models

<p style="color:red; font-style: italic;">TODO</p>

<a id="example-data"></a>
### 7. Example Data

<p style="color:red; font-style: italic;">TODO</p>

<a id="references"></a>
### 8. References

1. <a id="ref-gts"></a> Cox, S.J.D., Richard, S.M. _A geologic timescale ontology and service_. Earth Sci Inform 8, 5–19 (2015). <https://doi.org/10.1007/s12145-014-0170-6>
2. <a id="ref-thors"></a> Cox, S.J.D.,Richard, S.M. _A formal model for the geologic time scale and global stratotype section and point, compatible with geospatial information transfer standards_. Geosphere, 1, 119-137 (2005) <https://doi.org/10.1130/GES00022.1>
3<a id="ref-time"></a> World Wide Web Consortium, _Time Ontology in OWL_. W3C recommendation. (2022). (https://www.w3.org/TR/owl-time/)  
4. <a id="ref-skos"></a> World Wide Web Consortium, _SKOS Simple Knowledge Organization System Reference_. W3C recommendation. (2009). (https://www.w3.org/TR/skos-reference/)
5. <a id="ref-gsml"></a> Open Geospatial Consortium, _OGC Geoscience Markup Language 4.1 (GeoSciML)_. OGC Implementation Standard. <http://www.opengis.net/doc/geosciml/4.1>
 