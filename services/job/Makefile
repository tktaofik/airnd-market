
.DEFAULT: help

help:
	@echo "make start"
	@echo "    Run server."
	@echo "make start_watch"
	@echo "    Run server and watch for changes"
	@echo "make service_dependencies"
	@echo "    Install service dependencies and create database"
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."
	@echo "make install"
	@echo "    Install packages."


start:
	@python app.py 

start_watch:
	@nodemon app.py  
	
service_dependencies:
	@docker-compose up --remove-orphans -d
	@sleep 10
	@make teardown_db
	@python init_db.py

teardown_db:
	@python teardown_db.py

clean:
	@rm -rf `find . -name __pycache__`
	@rm -rf .venv

install:
	@poetry install

export_dependencies:
	@poetry export -f requirements.txt > requirements.txt