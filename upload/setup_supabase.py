#!/usr/bin/env python3
"""
Setup script untuk membuat tabel Supabase dan data awal
"""
import os
from supabase import create_client, Client
from datetime import datetime

def setup_supabase():
    """Setup Supabase database dengan tabel revenue_metrics"""
    
    # Konfigurasi Supabase (ganti dengan credentials yang benar)
    SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://your-project.supabase.co')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'your-anon-key')
    
    if SUPABASE_URL == 'https://your-project.supabase.co' or SUPABASE_KEY == 'your-anon-key':
        print("❌ SUPABASE_URL dan SUPABASE_KEY harus diset sebagai environment variable")
        print("   export SUPABASE_URL='https://your-project.supabase.co'")
        print("   export SUPABASE_KEY='your-anon-key'")
        return False
    
    try:
        # Koneksi ke Supabase
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Berhasil terhubung ke Supabase")
        
        # Data awal untuk revenue metrics
        initial_data = {
            'name': 'fmaa_bdi_metrics',
            'current_month': 25000,
            'target': 50000,
            'growth_rate': 15.5,
            'active_streams': 3,
            'updated_at': datetime.now().isoformat()
        }
        
        # Insert data awal
        response = supabase.table('revenue_metrics').upsert(initial_data).execute()
        print("✅ Data awal berhasil diinsert ke tabel revenue_metrics")
        print(f"   Data: {initial_data}")
        
        # Test query
        test_response = supabase.table('revenue_metrics').select("*").limit(1).single().execute()
        print("✅ Test query berhasil")
        print(f"   Retrieved data: {test_response.data}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setup Supabase: {e}")
        return False

def create_table_sql():
    """Generate SQL untuk membuat tabel revenue_metrics"""
    sql = """
-- Buat tabel revenue_metrics di Supabase
CREATE TABLE IF NOT EXISTS revenue_metrics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    current_month DECIMAL(12,2) DEFAULT 0,
    target DECIMAL(12,2) DEFAULT 50000,
    growth_rate DECIMAL(5,2) DEFAULT 0,
    active_streams INTEGER DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Insert data awal
INSERT INTO revenue_metrics (name, current_month, target, growth_rate, active_streams)
VALUES ('fmaa_bdi_metrics', 25000, 50000, 15.5, 3)
ON CONFLICT (name) DO UPDATE SET
    current_month = EXCLUDED.current_month,
    target = EXCLUDED.target,
    growth_rate = EXCLUDED.growth_rate,
    active_streams = EXCLUDED.active_streams,
    updated_at = NOW();

-- Enable RLS (Row Level Security) jika diperlukan
ALTER TABLE revenue_metrics ENABLE ROW LEVEL SECURITY;

-- Policy untuk akses publik (sesuaikan dengan kebutuhan)
CREATE POLICY "Allow public read access" ON revenue_metrics
FOR SELECT USING (true);

CREATE POLICY "Allow public write access" ON revenue_metrics
FOR ALL USING (true);
"""
    return sql

if __name__ == '__main__':
    print("🚀 FMAA BDI Supabase Setup")
    print("=" * 50)
    
    print("\n📋 SQL untuk membuat tabel (jalankan di Supabase SQL Editor):")
    print(create_table_sql())
    
    print("\n🔧 Setup otomatis dengan Python:")
    success = setup_supabase()
    
    if success:
        print("\n✅ Setup Supabase berhasil!")
        print("   Aplikasi sekarang dapat menggunakan real-time data dari Supabase")
    else:
        print("\n❌ Setup gagal. Pastikan:")
        print("   1. Tabel 'revenue_metrics' sudah dibuat di Supabase")
        print("   2. Environment variables SUPABASE_URL dan SUPABASE_KEY sudah diset")
        print("   3. API key memiliki akses read/write ke tabel")

