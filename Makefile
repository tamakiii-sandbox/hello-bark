.PHONY: help install uninstall

help:
	@cat $(firstword $(MAKEFILE_LIST))

install:
	python3 -m poetry install

uninstall:
	rm -rf $$(python3 -m poetry env -p)
