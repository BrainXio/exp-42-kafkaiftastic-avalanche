# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN apk add --no-cache gcc musl-dev && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --without dev --no-root

# Stage 2: Runtime
FROM python:3.11-alpine

# Build argument for dynamic creation date
ARG BUILD_DATE

# OCI-compliant labels
LABEL org.opencontainers.image.title="exp-42-kafkaïftastic-avalanche"
LABEL org.opencontainers.image.description="A Kafka pipeline in an Alpine container with AI artifacts"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.authors="Brain-X <github@brain-x.io>"
LABEL org.opencontainers.image.source="https://github.com/brainxio/exp-42-kafkaiftastic-avalanche"
LABEL org.opencontainers.image.created=$BUILD_DATE

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY src/ ./src/

ENTRYPOINT ["python", "src/consumer.py"]