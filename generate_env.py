#!/usr/bin/env python3
"""
Generate .env file for Supabase PostgreSQL connection
"""

import secrets
import string
import os

def generate_secret_key(length=32):
    """Generate a secure secret key"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def create_env_file():
    """Create .env file with Supabase configuration"""
    
    print("🔧 Supabase .env File Generator")
    print("=" * 40)
    
    print("\n📋 You need to get your database connection details from Supabase.")
    print("\n🔍 How to find your database password:")
    print("1. Go to https://supabase.com")
    print("2. Login and open your project dashboard")
    print("3. Click 'Settings' (gear icon) in the left sidebar")
    print("4. Click 'Database' from the settings menu")
    print("5. Scroll down to 'Connection string' section")
    print("6. Click the 'URI' tab")
    print("7. Copy the connection string or just the password")
    
    print("\n💡 Alternative method:")
    print("- Look for 'Database Password' in the Database settings")
    print("- Your host is: db.vxagyuidxthskmhqiaju.supabase.co")
    print("- Port: 5432")
    print("- Database: postgres")
    print("- Username: postgres")
    
    # Get connection details from user
    print("\n" + "="*50)
    print("Enter your database details:")
    
    db_password = input("Database Password: ").strip()
    
    if not db_password:
        print("❌ Database password is required!")
        return
    
    # Generate secure secret key
    secret_key = generate_secret_key(64)
    
    # Create .env content
    env_content = f"""# Supabase PostgreSQL Database Configuration
# Generated for project: vxagyuidxthskmhqiaju.supabase.co

# Database URL
DATABASE_URL=postgresql://postgres:{db_password}@db.vxagyuidxthskmhqiaju.supabase.co:5432/postgres

# Flask Secret Key (auto-generated)
SECRET_KEY={secret_key}

# Admin Configuration
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@sutrabyte.com
ADMIN_PASSWORD=admin123

# Environment
FLASK_ENV=production
FLASK_DEBUG=False
"""
    
    # Write to .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("\n✅ .env file created successfully!")
        print("📁 File location: .env")
        
        print("\n🔒 Security Note:")
        print("- Keep your .env file secure and never commit it to Git")
        print("- Your .env file is already in .gitignore")
        
        print("\n🚀 Next Steps:")
        print("1. Test your database connection: python test_postgresql_connection.py")
        print("2. Run your app: python app_postgresql.py")
        print("3. Deploy to Vercel with these environment variables")
        
        print(f"\n📋 Your connection string:")
        print(f"postgresql://postgres:{db_password}@db.vxagyuidxthskmhqiaju.supabase.co:5432/postgres")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        print("\n📝 Manual Setup:")
        print("Create a file named '.env' in your project root with:")
        print(env_content)

if __name__ == "__main__":
    create_env_file() 