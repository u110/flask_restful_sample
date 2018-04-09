all:
	cat Makefile

run:
	env/bin/python my_restful/app.py

test:
	env/bin/pytest tests -v
