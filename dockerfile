# Imagen base oficial de Python
FROM python:3.11-slim

# Seteamos el directorio de trabajo
WORKDIR /app

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y curl build-essential && apt-get clean

# Instalamos Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Agregamos el path de Poetry al entorno
ENV PATH="/root/.local/bin:$PATH"

# Copiamos el proyecto
COPY . .

# Instalamos las dependencias
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# Exponemos el puerto para Render
EXPOSE 8000

# Comando para iniciar la app (ajustá el path si es necesario)
CMD ["gunicorn", "src.app_web:app", "--bind", "0.0.0.0:8000"]
