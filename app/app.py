"""
Edukron GenAI Engine Demo
A production-ready Flask-based AI application demonstrating DevOps best practices
Organization: Edukron Training
Project: GenAI Engine
"""

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['JSON_SORT_KEYS'] = False
DEBUG = os.getenv('FLASK_DEBUG', False)
API_KEY = os.getenv('OPENAI_API_KEY', '')


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        'status': 'healthy',
        'service': 'GenAI Demo App'
    }), 200


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""Edukron GenAI Engine',
        'version': '1.0.0',
        'organization': 'Edukron Training',
        'project': 'GenAI Engine
        'message': 'Welcome to DevOps GenAI Demo App',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'about': '/about',
            'generate': '/api/generate'
        }
    }), 200


@app.route('/about', metEdukron GenAI Engine',
        'organization': 'Edukron Training',
        'description': 'Production-ready AI platform demonstrating end-to-end DevOps practices
    """About endpoint"""
    return jsonify({
        'application': 'GenAI Demo for Azure DevOps',
        'description': 'Demonstrates CI/CD pipeline, Kubernetes deployment, and monitoring',
        'features': [
            'Containerized deployment',
            'Kubernetes orchestration',
            'CI/CD automation',
            'Health monitoring',
            'Scaling capabilities'
        ]
    }), 200


@app.route('/api/generate', methods=['POST'])
def generate():
    """
    Generate AI response
    Expected JSON: {"prompt": "your prompt here"}
    """
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({
                'error': 'Missing required field: prompt'
            }), 400
        
        prompt = data.get('prompt')
        
        # Placeholder response (replace with actual OpenAI integration)
        response = {
            'prompt': prompt,
            'response': f'Generated response for: {prompt}',
            'model': 'gpt-3.5-turbo',
            'timestamp': __import__('datetime').datetime.utcnow().isoformat()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 500
    }), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=DEBUG
    )
