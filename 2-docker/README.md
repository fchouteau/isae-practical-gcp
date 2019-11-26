# Docker self-paced workshop

## 1. My first docker training using Play with Docker

- You need an account on docker hub to access play with docker: https://hub.docker.com/

OR

- You can do everything from google cloud shell (it has docker preinstalled)

- If you are not sure about images, containers etc, do this:
https://training.play-with-docker.com/ops-s1-hello/

- Then you can do this one:
https://training.play-with-docker.com/beginner-linux/

## 2. Hello World Dockerfile

You can use play with docker https://labs.play-with-docker.com or google cloud shell (both have file editors)

Source: https://github.com/docker-for-data-science/docker-for-data-science-tutorial/tree/master/exercises

Cloud Shell is easier to use and will be used later

This set of exercises will help you get familiar with Dockerfiles.

> A [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is a file that contains commands that are used to build a Docker image. We can write a `Dockerfile` to create custom images that contain only the things we want.

1. Create a directory on your local machine for this workflow.

```console
$ mkdir self-contained-container && cd self-contained-container
```

2. Create a python file that prints "Hello World" and save it as `hello_world.py`:

```python
# hello_world.py

print('Hello World!')
```

3. In the same folder, create a `Dockerfile` (filename `Dockerfile`) with the following contents:

```Dockerfile
# Dockerfile

# Use latest Python runtime as base image
FROM python:3.6.5-alpine3.7

# Set the working directory to /app and copy current dir
WORKDIR /app
COPY . /app

# Run hello_world.py when the container launches
CMD ["python", "hello_world.py"]
```

4. We can use `docker build -t hello-world .` to build an image from a `Dockerfile` located in the current directory with the tag, `hello-world`.

```console
$ docker build -t hello-world .
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM python:3.6.5-alpine3.7
 ---> 27e79c0fa4d2
Step 2/4 : WORKDIR /app
Removing intermediate container f9582523a722
 ---> 9045b5cfcbc1
Step 3/4 : COPY . /app
 ---> 5c1019a0993b
Step 4/4 : CMD ["python", "hello_world.py"]
 ---> Running in 6c013d2d0fe8
Removing intermediate container 6c013d2d0fe8
 ---> 0aabeeb989a8
Successfully built 0aabeeb989a8
Successfully tagged hello-world:latest
```

5. Use this image to create a new container using `docker run hello-world`. You should see a `Hello World` message printed to the console.

6. Take a look at all stopped containers using `docker ps -a`. Note the `container-name` or `container-id` of the image.

7. Restart the image using `docker start -ia [container-name OR container-id]`. You should see `Hello World` printed to the console once again.

***Tip:** `-i` attaches STDIN and `-a` attaches STDOUT/STDERR to terminal*

## 3.  Data Science Standardized Environment

- You can do this either from cloud shell 

OR
 
- play with docker https://labs.play-with-docker.com

I suggest to do it in Cloud Shell

NOTE: If you have a problem with your gcp project in cloud shell `gcloud config set projet`

### Intro

Those of us who work on a team know how hard it is to create a standardize development environment. Or if you have ever updated a dependency and had everything break, you understand the importance of keeping development environments isolated.

Using Docker, we can create a project / team image with our development environment and mount a volume with our notebooks and data.

The benefits of this workflow are that we can:
* Separate out projects
* Spin up a container to onboard new employees
* Build an automated testing pipeline to confirm upgrade dependencies do not break code

### Downloading Notebook and Data

1. Create a new folder for this project:

```console
mkdir self-contained-container && cd self-contained-container
```

2. Save a copy of the [notebook](https://github.com/docker-for-data-science/docker-for-data-science-tutorial/tree/docker-exercises/exercises) in the folder.

```console
wget https://github.com/alysivji/talks/raw/master/data-science-workflows-using-docker-containers/workflow1-self-contained/iris-analysis.ipynb
```

3. Create a subfolder called data and save a copy of [`iris.csv`](https://raw.githubusercontent.com/alysivji/talks/master/data-science-workflows-using-docker-containers/workflow1-self-contained/data/iris.csv) into this folder

```console
mkdir data && cd data
wget https://raw.githubusercontent.com/alysivji/talks/master/data-science-workflows-using-docker-containers/workflow1-self-contained/data/iris.csv
```

### Create Dockerfile

1. Create a new folder for this project:

```console
mkdir data-science-project && cd data-science-project
```

2. Create a `Dockerfile` in the `data-science-project` folder

3. We need to specify which image we are building off of. Although [Anaconda](https://hub.docker.com/r/continuumio/miniconda3/) is popular in the Data Science community, we will build off the Debian jessie slim image to not burden the conference wireless.

```dockerfile
FROM python:3.6.5-slim
```

4. Set the working directory:

```dockerfile
WORKDIR /app
```

5. `pip install` some required libraries, make sure to clean up the cache.

```dockerfile
RUN pip --no-cache-dir install pandas jupyter
```

6. In order to connect to the Jupyter instance that is running inside of the container, we will need to set up port forwarding.

```dockerfile
EXPOSE 8888
```

7. Create a mountpoint inside of our container:

```dockerfile
VOLUME /app
```

8. Start Jupyter when the container launches:

```Dockerfile
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

Complete `Dockerfile` should look as follows:

```Dockerfile
# data-science-project/Dockerfile

FROM python:3.6.5-slim

WORKDIR /app

RUN pip --no-cache-dir install pandas jupyter

EXPOSE 8888

VOLUME /app

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

9. Confirm directory structure looks as follows:

```console
.
└── Dockerfile
```

### Build Image

1. In the `data-science-project` folder, we can build an image as follows:

`docker build -t workflow2-data-science-project .`

2. Test image was built successfully by creating a container and mounting a directory. For this, you use the full path to a directory on your machine.

`docker run -p 8888:8888 -v /full/local/path:/app workflow2-data-science-project`

3. Confirm we can access the Jupyter process by going to the endpoint URL in the container output. You should see the files of the directory you mounted in the previous step in Jupyter.

- Note to do that from CLOUD SHELL you can use WEB PREVIEW to port 8888

5. `Ctrl+c` to stop the process

## 4. Using Google Cloud Tools for Docker

- Using cloud shell you should be able to do the Hello World Dockerfile exercise except that instead of using docker build you use GOogle Cloud Build

Tutorial: https://cloud.google.com/cloud-build/docs/quickstart-docker 
Example command :`gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/{image}:{tag} .`
Helping: to get your project id: `PROJECT_ID=$(gcloud config get-value project 2> /dev/null)`

## 5. Deploying models into production

[Go here](../3-deploy-model-into-production)

## 6. Optionnal - Docker Compose

https://hackernoon.com/practical-introduction-to-docker-compose-d34e79c4c2b6

https://github.com/dockersamples/example-voting-app

## Going further

https://container.training/
