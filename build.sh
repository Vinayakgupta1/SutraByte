#!/bin/bash
# Build script for Render deployment

# Install system dependencies for psycopg2
apt-get update
apt-get install -y libpq-dev python3-dev

# Install Python packages
pip install -r requirements.txt 