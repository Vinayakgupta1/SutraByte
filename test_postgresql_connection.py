#!/usr/bin/env python3
"""
Test script to verify PostgreSQL connection
Run this script to test if your PostgreSQL database is accessible
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_postgresql_connection():
    """Test PostgreSQL connection"""
    
    # Check if DATABASE_URL is set
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not set!")
        print("Please set DATABASE_URL in your .env file")
        return False
    
    print(f"🔍 Testing connection to: {database_url.split('@')[1] if '@' in database_url else 'Unknown'}")
    
    try:
        # Test with psycopg2
        import psycopg2
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        print(f"✅ Successfully connected to PostgreSQL!")
        print(f"📋 PostgreSQL version: {version[0]}")
        cursor.close()
        conn.close()
        
        # Test with Flask-SQLAlchemy
        print("\n🔍 Testing Flask-SQLAlchemy connection...")
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import app, db
        
        with app.app_context():
            # Test basic query
            result = db.engine.execute('SELECT 1 as test')
            row = result.fetchone()
            if row and row[0] == 1:
                print("✅ Flask-SQLAlchemy connection successful!")
            else:
                print("❌ Flask-SQLAlchemy connection failed!")
                return False
        
        print("\n🎉 All connection tests passed!")
        print("Your PostgreSQL database is ready to use.")
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install required packages: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check if your DATABASE_URL is correct")
        print("2. Verify your PostgreSQL database is running")
        print("3. Check if your IP is whitelisted (if required)")
        print("4. Ensure the database credentials are correct")
        return False

if __name__ == '__main__':
    test_postgresql_connection() 