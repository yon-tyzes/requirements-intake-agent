PYTHON ?= python3

.PHONY: help install install-dev check strict build test lint format clean

help:
	@echo "install      install runtime dependencies"
	@echo "install-dev  install runtime and development dependencies"
	@echo "check        validate config files"
	@echo "strict       validate and fail on unfilled <placeholders>"
	@echo "build        validate and write dist/"
	@echo "test         run tests"
	@echo "lint         run Ruff"
	@echo "format       format Python with Ruff"
	@echo "clean        remove build output and caches"

install:
	$(PYTHON) -m pip install -r requirements.txt

install-dev:
	$(PYTHON) -m pip install -r requirements-dev.txt

check:
	$(PYTHON) scripts/build.py --check

strict:
	$(PYTHON) scripts/build.py --check --strict

build:
	$(PYTHON) scripts/build.py

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m ruff format --check .

format:
	$(PYTHON) -m ruff format .
	$(PYTHON) -m ruff check --fix .

clean:
	rm -rf dist .pytest_cache .ruff_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
