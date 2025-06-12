# Imagen base liviana de Python 3.11
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y curl build-essential && apt-get clean

# Instalamos Poetry versión estable
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - \
 && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copiamos el código fuente
COPY . .

# Instalamos dependencias con Poetry, sin entorno virtual interno
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# Exponemos el puerto que usa Render
EXPOSE 8000

# Comando para iniciar la app en producción
CMD ["gunicorn", "src.app_web:app", "--bind", "0.0.0.0:8000"]
