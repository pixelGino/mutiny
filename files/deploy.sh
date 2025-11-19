#!/bin/bash

# Mutiny Labs Website - Google Cloud Run Deployment Script
# Usage: ./deploy.sh [PROJECT_ID] [REGION]

set -e

# Configuration
PROJECT_ID="${1:-mutiny-labs}"
REGION="${2:-us-central1}"
SERVICE_NAME="mutiny-labs-website"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "========================================="
echo "Mutiny Labs Website Deployment"
echo "========================================="
echo "Project ID: $PROJECT_ID"
echo "Region: $REGION"
echo "Service: $SERVICE_NAME"
echo "========================================="
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Error: gcloud CLI is not installed"
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed"
    echo "Please install it from: https://docs.docker.com/get-docker/"
    exit 1
fi

# Set the project
echo "📋 Setting Google Cloud project..."
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "🔌 Enabling required Google Cloud APIs..."
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

# Build the Docker image
echo "🐳 Building Docker image..."
docker build -t $IMAGE_NAME .

# Push to Google Container Registry
echo "☁️  Pushing image to Google Container Registry..."
docker push $IMAGE_NAME

# Deploy to Cloud Run
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --port 8080 \
  --memory 256Mi \
  --cpu 1 \
  --max-instances 10 \
  --set-env-vars "NODE_ENV=production"

# Get the service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --format 'value(status.url)')

echo ""
echo "========================================="
echo "✅ Deployment successful!"
echo "========================================="
echo "Service URL: $SERVICE_URL"
echo ""
echo "To map a custom domain, run:"
echo "gcloud run domain-mappings create --service $SERVICE_NAME --domain YOUR_DOMAIN --region $REGION"
echo ""
echo "To view logs, run:"
echo "gcloud run logs read --service $SERVICE_NAME --region $REGION"
echo "========================================="
