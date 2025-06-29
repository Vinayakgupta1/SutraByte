# Deployment Guide: PostgreSQL on Render

## Prerequisites

1. **GitHub Account**: Your code should be in a private GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Local PostgreSQL** (optional): For testing before deployment

## Step 1: Prepare Your Repository

### 1.1 Ensure Your Code is Ready
- ✅ All files are committed to GitHub
- ✅ `requirements.txt` includes `psycopg2-binary`
- ✅ `Procfile` exists with `web: gunicorn app:app`
- ✅ `runtime.txt` specifies Python version
- ✅ Database configuration supports PostgreSQL

### 1.2 Test Locally (Optional)
```bash
# Install PostgreSQL locally if you want to test
# Windows: Download from https://www.postgresql.org/download/windows/
# macOS: brew install postgresql
# Linux: sudo apt-get install postgresql

# Create database
createdb sutrabyte_dev

# Test your app locally
python app.py
```

## Step 2: Create PostgreSQL Database on Render

### 2.1 Access Render Dashboard
1. Go to [render.com](https://render.com)
2. Sign in to your account
3. Click "New +" → "PostgreSQL"

### 2.2 Configure PostgreSQL Database
- **Name**: `sutrabyte-db` (or your preferred name)
- **Database**: `sutrabyte_prod`
- **User**: `sutrabyte_user` (auto-generated)
- **Region**: Choose closest to your users
- **PostgreSQL Version**: Latest (15 or 16)
- **Plan**: Start with **Free** plan for testing

### 2.3 Save Database Credentials
After creation, Render will show:
- **Internal Database URL**: `postgresql://user:password@host:port/database`
- **External Database URL**: For external connections (if needed)

**⚠️ Important**: Copy the Internal Database URL - you'll need it for the next step.

## Step 3: Deploy Your Flask Application

### 3.1 Create Web Service
1. In Render dashboard, click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select your `SutraByte` repository

### 3.2 Configure Web Service
- **Name**: `sutrabyte-app` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Start with **Free** plan

### 3.3 Set Environment Variables
Click "Environment" tab and add:

```
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=your-secure-admin-password
FLASK_ENV=production
```

**Replace the DATABASE_URL** with the Internal Database URL from Step 2.3.

### 3.4 Advanced Settings (Optional)
- **Auto-Deploy**: Enable for automatic deployments on git push
- **Health Check Path**: `/` (your homepage)
- **Health Check Timeout**: 180 seconds

## Step 4: Deploy and Test

### 4.1 Deploy
1. Click "Create Web Service"
2. Render will build and deploy your application
3. Monitor the build logs for any errors

### 4.2 Verify Deployment
1. Wait for build to complete (usually 2-5 minutes)
2. Click on your service URL to test
3. Check that the application loads correctly

### 4.3 Database Initialization
Your app will automatically:
- Connect to PostgreSQL using the `DATABASE_URL`
- Create all database tables on first run
- Set up the admin user with your credentials

## Step 5: Post-Deployment Setup

### 5.1 Test Admin Access
1. Go to `https://your-app.onrender.com/create-admin`
2. Create your admin account (if not auto-created)
3. Test admin dashboard functionality

### 5.2 Verify Database Connection
1. Log into admin panel
2. Check that data is being saved/retrieved
3. Test feedback system and other features

### 5.3 Set Up Custom Domain (Optional)
1. In Render dashboard, go to your web service
2. Click "Settings" → "Custom Domains"
3. Add your domain and configure DNS

## Step 6: Monitoring and Maintenance

### 6.1 Monitor Performance
- Check Render dashboard for:
  - Response times
  - Error rates
  - Resource usage

### 6.2 Database Management
- **Backups**: Render provides automatic backups
- **Scaling**: Upgrade PostgreSQL plan as needed
- **Monitoring**: Use Render's built-in monitoring

### 6.3 Security Best Practices
- ✅ Use strong, unique passwords
- ✅ Keep dependencies updated
- ✅ Monitor for security issues
- ✅ Use HTTPS (automatic on Render)

## Troubleshooting

### Common Issues

#### 1. Build Failures
```bash
# Check requirements.txt has all dependencies
# Ensure psycopg2-binary is included
# Verify Python version in runtime.txt
```

#### 2. Database Connection Errors
```bash
# Verify DATABASE_URL is correct
# Check database is running
# Ensure firewall allows connections
```

#### 3. Application Errors
```bash
# Check Render logs
# Verify environment variables
# Test locally first
```

#### 4. Performance Issues
- Upgrade to paid plan for better performance
- Optimize database queries
- Use connection pooling if needed

### Getting Help
- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Render Support**: Available in dashboard
- **PostgreSQL Docs**: [postgresql.org/docs](https://www.postgresql.org/docs)

## Cost Optimization

### Free Tier Limits
- **Web Service**: 750 hours/month
- **PostgreSQL**: 90 days free trial
- **Bandwidth**: 100GB/month

### Paid Plans
- **Web Service**: $7/month for always-on
- **PostgreSQL**: $7/month for persistent database
- **Custom Domains**: Free with paid plans

## Next Steps

1. **Set up monitoring** and alerts
2. **Configure backups** and disaster recovery
3. **Implement CI/CD** for automated deployments
4. **Add SSL certificates** for custom domains
5. **Scale resources** as your application grows

---

**🎉 Congratulations!** Your Flask application is now deployed with PostgreSQL on Render.

**🔗 Your Application URL**: `https://your-app-name.onrender.com`
**📊 Monitor**: Check your Render dashboard regularly
**🔒 Security**: Keep your credentials secure and rotate them periodically 