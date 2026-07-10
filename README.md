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

## Stage:Terraform (IaC)
**What was built:**
Azure infra from code: VNet, subnet, public IP, NIC, NSG with SSH rule, Linux VM

**How it works:**
terraform plan compares the file with reality, apply builds the difference

**Problems I hit:**
the lab account had limited permissions (no subscription-level access) — got 403 on provider registration, fixed with resource_provider_registrations = "none" and worked inside the existing RG with a data block
SSH to the new VM hung — Azure blocks all inbound by default and no NSG existed → added NSG with port 22 rule + subnet association
wrote source_port = 22 instead of destination_port — the rule would pass silently but block me, because clients connect FROM random ports
drift test (Docker provider): deleted the container by hand → terraform plan detected it and offered to recreate it
the playground RG isn't mine → read it with a data block instead of resource — resource = I own it, data = I only read it

## Stage: Ansible
**What was built:**
playbook to prepare the servers: Docker + k3s + GitHub runner

**How it works:**
describes the desired state, not commands — safe to re-run any time (idempotent via creates)

**Problems I hit:**
sudo asked for a password and automation has no terminal to type it — set passwordless sudo for the lab user
pasted the full curl command into src — the unarchive module downloads by itself, src takes only the URL
learned the difference between ok / changed / skipping in the play recap

## Stage: Monitoring
**What was built:**
kube-prometheus-stack through Helm (Prometheus + Grafana + Alertmanager) inside the cluster

**How it works:**
exporters collect the metrics from the servers and pods → Prometheus stores them → Grafana draws them live

**Problems I hit / learned:**
Grafana was ClusterIP (reachable only inside the cluster) → patched it to NodePort for permanent browser access
killed a pod and watched the graph document it — one line stopped, a new line with a new name started from zero
first time using Helm — the apt of Kubernetes: one chart installed 6 connected pods
