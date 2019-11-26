# Deploying a ML model into "production"

It is **highly** suggested to open Google Cloud Shell https://ssh.cloud.google.com/cloudshell/

## 0 - Introduction to REST APIs and Services

We are going to build a "webservice" containing a deep learning model that can classify images from up to 1000 different classes

This is the easiest/standard way of packaging ML models.

For an introduction to RESTs APIS etc, I suggest that you read this:

- Introduction to Web App http://www.beginwithjava.com/servlet-jsp/web-application-overview/web-application.html
- RESTful API: https://en.wikipedia.org/wiki/Representational_state_transfer

- This TP is adapted from: https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

## 1 - Exploring the docker and building it locally

0. first step, in cloud shell, clone the repo

`git clone https://github.com/fchouteau/isae-practical-gcp`

Then

`cd 3-deploy-model-into-production`

1. Look at `app.py` and the `Dockerfile` What does this application seem to be doing ?

2. Build the docker image locally

```bash
docker build -t imagenet-predictor:1.0 -f Dockerfile .
```

3. Run a container while forwarding port. Use `-d` option if you want to do it on background

```bash
docker run --rm -p 8080:8080 imagenet-predictor:1.0
```

4. Check health 

`curl` is the tool we use to send http requests

```bash
# Check health
curl -X GET http://localhost:8080/api/v1/health
# Get description of service
curl -X GET http://localhost:8080/api/v1/describe
```
5. Launch prediction

```bash
curl -X POST -F "file=@cat.jpg" http://localhost:8080/api/v1/predict
```

If you want you can try to download another image from the web (`wget url` and send it as well)

## 2 - Building the image and pushing into Cloud Registry

We will be using cloud build to build our images

1. Build the image using gcloud build
```
PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/imagenet-predictor:1.0 .
```

2. Pull the image and verify it works (see above)

```bash
gcloud docker -- pull eu.gcr.io/$PROJECT_ID/imagenet-predictor:1.0 .
```

## 3 - Deployment using Google cloud Run

This is an intro to "Kubernetes" from  a user point of view
We are going to use a managed service called "Google cloud run"

https://cloud.google.com/run/

1. Follow the documentation to deploy your container image to Google Cloud Run

https://cloud.google.com/run/docs/deploying

Parameters:
- Select fully managed
- Select zone = europe-west1
- RAM = 512 Gb
- Allow Unauthenticated requests

2. Where was the service deployed to ? Can you get the URL ?

3. Query the /api/v1/health endpoint of your service (you can do it via your browser)

4. Send a request to your service (via curl)

5. You can ask everybody to send multiple images to see if the process scales...
