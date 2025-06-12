Write-Host "> Instalando Poetry"
pip install poetry

Write-Host "> Instalando dependencias"
poetry install

Write-Host "> Formateando codigo con Black"
poetry run black . --check

Write-Host "> Verificando codigo con Flake8"
poetry run flake8 .

Write-Host "> Ejecutando tests con Pytest"
poetry run pytest

Write-Host "> Levantando la aplicacion"
poetry run python app.py
