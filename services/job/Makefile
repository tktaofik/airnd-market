
.DEFAULT: help

help:
	@echo "make install"
	@echo "    Install service dependencies and initialize postgreSQL database"
	@echo "make start"
	@echo "    Run server."
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."
	@echo "make requirements_txt"
	@echo "    Export lock file into requirements.txt"

start:
	@make install
	@poetry run nodemon app.py 
	
service_dependencies:
	@docker-compose up --remove-orphans -d
	@sleep 10
	@make install
	@make teardown_db
	@poetry run python init_db.py

teardown_db:
	@poetry run python teardown_db.py

clean:
	@rm -rf `find . -name __pycache__`
	@rm -rf .venv
	@rm -rf requirements.txt
	@rm -rf job.egg-info

install:
	@poetry install

requirements_txt:
	@poetry export -f requirements.txt > requirements.txt