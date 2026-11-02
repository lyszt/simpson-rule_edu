.PHONY: run all 

all:
	python -m venv venv 
	. venv/bin/activate
	pip install -r requirements.txt
run: 
	python main.py