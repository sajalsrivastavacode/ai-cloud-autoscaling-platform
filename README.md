## Architecture

Client → FastAPI API → Docker Container → Kubernetes Auto Scaling

# AI Cloud Auto-Scaling Platform

A cloud-native microservice that simulates CPU load and demonstrates containerized deployment using Docker with future Kubernetes auto-scaling.

## Features

- FastAPI microservice
- Docker containerization
- CPU load simulation
- Health check endpoint
- Cloud-ready architecture

---

## API Running

![API Home](screenshots/api-home.png)

---

## CPU Load Endpoint

![Load Endpoint](screenshots/load-endpoint.png)

---

## Health Endpoint

![Health Endpoint](screenshots/health-endpoint.png)

---

## Docker Container Running

![Docker Running](screenshots/docker-running.png)
# AI Cloud Autoscaling Platform

A cloud-native AI API deployed using Docker and Kubernetes with Horizontal Pod Autoscaling.

## Tech Stack
- Python
- FastAPI
- Docker
- Kubernetes
- Horizontal Pod Autoscaler

## Architecture

FastAPI API
      ↓
Docker Container
      ↓
Kubernetes Deployment
      ↓
NodePort Service
      ↓
Horizontal Pod Autoscaler

## Run Locally

Build Docker image:

docker build -t ai-autoscaler .

Run container:

docker run -p 8000:80 ai-autoscaler

## Kubernetes Deployment

kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/autoscaler.yaml

## Screenshots

### API Running
![API](screenshots/api-home.png)

### Kubernetes Pods
![Pods](screenshots/pods-running.png)

### Horizontal Pod Autoscaler
![Autoscaler](screenshots/autoscaler.png)

### Service NodePort
![Service](screenshots/service-running.png)

