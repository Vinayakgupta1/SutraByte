#!/usr/bin/env python3
"""
Create a clean .env file for production testing
"""

env_content = """# Production Database Configuration
DATABASE_URL=postgresql://sutrabyte_admin:gikmd3YKT7lRpHqprpsNZnKBIdwXEjo7@dpg-d1gdr2vfte5s738h4ltg-a/sutrabyte_prod_mmyq

# Flask Security
SECRET_KEY=92a1b31036b5b79129a8b388f87b415594a040c053cace96cb381946f5ec86c8

# Admin Configuration
ADMIN_USERNAME=sutrabyte_admin
ADMIN_EMAIL=admin@sutrabyte.com
ADMIN_PASSWORD=SutraByte2024!
ADMIN_CREATION_TOKEN=RPO-c2bsv-ALl6klWmAi6ncLXFdj8Wm17q42JEXxjNA

# Production Environment
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
"""

# Write the .env file
with open('.env', 'w', encoding='utf-8') as f:
    f.write(env_content)

print("✅ .env file created successfully!")
print("📋 Environment variables set:")
print("- DATABASE_URL: PostgreSQL connection")
print("- SECRET_KEY: Flask security key")
print("- ADMIN_*: Admin user configuration")
print("- FLASK_*: Environment settings")
print()
print("🚀 Next steps:")
print("1. Install PostgreSQL dependencies: pip install psycopg2-binary")
print("2. Test connection: python test_postgresql_connection.py")
print("3. Setup database: python setup_postgresql.py")
print("4. Run application: python app.py") 