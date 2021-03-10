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
```
