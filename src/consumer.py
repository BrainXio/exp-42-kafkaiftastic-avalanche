from kafka import KafkaConsumer


def process_messages(bootstrap_servers: str, topic: str) -> None:
    """Consume messages from a Kafka topic and apply basic sentiment analysis.

    Args:
        bootstrap_servers (str): The Kafka server address.
        topic (str): The topic to consume messages from.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset="earliest",
    )
    print("Listening for messages...")
    for message in consumer:
        text = message.value.decode("utf-8")
        sentiment = "positive" if "avalanche" in text.lower() else "neutral"
        print(f"Message: {text} | Sentiment: {sentiment}")


if __name__ == "__main__":
    process_messages("localhost:9092", "avalanche-topic")
