
.DEFAULT: help

help:
	@echo "make prepare-dev"
	@echo "    Create python virtual environment."
	@echo "make start"
	@echo "    Run server."
	@echo "make start_watch"
	@echo "    Run server and watch for changes"
	@echo "make service_dependencies"
	@echo "    Install service dependencies and initialize database"
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

prepare-dev:
	@which ENV && rm -rf ENV
	@which pyenv || pyenv install 3.8.0
	@which virtualenv || python3 -m pip install virtualenv
	@virtualenv ENV

venv: ENV/bin/activate

start: venv
	@python app.py 

start_watch: venv
	@nodemon app.py 
	
service_dependencies:
	@docker-compose up --force-recreate --remove-orphans -d
	@sleep 10
	@python db/init_db.py
	
lint: 

test: 

build:

clean:
	@rm -rf `find . -name __pycache__`

install:
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@pip freeze > requirements.txt