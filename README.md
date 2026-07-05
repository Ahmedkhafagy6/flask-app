## Stage:Docker

**What was built:
Containerized the app with Docker

**How it works:

docker build -t flask-app:v1 .

docker run -d -p 5000:5000 --restart always flask-app:v1

**Problems I hit:
docker group permissions: added my user to the docker group
port conflict with systemd: stopped and disabled the old systemd service that was still holding port 5000

## Stage:CI

**What was built:
Added a CI pipeline with GitHub Actions

##how it works:
git add/commit/push
 
**Problems I hit:
YAML edits stayed in notes
