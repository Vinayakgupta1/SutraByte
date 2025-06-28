"""
SutraByte Security Configuration

This file contains security configuration instructions and helper functions.

SECURITY SETUP INSTRUCTIONS:
============================

1. Set Environment Variables:
   Create a .env file in the project root with the following variables:

   SECRET_KEY=your-super-secret-key-here-change-this-immediately
   ADMIN_USERNAME=your_admin_username
   ADMIN_EMAIL=admin@yourdomain.com
   ADMIN_PASSWORD=your_strong_admin_password
   ADMIN_CREATION_TOKEN=your-secure-admin-creation-token
   FLASK_DEBUG=False

2. Generate a Strong Secret Key:
   Run this in Python:
   import secrets
   print(secrets.token_hex(32))

3. Create Admin User:
   Option A: Set environment variables and restart the app
   Option B: Use the web interface at /create-admin with the token

4. Security Best Practices:
   - Use HTTPS in production
   - Regularly rotate admin passwords
   - Monitor access logs
   - Keep dependencies updated
   - Use strong, unique passwords
   - Enable two-factor authentication if possible

SECURITY FEATURES IMPLEMENTED:
==============================
- Password strength validation
- Input sanitization
- Secure admin creation
- Environment-based configuration
- Session security
- CSRF protection (basic)
- XSS prevention
- SQL injection prevention
"""

import os
import secrets
from typing import Tuple

def generate_secure_token() -> str:
    """Generate a secure random token for admin creation"""
    return secrets.token_urlsafe(32)

def generate_secret_key() -> str:
    """Generate a secure secret key for Flask"""
    return secrets.token_hex(32)

def validate_environment() -> Tuple[bool, list]:
    """Validate that all required environment variables are set"""
    required_vars = [
        'SECRET_KEY',
        'ADMIN_USERNAME',
        'ADMIN_EMAIL', 
        'ADMIN_PASSWORD',
        'ADMIN_CREATION_TOKEN'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    return len(missing_vars) == 0, missing_vars

def get_security_status() -> dict:
    """Get current security configuration status"""
    is_valid, missing = validate_environment()
    
    return {
        'environment_valid': is_valid,
        'missing_variables': missing,
        'debug_mode': os.environ.get('FLASK_DEBUG', 'False').lower() == 'true',
        'secure_cookies': os.environ.get('SESSION_COOKIE_SECURE', 'True').lower() == 'true',
        'secret_key_set': bool(os.environ.get('SECRET_KEY')),
        'admin_configured': bool(os.environ.get('ADMIN_USERNAME') and os.environ.get('ADMIN_PASSWORD'))
    }

if __name__ == "__main__":
    print("SutraByte Security Configuration")
    print("=" * 40)
    
    # Generate example values
    print(f"Example SECRET_KEY: {generate_secret_key()}")
    print(f"Example ADMIN_CREATION_TOKEN: {generate_secure_token()}")
    
    # Check current status
    status = get_security_status()
    print(f"\nSecurity Status:")
    print(f"Environment Valid: {status['environment_valid']}")
    print(f"Debug Mode: {status['debug_mode']}")
    print(f"Secure Cookies: {status['secure_cookies']}")
    print(f"Secret Key Set: {status['secret_key_set']}")
    print(f"Admin Configured: {status['admin_configured']}")
    
    if not status['environment_valid']:
        print(f"\nMissing Variables: {', '.join(status['missing_variables'])}")
        print("Please set these environment variables before running the application.") 