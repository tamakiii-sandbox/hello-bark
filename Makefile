.PHONY: help install uninstall

help:
	@cat $(firstword $(MAKEFILE_LIST))

install:
	python3 -m pip install git+https://github.com/suno-ai/bark.git

uninstall:
	python3 -m pip uninstall git+https://github.com/suno-ai/bark.git
