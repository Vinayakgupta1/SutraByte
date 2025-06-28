from datetime import datetime, timedelta
from app import db, User, Skill, UserSkill, Job, JobSkill, Course, CourseSkill

def update_skill_progression(user_id, skill_id, new_proficiency):
    """Record a user's skill progression."""
    from app import SkillProgression
    progression = SkillProgression(
        user_id=user_id,
        skill_id=skill_id,
        proficiency=new_proficiency
    )
    db.session.add(progression)
    db.session.commit()

def get_skill_progression_history(user_id, skill_id):
    """Get the progression history for a specific skill."""
    from app import SkillProgression
    return SkillProgression.query.filter_by(
        user_id=user_id,
        skill_id=skill_id
    ).order_by(SkillProgression.date_recorded).all()

def calculate_salary_impact(user_skills):
    """Calculate the potential salary impact of user's skills."""
    from app import SalaryImpact, Skill
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
    from app import IndustryTrend, Skill
    trends = IndustryTrend.query.order_by(IndustryTrend.demand_level.desc()).all()
    return [{
        'skill': trend.skill.name,
        'demand_level': trend.demand_level,
        'trend_direction': trend.trend_direction,
        'last_updated': trend.last_updated
    } for trend in trends]

def get_recommended_certifications(user_skills):
    """Get recommended certifications based on user's skills and gaps."""
    from app import Certification, CertificationSkill, Skill
    # Get all certifications
    all_certs = Certification.query.all()
    recommended = []
    
    for cert in all_certs:
        cert_skills = CertificationSkill.query.filter_by(certification_id=cert.id).all()
        relevance_score = 0
        missing_skills = []
        
        for cert_skill in cert_skills:
            if cert_skill.skill_id in user_skills:
                if user_skills[cert_skill.skill_id] < cert_skill.proficiency_level:
                    relevance_score += 1
                    missing_skills.append(cert_skill.skill.name)
            else:
                relevance_score += 2
                missing_skills.append(cert_skill.skill.name)
        
        if relevance_score > 0:
            recommended.append({
                'certification': cert,
                'relevance_score': relevance_score,
                'missing_skills': missing_skills
            })
    
    return sorted(recommended, key=lambda x: x['relevance_score'], reverse=True)

def initialize_enhanced_data():
    """Initialize sample data for enhanced features."""
    from app import IndustryTrend, SalaryImpact, Certification, CertificationSkill
    
    # Sample industry trends
    trends = [
        {'skill': 'Network Security', 'demand_level': 5, 'trend_direction': 'increasing'},
        {'skill': 'Cloud Security', 'demand_level': 5, 'trend_direction': 'increasing'},
        {'skill': 'Penetration Testing', 'demand_level': 4, 'trend_direction': 'increasing'},
        {'skill': 'Security Analysis', 'demand_level': 4, 'trend_direction': 'stable'},
        {'skill': 'Incident Response', 'demand_level': 4, 'trend_direction': 'increasing'}
    ]
    
    for trend_data in trends:
        skill = Skill.query.filter_by(name=trend_data['skill']).first()
        if skill:
            trend = IndustryTrend(
                skill_id=skill.id,
                demand_level=trend_data['demand_level'],
                trend_direction=trend_data['trend_direction']
            )
            db.session.add(trend)
    
    # Sample salary impacts
    salary_impacts = [
        {'skill': 'Network Security', 'impact': 15.0, 'min_salary': 80000, 'max_salary': 120000},
        {'skill': 'Cloud Security', 'impact': 20.0, 'min_salary': 90000, 'max_salary': 130000},
        {'skill': 'Penetration Testing', 'impact': 18.0, 'min_salary': 85000, 'max_salary': 125000},
        {'skill': 'Security Analysis', 'impact': 12.0, 'min_salary': 75000, 'max_salary': 110000},
        {'skill': 'Incident Response', 'impact': 14.0, 'min_salary': 78000, 'max_salary': 115000}
    ]
    
    for impact_data in salary_impacts:
        skill = Skill.query.filter_by(name=impact_data['skill']).first()
        if skill:
            impact = SalaryImpact(
                skill_id=skill.id,
                impact_percentage=impact_data['impact'],
                min_salary=impact_data['min_salary'],
                max_salary=impact_data['max_salary']
            )
            db.session.add(impact)
    
    # Sample certifications
    certifications = [
        {
            'name': 'CompTIA Security+',
            'provider': 'CompTIA',
            'description': 'Entry-level certification for IT security professionals',
            'level': 'beginner',
            'validity_period': 36,
            'url': 'https://www.comptia.org/certifications/security'
        },
        {
            'name': 'Certified Ethical Hacker (CEH)',
            'provider': 'EC-Council',
            'description': 'Professional certification for ethical hackers',
            'level': 'intermediate',
            'validity_period': 36,
            'url': 'https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/'
        },
        {
            'name': 'CISSP',
            'provider': 'ISC2',
            'description': 'Advanced certification for security professionals',
            'level': 'advanced',
            'validity_period': 36,
            'url': 'https://www.isc2.org/Certifications/CISSP'
        }
    ]
    
    for cert_data in certifications:
        cert = Certification(**cert_data)
        db.session.add(cert)
        db.session.flush()  # Get the cert ID
        
        # Add certification skills
        if cert.name == 'CompTIA Security+':
            skills = ['Network Security', 'Security Analysis']
        elif cert.name == 'Certified Ethical Hacker (CEH)':
            skills = ['Penetration Testing', 'Network Security']
        else:  # CISSP
            skills = ['Security Analysis', 'Incident Response', 'Cloud Security']
        
        for skill_name in skills:
            skill = Skill.query.filter_by(name=skill_name).first()
            if skill:
                cert_skill = CertificationSkill(
                    certification_id=cert.id,
                    skill_id=skill.id,
                    proficiency_level=4 if cert.level == 'advanced' else 3
                )
                db.session.add(cert_skill)
    
    db.session.commit() 