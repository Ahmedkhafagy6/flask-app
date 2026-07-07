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
