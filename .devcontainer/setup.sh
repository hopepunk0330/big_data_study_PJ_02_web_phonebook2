#!/usr/bin/env bash
set -e

if [ ! -f .env ]; then
  cat > .env <<'EOF'
POSTGRES_PASSWORD=localdevpass
DATABASE_URL=postgresql+psycopg://contact_app:localdevpass@localhost:5432/contact_app
EOF
fi

pip install --upgrade pip
pip install -r backend/requirements.txt
pip install pytest pytest-playwright
python -m playwright install --with-deps chromium
