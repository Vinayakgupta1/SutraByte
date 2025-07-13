# PostgreSQL Deployment Guide for SutraByte

## 🎯 Overview
This guide will help you deploy your Flask app with PostgreSQL database on Vercel.

## 📋 Prerequisites
- GitHub account
- Vercel account
- Supabase account (for PostgreSQL database)

## 🗄️ Step 1: Set Up PostgreSQL Database

### Option A: Supabase (Recommended)
1. **Create Supabase Account**
   - Go to https://supabase.com
   - Sign up with GitHub
   - Create a new project

2. **Get Database Connection String**
   - Go to your project dashboard
   - Navigate to Settings > Database
   - Copy the connection string (looks like: `postgresql://postgres:[password]@[host]:5432/postgres`)

### Option B: Neon (Alternative)
1. **Create Neon Account**
   - Go to https://neon.tech
   - Sign up and create a project
   - Get your connection string

## 🔧 Step 2: Prepare Your App

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Set Environment Variables
Create a `.env` file in your project root:
```env
DATABASE_URL=your_postgresql_connection_string_here
SECRET_KEY=your_secure_random_string_here
```

## 🚀 Step 3: Deploy to Vercel

### 1. Initialize Vercel Project
```bash
vercel
```

### 2. Set Environment Variables in Vercel Dashboard
1. Go to your Vercel project dashboard
2. Navigate to Settings > Environment Variables
3. Add these variables:
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `SECRET_KEY`: A secure random string (32+ characters)

### 3. Deploy
```bash
vercel --prod
```

## 📊 Step 4: Database Management

### View/Edit Data via Supabase Dashboard
1. Go to your Supabase project
2. Navigate to Table Editor
3. View and edit your data directly

### Add Data via Admin Panel
1. Visit your deployed app
2. Go to `/create-admin` to create admin user
3. Login with admin credentials
4. Use the admin dashboard to manage data

### Migrate Existing Data (Optional)
If you have data in your local SQLite database:
```bash
python migrate_to_postgresql.py
```

## 🔍 Step 5: Verify Deployment

### Test Your App
1. Visit your deployed URL
2. Test registration and login
3. Test admin functionality
4. Test skill analyzer features

### Check Database Connection
Your app will automatically create tables on first run.

## 🛠️ Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check your `DATABASE_URL` format
   - Ensure your database is accessible from Vercel
   - Verify SSL settings if required

2. **Tables Not Created**
   - Check if `DATABASE_URL` is set correctly
   - Look at Vercel function logs for errors

3. **Admin User Not Created**
   - Visit `/create-admin` to create admin user
   - Default admin: username=`admin`, password=`admin123`

### Environment Variables Format
```
DATABASE_URL=postgresql://username:password@host:port/database
SECRET_KEY=your-32-character-random-string
```

## 📈 Monitoring

### Vercel Analytics
- View deployment status in Vercel dashboard
- Monitor function performance
- Check error logs

### Database Monitoring
- Use Supabase dashboard for database metrics
- Monitor query performance
- Set up alerts for database issues

## 🔒 Security Best Practices

1. **Environment Variables**
   - Never commit `.env` files to Git
   - Use Vercel's environment variable system
   - Rotate secrets regularly

2. **Database Security**
   - Use strong passwords
   - Enable SSL connections
   - Restrict database access

3. **App Security**
   - Use HTTPS in production
   - Validate all user inputs
   - Implement rate limiting

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

## 🎉 Success!

Your SutraByte app is now deployed with PostgreSQL database!
- ✅ Persistent data storage
- ✅ Admin panel for data management
- ✅ User authentication
- ✅ Skill analyzer functionality
- ✅ Blog and resource management 