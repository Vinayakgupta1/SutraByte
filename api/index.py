from app import app

handler = app

# For Vercel serverless deployment
if __name__ == "__main__":
    app.run() 
