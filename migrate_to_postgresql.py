#!/usr/bin/env python3
"""
Migration script to transfer data from SQLite to PostgreSQL
Run this script after setting up your PostgreSQL database
"""

import os
import sys
from datetime import datetime
import sqlite3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def migrate_to_postgresql():
    """Migrate data from SQLite to PostgreSQL"""
    
    # Check if DATABASE_URL is set
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not set!")
        print("Please set DATABASE_URL to your PostgreSQL connection string")
        return False
    
    # Check if SQLite database exists
    sqlite_db_path = 'sutrabyte.db'
    if not os.path.exists(sqlite_db_path):
        print("❌ SQLite database not found!")
        print("Make sure sutrabyte.db exists in the current directory")
        return False
    
    print("🔄 Starting migration from SQLite to PostgreSQL...")
    
    try:
        # Connect to SQLite database
        sqlite_conn = sqlite3.connect(sqlite_db_path)
        sqlite_conn.row_factory = sqlite3.Row
        sqlite_cursor = sqlite_conn.cursor()
        
        # Import Flask app and models
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import app, db, User, Skill, Job, JobSkill, Course, CourseSkill, IndustryTrend, SalaryImpact, Certification, Resource, Feedback, Blog, UserSkill, SkillProgression, UserCertification, CertificationSkill
        
        with app.app_context():
            # Create all tables in PostgreSQL
            print("📋 Creating PostgreSQL tables...")
            db.create_all()
            print("✅ PostgreSQL tables created!")
            
            # Migrate data table by table
            tables_to_migrate = [
                ('user', User),
                ('skill', Skill),
                ('job', Job),
                ('course', Course),
                ('certification', Certification),
                ('resource', Resource),
                ('feedback', Feedback),
                ('blog', Blog),
                ('user_skill', UserSkill),
                ('job_skill', JobSkill),
                ('course_skill', CourseSkill),
                ('industry_trend', IndustryTrend),
                ('salary_impact', SalaryImpact),
                ('user_certification', UserCertification),
                ('certification_skill', CertificationSkill),
                ('skill_progression', SkillProgression)
            ]
            
            for table_name, model in tables_to_migrate:
                print(f"🔄 Migrating {table_name}...")
                
                # Get data from SQLite
                sqlite_cursor.execute(f"SELECT * FROM {table_name}")
                rows = sqlite_cursor.fetchall()
                
                if rows:
                    # Convert rows to dictionaries
                    for row in rows:
                        row_dict = dict(row)
                        
                        # Handle datetime fields
                        for key, value in row_dict.items():
                            if isinstance(value, str) and 'datetime' in str(type(value)):
                                try:
                                    row_dict[key] = datetime.fromisoformat(value.replace('Z', '+00:00'))
                                except:
                                    pass
                        
                        # Create new record in PostgreSQL
                        try:
                            new_record = model(**row_dict)
                            db.session.add(new_record)
                        except Exception as e:
                            print(f"⚠️ Warning: Could not migrate record in {table_name}: {e}")
                            continue
                    
                    db.session.commit()
                    print(f"✅ Migrated {len(rows)} records from {table_name}")
                else:
                    print(f"ℹ️ No data to migrate from {table_name}")
            
            print("\n🎉 Migration completed successfully!")
            print("Your data has been transferred from SQLite to PostgreSQL")
            
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    finally:
        if 'sqlite_conn' in locals():
            sqlite_conn.close()
    
    return True

if __name__ == '__main__':
    migrate_to_postgresql() 