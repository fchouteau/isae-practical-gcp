# Google Cloud Platform for Data Science Workshop

Do as much as you can :) You can do that as home as well

It is necessary to have done 1. and 2. before leaving !

## 1. Deploying a model in a scalable fashion using cloud run

[Finish Last Part](../3-deploy-model-into-production)

## 2. Creating a Jupyter AI Notebook Instance from the GUI

**Configuration**

Documentation: https://cloud.google.com/ai-platform/notebooks/docs/

- Go to the Jupyter AI Notebook Page
- Star a Custom instance with the following parameters
    - pytorch 1.2 base image
    - zone europe-west1-b
- Wait for creation (if you have a GPU issue you can ask for GPU, see troubleshooting below, then run CPU instances for now)
- Click on "Open in JupyterLab"
- You should be in a jupyterlab environment inside your machine !

What is JupyterLab ? https://jupyterlab.readthedocs.io/en/stable/

Basically a more advanced version of Jupyter that includes some IDE functionalities like code editing outside of jupyters

**What to do next ?**

- Familiarize yourself with Jupyterlab. You can use it as well (`pip install jupyterlab`) on your machine !

- You can open and run one of the many tutorials in /tutorial/ section

- Using the terminal available in jupyter lab you can download a notebook (wget) from the cloud
  

For example you can upload the notebook called `ai-notebook-demo-pytorch.ipynb` to your instance (use `wget URL-OF-THE-NOTEBOOK` from the terminal)

- You can also upload one of your own notebook + data using google cloud storage then downloading it (`gsutil cp {storage} {local}`)

**Warning: Don't use the colab notebook outside of collab it's not going to work !**

## 3. Discover Google Colaboratory

- Go to https://colab.research.google.com while logged in on a google account

- Load any notebook you have locally, or on github or on MLClass
    - For example the "Time Series Forecasting BE" you are working on
    - Or the `google-colab-demo-pytorch.ipynb` of this repository
    - Use the "load from github" if necessary

- If you have local data, upload it on google drive and learn how to connect google drive to google colab (see documentation)

- Make run work end-to-end without errors
    - Select the proper runtime and python version
    - You may need to install things from jupyter`!pip install {my-package}`
    - Refer to the built-in docs for more information

- Share it using a public link...

- ... And open it from a private browser tab ! (or give the link to your friend !)

- What are the differences between this and the AI Notebook ?

You're done !

## 4. Preparation for the Deep Learning Class this afternoon

- Using either colaboratory or jupyter ai notebook

- Upload to the machine or open in collaboratory the notebook located here:

https://github.com/erachelson/MLclass/tree/master/7%20-%20Deep%20Learning

Don't run it just yet ;) wait for this afternoon !

## 5. Schedule the execution of a local notebook remotely and retrieve a notebook

Clone this repo again ;) https://github.com/fchouteau/isae-practical-gcp

You should use cloud shell or your local terminal if you have gcloud installed

Documentation: https://blog.kovalevskyi.com/gcp-notebook-executor-v0-1-2-8e37abd6fae1

Underlying technology to schedule notebooks: https://github.com/nteract/papermill

Underlying VMs: https://cloud.google.com/ai-platform/deep-learning-vm/docs/

Do you ever wanted to submit a notebook for 2-day training and forget about it till after it has been finished? This is possible with GCP and even better you will specify exactly how much resources notebook requires and you will pay only for the resources that were used for training.

Just to clarify:

    you will not need to convert your notebook to python code (you can submit it as is)
    you will not have to monitor execution to make sure you deallocating resources immediately after execution is done, this is taken care for you
    you can precycle specify how much resources you need

 
- Create a bucket and remember its name
- Edit the following instructions to match with something you want to execute
- You can link to another one of your (local) jupyter notebook if you want

```bash
source utils.sh

INPUT_NOTEBOOK="/home/fchouteau/classes/isae-practical-gcp/4-gcp-for-data-science/scheduling-notebook.ipynb"
# Should be existing bucket
GCP_BUCKET="gs://fchouteau-storage/test-execution"
IMAGE_FAMILY_NAME="pytorch-latest-cpu"
INSTANCE_TYPE="n1-standard-4"
GPU_TYPE="p100"
GPU_COUNT=1
ZONE="europe-west1-b"

execute_notebook -i "${INPUT_NOTEBOOK}" \
                 -o "${GCP_BUCKET}" \
                 -f "${IMAGE_FAMILY_NAME}" \
                 -t "${INSTANCE_TYPE}" \
                 -z "${ZONE}"
```

- Check the Google Compute Engine UI to see what is happening

- Check that this happens

        notebook get’s uploaded to the Google Cloud Storage
        new Deep Learning VM created with the special argument that pointing to the notebook on Google Cloud Storage
        background Deep Learning VM executes the notebook
        background Deep Learning VM uploads resulted Notebook to the GCS
        background Deep Learning VM self terminate

- Check google cloud storage to see if execution was correctly handled

## Troubleshooting

**No GPU ?**

You have limited quota, which restricts you from using certain resources. You should ask for more GPU

https://stackoverflow.com/questions/45227064/how-to-request-gpu-quota-increase-in-google-cloud


