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

# Part 3: Google Cloud Platform for Data Scientists
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

### Day to day usage

- Data Stored in GCS
- Remote development on a GCE
- Distributed Training / HP Tuning using clusters
- Infrastructure as Code to instantiate clusters
- Deployment using docker containers

<!--v-->

### Going further (a bit too far ?)

![](https://miro.medium.com/max/1920/1*WOEEJizYnO8ibtU2l9jWbA.jpeg)
[source](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233)

<!--v-->

### Most useful products

- [Cloud Storage](https://cloud.google.com/storage/docs/): Object storage and serving
- Compute Engine
- Container Registry
- Kubernetes Engine

<!--v-->

### Some Managed Products

- All the storage / databases solutions + [BigQuery](https://cloud.google.com/bigquery/docs/)
- [Datalab](https://cloud.google.com/datalab/docs/): Managed Jupyter notebook
- [Dataproc](https://cloud.google.com/dataproc/docs/): Managed Spark Cluster 

(...and so many more)

<!--v-->

### AI (Deep Learning) Hub Products

https://aihub.cloud.google.com/

- [Deep Learning VM](https://cloud.google.com/deep-learning-vm/docs/)**: Preconfigured Compute Engine for Deep Learning
- [AI Platform Notebook](https://cloud.google.com/ml-engine/docs/notebooks/): Managed JupyterLab notebook instances

(...and so many more)

<!--v-->

Let's talk about one or two...

<!--s-->

## AI Platform Notebooks

![](https://kstatic.googleusercontent.com/files/1a04559c0bf2b9c2a1dbc31d0e908c7387d610ce617731ac220c0176b735ad96589c9ce88039efdbcfa11a094ae869cd8ad22ef5a4ae2d34c13e009e82594b8a)

<!--v-->

- Google Compute Engine
- Preconfigured for ML / DL
- With Jupyterlab pre-launched

<!--v-->

### Main Feature

- Preconfigured, Preinstalled data science instances
- GPU Option
- **Jupyterlab accessible without ssh !** 

... We will use them extensively later ;) <!-- .element: class="fragment" data-fragment-index="2" -->


<!--s-->

## Deep Learning VM & Notebook scheduling

![](https://kstatic.googleusercontent.com/files/54d34d2113f78c8ce1cabdec5ca5060e5d38a5ea68d1e47cb66aeb48c3b1b8efd3a9a91dd5bfdc4aca4d372dd9d94718e209adce9147981799275d38b669e37b)

<!--v-->

Intro

<!--s-->

## Google Colaboratory

https://colab.research.google.com

<img src="https://miro.medium.com/max/776/1*Eb4YFMdn8LJhxjJCuykiLg.png" alt="" style="width: 50%; height: 50%; background:none; border:none; box-shadow:none;"/>

<!--v-->

<img src="static/img/open_in_colab.png" alt="" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

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

### Limitations

- Long calculations w/ guarantees (you can checkpoint your models on colab though)

- Code syncing / huge codebase & huge datasets

- Full control over installation and data

<!--v-->

Demo !

<!--s-->

## QCM & Workshop

<!--v-->

https://kahoot.it/

GAME PIN: 

<!--v-->

![](https://media.giphy.com/media/FqfZhLdbTtGThAymdh/giphy.gif)

<!--v-->

### Workshop time

[Instructions](https://github.com/fchouteau/isae-practical-gcp/tree/master/4-gcp-for-data-science)
