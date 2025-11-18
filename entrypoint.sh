#!/bin/sh

echo "Intializing database..."
python -c "from app import db; db.create_all()"

echo "Starting Flask..."
exec flask run --host=0.0.0.0 --debug
