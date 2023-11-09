.PHONY: help install run uninstall

help:
	@cat $(firstword $(MAKEFILE_LIST))

install:
	python3 -m poetry install

run:
	python3 -m poetry run ipython main.py

uninstall:
	rm -rf $$(python3 -m poetry env -p)
