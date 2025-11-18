#!/bin/sh

echo "Intializing database..."
python -c "from app import db; db.create_all()"


