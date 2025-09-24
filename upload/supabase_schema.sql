-- OASIS v3 Production Database Schema
-- Ultra-Lightweight AI Superintelligence Ecosystem
-- Revenue Target: $50K+/month

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";

-- =============================================
-- AUTHENTICATION & USER MANAGEMENT
-- =============================================

-- Users table (extends Supabase auth.users)
CREATE TABLE public.users (
  id UUID REFERENCES auth.users(id) PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  username VARCHAR(50) UNIQUE,
  full_name VARCHAR(100),
  avatar_url TEXT,
  subscription_tier VARCHAR(20) DEFAULT 'free' CHECK (subscription_tier IN ('free', 'starter', 'professional', 'enterprise')),
  subscription_status VARCHAR(20) DEFAULT 'active' CHECK (subscription_status IN ('active', 'cancelled', 'suspended', 'trial')),
  subscription_expires_at TIMESTAMP WITH TIME ZONE,
  stripe_customer_id VARCHAR(255) UNIQUE,

  -- Usage tracking
  api_calls_current_month INTEGER DEFAULT 0,
  api_calls_limit INTEGER DEFAULT 1000,
  total_api_calls BIGINT DEFAULT 0,

  -- Revenue tracking
  total_revenue_generated DECIMAL(10,2) DEFAULT 0.00,
  lifetime_value DECIMAL(10,2) DEFAULT 0.00,

  -- Device & setup info
  termux_setup_completed BOOLEAN DEFAULT FALSE,
  device_info JSONB DEFAULT '{}',
  last_termux_sync TIMESTAMP WITH TIME ZONE,

  -- Timestamps
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  last_active_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- RLS policies for users
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own data" ON public.users
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own data" ON public.users  
  FOR UPDATE USING (auth.uid() = id);

-- =============================================
-- SUBSCRIPTION & BILLING
-- =============================================

-- Subscription plans
CREATE TABLE public.subscription_plans (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  slug VARCHAR(50) NOT NULL UNIQUE,
  price_monthly DECIMAL(8,2) NOT NULL,
  price_yearly DECIMAL(10,2),
  api_calls_limit INTEGER NOT NULL,
  features JSONB DEFAULT '[]',
  stripe_price_id VARCHAR(255),
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Insert default plans
INSERT INTO public.subscription_plans (name, slug, price_monthly, price_yearly, api_calls_limit, features, stripe_price_id) VALUES
('Free', 'free', 0.00, 0.00, 1000, '["Basic AI processing", "Community support"]', null),
('AI Starter', 'starter', 29.00, 290.00, 10000, '["Advanced AI models", "Email support", "Basic analytics"]', 'price_starter_monthly'),
('AI Professional', 'professional', 99.00, 990.00, 100000, '["Premium AI models", "Priority support", "Advanced analytics", "Custom integrations"]', 'price_pro_monthly'),
('AI Enterprise', 'enterprise', 299.00, 2990.00, -1, '["Unlimited API calls", "Dedicated support", "White-label solution", "Quantum optimization", "Custom model training"]', 'price_enterprise_monthly');

-- Subscriptions table
CREATE TABLE public.subscriptions (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  plan_id UUID REFERENCES public.subscription_plans(id),
  stripe_subscription_id VARCHAR(255) UNIQUE,
  status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'cancelled', 'past_due', 'unpaid', 'trialing')),
  current_period_start TIMESTAMP WITH TIME ZONE,
  current_period_end TIMESTAMP WITH TIME ZONE,
  cancel_at_period_end BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =============================================
-- API USAGE & ANALYTICS
-- =============================================

-- API calls tracking
CREATE TABLE public.api_calls (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  endpoint VARCHAR(255) NOT NULL,
  method VARCHAR(10) NOT NULL,
  status_code INTEGER NOT NULL,

  -- Request details
  request_data JSONB,
  response_data JSONB,
  processing_time_ms INTEGER,

  -- Billing & cost
  cost DECIMAL(6,4) DEFAULT 0.0000,
  billing_tier VARCHAR(20),

  -- Technical details
  user_agent TEXT,
  ip_address INET,
  device_type VARCHAR(50),
  termux_session_id VARCHAR(255),

  -- Performance metrics
  quantum_enhanced BOOLEAN DEFAULT FALSE,
  cache_hit BOOLEAN DEFAULT FALSE,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for performance
CREATE INDEX idx_api_calls_user_created ON public.api_calls(user_id, created_at DESC);
CREATE INDEX idx_api_calls_endpoint ON public.api_calls(endpoint);
CREATE INDEX idx_api_calls_status ON public.api_calls(status_code);

-- Daily usage aggregates
CREATE TABLE public.daily_usage (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  api_calls_count INTEGER DEFAULT 0,
  total_cost DECIMAL(8,4) DEFAULT 0.0000,
  total_processing_time_ms BIGINT DEFAULT 0,
  unique_endpoints INTEGER DEFAULT 0,
  error_rate DECIMAL(5,4) DEFAULT 0.0000,
  quantum_enhanced_calls INTEGER DEFAULT 0,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  UNIQUE(user_id, date)
);

-- =============================================
-- REVENUE & BUSINESS ANALYTICS
-- =============================================

-- Revenue events
CREATE TABLE public.revenue_events (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  revenue_stream VARCHAR(50) NOT NULL CHECK (revenue_stream IN ('subscription', 'api_usage', 'enterprise', 'consulting', 'custom_models')),
  amount DECIMAL(10,2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',

  -- Transaction details
  stripe_charge_id VARCHAR(255),
  stripe_invoice_id VARCHAR(255),
  description TEXT,
  metadata JSONB DEFAULT '{}',

  -- Business context
  plan_name VARCHAR(50),
  billing_period VARCHAR(20),

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Monthly revenue aggregates  
CREATE TABLE public.monthly_revenue (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  month DATE NOT NULL, -- First day of month
  total_revenue DECIMAL(12,2) DEFAULT 0.00,
  subscription_revenue DECIMAL(12,2) DEFAULT 0.00,
  api_revenue DECIMAL(12,2) DEFAULT 0.00,
  enterprise_revenue DECIMAL(12,2) DEFAULT 0.00,

  -- Metrics
  new_subscribers INTEGER DEFAULT 0,
  churned_subscribers INTEGER DEFAULT 0,
  active_subscribers INTEGER DEFAULT 0,
  average_revenue_per_user DECIMAL(8,2) DEFAULT 0.00,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(month)
);

-- =============================================
-- TERMUX ORCHESTRATION 
-- =============================================

-- Termux sessions
CREATE TABLE public.termux_sessions (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  session_id VARCHAR(255) NOT NULL,
  device_info JSONB DEFAULT '{}',

  -- Performance metrics
  total_requests INTEGER DEFAULT 0,
  successful_requests INTEGER DEFAULT 0,
  average_response_time DECIMAL(8,2) DEFAULT 0.00,

  -- Status
  is_active BOOLEAN DEFAULT TRUE,
  last_ping TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Sync data
  config_version VARCHAR(20),
  orchestrator_version VARCHAR(20),

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =============================================
-- QUANTUM OPTIMIZATION LOGS
-- =============================================

-- Quantum optimization results
CREATE TABLE public.quantum_optimizations (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  optimization_type VARCHAR(50) NOT NULL CHECK (optimization_type IN ('model_parameters', 'revenue_strategy', 'api_performance')),

  -- Input/Output
  input_parameters JSONB NOT NULL,
  optimized_parameters JSONB NOT NULL,
  improvement_percentage DECIMAL(5,2),

  -- Quantum metrics
  quantum_advantage BOOLEAN DEFAULT FALSE,
  quantum_backend VARCHAR(50),
  optimization_time_ms INTEGER,

  -- Business impact
  revenue_impact DECIMAL(8,4) DEFAULT 0.0000,

  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =============================================
-- VIEWS & FUNCTIONS
-- =============================================

-- Real-time revenue dashboard view
CREATE VIEW public.revenue_dashboard AS
SELECT 
  DATE_TRUNC('month', created_at) as month,
  COUNT(DISTINCT user_id) as active_users,
  SUM(amount) as total_revenue,
  AVG(amount) as avg_transaction,
  COUNT(*) as total_transactions
FROM public.revenue_events 
WHERE created_at >= DATE_TRUNC('year', NOW())
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month DESC;

-- User analytics view
CREATE VIEW public.user_analytics AS
SELECT 
  u.id,
  u.subscription_tier,
  u.api_calls_current_month,
  u.total_revenue_generated,
  COALESCE(du.api_calls_count, 0) as today_api_calls,
  COALESCE(du.total_cost, 0) as today_cost
FROM public.users u
LEFT JOIN public.daily_usage du ON u.id = du.user_id AND du.date = CURRENT_DATE;

-- Function to update user monthly API usage
CREATE OR REPLACE FUNCTION update_user_api_usage()
RETURNS TRIGGER AS $$
BEGIN
  -- Update user's monthly API call count
  UPDATE public.users 
  SET 
    api_calls_current_month = api_calls_current_month + 1,
    total_api_calls = total_api_calls + 1,
    last_active_at = NOW()
  WHERE id = NEW.user_id;

  -- Insert or update daily usage
  INSERT INTO public.daily_usage (user_id, date, api_calls_count, total_cost, total_processing_time_ms)
  VALUES (
    NEW.user_id, 
    CURRENT_DATE, 
    1, 
    COALESCE(NEW.cost, 0), 
    COALESCE(NEW.processing_time_ms, 0)
  )
  ON CONFLICT (user_id, date) 
  DO UPDATE SET
    api_calls_count = daily_usage.api_calls_count + 1,
    total_cost = daily_usage.total_cost + COALESCE(NEW.cost, 0),
    total_processing_time_ms = daily_usage.total_processing_time_ms + COALESCE(NEW.processing_time_ms, 0);

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for API usage tracking
CREATE TRIGGER trigger_update_api_usage
  AFTER INSERT ON public.api_calls
  FOR EACH ROW
  EXECUTE FUNCTION update_user_api_usage();

-- Function to reset monthly API usage (call monthly via cron)
CREATE OR REPLACE FUNCTION reset_monthly_api_usage()
RETURNS void AS $$
BEGIN
  UPDATE public.users SET api_calls_current_month = 0;
END;
$$ LANGUAGE plpgsql;

-- RLS policies for all tables
ALTER TABLE public.api_calls ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.daily_usage ENABLE ROW LEVEL SECURITY; 
ALTER TABLE public.revenue_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.termux_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.quantum_optimizations ENABLE ROW LEVEL SECURITY;

-- User can only see their own data
CREATE POLICY "Users can view own api_calls" ON public.api_calls FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can view own daily_usage" ON public.daily_usage FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can view own revenue_events" ON public.revenue_events FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can view own termux_sessions" ON public.termux_sessions FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can view own quantum_optimizations" ON public.quantum_optimizations FOR SELECT USING (auth.uid() = user_id);

-- Public read access for subscription plans
ALTER TABLE public.subscription_plans ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone can view subscription plans" ON public.subscription_plans FOR SELECT USING (true);