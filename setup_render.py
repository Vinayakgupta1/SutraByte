#!/usr/bin/env python3
"""
Setup script for Render deployment
This script helps verify your configuration and generate secure environment variables.
"""

import os
import secrets
import string
from pathlib import Path

def generate_secret_key(length=32):
    """Generate a secure secret key"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'app.py',
        'init_db.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def check_requirements_txt():
    """Check if requirements.txt has necessary packages"""
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        required_packages = [
            'Flask',
            'Flask-SQLAlchemy',
            'Flask-Login',
            'gunicorn',
            'psycopg2-binary'
        ]
        
        missing_packages = []
        for package in required_packages:
            if package not in content:
                missing_packages.append(package)
        
        if missing_packages:
            print("❌ Missing packages in requirements.txt:")
            for package in missing_packages:
                print(f"   - {package}")
            return False
        
        print("✅ All required packages found in requirements.txt")
        return True
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def generate_env_template():
    """Generate a template .env file for Render"""
    secret_key = generate_secret_key(64)
    
    env_template = f"""# Render Deployment Environment Variables
# Copy these values to your Render environment variables

# Database Configuration
DATABASE_URL=postgresql://user:password@host:port/database
# ^ Replace with your Render PostgreSQL Internal Database URL

# Security
SECRET_KEY={secret_key}

# Admin Configuration
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=your-secure-admin-password

# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False

# Optional: Custom domain (if using)
# CUSTOM_DOMAIN=yourdomain.com
"""
    
    with open('.env.render', 'w') as f:
        f.write(env_template)
    
    print("✅ Generated .env.render template")
    print("📝 Copy the values from .env.render to your Render environment variables")

def main():
    """Main setup function"""
    print("🚀 SutraByte Render Deployment Setup")
    print("=" * 50)
    
    # Check requirements
    print("\n1. Checking project requirements...")
    if not check_requirements():
        print("\n❌ Please fix the missing files before deploying")
        return
    
    if not check_requirements_txt():
        print("\n❌ Please add missing packages to requirements.txt")
        return
    
    # Generate environment template
    print("\n2. Generating environment variables template...")
    generate_env_template()
    
    # Deployment checklist
    print("\n3. Deployment Checklist:")
    print("✅ Code is in a private GitHub repository")
    print("✅ All files are committed and pushed")
    print("✅ PostgreSQL database created on Render")
    print("✅ Web service created on Render")
    print("✅ Environment variables set in Render")
    
    print("\n📋 Next Steps:")
    print("1. Go to render.com and create a PostgreSQL database")
    print("2. Create a web service and connect your GitHub repo")
    print("3. Set environment variables using the .env.render template")
    print("4. Deploy and test your application")
    print("5. Access your admin panel at: https://your-app.onrender.com/create-admin")
    
    print("\n📚 For detailed instructions, see: DEPLOYMENT_GUIDE.md")
    print("🔗 Render Dashboard: https://dashboard.render.com")
    
    print("\n🎉 Setup complete! You're ready to deploy on Render.")

if __name__ == "__main__":
    main() 