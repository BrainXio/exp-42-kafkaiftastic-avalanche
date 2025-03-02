# Makefile for exp-42-kafkaiftastic-avalanche workflows
.PHONY: all install format lint test build run-producer run-consumer clean

all: install format lint test build

install:
	poetry install --no-root

format:
	poetry run black --line-length 79 src/ tests/

lint:
	poetry run black --check --line-length 79 src/ tests/
	poetry run flake8 src/ tests/

test:
	poetry run pytest tests/

build:
	docker build --build-arg BUILD_DATE=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") -t exp-42-kafkaiftastic-avalanche .

run-producer:
	poetry run python src/producer.py

run-consumer:
	poetry run python src/consumer.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.pyc" -exec rm -r {} +
