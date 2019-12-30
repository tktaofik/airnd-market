
.DEFAULT: help

help:
	@echo "make prepare-dev"
	@echo "    Create python virtual environment."
	@echo "make start"
	@echo "    Run server."
	@echo "make start_watch"
	@echo "    Run server and watch for changes"
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
lint: 

test: 

build:

clean:
	@rm -rf ENV

install:
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@pip freeze > requirements.txt