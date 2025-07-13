from flask import Flask, render_template, redirect, url_for, request, flash, session, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')

# Database configuration - PostgreSQL for production
if os.environ.get('DATABASE_URL'):
    # Production: Use PostgreSQL from environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    # Fallback to SQLite for local development
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sutrabyte.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Security best practice for production
app.config['SESSION_COOKIE_SECURE'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_username(username):
    """Validate username format"""
    if len(username) < 3 or len(username) > 20:
        return False, "Username must be between 3 and 20 characters"
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    
    return True, "Username is valid"

def sanitize_input(text):
    """Basic input sanitization"""
    if not text:
        return ""
    # Remove potentially dangerous characters
    return re.sub(r'[<>"\']', '', str(text).strip())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)
    experience = db.Column(db.Integer, default=0)  # Years of experience
    used = db.Column(db.Boolean, default=False)
    plain_password = db.Column(db.String(64), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

class UserSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    proficiency = db.Column(db.Integer, default=1)  # 1-5 scale
    skill = db.relationship('Skill', backref='users')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    provider = db.Column(db.String(100))
    description = db.Column(db.Text)
    level = db.Column(db.String(50))
    url = db.Column(db.String(500))

class CourseSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    skill = db.relationship('Skill', backref='courses')

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    provider = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.String(50))
    validity_period = db.Column(db.Integer)
    url = db.Column(db.String(200))

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    subsection = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20))
    duration = db.Column(db.String(50))
    content = db.Column(db.Text)
    external_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    user = db.relationship('User', backref=db.backref('feedbacks', lazy=True))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
@login_required
def resources():
    resources = Resource.query.filter_by(is_active=True).all()
    return render_template('resources.html', resources=resources)

@app.route('/resource/<int:resource_id>')
@login_required
def resource_detail(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return render_template('resource_detail.html', resource=resource)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not validate_username(username)[0]:
            flash(validate_username(username)[1], 'error')
            return render_template('register.html')
        
        if not validate_email(email):
            flash('Invalid email format', 'error')
            return render_template('register.html')
        
        if not validate_password(password)[0]:
            flash(validate_password(password)[1], 'error')
            return render_template('register.html')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        abort(403)
    
    users = User.query.all()
    skills = Skill.query.all()
    resources = Resource.query.all()
    feedbacks = Feedback.query.all()
    
    return render_template('admin/dashboard.html', 
                         users=users, 
                         skills=skills, 
                         resources=resources, 
                         feedbacks=feedbacks)

@app.route('/admin/skills/add', methods=['GET', 'POST'])
@login_required
def admin_add_skill():
    if current_user.role != 'admin':
        abort(403)
    
    if request.method == 'POST':
        name = sanitize_input(request.form.get('name'))
        category = sanitize_input(request.form.get('category'))
        description = sanitize_input(request.form.get('description'))
        
        if Skill.query.filter_by(name=name).first():
            flash('Skill already exists', 'error')
        else:
            skill = Skill(name=name, category=category, description=description)
            db.session.add(skill)
            db.session.commit()
            flash('Skill added successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_skill.html')

@app.route('/admin/resources/add', methods=['GET', 'POST'])
@login_required
def admin_add_resource():
    if current_user.role != 'admin':
        abort(403)
    
    if request.method == 'POST':
        title = sanitize_input(request.form.get('title'))
        description = sanitize_input(request.form.get('description'))
        category = sanitize_input(request.form.get('category'))
        subsection = sanitize_input(request.form.get('subsection'))
        difficulty = sanitize_input(request.form.get('difficulty'))
        duration = sanitize_input(request.form.get('duration'))
        content = sanitize_input(request.form.get('content'))
        external_url = sanitize_input(request.form.get('external_url'))
        
        resource = Resource(
            title=title,
            description=description,
            category=category,
            subsection=subsection,
            difficulty=difficulty,
            duration=duration,
            content=content,
            external_url=external_url
        )
        
        db.session.add(resource)
        db.session.commit()
        flash('Resource added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_resource.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = sanitize_input(request.form.get('name'))
        email = sanitize_input(request.form.get('email'))
        message = sanitize_input(request.form.get('message'))
        
        feedback = Feedback(name=name, email=email, message=message)
        db.session.add(feedback)
        db.session.commit()
        
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('index'))
    
    return render_template('feedback.html')

@app.route('/create-admin', methods=['GET', 'POST'])
def create_admin():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        else:
            admin = User(username=username, email=email, role='admin')
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()
            flash('Admin user created successfully!', 'success')
            return redirect(url_for('login'))
    
    return render_template('create_admin.html')

@app.route('/skill-analyzer')
@login_required
def skill_analyzer():
    skills = Skill.query.all()
    return render_template('skill_analyzer/index.html', skills=skills)

@app.route('/skill-analyzer/profile', methods=['GET', 'POST'])
@login_required
def skill_profile():
    if request.method == 'POST':
        # Handle skill profile updates
        pass
    
    user_skills = UserSkill.query.filter_by(user_id=current_user.id).all()
    all_skills = Skill.query.all()
    return render_template('skill_analyzer/profile.html', 
                         user_skills=user_skills, 
                         all_skills=all_skills)

@app.route('/blog')
@login_required
def blog():
    blogs = Blog.query.filter_by(is_active=True).order_by(Blog.created_at.desc()).all()
    return render_template('blog.html', blogs=blogs)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('blog_detail.html', blog=blog)

# Initialize database tables
@app.before_first_request
def create_tables():
    db.create_all()
    
    # Create admin user if none exists
    if not User.query.filter_by(role='admin').first():
        admin = User(
            username='admin',
            email='admin@sutrabyte.com',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)

# For Vercel deployment
app.debug = False

# Export the app for Vercel
handler = app 