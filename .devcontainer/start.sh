#!/usr/bin/env bash
set -e

export $(grep -v '^#' .env | xargs)

docker compose up -d
sleep 3

cd backend
pkill -f "uvicorn main:app" 2>/dev/null || true
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > /tmp/uvicorn.log 2>&1 &
