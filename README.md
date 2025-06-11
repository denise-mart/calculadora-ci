# 🧮 Calculadora CI en Flask

Este proyecto es una calculadora simple hecha con Flask, preparada para integrarse con CI/CD (GitHub Actions), testing automático (`pytest`) y control de calidad de código (`flake8`, `black`). El entorno se maneja completamente con `Poetry`.

---

## 🚀 Instalación

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

## ⚙️ CI/CD

Este proyecto incluye un workflow de GitHub Actions que:

- Corre tests automáticamente
- Aplica linters
- Notifica a Slack
- Despliega a Render


---

## 👤 Autora

Denise – [agos.martinez02@hotmail.com](mailto:agos.martinez02@hotmail.com)
