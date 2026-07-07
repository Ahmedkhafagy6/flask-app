## Stage:Docker

**What was built:**
Containerized the app with Docker

**How it works:**
docker build -t flask-app:v1 .
docker run -d -p 5000:5000 --restart always flask-app:v1

**Problems I hit:**
docker group permissions: added my user to the docker group
port conflict with systemd: stopped and disabled the old systemd service that was still holding port 5000

## Stage:CI

**What was built:**
Added a CI pipeline with GitHub Actions

**how it works:**
on push → GitHub builds the image → pushes to GHCR → self-hosted runner on my VM pulls and redeploys
deploy via kubectl set image with commit SHA tags → rolling update
 
**Problems I hit:**
YAML edits stayed in notes
runner dies with terminal: automate the runner service to run the script in background 

## Kubernetes

**What was built:** 
k3s cluster, Deployment with 2 replicas, NodePort Service

**How it works:**
the Deployment pulls the image from GHCR and keeps 2 replicas running; the NodePort Service load-balances traffic to them.
  
**Problems I hit:**
deleted a pod created with kubectl run — nothing brought it back. 
Deleted a pod managed by a Deployment — a replacement was created automatically within seconds. 
Learned the difference between imperative commands and declarative state.
latest tag never changes as text, so the cluster saw no difference and skipped the update — switched to unique commit SHA tags so every deploy is a real change
sudo: a terminal is required — the runner has no terminal for password prompts; copied the kubeconfig to my user and set KUBECONFIG via env in the workflow, since background processes don't read .bashrc 
