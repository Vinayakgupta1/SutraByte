from flask import Flask, render_template, redirect, url_for, request, flash, session, abort, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')

# Mock data for demonstration
MOCK_USERS = {
    'admin': {
        'username': 'admin',
        'email': 'admin@sutrabyte.com',
        'role': 'admin',
        'password': 'admin123'  # In production, use proper hashing
    }
}

MOCK_SKILLS = [
    {'id': 1, 'name': 'Network Security', 'category': 'Cybersecurity'},
    {'id': 2, 'name': 'Penetration Testing', 'category': 'Cybersecurity'},
    {'id': 3, 'name': 'Incident Response', 'category': 'Cybersecurity'},
    {'id': 4, 'name': 'Risk Assessment', 'category': 'Cybersecurity'},
    {'id': 5, 'name': 'Security Auditing', 'category': 'Cybersecurity'}
]

MOCK_RESOURCES = [
    {
        'id': 1,
        'title': 'Getting Started with Cybersecurity',
        'description': 'Learn the basics of cybersecurity',
        'category': 'basic',
        'subsection': 'fundamentals',
        'difficulty': 'beginner',
        'duration': '30 min'
    },
    {
        'id': 2,
        'title': 'Essential Security Tools',
        'description': 'Overview of must-have security tools',
        'category': 'basic',
        'subsection': 'tools',
        'difficulty': 'beginner',
        'duration': '45 min'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    social_links = {
        'LinkedIn': 'https://www.linkedin.com/company/sutrabyte',
        'Founder LinkedIn': 'https://www.linkedin.com/in/vinayak15/',
        'Founder Portfolio': 'https://vinayakgupta15.github.io/Vinayak-Portfolio/',
        'Co-Founder LinkedIn': 'https://www.linkedin.com/in/anushika-dutta-a04959313/',
        'Co-Founder Portfolio': 'https://anushika006.github.io/Anushika-Portfolio/',
    }
    return render_template('about.html', social_links=social_links)

@app.route('/resources')
def resources():
    return render_template('resources.html', resources=MOCK_RESOURCES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in MOCK_USERS and MOCK_USERS[username]['password'] == password:
            session['user_id'] = username
            session['role'] = MOCK_USERS[username]['role']
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/admin')
def admin_dashboard():
    if session.get('role') != 'admin':
        abort(403)
    return render_template('admin/dashboard.html', users=MOCK_USERS)

@app.route('/skill-analyzer')
def skill_analyzer():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    return render_template('skill_analyzer/index.html', skills=MOCK_SKILLS)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real app, you'd save this to a database
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('index'))
    
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)

# For Vercel deployment
app.debug = False 