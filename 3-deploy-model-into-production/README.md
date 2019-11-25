# Deploying a ML model into "production"

It is **highly** suggested to open Google Cloud Shell

https://ssh.cloud.google.com/cloudshell/

## 0 - Introduction to REST APIs and Services

Read this:

Intro to web app: http://www.beginwithjava.com/servlet-jsp/web-application-overview/web-application.html

Rest api: https://en.wikipedia.org/wiki/Representational_state_transfer

Source of this tp: https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

## 1 - Exploring the docker and building it locally

1. What does this application seem to be doing ?

2. Build the docker image locally

```bash
docker build -t imagenet-predictor:1.0 -f Dockerfile .
```

3. Run a container while forwarding port

```bash
docker run --rm -p 8080:8080 imagenet-predictor:1.0
```

4. Check health 
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

1. Follow the documentation to deploy your container image to Google Cloud Run

https://cloud.google.com/run/docs/deploying

Parameters:
- Select fully managed
- Select zone = europe-west1
- RAM = 512 Gb
- Allow Unauthenticated requests

2. Where was the service deployed to ? 

3. Query the /api/v1/health endpoint of your service

4. Send a request to your service

5. Send several requests to your service to check if it autoscales
