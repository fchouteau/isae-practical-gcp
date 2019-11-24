---
title: GCP 4 Data Science
theme: solarized
highlightTheme: solarized-light
separator: <!--s-->
verticalSeparator: <!--v-->
revealOptions:
    transition: 'fade'
    transitionSpeed: 'default'
    controls: false
---

# (3/3) Google Cloud Platform for Data Scientists
### Intro to useful managed services

**ISAE-SUPAERO, SDD, 27th November 2019**

Florient CHOUTEAU, Dennis WILSON

<!--v-->

### Objectives of this class

...

<!--v-->

### Outline

**Presentation ( < 1h)**

- How we use GCP at work (quick demo)
- Overview of useful GCP services 
- Intro to Jupyter AI Notebook
- Jupyter Notebook remote execution
- Intro to Google Colaboratory

**Quizz**

<!--v-->

### Outline

**TP (remaining time)**

Essentials...

- My first production model in cloud run ! (continued.)
- Starting a Jupyter AI Notebook and connecting to it (w/o ssh)

Bonus... 

- Scheduling a notebook on a Deep Learning VM (intro to scheduled computing)
- Using Colaboratory

<!--s-->

## Google Cloud Platform 4 Data Science

<!--v-->

Day to day usage

- Data Stored in GCS
- Remote development on a GCE
- Distributed Training / HP Tuning using clusters
- Infrastructure as Code to instantiate clusters
- Deployment using docker containers

<!--s-->

## Jupyter AI Notebook

<!--v-->

Intro

<!--s-->

## Google Collaboratory
https://colab.research.google.com

<img src="static/colab.png" alt="" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

<img src="static/open_in_colab.png" alt="" style="background:none; border:none; box-shadow:none;"/>

### WTF is... Google Colab ?

- Jupyter Notebook + Google Drive

- Full python data science environment

- 12h max session lifetime

<!--v-->

### Is it for YOU ? 

**Yes !**

Reproducible jupyter <!-- .element: class="fragment" data-fragment-index="1" -->

Shareable jupyters that runs <!-- .element: class="fragment" data-fragment-index="2" -->

<!--v-->

### Nice features

- You just need a google account

- Can use your data: gdrive, gsheet, local filesystem

- Jupyter-based: All the power of interactive & visualisations

- You can `apt-get` and `pip install` what you need

<!--v-->

### Nicer features

- GPU (P100 !) ! (Nvidia Tesla T4, 16 GB GPU RAM = 3000$)

- Collaboration ! (share and co-edit notebooks)

- Open notebook from github to colab ! 

<!--v-->

Demo !

<!--v-->

### Limitations

- Long calculations w/ guarantees (you can checkpoint your models on colab though)

- Code syncing / huge codebase & huge datasets

- Full control over installation and data

<!--s-->

## Quizz

<!--v-->

https://kahoot.it/

GAME PIN: 

<!--v-->

![](https://media.giphy.com/media/FqfZhLdbTtGThAymdh/giphy.gif)

<!--v-->

### Workshop ! 

[Go Here](4-gcp-for-data-science/README.md)