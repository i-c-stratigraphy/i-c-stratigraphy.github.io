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


### Abstract

The ICS Stratigraphy 'Supermodel' an overarching, enterprise and integrative, formal information model covering aspects of
the stratigraphy domain as characterised by the [International Commission on Stratigraphy (ICS)](https://stratigraphy.org). 
It includes several specialised 'component models' that can be used individually or together.

The Supermodel and the component models are implemented using Semantic Web 
techniques which includes reusing general-purpose data modelling patterns. This allows these models can be integrated 
with more general geology models and even more general resources sector, environmental, scientific and economic models.

### Motivation

Geology and resource sector science and engineering have long used large volumes of and sophisticated data however many 
projects have to re-implement data associations related to stratigraphy due to a lack of standardised models and datasets
in the domain.

The ICS, as the international authority responsible for establishing the fundamental scale used to represent the history 
of the Earth, has long published the [Chronostratigraphic Chart](https://stratigraphy.org/chart) as the principal reference 
resource within the field. Since 2025, this Chart has been made available as data, rather than solely as a document. 
The ICS is now undertaking efforts to define additional stratigraphic elements through the suite of standardised resources 
encompassed by this Supermodel, to enable projects to maximise reuse and minimise redundant reimplementation.

### Modelling System

The [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web) as a system and specific set of data models is used for 
this Supermodel and the component and background models. It is chosen for three main reasons:

1. Semantic Web models can reuse other model's elements to a degree other modelling systems can't
   * this allows for maximal interoperability through shared model elements and modelling patterns
2. A large body of Semantic Web models in relevant domains already exist that can be reused
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

#### Modelling Patterns

#### Data Syntax

#### Namespaces

### Integrative Model

![](/images/ics-supermodel-overview.svg){: width="90%"}

### Component Models

#### Geologic Timescale Model

#### Stratigraphy Model

#### Visual ICS Chart Model 

#### GSSP Model

#### Other Component Models

### Background Models

### Example Data