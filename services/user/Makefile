
.DEFAULT: help

help:
	@echo "make install"
	@echo "    Install service dependencies and initialize postgreSQL database"
	@echo "make database"
	@echo "    Install and initialize mongoDB database"
	@echo "make start"
	@echo "    Run server on watch mode"
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv"
	@echo "make requirements_txt"
	@echo "    Export lock file into requirements.txt"
	@echo "make docker-compose"
	@echo "    Run service with docker-compose"

start:
	@poetry run nodemon main.py 
	
database:
	@docker-compose down
	@docker-compose run -d -p 5432:5432 --name=user_postgres postgres
	@sleep 10
	@make install
	@poetry run python init-postgres.py

install:
	@poetry install
	@poetry export -f requirements.txt > requirements.txt

build:
	@make install
	@docker build -t user .

clean:
	@rm -rf `find . -name __pycache__`
	@rm -rf .venv
	@rm -rf poetry.lock
	@rm -rf requirements.txt
	@rm -rf user.egg-info

docker-compose:
	@docker-compose down && docker-compose up --build --remove-orphans

docker-compose-init:
	@nodemon main.py 
