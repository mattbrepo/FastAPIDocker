# FastAPIDocker
A project to test [FastAPI](https://fastapi.tiangolo.com/) and [Docker](https://www.docker.com/).

**Language: Python**

**Start: 2023**

## Why
I wanted to test [FastAPI](https://fastapi.tiangolo.com/) to create a simple API server. I took this opportunity also to try [Docker](https://www.docker.com/). Therefore, I packaged the Python project in a Docker container and moved it to a Google Cloud machine. 

Example of output of one of the get command:

![output](/images/output.jpg)

## Steps

### Create the environment
- python3 -m venv venv
- . venv/bin/activate
- pip install (all necessary packages including -of course- FastAPI)
- pip freeze > requirements.txt

### Build the container image
- docker build -t python-fastapi .

### Start the container
- docker run -p 8000:8000 python-fastapi
- docker run -p 8000:8000 --detach python-fastapi
- docker run -p 8000:8000 --mount type=bind,source="$(pwd)"/../external.txt,target=/mypath/external.txt,readonly python-fastapi

### Move the container to a differnent computer
- docker save -o <path of tar file> <image name>
- docker load -i <path of tar file>

### Move the image to Goolge Container Registry
- read the project ID on Google (e.g., google-id)
- gcloud auth configure-docker
- docker tag python-fastapi eu.gcr.io/google-id/python-fastapi
- docker push eu.gcr.io/google-id/python-fastapi
- created an ad hoc VM mounting the docker image present in the Container Registry

## Resources
- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Video docker tutorial for python](https://www.youtube.com/watch?v=bi0cKgmRuiA)
- [Docker vs Podmad](https://www.youtube.com/watch?v=jzd0YoqBJjc)
- [Docker vs Podman (2)](https://www.youtube.com/watch?v=NqxWiwjYlBs)
