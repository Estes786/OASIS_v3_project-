"""
OASIS Monitoring and Analytics API Routes
"""

from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import json
import random
import time
from collections import defaultdict

monitoring_bp = Blueprint('monitoring', __name__)

# In-memory storage for demo purposes (replace with proper database in production)
class MonitoringData:
    def __init__(self):
        self.metrics = defaultdict(list)
        self.events = []
        self.alerts = []
        self.system_status = {
            'status': 'healthy',
            'uptime': 0,
            'last_check': datetime.now()
        }
        self.revenue_data = {
            'monthly_revenue': 46650,
            'daily_revenue': [],
            'customer_count': 1247,
            'churn_rate': 2.3
        }
        
    def add_metric(self, metric_name, value, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.metrics[metric_name].append({
            'value': value,
            'timestamp': timestamp.isoformat()
        })
        # Keep only last 1000 entries per metric
        if len(self.metrics[metric_name]) > 1000:
            self.metrics[metric_name] = self.metrics[metric_name][-1000:]
    
    def add_event(self, event_type, message, severity='info'):
        self.events.append({
            'type': event_type,
            'message': message,
            'severity': severity,
            'timestamp': datetime.now().isoformat()
        })
        # Keep only last 500 events
        if len(self.events) > 500:
            self.events = self.events[-500:]
    
    def add_alert(self, alert_type, message, severity='warning'):
        self.alerts.append({
            'type': alert_type,
            'message': message,
            'severity': severity,
            'timestamp': datetime.now().isoformat(),
            'resolved': False
        })

# Global monitoring instance
monitoring_data = MonitoringData()

# Initialize with some sample data
def initialize_sample_data():
    """Initialize with realistic sample data"""
    now = datetime.now()
    
    # Generate sample metrics for the last 24 hours
    for i in range(24):
        timestamp = now - timedelta(hours=23-i)
        
        # System metrics
        monitoring_data.add_metric('cpu_usage', random.uniform(15.0, 85.0), timestamp)
        monitoring_data.add_metric('memory_usage', random.uniform(30.0, 70.0), timestamp)
        monitoring_data.add_metric('response_time', random.uniform(0.1, 2.0), timestamp)
        monitoring_data.add_metric('requests_per_hour', random.randint(500, 2000), timestamp)
        
        # Business metrics
        monitoring_data.add_metric('active_users', random.randint(100, 500), timestamp)
        monitoring_data.add_metric('revenue_hourly', random.uniform(50.0, 200.0), timestamp)
        monitoring_data.add_metric('api_calls', random.randint(1000, 5000), timestamp)
        
        # AI/ML metrics
        monitoring_data.add_metric('model_accuracy', random.uniform(95.0, 99.9), timestamp)
        monitoring_data.add_metric('inference_time', random.uniform(0.05, 0.5), timestamp)
        monitoring_data.add_metric('quantum_operations', random.randint(10, 100), timestamp)
    
    # Add sample events
    monitoring_data.add_event('system', 'OASIS monitoring system initialized', 'info')
    monitoring_data.add_event('deployment', 'New model deployed to production', 'info')
    monitoring_data.add_event('performance', 'Response time improved by 15%', 'success')
    
    # Add sample alerts
    monitoring_data.add_alert('performance', 'High CPU usage detected', 'warning')
    monitoring_data.add_alert('business', 'Revenue target 95% achieved', 'info')

# Initialize sample data on module load
initialize_sample_data()

@monitoring_bp.route('/health', methods=['GET'])
def health_check():
    """System health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'uptime': time.time() - monitoring_data.system_status['last_check'].timestamp()
    })

@monitoring_bp.route('/metrics', methods=['GET'])
def get_metrics():
    """Get system metrics"""
    metric_name = request.args.get('metric')
    hours = int(request.args.get('hours', 24))
    
    cutoff_time = datetime.now() - timedelta(hours=hours)
    
    if metric_name:
        # Return specific metric
        if metric_name in monitoring_data.metrics:
            filtered_data = [
                entry for entry in monitoring_data.metrics[metric_name]
                if datetime.fromisoformat(entry['timestamp']) > cutoff_time
            ]
            return jsonify({
                'success': True,
                'metric': metric_name,
                'data': filtered_data,
                'count': len(filtered_data)
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Metric {metric_name} not found'
            }), 404
    else:
        # Return all metrics summary
        summary = {}
        for metric, data in monitoring_data.metrics.items():
            filtered_data = [
                entry for entry in data
                if datetime.fromisoformat(entry['timestamp']) > cutoff_time
            ]
            if filtered_data:
                values = [entry['value'] for entry in filtered_data]
                summary[metric] = {
                    'current': filtered_data[-1]['value'],
                    'average': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'count': len(filtered_data)
                }
        
        return jsonify({
            'success': True,
            'summary': summary,
            'timestamp': datetime.now().isoformat()
        })

@monitoring_bp.route('/metrics', methods=['POST'])
def add_metric():
    """Add a new metric data point"""
    data = request.get_json()
    
    if not data or 'metric' not in data or 'value' not in data:
        return jsonify({
            'success': False,
            'error': 'Missing required fields: metric, value'
        }), 400
    
    metric_name = data['metric']
    value = data['value']
    timestamp = data.get('timestamp')
    
    if timestamp:
        timestamp = datetime.fromisoformat(timestamp)
    
    monitoring_data.add_metric(metric_name, value, timestamp)
    
    return jsonify({
        'success': True,
        'message': f'Metric {metric_name} added successfully'
    })

@monitoring_bp.route('/events', methods=['GET'])
def get_events():
    """Get system events"""
    limit = int(request.args.get('limit', 100))
    event_type = request.args.get('type')
    
    events = monitoring_data.events
    
    if event_type:
        events = [event for event in events if event['type'] == event_type]
    
    # Return most recent events first
    events = sorted(events, key=lambda x: x['timestamp'], reverse=True)[:limit]
    
    return jsonify({
        'success': True,
        'events': events,
        'count': len(events)
    })

@monitoring_bp.route('/events', methods=['POST'])
def add_event():
    """Add a new system event"""
    data = request.get_json()
    
    if not data or 'type' not in data or 'message' not in data:
        return jsonify({
            'success': False,
            'error': 'Missing required fields: type, message'
        }), 400
    
    event_type = data['type']
    message = data['message']
    severity = data.get('severity', 'info')
    
    monitoring_data.add_event(event_type, message, severity)
    
    return jsonify({
        'success': True,
        'message': 'Event added successfully'
    })

@monitoring_bp.route('/alerts', methods=['GET'])
def get_alerts():
    """Get system alerts"""
    active_only = request.args.get('active_only', 'false').lower() == 'true'
    
    alerts = monitoring_data.alerts
    
    if active_only:
        alerts = [alert for alert in alerts if not alert['resolved']]
    
    # Return most recent alerts first
    alerts = sorted(alerts, key=lambda x: x['timestamp'], reverse=True)
    
    return jsonify({
        'success': True,
        'alerts': alerts,
        'count': len(alerts)
    })

@monitoring_bp.route('/alerts', methods=['POST'])
def add_alert():
    """Add a new system alert"""
    data = request.get_json()
    
    if not data or 'type' not in data or 'message' not in data:
        return jsonify({
            'success': False,
            'error': 'Missing required fields: type, message'
        }), 400
    
    alert_type = data['type']
    message = data['message']
    severity = data.get('severity', 'warning')
    
    monitoring_data.add_alert(alert_type, message, severity)
    
    return jsonify({
        'success': True,
        'message': 'Alert added successfully'
    })

@monitoring_bp.route('/alerts/<int:alert_id>/resolve', methods=['POST'])
def resolve_alert(alert_id):
    """Resolve a system alert"""
    if alert_id < len(monitoring_data.alerts):
        monitoring_data.alerts[alert_id]['resolved'] = True
        monitoring_data.alerts[alert_id]['resolved_at'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'message': 'Alert resolved successfully'
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Alert not found'
        }), 404

@monitoring_bp.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    """Get comprehensive dashboard data"""
    
    # Calculate current system status
    now = datetime.now()
    cutoff_time = now - timedelta(hours=1)
    
    # Get recent metrics
    recent_metrics = {}
    for metric, data in monitoring_data.metrics.items():
        recent_data = [
            entry for entry in data
            if datetime.fromisoformat(entry['timestamp']) > cutoff_time
        ]
        if recent_data:
            recent_metrics[metric] = recent_data[-1]['value']
    
    # Count active alerts
    active_alerts = len([alert for alert in monitoring_data.alerts if not alert['resolved']])
    
    # Calculate uptime
    uptime_seconds = (now - monitoring_data.system_status['last_check']).total_seconds()
    uptime_percentage = 99.95  # Simulated high uptime
    
    dashboard_data = {
        'system_status': {
            'status': 'healthy',
            'uptime_percentage': uptime_percentage,
            'uptime_seconds': uptime_seconds,
            'active_alerts': active_alerts,
            'last_updated': now.isoformat()
        },
        'current_metrics': recent_metrics,
        'revenue_data': monitoring_data.revenue_data,
        'recent_events': monitoring_data.events[-10:],  # Last 10 events
        'active_alerts': [alert for alert in monitoring_data.alerts if not alert['resolved']][-5:]  # Last 5 active alerts
    }
    
    return jsonify({
        'success': True,
        'dashboard': dashboard_data,
        'timestamp': now.isoformat()
    })

@monitoring_bp.route('/analytics/performance', methods=['GET'])
def get_performance_analytics():
    """Get detailed performance analytics"""
    hours = int(request.args.get('hours', 24))
    cutoff_time = datetime.now() - timedelta(hours=hours)
    
    performance_metrics = ['cpu_usage', 'memory_usage', 'response_time', 'requests_per_hour']
    analytics = {}
    
    for metric in performance_metrics:
        if metric in monitoring_data.metrics:
            filtered_data = [
                entry for entry in monitoring_data.metrics[metric]
                if datetime.fromisoformat(entry['timestamp']) > cutoff_time
            ]
            
            if filtered_data:
                values = [entry['value'] for entry in filtered_data]
                analytics[metric] = {
                    'data': filtered_data,
                    'statistics': {
                        'current': filtered_data[-1]['value'],
                        'average': sum(values) / len(values),
                        'min': min(values),
                        'max': max(values),
                        'trend': 'stable'  # Simplified trend analysis
                    }
                }
    
    return jsonify({
        'success': True,
        'performance_analytics': analytics,
        'period_hours': hours,
        'timestamp': datetime.now().isoformat()
    })

@monitoring_bp.route('/analytics/business', methods=['GET'])
def get_business_analytics():
    """Get business metrics and analytics"""
    
    # Calculate business KPIs
    business_kpis = {
        'monthly_recurring_revenue': monitoring_data.revenue_data['monthly_revenue'],
        'customer_count': monitoring_data.revenue_data['customer_count'],
        'churn_rate': monitoring_data.revenue_data['churn_rate'],
        'average_revenue_per_user': monitoring_data.revenue_data['monthly_revenue'] / monitoring_data.revenue_data['customer_count'],
        'growth_rate': 23.5,  # Simulated growth rate
        'customer_acquisition_cost': 45.0,
        'customer_lifetime_value': 850.0
    }
    
    # Get revenue trend data
    revenue_trend = []
    for i in range(30):  # Last 30 days
        date = datetime.now() - timedelta(days=29-i)
        daily_revenue = random.uniform(1400, 1800)  # Simulated daily revenue
        revenue_trend.append({
            'date': date.strftime('%Y-%m-%d'),
            'revenue': daily_revenue
        })
    
    return jsonify({
        'success': True,
        'business_analytics': {
            'kpis': business_kpis,
            'revenue_trend': revenue_trend,
            'customer_segments': {
                'enterprise': 45,
                'professional': 234,
                'starter': 968
            },
            'top_features': [
                {'name': 'AI Text Generation', 'usage': 89},
                {'name': 'Sentiment Analysis', 'usage': 76},
                {'name': 'Question Answering', 'usage': 65},
                {'name': 'Custom Models', 'usage': 43}
            ]
        },
        'timestamp': datetime.now().isoformat()
    })

