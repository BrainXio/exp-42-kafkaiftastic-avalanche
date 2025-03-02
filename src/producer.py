import os
import time
from kafka import KafkaProducer


def send_messages(bootstrap_servers: str, topic: str) -> None:
    """Send a series of test messages to a Kafka topic.

    Args:
        bootstrap_servers (str): The Kafka server address.
        topic (str): The topic to send messages to.
    """
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    for i in range(10):
        message = f"Message {i}: Avalanche incoming!"
        producer.send(topic, message.encode("utf-8"))
        print(f"Sent: {message}")
        time.sleep(1)
    producer.flush()


if __name__ == "__main__":
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "avalanche-topic")
    send_messages(bootstrap_servers, topic)
