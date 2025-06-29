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
- **Feedback System**: User feedback management with admin panel

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL (production) / Local PostgreSQL (development)
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render ready with PostgreSQL

## Quick Start

### Prerequisites
- Python 3.11+
- pip
- PostgreSQL (for local development)

### Installation

1. Clone the repository
```bash
git clone <your-private-repo-url>
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

4. Set up PostgreSQL database (local development)
```bash
# Create database
createdb sutrabyte_dev

# Or set custom DATABASE_URL in .env file
```

5. Set up environment variables
```bash
# Create .env file with:
SECRET_KEY=your-secret-key
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=secure-password
DATABASE_URL=postgresql://localhost/sutrabyte_dev  # Optional for local dev
```

6. Initialize database
```bash
python init_db.py
```

7. Run the application
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
DATABASE_URL=postgresql://username:password@host:port/database  # For production
FLASK_DEBUG=False
```

## Deployment

This application is configured for deployment on Render with PostgreSQL:

1. **Create PostgreSQL Database** in Render
2. **Set Environment Variables**:
   - `DATABASE_URL` (from Render PostgreSQL)
   - `SECRET_KEY`
   - `ADMIN_USERNAME`
   - `ADMIN_EMAIL`
   - `ADMIN_PASSWORD`
3. **Deploy** - Database will be initialized automatically

## Database Configuration

- **Production**: Uses `DATABASE_URL` environment variable (PostgreSQL on Render)
- **Development**: Uses local PostgreSQL database `sutrabyte_dev`
- **Automatic**: Database tables created on first run

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