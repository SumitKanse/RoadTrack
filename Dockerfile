# ---------- FRONTEND BUILD ----------
FROM node:20 as frontend-build

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build

# ---------- BACKEND ----------
FROM python:3.12-slim

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend
COPY backend ./backend

# Copy frontend build into static folder
COPY --from=frontend-build /app/frontend/dist ./frontend_build

# Install nginx
RUN apt-get update && apt-get install -y nginx

# Copy frontend to nginx
RUN rm -rf /var/www/html/*
RUN cp -r frontend_build/* /var/www/html/

# Expose port
EXPOSE 80

# Start both backend + nginx
CMD service nginx start && python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000