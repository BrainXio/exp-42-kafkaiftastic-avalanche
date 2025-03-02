import os
import time
import logging
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_messages(bootstrap_servers: str, topic: str) -> None:
    """Consume messages from a Kafka topic and apply basic sentiment analysis.

    Args:
        bootstrap_servers (str): The Kafka server address.
        topic (str): The topic to consume messages from.
    """
    max_retries = 20
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            logger.info(
                f"Attempting to connect to Kafka at {bootstrap_servers}, attempt {attempt + 1}/{max_retries}"
            )
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=bootstrap_servers,
                auto_offset_reset="earliest",
            )
            logger.info("Connected to Kafka. Listening for messages...")
            break
        except NoBrokersAvailable as e:
            logger.warning(
                f"No brokers available: {e}. Retrying in {retry_delay} seconds..."
            )
            if attempt == max_retries - 1:
                logger.error("Max retries reached. Giving up.")
                raise
            time.sleep(retry_delay)

    # Continuous loop to keep consuming
    while True:
        try:
            # Poll for messages with a timeout
            msg_pack = consumer.poll(timeout_ms=1000)  # 1 second timeout
            if not msg_pack:
                logger.info("No messages received, waiting...")
                continue

            for _, messages in msg_pack.items():
                for message in messages:
                    text = message.value.decode("utf-8")
                    sentiment = "positive" if "avalanche" in text.lower() else "neutral"
                    logger.info(f"Message: {text} | Sentiment: {sentiment}")
        except Exception as e:
            logger.error(f"Error while consuming messages: {e}")
            time.sleep(retry_delay)  # Avoid tight loop on error


if __name__ == "__main__":
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "avalanche-topic")
    process_messages(bootstrap_servers, topic)
