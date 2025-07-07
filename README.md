# SutraByte - Cybersecurity Skill Assessment Platform

A comprehensive web application for assessing, tracking, and developing cybersecurity skills with personalized learning recommendations.

## Features

- **User Authentication & Authorization**: Secure login system with role-based access
- **Skill Assessment**: Interactive skill evaluation with proficiency tracking
- **Personalized Recommendations**: AI-driven course and certification suggestions
- **Progress Tracking**: Visual skill progression over time
- **Resource Management**: Curated learning materials and tools
- **Admin Dashboard**: Comprehensive management interface
- **Security Analytics**: Industry trends and salary impact analysis

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render/Railway/Heroku ready

## Quick Start

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/Vinayakgupta1/SutraByte
cd SutraByte
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Create .env file with:
SECRET_KEY=your-secret-key
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=secure-password
```

5. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
ADMIN_USERNAME=your-admin-username
ADMIN_EMAIL=your-admin-email
ADMIN_PASSWORD=your-admin-password
FLASK_DEBUG=False
```

## Deployment

This application is configured for deployment on:
- **Render** (recommended)
- **Railway**
- **Heroku**

See deployment-specific documentation for setup instructions.

## Security Features

- Password strength validation
- Input sanitization
- Secure session management
- Role-based access control
- SQL injection protection
- XSS prevention

## Contributing

This is a private repository. For internal development:
1. Create feature branches
2. Follow security best practices
3. Test thoroughly before merging
4. Update documentation

## License

Private - All rights reserved

## Support

For internal support and questions, contact the development team. 