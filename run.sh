#!/bin/bash

# Check if PostgreSQL is running
if ! pg_isready; then
    echo "Starting PostgreSQL..."
    # For Mac
    brew services start postgresql
    # For Linux
    # sudo service postgresql start
fi

# Create database if it doesn't exist
psql -lqt | cut -d \| -f 1 | grep -qw needhelp
if [ $? -ne 0 ]; then
    echo "Creating database..."
    createdb needhelp
fi

# Run migrations
cd backend
alembic upgrade head

# Start backend in background
echo "Starting backend..."
python app/main.py &
BACKEND_PID=$!

# Start frontend
cd ../frontend
echo "Starting frontend..."
npm run dev

# Cleanup when script is terminated
trap 'kill $BACKEND_PID' EXIT 