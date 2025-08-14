#!/bin/bash

# DineEase Restaurant Website Startup Script

echo "Starting DineEase Restaurant Website..."
echo "======================================"

# Activate virtual environment
source venv/bin/activate

# Check if database exists, if not run setup
if [ ! -f "db.sqlite3" ]; then
    echo "Database not found. Running initial setup..."
    python setup.py
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the development server
echo "Starting development server..."
echo "Website will be available at: http://127.0.0.1:8000/"
echo "Admin panel: http://127.0.0.1:8000/admin/"
echo "Admin credentials: admin/admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
