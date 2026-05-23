FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el requirements que está en la raíz externa
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 📁 CAMBIO AQUÍ: Copiamos solo el contenido de 'uno' directamente en '/app'
COPY ./uno/ /app/

EXPOSE 8000

# El script se mantiene igual, porque ahora manage.py sí estará en la raíz
CMD sh -c "\
    echo 'Esperando a que la base de datos esté lista...'; \
    while ! nc -z db 5432; do sleep 1; done; \
    echo 'Base de datos detectada. Aplicando migraciones...'; \
    python manage.py migrate --noinput && \
    python manage.py runserver 0.0.0.0:8000"