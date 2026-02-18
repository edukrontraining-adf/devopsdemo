# GenAI Application

A simple, production-ready Flask-based OpenSource GenAI application.

## 📦 Features

- Containerized Python Flask application
- OpenAI API integration
- Health check endpoints
- Kubernetes-ready deployment
- Multi-stage Docker build
- Non-root user security

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=development
export OPENAI_API_KEY=your_key_here

# Run application
python app.py
```

Access at: http://localhost:5000

### Docker Build & Run

```bash
# Build image
docker build -t genai-app:latest -f Dockerfile .

# Run container
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=your_key \
  genai-app:latest
```

## 📡 API Endpoints

### GET /
Home endpoint
```bash
curl http://localhost:5000/
```

### GET /health
Health check (Kubernetes probes)
```bash
curl http://localhost:5000/health
```

### GET /about
Application information
```bash
curl http://localhost:5000/about
```

### POST /api/generate
Generate AI response
```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is DevOps?"}'
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

## 🐳 Docker Image

Pre-built image available at:
```
acrdevopsdemo.azurecr.io/genai-app:latest
```

## 📋 Requirements

See `requirements.txt` for dependencies:
- Flask 2.3+
- Python 3.11+
- Gunicorn for production
- OpenAI Python SDK

## 🔒 Security

- Runs as non-root user (UID 1000)
- Read-only root filesystem support
- No privileged capabilities
- Minimal base image (python:3.11-slim)
- Health checks configured

## 📊 Performance

- CPU: 100m request, 500m limit
- Memory: 128Mi request, 512Mi limit
- Auto-scaling: 2-10 replicas

## 📚 Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Kubernetes Deployment Guide](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
