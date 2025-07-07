#!/usr/bin/env python3
"""
Generate a secure Flask secret key
Run this script to generate a cryptographically secure secret key
"""

import secrets
import string

def generate_secret_key(length=32):
    """Generate a secure random secret key"""
    # Use a combination of letters, digits, and special characters
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Generate a cryptographically secure random string
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    
    return secret_key

def main():
    """Generate and display a secure secret key"""
    print("🔐 Generating a secure Flask SECRET_KEY...")
    print()
    
    # Generate a secure key
    secret_key = generate_secret_key(32)
    
    print("✅ Your secure SECRET_KEY:")
    print(f"SECRET_KEY={secret_key}")
    print()
    
    print("📝 Copy this line to your .env file:")
    print(f"DATABASE_URL=postgresql://sutrabyte_admin:gikmd3YKT7lRpHqprpsNZnKBIdwXEjo7@dpg-d1gdr2vfte5s738h4ltg-a/sutrabyte_prod_mmyq")
    print(f"SECRET_KEY={secret_key}")
    print()
    
    print("⚠️  Important Security Notes:")
    print("1. Keep this secret key private and secure")
    print("2. Never commit it to version control")
    print("3. Use different keys for development and production")
    print("4. If compromised, generate a new one and update your app")
    print()
    
    print("🎯 Next Steps:")
    print("1. Create a .env file in your project root")
    print("2. Add the DATABASE_URL and SECRET_KEY lines above")
    print("3. Run: python test_postgresql_connection.py")
    print("4. Run: python setup_postgresql.py")

if __name__ == '__main__':
    main() 