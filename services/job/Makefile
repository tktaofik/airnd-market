
.DEFAULT: help

help:
	@echo "make start"
	@echo "    Run server."
	@echo "make start_watch"
	@echo "    Run server and watch for changes"
	@echo "make service_dependencies"
	@echo "    Install service dependencies and create database"
	@echo "make lint"
	@echo "    Run lint on project."
	@echo "make test"
	@echo "    Run tests on project."
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."
	@echo "make build"
	@echo "    Creates docker image of app."
	@echo "make install"
	@echo "    Install packages."

venv: ../../python_venv/bin/activate

start: venv
	@python app.py 

start_watch: venv
	@nodemon -L app.py 
	
service_dependencies:
	@docker-compose up --remove-orphans -d
	@sleep 10
	@python init_db.py

teardown_db:
	@python teardown_db.py
	
lint: 

test: 

build:

clean:
	@rm -rf `find . -name __pycache__`

install:
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@pip freeze > requirements.txt