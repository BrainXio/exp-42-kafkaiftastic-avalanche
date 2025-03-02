# Makefile for exp-42-kafkaiftastic-avalanche workflows
.PHONY: all install format lint test pre-commit-checks build run-producer run-consumer clean

all: install format lint test pre-commit-checks

install:
	poetry install --no-root

format:
	poetry run tools/fix_eof.py
	poetry run tools/format_python.py
	poetry run tools/format_json.py
	poetry run tools/format_yaml.py
	poetry run tools/format_markdown.py
	poetry run tools/fix_whitespace.py

lint:
	poetry run tools/lint.py

test:
	poetry run tools/test.py

pre-commit-check:
	poetry run pre-commit migrate-config
	poetry run tools/pre_commit_check.py

run-producer:
	poetry run tools/run_producer.py

run-consumer:
	poetry run tools/run_consumer.py

docker-build:
	poetry run tools/build.py

compose-up: build
	docker compose up -d

compose-logs: compose-up
	docker compose logs

compose-down:
	docker compose down -v

clean: compose-down
	poetry run tools/clean.py
