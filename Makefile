all:
	cat Makefile

setup: env pip

env:
	python -m virtualenv env -p python3

pip:
	env/bin/pip install requirements.txt
	env/bin/pip install -e .

run:
	env/bin/python my_restful/app.py

test:
	env/bin/pytest tests -v
