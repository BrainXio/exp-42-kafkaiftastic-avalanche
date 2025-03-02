import os
import time
import logging
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_messages(bootstrap_servers: str, topic: str) -> None:
    """Send dummy messages to a Kafka topic.

    Args:
        bootstrap_servers (str): The Kafka server address.
        topic (str): The topic to send messages to.
    """
    max_retries = 20
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            logger.info(
                f"Attempting to connect to Kafka at {bootstrap_servers}, "
                f"attempt {attempt + 1}/{max_retries}"
            )
            producer = KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: v.encode("utf-8"),
            )
            logger.info("Connected to Kafka. Starting to send messages...")
            break
        except NoBrokersAvailable as e:
            logger.warning(
                f"No brokers available: {e}. Retrying in "
                f"{retry_delay} seconds..."
            )
            if attempt == max_retries - 1:
                logger.error("Max retries reached. Giving up.")
                raise
            time.sleep(retry_delay)

    # Send dummy messages in a loop
    message_count = 0
    while True:
        try:
            message = f"Dummy message {message_count}: Avalanche is coming!"
            producer.send(topic, value=message)
            logger.info(f"Sent: {message}")
            message_count += 1
            time.sleep(1)  # Delay tussen berichten
        except Exception as e:
            logger.error(f"Error while sending message: {e}")
            time.sleep(retry_delay)


if __name__ == "__main__":
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "avalanche-topic")
    send_messages(bootstrap_servers, topic)
