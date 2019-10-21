default:
	cat makefile

env:
	python3 -m venv env

pip_install: env
	. env/bin/activate; pip install -r requirements.txt 

session:
	ipython -i do/load_facts.py
