# PostgreSQL Migration Guide for SutraByte

This guide will help you migrate your SutraByte application from SQLite to PostgreSQL using your Render PostgreSQL database.

## Prerequisites

1. **PostgreSQL Database**: You already have a PostgreSQL database on Render with the connection string:
   ```
   postgresql://sutrabyte_admin:gikmd3YKT7lRpHqprpsNZnKBIdwXEjo7@dpg-d1gdr2vfte5s738h4ltg-a/sutrabyte_prod_mmyq
   ```

2. **Python Environment**: Make sure you have Python 3.7+ installed

## Step 1: Install New Dependencies

The following new dependencies have been added to `requirements.txt`:
- `psycopg2-binary==2.9.9` - PostgreSQL adapter for Python
- `Flask-Migrate==4.0.5` - Database migration support

Install the new dependencies:
```bash
pip install -r requirements.txt
```

## Step 2: Set Up Environment Variables

Create a `.env` file in your project root with the following content:

```env
# Database Configuration
DATABASE_URL=postgresql://sutrabyte_admin:gikmd3YKT7lRpHqprpsNZnKBIdwXEjo7@dpg-d1gdr2vfte5s738h4ltg-a/sutrabyte_prod_mmyq

# Flask Secret Key (generate a strong random key for production)
SECRET_KEY=your-secret-key-here

# Admin User Configuration (optional)
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@sutrabyte.com
ADMIN_PASSWORD=your-admin-password

# Environment
FLASK_ENV=production
```

**Important**: Replace `your-secret-key-here` with a strong random string for security.

## Step 3: Choose Your Migration Path

You have two options for setting up your PostgreSQL database:

### Option A: Fresh Setup (Recommended for new deployments)

If you don't need to preserve existing data from SQLite:

```bash
python setup_postgresql.py
```

This will:
- Create all database tables in PostgreSQL
- Initialize with sample skills, jobs, courses, and certifications
- Generate 100 pre-registered users
- Create an admin user (if environment variables are set)

### Option B: Migrate Existing Data

If you want to preserve your existing SQLite data:

```bash
python migrate_to_postgresql.py
```

This will:
- Transfer all existing data from SQLite to PostgreSQL
- Preserve all user accounts, skills, jobs, courses, etc.
- Handle data type conversions automatically

## Step 4: Test the Connection

Run your Flask application to test the PostgreSQL connection:

```bash
python app.py
```

The application should now connect to PostgreSQL instead of SQLite.

## Step 5: Verify Migration

1. **Check Database Tables**: The application should work exactly as before, but now using PostgreSQL
2. **Test User Login**: Try logging in with existing users
3. **Check Admin Panel**: Verify that all admin functions work correctly

## Step 6: Deploy to Production

When deploying to Render or other platforms:

1. **Set Environment Variables**: Make sure `DATABASE_URL` is set in your deployment environment
2. **Update Dependencies**: Ensure all new dependencies are installed
3. **Database Initialization**: Run the setup script on first deployment

## Troubleshooting

### Common Issues

1. **Connection Error**: 
   - Verify your `DATABASE_URL` is correct
   - Check if your PostgreSQL database is accessible from your deployment environment

2. **Import Errors**:
   - Make sure you've installed the new dependencies: `pip install -r requirements.txt`

3. **Data Migration Issues**:
   - If migration fails, you can run the fresh setup script instead
   - Check the console output for specific error messages

4. **Performance Issues**:
   - PostgreSQL should provide better performance than SQLite for production use
   - Consider adding database indexes for frequently queried fields

### Database Connection Testing

You can test your database connection separately:

```python
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    print("✅ Successfully connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

## Benefits of PostgreSQL

1. **Better Performance**: Optimized for concurrent access and large datasets
2. **ACID Compliance**: Full transaction support
3. **Advanced Features**: JSON support, full-text search, etc.
4. **Scalability**: Better suited for production environments
5. **Backup & Recovery**: Robust backup and recovery options

## Rollback Plan

If you need to rollback to SQLite:

1. Change the `DATABASE_URL` environment variable to `sqlite:///sutrabyte.db`
2. The application will automatically fall back to SQLite
3. Your SQLite database file should still be available

## Support

If you encounter any issues during migration:

1. Check the console output for error messages
2. Verify your environment variables are set correctly
3. Test the database connection separately
4. Consider running the fresh setup if data migration fails

---

**Note**: After successful migration, you can safely delete the `sutrabyte.db` file if you no longer need the SQLite database. 