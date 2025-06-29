#!/usr/bin/env python3
"""
Database initialization script for SutraByte
Run this script to create all database tables and populate initial data
"""

import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, Skill, Job, JobSkill, Course, CourseSkill, IndustryTrend, SalaryImpact, Certification, Resource, Feedback
from werkzeug.security import generate_password_hash

def init_database():
    """Initialize the database with all tables and sample data"""
    with app.app_context():
        print("🔧 Database Configuration:")
        print(f"   Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        print("\n📦 Creating database tables...")
        try:
            db.create_all()
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
            print("💡 Make sure PostgreSQL is running and the database exists.")
            print("   For local development, create database: createdb sutrabyte_dev")
            return
        
        # Create admin user if environment variables are set
        admin_username = os.environ.get('ADMIN_USERNAME')
        admin_email = os.environ.get('ADMIN_EMAIL')
        admin_password = os.environ.get('ADMIN_PASSWORD')
        
        if admin_username and admin_email and admin_password:
            admin_user = User.query.filter_by(username=admin_username).first()
            if not admin_user:
                admin_user = User(username=admin_username, email=admin_email, role='admin')
                admin_user.set_password(admin_password)
                db.session.add(admin_user)
                db.session.commit()
                print(f"✅ Admin user '{admin_username}' created successfully.")
            else:
                print(f"ℹ️ Admin user '{admin_username}' already exists.")
        else:
            print("⚠️ Admin credentials not provided in environment variables.")
            print("To create admin user, set: ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD")

        # Initialize skills and jobs if they don't exist
        if not Skill.query.first():
            print("\n🎯 Creating initial skills and jobs...")
            
            # Cybersecurity Skills
            skills = [
                Skill(name='Network Security', category='Networking', 
                      description='Understanding of network protocols, firewalls, and security measures'),
                Skill(name='Penetration Testing', category='Offensive Security',
                      description='Ability to perform security assessments and vulnerability testing'),
                Skill(name='Security Operations', category='Defensive Security',
                      description='Experience with SIEM tools and security monitoring'),
                Skill(name='Incident Response', category='Defensive Security',
                      description='Handling and responding to security incidents'),
                Skill(name='Malware Analysis', category='Forensics',
                      description='Analyzing and understanding malicious software'),
                Skill(name='Cryptography', category='Security Fundamentals',
                      description='Understanding of encryption and cryptographic protocols'),
                Skill(name='Cloud Security', category='Cloud',
                      description='Security in cloud environments (AWS, Azure, GCP)'),
                Skill(name='Web Application Security', category='Application Security',
                      description='Securing web applications and APIs'),
                Skill(name='Security Compliance', category='Governance',
                      description='Understanding of security standards and compliance requirements'),
                Skill(name='Threat Intelligence', category='Intelligence',
                      description='Analyzing and understanding security threats')
            ]
            db.session.add_all(skills)
            db.session.commit()
            print("✅ Skills created successfully!")

            # Cybersecurity Jobs
            jobs = [
                Job(
                    title='Security Analyst',
                    description='Monitor and analyze security events, investigate incidents, and implement security measures.',
                    salary_range='$60,000 - $90,000',
                    category='Entry Level'
                ),
                Job(
                    title='Penetration Tester',
                    description='Perform security assessments, identify vulnerabilities, and provide remediation recommendations.',
                    salary_range='$80,000 - $120,000',
                    category='Mid Level'
                ),
                Job(
                    title='Security Engineer',
                    description='Design and implement security solutions, manage security infrastructure, and respond to incidents.',
                    salary_range='$90,000 - $130,000',
                    category='Mid Level'
                ),
                Job(
                    title='Security Architect',
                    description='Design and implement security architecture, develop security strategies, and provide technical leadership.',
                    salary_range='$120,000 - $180,000',
                    category='Senior Level'
                ),
                Job(
                    title='Security Operations Center (SOC) Manager',
                    description='Lead security operations, manage incident response, and oversee security monitoring.',
                    salary_range='$100,000 - $150,000',
                    category='Senior Level'
                )
            ]
            db.session.add_all(jobs)
            db.session.commit()
            print("✅ Jobs created successfully!")

            # Add required skills for each job
            job_skills = [
                # Security Analyst
                JobSkill(job_id=1, skill_id=1, required_proficiency=3),  # Network Security
                JobSkill(job_id=1, skill_id=3, required_proficiency=3),  # Security Operations
                JobSkill(job_id=1, skill_id=4, required_proficiency=2),  # Incident Response
                
                # Penetration Tester
                JobSkill(job_id=2, skill_id=2, required_proficiency=4),  # Penetration Testing
                JobSkill(job_id=2, skill_id=8, required_proficiency=3),  # Web Application Security
                JobSkill(job_id=2, skill_id=1, required_proficiency=3),  # Network Security
                
                # Security Engineer
                JobSkill(job_id=3, skill_id=1, required_proficiency=4),  # Network Security
                JobSkill(job_id=3, skill_id=7, required_proficiency=3),  # Cloud Security
                JobSkill(job_id=3, skill_id=3, required_proficiency=4),  # Security Operations
                
                # Security Architect
                JobSkill(job_id=4, skill_id=1, required_proficiency=5),  # Network Security
                JobSkill(job_id=4, skill_id=7, required_proficiency=4),  # Cloud Security
                JobSkill(job_id=4, skill_id=9, required_proficiency=4),  # Security Compliance
                
                # SOC Manager
                JobSkill(job_id=5, skill_id=3, required_proficiency=5),  # Security Operations
                JobSkill(job_id=5, skill_id=4, required_proficiency=4),  # Incident Response
                JobSkill(job_id=5, skill_id=10, required_proficiency=4)  # Threat Intelligence
            ]
            db.session.add_all(job_skills)
            db.session.commit()
            print("✅ Job skills created successfully!")

            # Add some sample courses
            courses = [
                Course(
                    title='Network Security Fundamentals',
                    provider='Coursera',
                    description='Learn the basics of network security, including protocols, firewalls, and security measures.',
                    level='Beginner',
                    url='https://www.coursera.org/learn/network-security'
                ),
                Course(
                    title='Ethical Hacking and Penetration Testing',
                    provider='Udemy',
                    description='Master the art of penetration testing and ethical hacking techniques.',
                    level='Intermediate',
                    url='https://www.udemy.com/course/ethical-hacking-penetration-testing'
                ),
                Course(
                    title='Cloud Security Architecture',
                    provider='AWS',
                    description='Learn to design and implement secure cloud architectures.',
                    level='Advanced',
                    url='https://aws.amazon.com/training/security'
                )
            ]
            db.session.add_all(courses)
            db.session.commit()
            print("✅ Courses created successfully!")

            # Add skills taught in courses
            course_skills = [
                CourseSkill(course_id=1, skill_id=1),  # Network Security
                CourseSkill(course_id=2, skill_id=2),  # Penetration Testing
                CourseSkill(course_id=3, skill_id=7)   # Cloud Security
            ]
            db.session.add_all(course_skills)
            db.session.commit()
            print("✅ Course skills created successfully!")

        else:
            print("ℹ️ Skills and jobs already exist, skipping initialization.")

        print("\n🎉 Database initialization completed successfully!")
        print("You can now start the application.")

if __name__ == '__main__':
    init_database() 