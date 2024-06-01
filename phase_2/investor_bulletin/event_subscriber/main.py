import pika
import json

from db.models.model_base import get_db
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_service import create_new_alert

# Connection parameters
host = 'localhost'
username = 'guest'
password = 'guest'
queue_name = 'events'

def callback(ch, method, properties, body):
    event = json.loads(body)
    print(f"Received event: {event}")

    # Extract necessary data from the event
    alert_data = AlertCreate(
        name=event["name"],
        threshold_price=event["threshold_price"],
        symbol=event["symbol"]
    )

    db = next(get_db())

    create_new_alert(alert_data, db)

def consume_events(host, username, password, queue_name):
    # Create a connection to the RabbitMQ server
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=credentials))

    # Open a channel
    channel = connection.channel()

    # Declare the queue (it should match the queue to which events are published)
    channel.queue_declare(queue=queue_name, durable=True)

    # Bind the queue to the exchange (if necessary)
    channel.queue_bind(exchange='events', queue=queue_name, routing_key='events')

    # Set up subscription on the queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("Waiting for events. To exit press CTRL+C")
    try:
        # Start consuming
        channel.start_consuming()
    except KeyboardInterrupt:
        # Graceful shutdown
        channel.stop_consuming()
        connection.close()
        print("Consumer stopped.")

if __name__ == "__main__":
    consume_events(host, username, password, queue_name)
