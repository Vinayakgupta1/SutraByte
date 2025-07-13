# Supabase PostgreSQL Setup Guide

## 1. Create Supabase Account
1. Go to https://supabase.com
2. Sign up with GitHub
3. Create a new project

## 2. Get Database Connection Details
1. Go to your project dashboard
2. Navigate to Settings > Database
3. Copy the connection string

## 3. Environment Variables
Add these to your Vercel environment variables:
- `DATABASE_URL`: Your Supabase PostgreSQL connection string
- `SECRET_KEY`: A secure random string for Flask sessions

## 4. Database Schema
Your app will automatically create all tables when it first runs.

## 5. Data Management
- Use Supabase Dashboard to view/edit data
- Use the admin panel in your app
- Use Flask-Migrate for schema changes 