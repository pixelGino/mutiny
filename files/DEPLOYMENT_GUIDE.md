# Mutiny Labs Website - Deployment Guide

## Google Cloud Container Deployment

### Prerequisites
- Google Cloud Platform account with billing enabled
- Google Cloud SDK installed (`gcloud` command)
- Docker installed locally

### Current Stack
- **Technology:** HTML5, Tailwind CSS (CDN), Vanilla JavaScript
- **Type:** Single-page static website
- **Assets:** 1 HTML file, 1 logo PNG file

---

## Option 1: Google Cloud Storage (Simplest for Static Sites)

### Step 1: Create Storage Bucket
```bash
# Set project
gcloud config set project YOUR_PROJECT_ID

# Create bucket
gsutil mb -c STANDARD -l us-central1 gs://mutiny-labs-website

# Make bucket public
gsutil iam ch allUsers:objectViewer gs://mutiny-labs-website
```

### Step 2: Configure for Website Hosting
```bash
gsutil web set -m mutiny-labs-website.html -e mutiny-labs-website.html gs://mutiny-labs-website
```

### Step 3: Upload Files
```bash
gsutil cp mutiny-labs-website.html gs://mutiny-labs-website/
gsutil cp mutiny_logo.png gs://mutiny-labs-website/

# Set cache control
gsutil setmeta -h "Cache-Control:public, max-age=3600" gs://mutiny-labs-website/*
```

### Step 4: Access Website
Your website will be available at:
`https://storage.googleapis.com/mutiny-labs-website/mutiny-labs-website.html`

---

## Option 2: Google Cloud Run (Containerized Deployment)

### Step 1: Create Dockerfile
```dockerfile
FROM nginx:alpine

# Copy website files
COPY mutiny-labs-website.html /usr/share/nginx/html/index.html
COPY mutiny_logo.png /usr/share/nginx/html/

# Configure nginx
RUN echo 'server { \
    listen 8080; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files $uri $uri/ /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 8080
```

### Step 2: Build and Push Container
```bash
# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

# Build container
docker build -t gcr.io/YOUR_PROJECT_ID/mutiny-labs-website .

# Push to Google Container Registry
docker push gcr.io/YOUR_PROJECT_ID/mutiny-labs-website
```

### Step 3: Deploy to Cloud Run
```bash
gcloud run deploy mutiny-labs-website \
  --image gcr.io/YOUR_PROJECT_ID/mutiny-labs-website \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```

### Step 4: Custom Domain (Optional)
```bash
# Map custom domain
gcloud run domain-mappings create \
  --service mutiny-labs-website \
  --domain www.mutiny-labs.com \
  --region us-central1
```

---

## Option 3: Google Kubernetes Engine (Enterprise Scale)

### Step 1: Create GKE Cluster
```bash
gcloud container clusters create mutiny-labs-cluster \
  --num-nodes=2 \
  --machine-type=e2-micro \
  --region=us-central1
```

### Step 2: Deploy with Kubernetes
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mutiny-labs-website
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mutiny-labs
  template:
    metadata:
      labels:
        app: mutiny-labs
    spec:
      containers:
      - name: website
        image: gcr.io/YOUR_PROJECT_ID/mutiny-labs-website
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: mutiny-labs-service
spec:
  type: LoadBalancer
  selector:
    app: mutiny-labs
  ports:
  - port: 80
    targetPort: 8080
```

Apply configuration:
```bash
kubectl apply -f deployment.yaml
kubectl get service mutiny-labs-service
```

---

## Recommended Approach

**For Current Needs:** Option 1 (Cloud Storage) or Option 2 (Cloud Run)
- **Cloud Storage:** Simplest, most cost-effective for static sites (~$0.01/month)
- **Cloud Run:** Better for future dynamic features, automatic scaling (~$0-5/month)

**For Future Growth:** Option 3 (GKE)
- Enterprise-scale
- More complex, higher cost
- Recommended only when scaling to multiple services

---

## CI/CD Setup (GitHub Actions Example)

```yaml
# .github/workflows/deploy.yml
name: Deploy to Google Cloud

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v0
      with:
        project_id: ${{ secrets.GCP_PROJECT_ID }}
        service_account_key: ${{ secrets.GCP_SA_KEY }}
    
    - name: Upload to Cloud Storage
      run: |
        gsutil cp mutiny-labs-website.html gs://mutiny-labs-website/
        gsutil cp mutiny_logo.png gs://mutiny-labs-website/
```

---

## Performance Optimization

### Enable Cloud CDN
```bash
# For Cloud Storage
gcloud compute backend-buckets create mutiny-labs-backend \
  --gcs-bucket-name=mutiny-labs-website \
  --enable-cdn

# Create URL map
gcloud compute url-maps create mutiny-labs-url-map \
  --default-backend-bucket=mutiny-labs-backend
```

### Add Cloud Armor (DDoS Protection)
```bash
gcloud compute security-policies create mutiny-labs-security \
  --description "Security policy for Mutiny Labs website"
```

---

## Monitoring Setup

### Enable Cloud Monitoring
```bash
# Create uptime check
gcloud monitoring uptime-check-configs create \
  --display-name="Mutiny Labs Website" \
  --http-check \
  --resource-type=uptime-url \
  --host=YOUR_DOMAIN
```

### Set Up Alerts
- Page load time > 3 seconds
- Downtime detection
- SSL certificate expiration

---

## Cost Estimates

### Cloud Storage + CDN
- Storage: ~$0.02/GB/month
- Network: ~$0.12/GB egress
- **Estimated:** $0.50-2/month

### Cloud Run
- vCPU: $0.00002400/vCPU-second
- Memory: $0.00000250/GB-second
- Requests: $0.40/million
- **Estimated:** $0-5/month (with generous free tier)

### GKE
- e2-micro nodes: ~$13/node/month
- Load balancer: ~$18/month
- **Estimated:** $45-75/month

---

## Domain Setup

### Configure DNS
```
A Record:    @ → Cloud Run/GKE IP
CNAME:       www → Cloud Run URL
```

### SSL Certificate
Cloud Run and GKE automatically provision SSL certificates for custom domains.

---

## Files Required for Deployment

1. `mutiny-labs-website.html` - Main website file
2. `mutiny_logo.png` - Logo asset
3. `Dockerfile` - For containerized deployment (Option 2 & 3)
4. `deployment.yaml` - For Kubernetes deployment (Option 3)

All files are available in `/mnt/user-data/outputs/`

---

## Next Steps

1. Choose deployment option based on needs
2. Set up Google Cloud project
3. Configure domain (optional)
4. Deploy website
5. Set up monitoring and alerts
6. Configure CDN for performance

## Support

For questions or issues, contact:
- **Mutiny Labs:** info@mutiny-labs.com
- **Phone:** 1-888-449-4466
