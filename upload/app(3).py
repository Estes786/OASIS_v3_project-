
from flask import Flask, jsonify, render_template_string
import os
import json
from datetime import datetime

app = Flask(__name__)

# Simplified dashboard template
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FMAA BDI Agent Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body class="bg-gray-100 text-gray-900 p-6">
    <div class="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-md">
        <h1 class="text-3xl font-bold mb-6 text-center">🤖 FMAA BDI Agent Dashboard</h1>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="bg-blue-100 p-4 rounded-lg shadow-sm">
                <h2 class="text-xl font-semibold text-blue-800">System Status</h2>
                <p><strong>Running:</strong> {{ running }}</p>
                <p><strong>Last Updated:</strong> {{ last_updated }}</p>
                <p><strong>Environment:</strong> {{ environment }}</p>
            </div>
            <div class="bg-green-100 p-4 rounded-lg shadow-sm">
                <h2 class="text-xl font-semibold text-green-800">Key Metrics</h2>
                <p><strong>Beliefs Count:</strong> {{ beliefs_count }}</p>
                <p><strong>Desires Count:</strong> {{ desires_count }}</p>
                <p><strong>Intentions Count:</strong> {{ intentions_count }}</p>
            </div>
            <div class="bg-purple-100 p-4 rounded-lg shadow-sm">
                <h2 class="text-xl font-semibold text-purple-800">Quantum Status</h2>
                <p><strong>Quantum Available:</strong> {{ quantum_available }}</p>
            </div>
        </div>

        <div class="mb-8">
            <h2 class="text-2xl font-semibold mb-4">🧠 Beliefs (Current System State)</h2>
            <pre>{{ beliefs | tojson(indent=2) }}</pre>
        </div>

        <div class="mb-8">
            <h2 class="text-2xl font-semibold mb-4">🎯 Desires (Goals)</h2>
            <pre>{{ desires | tojson(indent=2) }}</pre>
        </div>

        <div class="mb-8">
            <h2 class="text-2xl font-semibold mb-4">⚡ Intentions (Actions)</h2>
            <pre>{{ intentions | tojson(indent=2) }}</pre>
        </div>

        <div class="text-center mt-8">
            <button onclick="location.reload()" class="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg shadow-md transition duration-300">
                🔄 Refresh Dashboard
            </button>
            <a href="/api/status" class="ml-4 bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg shadow-md transition duration-300">
                📊 API Status
            </a>
        </div>
    </div>
</body>
</html>
"""

# Sample data generator for demo
def generate_sample_data():
    return {
        'beliefs': {
            'system_health': 95,
            'resource_usage': 23.5,
            'active_agents': ['agent_1', 'agent_2', 'agent_3'],
            'revenue_metrics': {
                'current_month': 32500,
                'target': 50000,
                'growth_rate': 15.2
            },
            'cloud_status': {
                'vercel': True,
                'supabase': True,
                'github': True
            },
            'last_updated': datetime.now().isoformat()
        },
        'desires': [
            {'type': 'revenue_optimization', 'priority': 10, 'target_increase': 17500, 'strategy': 'aggressive_scaling'},
            {'type': 'agent_scaling', 'priority': 8, 'target_agents': 10}
        ],
        'intentions': [
            {'action': 'trigger_github_workflow', 'workflow': 'bdi-action.yml', 'priority': 10},
            {'action': 'deploy_agents', 'platform': 'vercel', 'count': 5}
        ],
        'beliefs_count': 5, # Example count
        'desires_count': 2, # Example count
        'intentions_count': 2, # Example count
        'quantum_available': True, # Example status
    }

@app.route('/')
def dashboard():
    data = generate_sample_data()
    return render_template_string(
        DASHBOARD_TEMPLATE,
        beliefs=data['beliefs'],
        desires=data['desires'],
        intentions=data['intentions'],
        running='True',
        last_updated=datetime.now().isoformat(),
        environment='Vercel Production',
        beliefs_count=data['beliefs_count'],
        desires_count=data['desires_count'],
        intentions_count=data['intentions_count'],
        quantum_available=data['quantum_available']
    )

@app.route('/api/status')
def api_status():
    data = generate_sample_data()
    return jsonify({
        'status': 'running',
        'environment': 'vercel',
        'timestamp': datetime.now().isoformat(),
        'data': data
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'fmaa-bdi-agent'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)


