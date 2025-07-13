#!/usr/bin/env python3
"""
Migration script to transfer data from SQLite to PostgreSQL
Run this script after setting up your PostgreSQL database
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def migrate_data():
    """Migrate data from SQLite to PostgreSQL"""
    
    # SQLite connection (source)
    sqlite_engine = create_engine('sqlite:///instance/sutrabyte.db')
    # PostgreSQL connection (destination)
    if not os.environ.get('DATABASE_URL'):
        print("Error: DATABASE_URL environment variable not set")
        print("Please set your PostgreSQL connection string")
        return
    pg_engine = create_engine(os.environ.get('DATABASE_URL'))

    try:
        with pg_engine.connect() as pg_conn, sqlite_engine.connect() as sqlite_conn:
            # Test PostgreSQL connection
            pg_conn.execute(text("SELECT 1"))
            print("✅ PostgreSQL connection successful")
            # Test SQLite connection
            sqlite_conn.execute(text("SELECT 1"))
            print("✅ SQLite connection successful")
            # Get table names from SQLite
            result = sqlite_conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            tables = [row[0] for row in result]
            print(f"Found tables: {tables}")
            # Migrate each table
            for table in tables:
                if table == 'sqlite_sequence':
                    continue
                print(f"Migrating table: {table}")
                # Get data from SQLite
                data = sqlite_conn.execute(text(f"SELECT * FROM {table}"))
                columns = data.keys()
                # Insert into PostgreSQL
                for row in data:
                    values = dict(zip(columns, row))
                    placeholders = ', '.join([f':{col}' for col in columns])
                    insert_query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
                    try:
                        pg_conn.execute(text(insert_query), values)
                        except Exception as e:
                        print(f"Warning: Could not insert row in {table}: {e}")
                print(f"✅ Migrated table: {table}")
            print("🎉 Migration completed successfully!")
    except Exception as e:
        print(f"❌ Migration failed: {e}")

if __name__ == "__main__":
    print("Starting SQLite to PostgreSQL migration...")
    migrate_data() 