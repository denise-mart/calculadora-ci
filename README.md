# 🧮 Calculadora CI en Flask

Este proyecto es una calculadora simple hecha con Flask, preparada para integrarse con CI/CD (GitHub Actions), testing automático (`pytest`) y control de calidad de código (`flake8`, `black`). El entorno se maneja completamente con `Poetry`, y se encuentra contenedorizado con Docker para facilitar su despliegue en producción.

---

## 🚀 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/denise-mart/calculadora-ci.git
cd calculadora-ci
```

### 2. Instalar dependencias

```bash
pip install poetry
poetry install
```

### 3. Activar el entorno

```bash
poetry shell
```

---

## 🧪 Correr tests

```bash
poetry run pytest
```

---

## 🧼 Verificar calidad de código

```bash
poetry run flake8 .
poetry run black . --check
```

---

## 🖥️ Ejecutar la app

```bash
poetry run python app.py
```

Accedé desde el navegador en:  
[http://localhost:10000](http://localhost:10000)

---

## 🐳 Uso con Docker

### Build de imagen

```bash
docker build -t calculadora-ci .
```

### Ejecutar contenedor

```bash
docker run -p 8000:8000 calculadora-ci
```

Luego acceder en: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ CI/CD

Este proyecto incluye un workflow de GitHub Actions que:

- Corre tests automáticamente (`pytest`)
- Aplica linters (`flake8`, `black`)
- Crea una imagen Docker
- La sube a **GitHub Container Registry (GHCR)**
- Llama al Webhook de **Render** para desplegar automáticamente la nueva versión
- Envía notificaciones al canal de **Slack** del equipo

---

## 🌐 Producción

App desplegada automáticamente en:  
👉 [`https://calculadora-ci-latest.onrender.com`](https://calculadora-ci-latest.onrender.com)

---

## 📂 Estructura del proyecto

```
calculadora-ci/
├── app.py               # App Flask
├── templates/           # HTMLs de la interfaz
├── tests/               # Tests unitarios
├── Dockerfile           # Imagen del contenedor
├── .dockerignore
├── pyproject.toml       # Configuración con Poetry
├── poetry.lock
├── .github/workflows/   # CI/CD con GitHub Actions
└── README.md
```

---

## 👤 Autora

Denise – [agos.martinez02@hotmail.com](mailto:agos.martinez02@hotmail.com)
