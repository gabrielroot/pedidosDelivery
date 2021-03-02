clean:
	@echo "Execute cleaning ..."
	rm -f *.pyc
	rm -f .coverage
	rm -f coverage.xml

pep8:
	flake8 .
	isort training --check-only

migrate:
	python manage.py db upgrade

test: clean pep8
	pytest --cov=. -v

coverage: clean pep8
	pytest --cov=. --cov-report=html

deps:
	docker-compose up -d

fix-import: clean
	isort . -rc

up: deps
	python manage.py runserver

down:
	docker-compose down
