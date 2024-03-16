#!/bin/bash

APP_PORT=${PORT:-8000}

gunicorn --bind=0.0.0.0:${APP_PORT} --workers 4 --threads 4 src.main:app --worker-class uvicorn.workers.UvicornH11Worker --preload --timeout 600