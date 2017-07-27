# Zilean Makefile

# Shell
SHELL := /bin/bash
#Project
PROJECT = "Zilean"
#Version
RELEASE = "0.0.1"
#Authors
AUTHORS = ""
# Compiler
PYTHON ?= python3
# SQL files
SQLDIR = "zilean/"
# Path to source directory
ZILEAN_PATH := .
# OS machine
OS_TYPE = 'uname -a'
# PYTHON EXTENSIONS
PY_EXT = ".py"
# SQL SCRIPTS EXTENSIONS
SQL_EXT = ".sql"

getreq:
	@echo "[INFO] Installing requirements"
	pip install -r requirements.txt

getbreq:
	@echo "[INFO] Installing Babtu requirements"
	babtu --makebreq breq.txt

zilean_python_install:
	@echo "[INFO] Installing Zilean python package"
	python3 setup.py install

zilean_make_dependencies:
	python3 setup.py makedependencies

zilean_initial_configuration:
	python3 zilean.py config --init

zilean_cmd_install:
	bash zilean_cmd.sh makezilean

clearzileancache:
	python3 zilean.py clearcache

test:
	echo "[INFO] Testing Zilean"
	python setup.py test

reported_test:
	echo "[INFO] Test Zilean with reports"
	sudo python setup.py rtest

clean:
	rm -f MANIFEST
	rm -rf build dist

.PHONY: clean
