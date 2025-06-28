from flask import Flask, render_template, redirect, url_for, request, flash, session, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sutrabyte.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Security best practice for production
app.config['SESSION_COOKIE_SECURE'] = True

db = SQLAlchemy(app)
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
    skills = db.relationship('UserSkill', backref='user', lazy=True)
    experience = db.Column(db.Integer, default=0)  # Years of experience

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'Cybersecurity', 'Networking', etc.
    description = db.Column(db.Text)

class UserSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    proficiency = db.Column(db.Integer, default=1)  # 1-5 scale
    skill = db.relationship('Skill', backref='users')

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    required_skills = db.relationship('JobSkill', backref='job', lazy=True)
    salary_range = db.Column(db.String(50))
    category = db.Column(db.String(50))  # e.g., 'Entry Level', 'Mid Level', 'Senior'

class JobSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    required_proficiency = db.Column(db.Integer, default=1)  # 1-5 scale
    skill = db.relationship('Skill', backref='jobs')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    provider = db.Column(db.String(100))
    description = db.Column(db.Text)
    skills_taught = db.relationship('CourseSkill', backref='course', lazy=True)
    level = db.Column(db.String(50))  # e.g., 'Beginner', 'Intermediate', 'Advanced'
    url = db.Column(db.String(500))

class CourseSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    skill = db.relationship('Skill', backref='courses')

class SkillProgression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    date_recorded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('skill_progressions', lazy=True))
    skill = db.relationship('Skill', backref=db.backref('progressions', lazy=True))

class IndustryTrend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    demand_level = db.Column(db.Integer, nullable=False)  # 1-5 scale
    trend_direction = db.Column(db.String(20), nullable=False)  # 'increasing', 'stable', 'decreasing'
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    skill = db.relationship('Skill', backref=db.backref('industry_trends', lazy=True))

class SalaryImpact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    impact_percentage = db.Column(db.Float, nullable=False)  # Percentage impact on salary
    min_salary = db.Column(db.Float, nullable=False)
    max_salary = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    skill = db.relationship('Skill', backref=db.backref('salary_impacts', lazy=True))

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    provider = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.String(50))  # beginner, intermediate, advanced
    validity_period = db.Column(db.Integer)  # in months
    url = db.Column(db.String(200))

class UserCertification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    certification_id = db.Column(db.Integer, db.ForeignKey('certification.id'), nullable=False)
    date_obtained = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime)
    verification_url = db.Column(db.String(200))
    
    user = db.relationship('User', backref=db.backref('certifications', lazy=True))
    certification = db.relationship('Certification', backref=db.backref('user_certifications', lazy=True))

class CertificationSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certification_id = db.Column(db.Integer, db.ForeignKey('certification.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    proficiency_level = db.Column(db.Integer, nullable=False)  # 1-5 scale
    
    certification = db.relationship('Certification', backref=db.backref('certification_skills', lazy=True))
    skill = db.relationship('Skill', backref=db.backref('certification_skills', lazy=True))

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)  # 'basic', 'advanced', 'quiz', 'challenge'
    subsection = db.Column(db.String(100), nullable=False)  # e.g., 'fundamentals', 'tools', 'practices'
    difficulty = db.Column(db.String(20))  # 'beginner', 'intermediate', 'advanced'
    duration = db.Column(db.String(50))  # e.g., '30 min', '2 hours', '45 days'
    content = db.Column(db.Text)  # Detailed content for the resource
    external_url = db.Column(db.String(500))  # Optional external link
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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
    # Get resources organized by category and subsection
    basic_resources = Resource.query.filter_by(category='basic', is_active=True).order_by(Resource.subsection, Resource.title).all()
    advanced_resources = Resource.query.filter_by(category='advanced', is_active=True).order_by(Resource.subsection, Resource.title).all()
    quizzes = Resource.query.filter_by(category='quiz', is_active=True).order_by(Resource.title).all()
    challenges = Resource.query.filter_by(category='challenge', is_active=True).order_by(Resource.title).all()
    
    return render_template('resources.html', 
                         basic_resources=basic_resources,
                         advanced_resources=advanced_resources,
                         quizzes=quizzes,
                         challenges=challenges)

@app.route('/resource/<int:resource_id>')
@login_required
def resource_detail(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return render_template('resource_detail.html', resource=resource)

@app.route('/resources/<category>')
@login_required
def resources_by_category(category):
    if category not in ['basic', 'advanced', 'quiz', 'challenge']:
        abort(404)
    
    resources = Resource.query.filter_by(category=category, is_active=True).order_by(Resource.subsection, Resource.title).all()
    return render_template('resources_category.html', resources=resources, category=category)

@app.route('/blog')
@login_required
def blog():
    return render_template('blog.html')

@app.route('/blog/getting-started')
@login_required
def blog_getting_started():
    return render_template('blog-getting-started.html')

@app.route('/blog/top-5-tools')
@login_required
def blog_top_5_tools():
    return render_template('blog-top-5-tools.html')

@app.route('/blog/practice-safely')
@login_required
def blog_practice_safely():
    return render_template('blog-practice-safely.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Sanitize inputs
        username = sanitize_input(request.form.get('username', ''))
        email = sanitize_input(request.form.get('email', ''))
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validate inputs
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return render_template('register.html')
        
        # Validate username
        username_valid, username_msg = validate_username(username)
        if not username_valid:
            flash(username_msg, 'error')
            return render_template('register.html')
        
        # Validate email
        if not validate_email(email):
            flash('Please enter a valid email address.', 'error')
            return render_template('register.html')
        
        # Validate password
        password_valid, password_msg = validate_password(password)
        if not password_valid:
            flash(password_msg, 'error')
            return render_template('register.html')
        
        # Check password confirmation
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('register.html')
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('register.html')
        
        # Create user
        try:
            user = User(username=username, email=email, role='student')
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return render_template('register.html')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Sanitize inputs
        username = sanitize_input(request.form.get('username', ''))
        password = request.form.get('password', '')
        
        # Validate inputs
        if not username or not password:
            flash('Please enter both username and password.', 'error')
            return render_template('login.html')
        
        try:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect(url_for('index'))
            else:
                # Don't reveal whether username or password is wrong
                flash('Invalid username or password.', 'error')
        except Exception as e:
            flash('Login failed. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

# Example of a protected route for admins only
@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    users = User.query.order_by(User.registered_on.desc()).all()
    return render_template('admin.html', users=users)

@app.route('/create-admin', methods=['GET', 'POST'])
def create_admin():
    """Secure admin creation route - only accessible with secret token"""
    secret_token = os.environ.get('ADMIN_CREATION_TOKEN')
    
    if not secret_token:
        flash('Admin creation is not configured.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        provided_token = request.form.get('token', '')
        username = sanitize_input(request.form.get('username', ''))
        email = sanitize_input(request.form.get('email', ''))
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validate token
        if provided_token != secret_token:
            flash('Invalid admin creation token.', 'error')
            return render_template('create_admin.html')
        
        # Validate inputs
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return render_template('create_admin.html')
        
        # Validate username
        username_valid, username_msg = validate_username(username)
        if not username_valid:
            flash(username_msg, 'error')
            return render_template('create_admin.html')
        
        # Validate email
        if not validate_email(email):
            flash('Please enter a valid email address.', 'error')
            return render_template('create_admin.html')
        
        # Validate password
        password_valid, password_msg = validate_password(password)
        if not password_valid:
            flash(password_msg, 'error')
            return render_template('create_admin.html')
        
        # Check password confirmation
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('create_admin.html')
        
        # Check if admin already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('create_admin.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('create_admin.html')
        
        # Create admin user
        try:
            admin_user = User(username=username, email=email, role='admin')
            admin_user.set_password(password)
            db.session.add(admin_user)
            db.session.commit()
            flash('Admin user created successfully. You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Admin creation failed. Please try again.', 'error')
            return render_template('create_admin.html')
    
    return render_template('create_admin.html')

# Skill Analyzer Routes
@app.route('/skill-analyzer')
@login_required
def skill_analyzer():
    return render_template('skill_analyzer/index.html')

@app.route('/skill-analyzer/profile', methods=['GET', 'POST'])
@login_required
def skill_profile():
    if request.method == 'POST':
        # Update user experience
        experience = request.form.get('experience', type=int)
        if experience is not None:
            current_user.experience = experience
        
        # Update skills
        skills = request.form.getlist('skills')
        proficiencies = request.form.getlist('proficiencies')
        
        # Clear existing skills
        UserSkill.query.filter_by(user_id=current_user.id).delete()
        
        # Add new skills
        for skill_name, proficiency in zip(skills, proficiencies):
            skill = Skill.query.filter_by(name=skill_name).first()
            if skill:
                user_skill = UserSkill(
                    user_id=current_user.id,
                    skill_id=skill.id,
                    proficiency=int(proficiency)
                )
                db.session.add(user_skill)
        
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('skill_recommendations'))
    
    # Get all available skills
    all_skills = Skill.query.all()
    # Get user's current skills
    user_skills = UserSkill.query.filter_by(user_id=current_user.id).all()
    
    return render_template('skill_analyzer/profile.html', 
                         all_skills=all_skills,
                         user_skills=user_skills)

def calculate_skill_match_score(user_skills, required_skills):
    """Calculate a weighted match score between user skills and required skills."""
    total_weight = 0
    matched_weight = 0
    
    for req_skill in required_skills:
        weight = req_skill.required_proficiency  # Higher proficiency requirements have more weight
        total_weight += weight
        
        if req_skill.skill_id in user_skills:
            user_proficiency = user_skills[req_skill.skill_id]
            if user_proficiency >= req_skill.required_proficiency:
                matched_weight += weight
            else:
                # Partial credit for having the skill but not at required level
                matched_weight += (user_proficiency / req_skill.required_proficiency) * weight
    
    return (matched_weight / total_weight) * 100 if total_weight > 0 else 0

def get_skill_category_gaps(user_skills):
    """Analyze skill gaps by category."""
    all_skills = Skill.query.all()
    categories = {}
    
    for skill in all_skills:
        if skill.category not in categories:
            categories[skill.category] = {
                'total_skills': 0,
                'user_skills': 0,
                'avg_proficiency': 0
            }
        
        categories[skill.category]['total_skills'] += 1
        if skill.id in user_skills:
            categories[skill.category]['user_skills'] += 1
            categories[skill.category]['avg_proficiency'] += user_skills[skill.id]
    
    # Calculate averages and identify weak categories
    weak_categories = []
    for category, stats in categories.items():
        if stats['total_skills'] > 0:
            stats['coverage'] = (stats['user_skills'] / stats['total_skills']) * 100
            if stats['user_skills'] > 0:
                stats['avg_proficiency'] /= stats['user_skills']
            if stats['coverage'] < 50 or stats['avg_proficiency'] < 3:
                weak_categories.append(category)
    
    return categories, weak_categories

def get_personalized_course_recommendations(user_skills, missing_skills, weak_categories):
    """Get personalized course recommendations based on skill gaps and weak categories."""
    recommended_courses = []
    
    # First, recommend courses for missing skills
    for skill_name in missing_skills:
        skill = Skill.query.filter_by(name=skill_name).first()
        if skill:
            courses = Course.query.join(CourseSkill).filter(
                CourseSkill.skill_id == skill.id
            ).order_by(Course.level).all()
            recommended_courses.extend(courses)
    
    # Then, recommend courses for weak categories
    for category in weak_categories:
        category_skills = Skill.query.filter_by(category=category).all()
        for skill in category_skills:
            if skill.id not in user_skills or user_skills[skill.id] < 3:
                courses = Course.query.join(CourseSkill).filter(
                    CourseSkill.skill_id == skill.id
                ).order_by(Course.level).all()
                recommended_courses.extend(courses)
    
    # Remove duplicates and sort by relevance
    unique_courses = {}
    for course in recommended_courses:
        if course.id not in unique_courses:
            unique_courses[course.id] = {
                'course': course,
                'relevance_score': 0
            }
        unique_courses[course.id]['relevance_score'] += 1
    
    return sorted(unique_courses.values(), 
                 key=lambda x: x['relevance_score'], 
                 reverse=True)

@app.route('/skill-analyzer/recommendations')
@login_required
def skill_recommendations():
    # Get user's skills and their proficiencies
    user_skills = UserSkill.query.filter_by(user_id=current_user.id).all()
    user_skill_ids = {us.skill_id: us.proficiency for us in user_skills}
    
    # Get skill category analysis
    categories, weak_categories = get_skill_category_gaps(user_skill_ids)
    
    # Get industry trends
    industry_trends = get_industry_trends()
    
    # Calculate salary impact
    salary_impact, skill_impacts = calculate_salary_impact(user_skill_ids)
    
    # Get recommended certifications
    recommended_certs = get_recommended_certifications(user_skills)
    
    # Find matching jobs with improved scoring
    matching_jobs = []
    all_jobs = Job.query.all()
    
    for job in all_jobs:
        required_skills = JobSkill.query.filter_by(job_id=job.id).all()
        missing_skills = []
        matching_skills = []
        
        for req_skill in required_skills:
            if req_skill.skill_id in user_skill_ids:
                if user_skill_ids[req_skill.skill_id] >= req_skill.required_proficiency:
                    matching_skills.append(req_skill.skill.name)
                else:
                    missing_skills.append(req_skill.skill.name)
            else:
                missing_skills.append(req_skill.skill.name)
        
        if matching_skills:
            match_score = calculate_skill_match_score(user_skill_ids, required_skills)
            matching_jobs.append({
                'job': job,
                'matching_skills': matching_skills,
                'missing_skills': missing_skills,
                'match_score': match_score
            })
    
    # Sort jobs by match score
    matching_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    
    # Get personalized course recommendations
    missing_skills = set()
    for job_match in matching_jobs:
        missing_skills.update(job_match['missing_skills'])
    
    recommended_courses = get_personalized_course_recommendations(
        user_skill_ids, 
        missing_skills,
        weak_categories
    )
    
    return render_template('skill_analyzer/recommendations.html',
                         matching_jobs=matching_jobs,
                         recommended_courses=[item['course'] for item in recommended_courses],
                         categories=categories,
                         weak_categories=weak_categories,
                         industry_trends=industry_trends,
                         salary_impact=salary_impact,
                         skill_impacts=skill_impacts,
                         recommended_certs=recommended_certs)

@app.route('/skill-analyzer/progression/<int:skill_id>')
@login_required
def skill_progression(skill_id):
    progression_history = get_skill_progression_history(current_user.id, skill_id)
    skill = Skill.query.get_or_404(skill_id)
    
    return render_template('skill_analyzer/progression.html',
                         skill=skill,
                         progression_history=progression_history)

def update_skill_progression(user_id, skill_id, new_proficiency):
    """Record a user's skill progression."""
    progression = SkillProgression(
        user_id=user_id,
        skill_id=skill_id,
        proficiency=new_proficiency
    )
    db.session.add(progression)
    db.session.commit()

def get_skill_progression_history(user_id, skill_id):
    """Get the progression history for a specific skill."""
    return SkillProgression.query.filter_by(
        user_id=user_id,
        skill_id=skill_id
    ).order_by(SkillProgression.date_recorded).all()

def calculate_salary_impact(user_skills):
    """Calculate the potential salary impact of user's skills."""
    total_impact = 0
    skill_impacts = []
    
    for skill_id, proficiency in user_skills.items():
        impact = SalaryImpact.query.filter_by(skill_id=skill_id).first()
        if impact:
            # Weight the impact by proficiency level
            weighted_impact = impact.impact_percentage * (proficiency / 5)
            total_impact += weighted_impact
            skill_impacts.append({
                'skill': Skill.query.get(skill_id).name,
                'impact': weighted_impact,
                'min_salary': impact.min_salary,
                'max_salary': impact.max_salary
            })
    
    return total_impact, skill_impacts

def get_industry_trends():
    """Get current industry trends for skills."""
    trends = IndustryTrend.query.order_by(IndustryTrend.demand_level.desc()).all()
    return [{
        'skill': trend.skill.name,
        'demand_level': trend.demand_level,
        'trend_direction': trend.trend_direction,
        'last_updated': trend.last_updated
    } for trend in trends]

def get_recommended_certifications(user_skills):
    # Get user's skill IDs
    user_skill_ids = [skill.skill_id for skill in user_skills]
    
    # Find certifications that teach skills the user doesn't have or has low proficiency in
    recommended_certs = []
    
    all_certifications = Certification.query.all()
    for cert in all_certifications:
        cert_skills = CertificationSkill.query.filter_by(certification_id=cert.id).all()
        
        # Calculate how many skills from this certification the user needs
        needed_skills = 0
        total_skills = len(cert_skills)
        
        for cert_skill in cert_skills:
            user_skill = next((us for us in user_skills if us.skill_id == cert_skill.skill_id), None)
            if not user_skill or user_skill.proficiency < cert_skill.proficiency_level:
                needed_skills += 1
        
        if needed_skills > 0:
            relevance_score = needed_skills / total_skills
            recommended_certs.append({
                'certification': cert,
                'relevance_score': relevance_score,
                'needed_skills': needed_skills,
                'total_skills': total_skills
            })
    
    # Sort by relevance score
    recommended_certs.sort(key=lambda x: x['relevance_score'], reverse=True)
    return recommended_certs[:5]

def populate_initial_resources():
    """Populate the database with initial cybersecurity resources"""
    if Resource.query.first():
        return  # Already populated
    
    resources_data = [
        # Basic Resources - Fundamentals
        {
            'title': 'Cybersecurity Fundamentals',
            'description': 'Understand the basics: what is cybersecurity, why it matters, and key concepts every beginner should know.',
            'category': 'basic',
            'subsection': 'fundamentals',
            'difficulty': 'beginner',
            'duration': '30 min',
            'content': '''
# Cybersecurity Fundamentals

## What is Cybersecurity?
Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks.

## Why Cybersecurity Matters
- Personal Protection
- Business Security
- National Security
- Economic Impact

## Key Concepts
- **Confidentiality:** Ensuring information is accessible only to those authorized
- **Integrity:** Maintaining accuracy and completeness of data
- **Availability:** Ensuring authorized users have access when needed

## Types of Threats
- Malware
- Phishing
- Ransomware
- Social Engineering

## Basic Protection Measures
- Use strong, unique passwords
- Enable two-factor authentication
- Keep software updated
- Be cautious with email attachments and links
- Use antivirus software
- Regular data backups
'''
        },
        {
            'title': 'Safe Internet Habits',
            'description': 'Practical tips for staying safe online, protecting your accounts, and avoiding common threats.',
            'category': 'basic',
            'subsection': 'practices',
            'difficulty': 'beginner',
            'duration': '45 min',
            'content': '''
# Safe Internet Habits

## Password Security
- Use at least 12 characters
- Include uppercase, lowercase, numbers, and symbols
- Use unique passwords for each account

## Email Security
- Check sender email addresses carefully
- Look for urgent or threatening language
- Verify links before clicking

## Social Media Safety
- Review and adjust privacy settings regularly
- Limit personal information sharing

## Online Shopping Security
- Shop only on secure websites (HTTPS)
- Use credit cards with fraud protection

## Mobile Device Security
- Use screen locks and biometric authentication
- Keep apps updated
'''
        },
        {
            'title': 'Essential Security Tools',
            'description': 'Intro to password managers, VPNs, antivirus, and other must-have tools for digital safety.',
            'category': 'basic',
            'subsection': 'tools',
            'difficulty': 'beginner',
            'duration': '60 min',
            'content': '''
# Essential Security Tools

## Password Managers
- Bitwarden, 1Password, LastPass

## VPNs
- NordVPN, ExpressVPN, ProtonVPN

## Antivirus Software
- Windows Defender, Malwarebytes, Bitdefender

## Two-Factor Authentication (2FA)
- Authenticator apps, hardware tokens

## File Encryption Tools
- VeraCrypt, 7-Zip, BitLocker

## Browser Security Extensions
- uBlock Origin, HTTPS Everywhere, Privacy Badger
'''
        },
        # Advanced Resources
        {
            'title': 'Network Security Fundamentals',
            'description': 'Learn about network protocols, firewalls, and basic network security concepts.',
            'category': 'advanced',
            'subsection': 'networking',
            'difficulty': 'intermediate',
            'duration': '2 hours',
            'content': '''
# Network Security Fundamentals

## Understanding Networks
- LAN, WAN, VPN

## Network Protocols
- TCP/IP, HTTP/HTTPS, FTP, SMTP, DNS, DHCP

## Network Security Threats
- MITM, DNS Spoofing, ARP Spoofing, Packet Sniffing, DDoS

## Firewalls
- Packet Filtering, Stateful Inspection, Application Layer, Next-Gen

## Network Monitoring
- Wireshark, Nmap, tcpdump, Netstat

## Wireless Security
- WEP, WPA, WPA2, WPA3

## Network Segmentation
- VLANs, Subnets, DMZ
'''
        },
        {
            'title': 'Web Application Security',
            'description': 'Understanding common web vulnerabilities and security best practices.',
            'category': 'advanced',
            'subsection': 'web-security',
            'difficulty': 'intermediate',
            'duration': '3 hours',
            'content': '''
# Web Application Security

## Common Web Vulnerabilities
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Authentication Vulnerabilities
- Authorization Flaws

## Security Headers
- Content Security Policy (CSP)
- HTTP Strict Transport Security (HSTS)
- X-Frame-Options
- X-Content-Type-Options

## Input Validation and Sanitization
- Length limits, character sets, format validation

## Secure Development Practices
- Follow OWASP guidelines
- Use secure coding standards
- Regular code reviews
'''
        },
        # Quiz
        {
            'title': 'Network Security Basics Quiz',
            'description': 'Test your knowledge of network protocols, firewalls, and basic network security concepts.',
            'category': 'quiz',
            'subsection': 'weekly',
            'difficulty': 'beginner',
            'duration': '15 min',
            'content': '''
# Network Security Basics Quiz

### 1. What does TCP/IP stand for?
A) Transmission Control Protocol/Internet Protocol  
B) Transfer Control Protocol/Internet Protocol  
C) Transmission Control Program/Internet Program  
D) Transfer Control Program/Internet Program  
**Answer:** A

### 2. Which of the following is NOT a common network security threat?
A) Man-in-the-Middle attacks  
B) DNS Spoofing  
C) Packet Sniffing  
D) CPU Overheating  
**Answer:** D

### 3. What is the primary purpose of a firewall?
A) To speed up internet connection  
B) To monitor and control network traffic  
C) To store network data  
D) To provide wireless connectivity  
**Answer:** B

### 4. Which Wi-Fi security protocol is considered the most secure?
A) WEP  
B) WPA  
C) WPA2  
D) WPA3  
**Answer:** D

### 5. What does HTTPS stand for?
A) HyperText Transfer Protocol Secure  
B) HyperText Transfer Protocol Standard  
C) HyperText Transfer Protocol System  
D) HyperText Transfer Protocol Service  
**Answer:** A
'''
        },
        # Challenge
        {
            'title': '45 Days of Cybersecurity Challenge',
            'description': 'A complete, detailed, and visually structured 45-day roadmap to build your cybersecurity skills from scratch to advanced topics, with daily topics, learning resources, and actionable tasks.',
            'category': 'challenge',
            'subsection': 'daily',
            'difficulty': 'all-levels',
            'duration': '45 days',
            'content': '''
# 45 Days of Cybersecurity Challenge: Complete Roadmap

Welcome to your **45-day journey** to cybersecurity mastery! Each day has a focused topic, learning resources, and a practical task. **Check off each day and build your skills step by step!**

---

## 🟠 Week 1: Cybersecurity Foundations

### Day 1: Introduction to Cybersecurity
**Topics to Learn:**
- What is cybersecurity?
- Why is it important?
- Key terms: threat, vulnerability, risk
**Learn:**
- [Cybersecurity Basics (YouTube)](https://www.youtube.com/watch?v=inWWhr5tnEA)
- [What is Cybersecurity? (CISA)](https://www.cisa.gov/news-events/news/what-cybersecurity)
**Task:** Write down 3 reasons why cybersecurity matters to you.

### Day 2: Types of Cyber Threats
**Topics to Learn:**
- Malware, phishing, ransomware, social engineering
**Learn:**
- [Types of Cyber Threats (Kaspersky)](https://www.kaspersky.com/resource-center/threats)
**Task:** Find a recent news article about a cyberattack and summarize it.

### Day 3: The CIA Triad
**Topics to Learn:**
- Confidentiality, Integrity, Availability
**Learn:**
- [CIA Triad Explained](https://www.csoonline.com/article/3519908/what-is-the-cia-triad.html)
**Task:** Write a real-life example for each part of the triad.

### Day 4: Password Security
**Topics to Learn:**
- What makes a strong password?
- Password managers
**Learn:**
- [Password Security Tips (NIST)](https://www.nist.gov/blogs/taking-measure/passwords)
- [Best Password Managers (PCMag)](https://www.pcmag.com/picks/the-best-password-managers)
**Task:** Use a password manager to generate and store a new password.

### Day 5: Two-Factor Authentication (2FA)
**Topics to Learn:**
- What is 2FA?
- Types of 2FA (SMS, app, hardware)
**Learn:**
- [What is 2FA? (CISA)](https://www.cisa.gov/news-events/news/multi-factor-authentication)
**Task:** Enable 2FA on one of your accounts.

### Day 6: Safe Internet Habits
**Topics to Learn:**
- Recognizing phishing emails
- Safe browsing
**Learn:**
- [Google Phishing Quiz](https://phishingquiz.withgoogle.com/)
- [Staying Safe Online (StaySafeOnline)](https://staysafeonline.org/stay-safe-online/)
**Task:** Take the phishing quiz and share your score.

### Day 7: Backups and Data Protection
**Topics to Learn:**
- Why backups matter
- Backup strategies (cloud, local)
**Learn:**
- [How to Back Up Your Computer (HowToGeek)](https://www.howtogeek.com/242428/whats-the-best-way-to-back-up-my-computer/)
**Task:** Set up an automatic backup for your important files.

---

## 🟡 Week 2: Networking & Network Security

### Day 8: Networking Basics
**Topics to Learn:**
- What is a network? LAN, WAN, VPN
**Learn:**
- [Networking Basics (Cisco)](https://www.cisco.com/c/en/us/products/switches/what-is-a-network.html)
**Task:** Draw a simple home/office network diagram.

### Day 9: Network Protocols
**Topics to Learn:**
- TCP/IP, HTTP, HTTPS, DNS, DHCP
**Learn:**
- [TCP/IP Explained (YouTube)](https://www.youtube.com/watch?v=3E5b5Qk8mZc)
**Task:** Use `ping` and `tracert` commands on your computer.

### Day 10: Firewalls
**Topics to Learn:**
- Types of firewalls
- How firewalls work
**Learn:**
- [What is a Firewall? (Kaspersky)](https://www.kaspersky.com/resource-center/definitions/firewall)
**Task:** Check your OS firewall settings and ensure it's enabled.

### Day 11: Wi-Fi Security
**Topics to Learn:**
- WPA2/WPA3
- Risks of public Wi-Fi
**Learn:**
- [Wi-Fi Security Tips (FTC)](https://consumer.ftc.gov/articles/how-secure-your-home-wi-fi-network)
**Task:** Change your Wi-Fi password to something strong.

### Day 12: VPNs (Virtual Private Networks)
**Topics to Learn:**
- What is a VPN?
- When to use a VPN
**Learn:**
- [What is a VPN? (Cloudflare)](https://www.cloudflare.com/learning/privacy/what-is-a-vpn/)
**Task:** Try a free VPN or research reputable VPN providers.

### Day 13: Network Attacks
**Topics to Learn:**
- MITM, DDoS, ARP/DNS spoofing
**Learn:**
- [Common Network Attacks (Imperva)](https://www.imperva.com/learn/application-security/cyber-attacks/)
**Task:** Watch a YouTube demo of a network attack (e.g., MITM).

### Day 14: Network Monitoring Tools
**Topics to Learn:**
- Wireshark, Nmap basics
**Learn:**
- [Wireshark Tutorial (YouTube)](https://www.youtube.com/watch?v=TkCSr30UojM)
**Task:** Download Wireshark and capture your own network traffic (just observe, don't analyze private data).

---

## 🟢 Week 3: System & Endpoint Security

### Day 15: Operating System Security
**Topics to Learn:**
- Windows, Linux, macOS security basics
**Learn:**
- [Windows Security Basics (Microsoft)](https://support.microsoft.com/en-us/windows/windows-security-help-5fae0b8b-4b7b-4e0e-9b7b-6b7e3b5c5b8e)
**Task:** Update your OS and review security settings.

### Day 16: Antivirus & Anti-malware
**Topics to Learn:**
- How antivirus works
- Best practices
**Learn:**
- [How Antivirus Works (HowStuffWorks)](https://computer.howstuffworks.com/virus-detection.htm)
**Task:** Run a full antivirus scan on your device.

### Day 17: Secure Software Installation
**Topics to Learn:**
- Dangers of pirated/cracked software
**Learn:**
- [Risks of Pirated Software (Microsoft)](https://www.microsoft.com/en-us/safety/pc-security/piracy.aspx)
**Task:** Uninstall any untrusted or unused software.

### Day 18: Mobile Device Security
**Topics to Learn:**
- Mobile threats
- App permissions
**Learn:**
- [Mobile Security Tips (Kaspersky)](https://www.kaspersky.com/resource-center/preemptive-safety/mobile-security-tips)
**Task:** Review app permissions on your phone and remove unnecessary apps.

### Day 19: Browser Security
**Topics to Learn:**
- Secure browser settings
- Privacy extensions
**Learn:**
- [Browser Security (Mozilla)](https://support.mozilla.org/en-US/products/firefox/protect-your-privacy)
**Task:** Install privacy extensions (uBlock Origin, HTTPS Everywhere).

### Day 20: Social Engineering
**Topics to Learn:**
- What is social engineering?
- Common tactics
**Learn:**
- [Social Engineering (Imperva)](https://www.imperva.com/learn/application-security/social-engineering-attack/)
**Task:** Share a social engineering story with a friend/family.

### Day 21: Physical Security
**Topics to Learn:**
- Why physical access matters
**Learn:**
- [Physical Security (CISA)](https://www.cisa.gov/news-events/news/physical-security)
**Task:** Secure your workspace and devices physically.

---

## 🔵 Week 4: Web & Application Security

### Day 22: Web Application Basics
**Topics to Learn:**
- How websites work
- Client/server model
**Learn:**
- [How Websites Work (MDN)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
**Task:** Use browser dev tools to inspect a website.

### Day 23: Common Web Vulnerabilities
**Topics to Learn:**
- OWASP Top 10 (SQLi, XSS, CSRF, etc.)
**Learn:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
**Task:** Watch a video on SQL Injection or XSS.

### Day 24: Secure Authentication
**Topics to Learn:**
- Password policies
- Session management
**Learn:**
- [Authentication Best Practices (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
**Task:** Review your accounts for weak or reused passwords.

### Day 25: HTTPS & Certificates
**Topics to Learn:**
- What is HTTPS?
- How SSL/TLS works
**Learn:**
- [What is HTTPS? (Cloudflare)](https://www.cloudflare.com/learning/ssl/what-is-https/)
**Task:** Check if your favorite sites use HTTPS.

### Day 26: Cookies & Privacy
**Topics to Learn:**
- What are cookies?
- Privacy risks
**Learn:**
- [Cookies and Privacy (AllAboutCookies)](https://www.allaboutcookies.org/)
**Task:** Clear cookies and set browser to block third-party cookies.

### Day 27: Secure Coding Principles
**Topics to Learn:**
- Input validation
- Least privilege
- Error handling
**Learn:**
- [Secure Coding (OWASP)](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
**Task:** Try a simple secure coding exercise (e.g., input validation in Python).

### Day 28: Bug Bounty & Responsible Disclosure
**Topics to Learn:**
- What is a bug bounty?
- How to report vulnerabilities
**Learn:**
- [Bug Bounty Platforms (HackerOne)](https://www.hackerone.com/)
**Task:** Read a real bug bounty write-up.

---

## 🟣 Week 5: Advanced Topics & Hands-On Practice

### Day 29: Cryptography Basics
**Topics to Learn:**
- Encryption, hashing, symmetric/asymmetric crypto
**Learn:**
- [Cryptography Basics (YouTube)](https://www.youtube.com/watch?v=6VqTfR3p9Jw)
**Task:** Use an online tool to hash a string (e.g., SHA-256).

### Day 30: Public Key Infrastructure (PKI)
**Topics to Learn:**
- Certificates, CAs, digital signatures
**Learn:**
- [What is PKI? (SSL.com)](https://www.ssl.com/faqs/what-is-pki/)
**Task:** View a website's certificate details in your browser.

### Day 31: Digital Forensics
**Topics to Learn:**
- What is digital forensics?
- Basic tools
**Learn:**
- [Digital Forensics (Cybrary)](https://www.cybrary.it/course/digital-forensics/)
**Task:** Try a free forensic tool (e.g., Autopsy).

### Day 32: Incident Response
**Topics to Learn:**
- Steps in incident response
**Learn:**
- [Incident Response (CISA)](https://www.cisa.gov/news-events/news/incident-response)
**Task:** Write a simple incident response plan for your home or office.

### Day 33: Security Policies & Compliance
**Topics to Learn:**
- What are security policies?
- GDPR, HIPAA, etc.
**Learn:**
- [Security Policies (SANS)](https://www.sans.org/information-security-policy/)
**Task:** Find out if your workplace/school has a security policy.

### Day 34: Cloud Security
**Topics to Learn:**
- Cloud risks
- Shared responsibility model
**Learn:**
- [Cloud Security (AWS)](https://aws.amazon.com/what-is/cloud-security/)
**Task:** List cloud services you use and their security features.

### Day 35: IoT Security
**Topics to Learn:**
- Risks of smart devices
**Learn:**
- [IoT Security (Kaspersky)](https://www.kaspersky.com/resource-center/threats/internet-of-things)
**Task:** Secure your home IoT device (change default password, update firmware).

---

## 🟤 Week 6: Real-World Scenarios & Career Prep

### Day 36: Penetration Testing Basics
**Topics to Learn:**
- What is pentesting?
- Phases of a pentest
**Learn:**
- [Penetration Testing (OWASP)](https://owasp.org/www-community/penetration-testing/)
**Task:** Try a free pentesting lab (e.g., TryHackMe, Hack The Box).

### Day 37: Capture The Flag (CTF) Challenges
**Topics to Learn:**
- What is a CTF?
- Types of challenges
**Learn:**
- [CTF Guide (CTFtime)](https://ctftime.org/ctf-wiki/)
**Task:** Register for a beginner CTF or try a CTF challenge online.

### Day 38: Security Tools Overview
**Topics to Learn:**
- Nmap, Metasploit, Burp Suite, John the Ripper
**Learn:**
- [Top Security Tools (OWASP)](https://owasp.org/www-community/Vulnerability_Scanning_Tools)
**Task:** Watch a demo of one tool in action.

### Day 39: Security Certifications
**Topics to Learn:**
- CompTIA Security+, CEH, CISSP, etc.
**Learn:**
- [Security Certifications (CompTIA)](https://www.comptia.org/certifications/security)
**Task:** Research which certification fits your goals.

### Day 40: Cybersecurity Careers
**Topics to Learn:**
- Roles (SOC analyst, pentester, auditor, etc.)
**Learn:**
- [Cybersecurity Careers (CyberSeek)](https://www.cyberseek.org/pathway.html)
**Task:** List 3 cybersecurity jobs that interest you.

### Day 41: Building a Cybersecurity Lab
**Topics to Learn:**
- How to set up a home lab (VMs, tools)
**Learn:**
- [Home Lab Guide (Reddit)](https://www.reddit.com/r/homelab/wiki/index/)
**Task:** Set up a virtual machine for testing.

### Day 42: Security Communities & Networking
**Topics to Learn:**
- Online forums, local meetups, conferences
**Learn:**
- [Cybersecurity Communities (Reddit)](https://www.reddit.com/r/cybersecurity/)
**Task:** Join a cybersecurity community (Discord, Reddit, etc.).

### Day 43: Review & Reflect
**Topics to Learn:**
- Review your notes and progress
**Learn:**
- [Cybersecurity News (KrebsOnSecurity)](https://krebsonsecurity.com/)
**Task:** Write down your top 5 takeaways from this challenge.

### Day 44: Final Assessment
**Topics to Learn:**
- Take a free online cybersecurity quiz or assessment
**Learn:**
- [Cybersecurity Quiz (Cybrary)](https://www.cybrary.it/quiz/)
**Task:** Identify your strengths and areas for improvement.

### Day 45: Next Steps
**Topics to Learn:**
- How to keep learning and growing
**Learn:**
- [Continuous Learning (SANS)](https://www.sans.org/cyber-security-courses/)
**Task:** Set your next cybersecurity goal and plan your continued learning journey.

---

**Congratulations!** 🎉 You've completed the 45 Days of Cybersecurity Challenge. Share your journey, help others, and keep building your skills!
'''
        },
    ]
    
    for resource_data in resources_data:
        resource = Resource(**resource_data)
        db.session.add(resource)
    
    db.session.commit()

@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    # Get statistics
    total_users = User.query.count()
    total_skills = Skill.query.count()
    total_jobs = Job.query.count()
    total_courses = Course.query.count()
    total_resources = Resource.query.count()
    
    # Get all users with their skills
    users = User.query.all()
    
    # Get all skills with their trends
    skills = Skill.query.all()
    
    # Get all certifications
    certifications = Certification.query.all()
    
    # Get all courses
    courses = Course.query.all()
    
    # Get all resources
    resources = Resource.query.order_by(Resource.category, Resource.subsection, Resource.title).all()
    
    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_skills=total_skills,
                         total_jobs=total_jobs,
                         total_courses=total_courses,
                         total_resources=total_resources,
                         users=users,
                         skills=skills,
                         certifications=certifications,
                         courses=courses,
                         resources=resources)

@app.route('/admin/users/<int:user_id>')
@login_required
def admin_user_details(user_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.get_or_404(user_id)
    user_skills = UserSkill.query.filter_by(user_id=user_id).all()
    skill_progressions = SkillProgression.query.filter_by(user_id=user_id).all()
    user_certifications = UserCertification.query.filter_by(user_id=user_id).all()
    
    return render_template('admin/user_details.html',
                         user=user,
                         user_skills=user_skills,
                         skill_progressions=skill_progressions,
                         user_certifications=user_certifications)

@app.route('/admin/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.role = request.form.get('role')
        user.experience = int(request.form.get('experience', 0))
        
        # Update user skills
        UserSkill.query.filter_by(user_id=user_id).delete()
        for skill_id, proficiency in request.form.items():
            if skill_id.startswith('skill_'):
                skill_id = int(skill_id.split('_')[1])
                proficiency = int(proficiency)
                user_skill = UserSkill(
                    user_id=user_id,
                    skill_id=skill_id,
                    proficiency=proficiency
                )
                db.session.add(user_skill)
        
        db.session.commit()
        flash('User updated successfully.', 'success')
        return redirect(url_for('admin_user_details', user_id=user_id))
    
    all_skills = Skill.query.all()
    return render_template('admin/edit_user.html',
                         user=user,
                         all_skills=all_skills)

@app.route('/admin/users/<int:user_id>', methods=['DELETE'])
@login_required
def admin_delete_user(user_id):
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

@app.route('/admin/skills/add', methods=['GET', 'POST'])
@login_required
def admin_add_skill():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        demand_level = int(request.form.get('demand_level'))
        trend_direction = request.form.get('trend_direction')
        impact_percentage = float(request.form.get('impact_percentage'))
        min_salary = float(request.form.get('min_salary'))
        max_salary = float(request.form.get('max_salary'))
        
        skill = Skill(name=name, category=category)
        db.session.add(skill)
        db.session.flush()
        
        trend = IndustryTrend(
            skill_id=skill.id,
            demand_level=demand_level,
            trend_direction=trend_direction
        )
        
        impact = SalaryImpact(
            skill_id=skill.id,
            impact_percentage=impact_percentage,
            min_salary=min_salary,
            max_salary=max_salary
        )
        
        db.session.add(trend)
        db.session.add(impact)
        db.session.commit()
        
        flash('Skill added successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_skill.html')

@app.route('/admin/skills/<int:skill_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_skill(skill_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    skill = Skill.query.get_or_404(skill_id)
    trend = IndustryTrend.query.filter_by(skill_id=skill_id).first()
    impact = SalaryImpact.query.filter_by(skill_id=skill_id).first()
    
    if request.method == 'POST':
        skill.name = request.form.get('name')
        skill.category = request.form.get('category')
        
        if trend:
            trend.demand_level = int(request.form.get('demand_level'))
            trend.trend_direction = request.form.get('trend_direction')
        
        if impact:
            impact.impact_percentage = float(request.form.get('impact_percentage'))
            impact.min_salary = float(request.form.get('min_salary'))
            impact.max_salary = float(request.form.get('max_salary'))
        
        db.session.commit()
        flash('Skill updated successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/edit_skill.html',
                         skill=skill,
                         trend=trend,
                         impact=impact)

@app.route('/admin/skills/<int:skill_id>', methods=['DELETE'])
@login_required
def admin_delete_skill(skill_id):
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    skill = Skill.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill deleted successfully'})

@app.route('/admin/certifications/add', methods=['GET', 'POST'])
@login_required
def admin_add_certification():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        provider = request.form.get('provider')
        description = request.form.get('description')
        level = request.form.get('level')
        validity_period = int(request.form.get('validity_period'))
        url = request.form.get('url')
        
        certification = Certification(
            name=name,
            provider=provider,
            description=description,
            level=level,
            validity_period=validity_period,
            url=url
        )
        db.session.add(certification)
        db.session.flush()
        
        # Add certification skills
        skill_ids = request.form.getlist('skills')
        proficiency_levels = request.form.getlist('proficiency_levels')
        
        for skill_id, proficiency in zip(skill_ids, proficiency_levels):
            cert_skill = CertificationSkill(
                certification_id=certification.id,
                skill_id=int(skill_id),
                proficiency_level=int(proficiency)
            )
            db.session.add(cert_skill)
        
        db.session.commit()
        flash('Certification added successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    skills = Skill.query.all()
    return render_template('admin/add_certification.html', skills=skills)

@app.route('/admin/certifications/<int:cert_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_certification(cert_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    certification = Certification.query.get_or_404(cert_id)
    cert_skills = CertificationSkill.query.filter_by(certification_id=cert_id).all()
    
    if request.method == 'POST':
        certification.name = request.form.get('name')
        certification.provider = request.form.get('provider')
        certification.description = request.form.get('description')
        certification.level = request.form.get('level')
        certification.validity_period = int(request.form.get('validity_period'))
        certification.url = request.form.get('url')
        
        # Update certification skills
        CertificationSkill.query.filter_by(certification_id=cert_id).delete()
        
        skill_ids = request.form.getlist('skills')
        proficiency_levels = request.form.getlist('proficiency_levels')
        
        for skill_id, proficiency in zip(skill_ids, proficiency_levels):
            cert_skill = CertificationSkill(
                certification_id=cert_id,
                skill_id=int(skill_id),
                proficiency_level=int(proficiency)
            )
            db.session.add(cert_skill)
        
        db.session.commit()
        flash('Certification updated successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    all_skills = Skill.query.all()
    return render_template('admin/edit_certification.html',
                         certification=certification,
                         cert_skills=cert_skills,
                         all_skills=all_skills)

@app.route('/admin/certifications/<int:cert_id>', methods=['DELETE'])
@login_required
def admin_delete_certification(cert_id):
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    certification = Certification.query.get_or_404(cert_id)
    db.session.delete(certification)
    db.session.commit()
    return jsonify({'message': 'Certification deleted successfully'})

@app.route('/admin/courses/add', methods=['GET', 'POST'])
@login_required
def admin_add_course():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        provider = request.form.get('provider')
        description = request.form.get('description')
        level = request.form.get('level')
        duration = request.form.get('duration')
        url = request.form.get('url')
        
        course = Course(
            title=title,
            provider=provider,
            description=description,
            level=level,
            duration=duration,
            url=url
        )
        db.session.add(course)
        db.session.flush()
        
        # Add course skills
        skill_ids = request.form.getlist('skills')
        for skill_id in skill_ids:
            course_skill = CourseSkill(
                course_id=course.id,
                skill_id=int(skill_id)
            )
            db.session.add(course_skill)
        
        db.session.commit()
        flash('Course added successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    skills = Skill.query.all()
    return render_template('admin/add_course.html', skills=skills)

@app.route('/admin/courses/<int:course_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_course(course_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    course = Course.query.get_or_404(course_id)
    course_skills = CourseSkill.query.filter_by(course_id=course_id).all()
    
    if request.method == 'POST':
        course.title = request.form.get('title')
        course.provider = request.form.get('provider')
        course.description = request.form.get('description')
        course.level = request.form.get('level')
        course.duration = request.form.get('duration')
        course.url = request.form.get('url')
        
        # Update course skills
        CourseSkill.query.filter_by(course_id=course_id).delete()
        
        skill_ids = request.form.getlist('skills')
        for skill_id in skill_ids:
            course_skill = CourseSkill(
                course_id=course_id,
                skill_id=int(skill_id)
            )
            db.session.add(course_skill)
        
        db.session.commit()
        flash('Course updated successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    
    all_skills = Skill.query.all()
    return render_template('admin/edit_course.html',
                         course=course,
                         course_skills=course_skills,
                         all_skills=all_skills)

@app.route('/admin/courses/<int:course_id>', methods=['DELETE'])
@login_required
def admin_delete_course(course_id):
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'})

@app.route('/admin/resources/add', methods=['GET', 'POST'])
@login_required
def admin_add_resource():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        subsection = request.form['subsection']
        difficulty = request.form['difficulty']
        duration = request.form['duration']
        content = request.form['content']
        external_url = request.form.get('external_url', '')
        is_active = 'is_active' in request.form
        
        resource = Resource(
            title=title,
            description=description,
            category=category,
            subsection=subsection,
            difficulty=difficulty,
            duration=duration,
            content=content,
            external_url=external_url,
            is_active=is_active
        )
        
        db.session.add(resource)
        db.session.commit()
        
        flash('Resource added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_resource.html')

@app.route('/admin/resources/<int:resource_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_resource(resource_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    resource = Resource.query.get_or_404(resource_id)
    
    if request.method == 'POST':
        resource.title = request.form['title']
        resource.description = request.form['description']
        resource.category = request.form['category']
        resource.subsection = request.form['subsection']
        resource.difficulty = request.form['difficulty']
        resource.duration = request.form['duration']
        resource.content = request.form['content']
        resource.external_url = request.form.get('external_url', '')
        resource.is_active = 'is_active' in request.form
        
        db.session.commit()
        
        flash('Resource updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/edit_resource.html', resource=resource)

@app.route('/admin/resources/<int:resource_id>', methods=['DELETE'])
@login_required
def admin_delete_resource(resource_id):
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({'message': 'Resource deleted successfully'})

@app.route('/populate-resources')
@login_required
def populate_resources():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    try:
        populate_initial_resources()
        flash('Resources populated successfully!', 'success')
    except Exception as e:
        flash(f'Error populating resources: {str(e)}', 'error')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/security-status')
@login_required
def admin_security_status():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    # Import security functions
    try:
        from security_config import get_security_status
        status = get_security_status()
    except ImportError:
        status = {
            'environment_valid': False,
            'missing_variables': ['security_config module not found'],
            'debug_mode': os.environ.get('FLASK_DEBUG', 'False').lower() == 'true',
            'secure_cookies': os.environ.get('SESSION_COOKIE_SECURE', 'True').lower() == 'true',
            'secret_key_set': bool(os.environ.get('SECRET_KEY')),
            'admin_configured': bool(os.environ.get('ADMIN_USERNAME') and os.environ.get('ADMIN_PASSWORD'))
        }
    
    return render_template('admin/security_status.html', status=status)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        feedback_line = f"[{timestamp}] Name: {name}, Email: {email}, Message: {message}\n"
        feedback_path = os.path.join(os.path.dirname(__file__), 'feedback.txt')
        with open(feedback_path, 'a', encoding='utf-8') as f:
            f.write(feedback_line)
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback'))
    return render_template('feedback.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Secure admin user creation - only create if environment variables are set
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
                print(f"Admin user '{admin_username}' created successfully.")
            else:
                print(f"Admin user '{admin_username}' already exists.")
        else:
            print("Admin credentials not provided in environment variables.")
            print("To create admin user, set: ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD")

        # Initialize skills and jobs if they don't exist
        if not Skill.query.first():
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

            # Add skills taught in courses
            course_skills = [
                CourseSkill(course_id=1, skill_id=1),  # Network Security
                CourseSkill(course_id=2, skill_id=2),  # Penetration Testing
                CourseSkill(course_id=3, skill_id=7)   # Cloud Security
            ]
            db.session.add_all(course_skills)
            db.session.commit()

    # Only run in debug mode if explicitly set in environment
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000) 