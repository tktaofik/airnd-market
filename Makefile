
.DEFAULT: help

help:
	@echo "make python_venv"
	@echo "    Create python virtual environment."
	@echo "make clean"
	@echo "    Delete python virtual env and clean pycache."

python_venv:
	@make clean
	@which pyenv || pyenv install 3.8.0
	@which virtualenv || python3 -m pip install virtualenv
	@virtualenv python_venv	

clean:
	@rm -rf python_venv
	@rm -rf `find . -name __pycache__`