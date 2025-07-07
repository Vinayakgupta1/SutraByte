# Deployment Guide: SutraByte on Render

## Prerequisites

1. **GitHub Account**: Your code should be in a private GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Local SQLite**: No need to install PostgreSQL. SQLite is used by default for development and production.

## Step 1: Prepare Your Repository

### 1.1 Ensure Your Code is Ready
- ✅ All files are committed to GitHub
- ✅ `requirements.txt` includes all dependencies (no PostgreSQL required)
- ✅ `Procfile` exists with `web: gunicorn app:app`
- ✅ `runtime.txt` specifies Python version
- ✅ Database configuration uses SQLite

### 1.2 Test Locally
```bash
# No need to install PostgreSQL
# SQLite database will be created automatically
python app.py
```

## Step 2: Deploy Your Flask Application

### 2.1 Create Web Service
1. In Render dashboard, click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select your `SutraByte` repository

### 2.2 Configure Web Service
- **Name**: `sutrabyte-app` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Start with **Free** plan

### 2.3 Set Environment Variables
Click "Environment" tab and add:

```
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=your-secure-admin-password
FLASK_ENV=production
```

### 2.4 Advanced Settings (Optional)
- **Auto-Deploy**: Enable for automatic deployments on git push
- **Health Check Path**: `/` (your homepage)
- **Health Check Timeout**: 180 seconds

## Step 3: Deploy and Test

### 3.1 Deploy
1. Click "Create Web Service"
2. Render will build and deploy your application
3. Monitor the build logs for any errors

### 3.2 Verify Deployment
1. Wait for build to complete (usually 2-5 minutes)
2. Click on your service URL to test
3. Check that the application loads correctly

### 3.3 Database Initialization
Your app will automatically:
- Use SQLite as the database
- Create all database tables on first run
- Set up the admin user with your credentials

## Step 4: Post-Deployment Setup

### 4.1 Test Admin Access
1. Go to `https://your-app.onrender.com/create-admin`
2. Create your admin account (if not auto-created)
3. Test admin dashboard functionality

### 4.2 Verify Database Connection
1. Log into admin panel
2. Check that data is being saved/retrieved
3. Test feedback system and other features

### 4.3 Set Up Custom Domain (Optional)
1. In Render dashboard, go to your web service
2. Click "Settings" → "Custom Domains"
3. Add your domain and configure DNS

## Step 5: Monitoring and Maintenance

### 5.1 Monitor Performance
- Check Render dashboard for:
  - Response times
  - Error rates
  - Resource usage

### 5.2 Database Management
- **Backups**: Download the SQLite file as needed
- **Scaling**: Upgrade web service plan as needed
- **Monitoring**: Use Render's built-in monitoring

### 5.3 Security Best Practices
- ✅ Use strong, unique passwords
- ✅ Keep dependencies updated
- ✅ Monitor for security issues
- ✅ Use HTTPS (automatic on Render)

## Troubleshooting

### Common Issues

#### 1. Build Failures
```bash
# Check requirements.txt has all dependencies
# Verify Python version in runtime.txt
```

#### 2. Application Errors
```bash
# Check Render logs
# Verify environment variables
# Test locally first
```

#### 3. Performance Issues
- Upgrade to paid plan for better performance
- Optimize database queries

### Getting Help
- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Render Support**: Available in dashboard
- **SQLite Docs**: [sqlite.org/docs](https://sqlite.org/docs)

## Cost Optimization

### Free Tier Limits
- **Web Service**: 750 hours/month
- **Bandwidth**: 100GB/month

### Paid Plans
- **Web Service**: $7/month for always-on
- **Custom Domains**: Free with paid plans

## Next Steps

1. **Set up monitoring** and alerts
2. **Configure backups** and disaster recovery
3. **Implement CI/CD** for automated deployments
4. **Add SSL certificates** for custom domains
5. **Scale resources** as your application grows

---

**🎉 Congratulations!** Your Flask application is now deployed with SQLite on Render.

**🔗 Your Application URL**: `https://your-app-name.onrender.com`
**📊 Monitor**: Check your Render dashboard regularly
**🔒 Security**: Keep your credentials secure and rotate them periodically 