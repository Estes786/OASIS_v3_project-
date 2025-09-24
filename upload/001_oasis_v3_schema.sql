-- OASIS v3 Database Schema
-- Ultra-Lightweight AI Superintelligence Ecosystem
-- Revenue Target: $50K+/month

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Users table for authentication and tracking
CREATE TABLE users (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(50) UNIQUE,
  full_name VARCHAR(100),
  avatar_url TEXT,
  subscription_tier VARCHAR(20) DEFAULT 'free' CHECK (subscription_tier IN ('free', 'premium', 'enterprise')),
  subscription_expires_at TIMESTAMP WITH TIME ZONE,
  total_api_calls INTEGER DEFAULT 0,
  total_revenue_generated DECIMAL(10,2) DEFAULT 0.00,
  device_info JSONB,
  termux_setup_completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  last_active_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- API calls tracking for revenue calculation
CREATE TABLE api_calls (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  endpoint VARCHAR(100) NOT NULL,
  method VARCHAR(10) NOT NULL,
  request_data JSONB,
  response_data JSONB,
  processing_time_ms INTEGER,
  status_code INTEGER,
  error_message TEXT,
  revenue_generated DECIMAL(8,4) DEFAULT 0.01,
  device_type VARCHAR(50),
  user_agent TEXT,
  ip_address INET,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Revenue tracking and analytics
CREATE TABLE revenue_records (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  revenue_stream VARCHAR(50) NOT NULL CHECK (revenue_stream IN ('api_calls', 'premium_subscription', 'enterprise_subscription', 'data_insights')),
  amount DECIMAL(10,2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  description TEXT,
  metadata JSONB,
  transaction_id VARCHAR(100),
  payment_method VARCHAR(50),
  status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
  processed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Business intelligence and analytics
CREATE TABLE business_metrics (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  metric_name VARCHAR(100) NOT NULL,
  metric_value DECIMAL(15,4) NOT NULL,
  metric_type VARCHAR(50) NOT NULL CHECK (metric_type IN ('revenue', 'usage', 'performance', 'growth')),
  time_period VARCHAR(20) NOT NULL CHECK (time_period IN ('hourly', 'daily', 'weekly', 'monthly', 'yearly')),
  metadata JSONB,
  recorded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(metric_name, time_period, DATE_TRUNC(time_period, recorded_at))
);

-- AI processing results cache
CREATE TABLE ai_cache (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  cache_key VARCHAR(255) UNIQUE NOT NULL,
  ai_model VARCHAR(100) NOT NULL,
  input_hash VARCHAR(64) NOT NULL,
  input_data JSONB NOT NULL,
  output_data JSONB NOT NULL,
  processing_time_ms INTEGER,
  token_count INTEGER,
  expires_at TIMESTAMP WITH TIME ZONE,
  hit_count INTEGER DEFAULT 0,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- System configuration and feature flags
CREATE TABLE system_config (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  config_key VARCHAR(100) UNIQUE NOT NULL,
  config_value JSONB NOT NULL,
  description TEXT,
  is_active BOOLEAN DEFAULT TRUE,
  environment VARCHAR(20) DEFAULT 'production' CHECK (environment IN ('development', 'staging', 'production')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Termux installations and device tracking
CREATE TABLE termux_installations (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  device_id VARCHAR(100) UNIQUE NOT NULL,
  device_model VARCHAR(100),
  android_version VARCHAR(20),
  termux_version VARCHAR(20),
  oasis_client_version VARCHAR(20) DEFAULT '3.0.0',
  installation_size_mb DECIMAL(5,2),
  setup_completed BOOLEAN DEFAULT FALSE,
  last_sync_at TIMESTAMP WITH TIME ZONE,
  total_requests INTEGER DEFAULT 0,
  status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'uninstalled')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Feedback and support tickets
CREATE TABLE support_tickets (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES users(id) ON DELETE SET NULL,
  subject VARCHAR(200) NOT NULL,
  description TEXT NOT NULL,
  category VARCHAR(50) NOT NULL CHECK (category IN ('technical', 'billing', 'feature_request', 'bug_report', 'general')),
  priority VARCHAR(20) DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
  status VARCHAR(20) DEFAULT 'open' CHECK (status IN ('open', 'in_progress', 'resolved', 'closed')),
  assigned_to VARCHAR(100),
  resolution TEXT,
  metadata JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  resolved_at TIMESTAMP WITH TIME ZONE
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_subscription_tier ON users(subscription_tier);
CREATE INDEX idx_users_created_at ON users(created_at);

CREATE INDEX idx_api_calls_user_id ON api_calls(user_id);
CREATE INDEX idx_api_calls_endpoint ON api_calls(endpoint);
CREATE INDEX idx_api_calls_created_at ON api_calls(created_at);
CREATE INDEX idx_api_calls_revenue ON api_calls(revenue_generated);

CREATE INDEX idx_revenue_records_user_id ON revenue_records(user_id);
CREATE INDEX idx_revenue_records_stream ON revenue_records(revenue_stream);
CREATE INDEX idx_revenue_records_created_at ON revenue_records(created_at);
CREATE INDEX idx_revenue_records_amount ON revenue_records(amount);

CREATE INDEX idx_business_metrics_name ON business_metrics(metric_name);
CREATE INDEX idx_business_metrics_type ON business_metrics(metric_type);
CREATE INDEX idx_business_metrics_recorded_at ON business_metrics(recorded_at);

CREATE INDEX idx_ai_cache_key ON ai_cache(cache_key);
CREATE INDEX idx_ai_cache_model ON ai_cache(ai_model);
CREATE INDEX idx_ai_cache_expires_at ON ai_cache(expires_at);

CREATE INDEX idx_termux_installations_user_id ON termux_installations(user_id);
CREATE INDEX idx_termux_installations_device_id ON termux_installations(device_id);
CREATE INDEX idx_termux_installations_status ON termux_installations(status);

CREATE INDEX idx_support_tickets_user_id ON support_tickets(user_id);
CREATE INDEX idx_support_tickets_status ON support_tickets(status);
CREATE INDEX idx_support_tickets_category ON support_tickets(category);

-- Triggers for automatic timestamp updates
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users 
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_system_config_updated_at BEFORE UPDATE ON system_config 
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_termux_installations_updated_at BEFORE UPDATE ON termux_installations 
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_support_tickets_updated_at BEFORE UPDATE ON support_tickets 
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- RLS (Row Level Security) policies
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE api_calls ENABLE ROW LEVEL SECURITY;
ALTER TABLE revenue_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE termux_installations ENABLE ROW LEVEL SECURITY;
ALTER TABLE support_tickets ENABLE ROW LEVEL SECURITY;

-- Policies for users
CREATE POLICY "Users can view own data" ON users FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own data" ON users FOR UPDATE USING (auth.uid() = id);

-- Policies for API calls
CREATE POLICY "Users can view own API calls" ON api_calls FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Service role can insert API calls" ON api_calls FOR INSERT WITH CHECK (true);

-- Policies for revenue records
CREATE POLICY "Users can view own revenue" ON revenue_records FOR SELECT USING (auth.uid() = user_id);

-- Policies for Termux installations
CREATE POLICY "Users can view own installations" ON termux_installations FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can update own installations" ON termux_installations FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own installations" ON termux_installations FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Policies for support tickets
CREATE POLICY "Users can view own tickets" ON support_tickets FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can create tickets" ON support_tickets FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Insert initial system configuration
INSERT INTO system_config (config_key, config_value, description) VALUES
('revenue_target_monthly', '50000', 'Monthly revenue target in USD'),
('api_call_base_price', '0.01', 'Base price per API call in USD'),
('premium_subscription_price', '9.99', 'Monthly premium subscription price'),
('enterprise_subscription_price', '99.99', 'Monthly enterprise subscription price'),
('data_insights_price', '0.05', 'Price per data insights analysis'),
('termux_max_footprint_mb', '5', 'Maximum allowed Termux footprint in MB'),
('ai_cache_ttl_hours', '24', 'AI response cache TTL in hours'),
('max_api_calls_free_tier', '1000', 'Maximum API calls for free tier per month'),
('max_api_calls_premium_tier', '10000', 'Maximum API calls for premium tier per month');

-- Insert initial business metrics
INSERT INTO business_metrics (metric_name, metric_value, metric_type, time_period) VALUES
('revenue_target', 50000.00, 'revenue', 'monthly'),
('mobile_footprint_target_mb', 5.00, 'performance', 'daily'),
('zero_dependencies_compliance', 100.00, 'performance', 'daily'),
('user_acquisition_target', 10000.00, 'growth', 'monthly'),
('api_calls_target', 1000000.00, 'usage', 'monthly');

-- Views for analytics and reporting
CREATE VIEW revenue_dashboard AS
SELECT 
  DATE_TRUNC('month', created_at) as month,
  revenue_stream,
  COUNT(*) as transaction_count,
  SUM(amount) as total_amount,
  AVG(amount) as average_amount
FROM revenue_records 
WHERE status = 'completed'
GROUP BY DATE_TRUNC('month', created_at), revenue_stream
ORDER BY month DESC, total_amount DESC;

CREATE VIEW user_analytics AS
SELECT 
  subscription_tier,
  COUNT(*) as user_count,
  AVG(total_api_calls) as avg_api_calls,
  SUM(total_revenue_generated) as total_revenue,
  AVG(total_revenue_generated) as avg_revenue_per_user
FROM users
GROUP BY subscription_tier;

CREATE VIEW termux_deployment_stats AS
SELECT 
  oasis_client_version,
  COUNT(*) as installation_count,
  AVG(installation_size_mb) as avg_size_mb,
  COUNT(CASE WHEN setup_completed THEN 1 END) as completed_setups,
  COUNT(CASE WHEN status = 'active' THEN 1 END) as active_installations
FROM termux_installations
GROUP BY oasis_client_version
ORDER BY installation_count DESC;

-- Function to calculate monthly revenue
CREATE OR REPLACE FUNCTION get_monthly_revenue(target_month DATE DEFAULT CURRENT_DATE)
RETURNS TABLE(
  stream VARCHAR(50),
  amount DECIMAL(10,2),
  transaction_count BIGINT
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    r.revenue_stream::VARCHAR(50),
    SUM(r.amount)::DECIMAL(10,2),
    COUNT(*)::BIGINT
  FROM revenue_records r
  WHERE DATE_TRUNC('month', r.created_at) = DATE_TRUNC('month', target_month)
    AND r.status = 'completed'
  GROUP BY r.revenue_stream
  ORDER BY SUM(r.amount) DESC;
END;
$$ LANGUAGE plpgsql;