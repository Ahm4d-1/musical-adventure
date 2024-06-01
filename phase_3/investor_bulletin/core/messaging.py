import json
from amqpstorm import Connection, Message, AMQPError

# Connection parameters
host = 'localhost'
username = 'guest'
password = 'guest'


def publish_event(event):
    try:
        # Create a connection object to publish events
        with Connection(host, username, password) as broker:
            # Create a channel
            channel = broker.channel()

            # Declare the exchange if it doesn't exist
            channel.exchange.declare(exchange='events', exchange_type='topic', durable=True)

            # Create a persistent message
            message = Message.create(channel, json.dumps(event), properties={'delivery_mode': 2})

            # Publish the message
            message.publish(routing_key='alert.threshold', exchange='events')

            # Close the channel
            channel.close()

        print("Event published successfully.")

    except AMQPError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    event = {
        "type": "THRESHOLD_ALERT",
        "message": "Threshold exceeded",
        "name": "Price Drop Alert for AAPL (test event)",
        "threshold_price": 170.00,
        "symbol": "AAPL"
    }
    publish_event(event)
