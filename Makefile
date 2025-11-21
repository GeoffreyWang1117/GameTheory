# Makefile for Game Theory Learning Platform

.PHONY: help install test clean run watch list format lint

help:
	@echo "Game Theory Learning Platform - Makefile"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make run        - Start interactive mode"
	@echo "  make watch      - Start watch mode"
	@echo "  make list       - List all exercises"
	@echo "  make test       - Run tests"
	@echo "  make format     - Format code with black"
	@echo "  make lint       - Run linters"
	@echo "  make clean      - Remove cache files"

install:
	pip install -r requirements.txt

run:
	python run.py

watch:
	python run.py watch

list:
	python run.py list

test:
	pytest tests/ -v

format:
	black gametheory/ exercises/ tests/

lint:
	flake8 gametheory/ --max-line-length=100
	pylint gametheory/ --max-line-length=100

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
	rm -f exercises/.progress

.PHONY: dev-install
dev-install: install
	pip install pytest black flake8 pylint

.PHONY: verify-exercise
verify-exercise:
	@if [ -z "$(EXERCISE)" ]; then \
		echo "Usage: make verify-exercise EXERCISE=path/to/exercise.py"; \
		exit 1; \
	fi
	python "$(EXERCISE)"
