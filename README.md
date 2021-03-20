# pedidosDelivery
### A project for training

# Conceptual data model
![Captura de tela](modelo_conceitual.png?raw=true "Title")

### Make environment ###
```
pyenv shell 3.8.0 &&  python -m venv .venv && source .venv/bin/activate
pip install -U pip setuptools
pip install -r requirements-dev.txt
docker-compose up -d && source .venv/bin/activate
```
<div style="display: flex;">
<img src="https://img.shields.io/static/v1?label=Python&message=3.7&color=3776AB&style=flat-square&logo=python" style="margin: 10px"/>
<img src="https://img.shields.io/static/v1?label=Flask&message=1.1.1&color=000&style=flat-square&logo=flask" style="margin: 10px"/>
<img src="https://img.shields.io/static/v1?label=PostgreSQL&message=11.9&color=336791&style=flat-square&logo=PostgreSQL" style="margin: 10px"/>
</div>
