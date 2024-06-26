## Candidate (Ahmad Alturki) Phase 2 Feedback

- most challenging: I noticed in the tasks the publisher will publish an event and THEN we would run the consumer, took me some time to make the messages persistent.
- I like how tasks are divided, clear objective for each phase.

## Setup
- make sure required services are running `make up`
- go to phase_2 directory `cd phase_2`
- open a pipenv shell `pipenv install`
- open a terminal and update pythonpath `export PYTHONPATH="$(pwd)/investor_bulletin"`
- run the publisher `python3 investor_bulletin/core/messaging.py`
- run the consumer `python3 investor_bulletin/event_subscriber/main.py`

## Explanation
Phase two introduces asynchronous messaging, which offers benefits such as improved scalability and fault tolerance. However, it also adds complexity compared to synchronous communication. Consider the tradeoffs and evaluate whether the benefits outweigh the added complexity.

## Functionality

- **Publish a `THRESHOLD_ALERT` event**
- **Consume the `THRESHOLD_ALERT` event and print the message aka the alert**

## TASKS Breakdown

- [x] **Copy all your work in phase one**
--
- [x] **Set up your environment**
 Whether on your machine or using docker, make sure you have a running rabbitmq broker
--
- [x] **Get to know Rabbitmq and Configure the queues**
--
- [x] **Create a publisher connection using amqpstorm inside the core/messaging.py file**
--
- [x] **Publish a `THRESHOLD_ALERT` event by running the core/messaging.py file**
--
- [x] **Create a consumer connection using pika inside the event_subscriber/main.py**
--
- [x] **Consume the published event and print the message by running the the event_subscriber/main.py**
--
- [x] **Create an event record by using the alert_service.py**

## What's next

- **If you complete the tasks**, just send an email with the a link of your work in your github, tell us more about your comfort level out of 5 and what was the most challenging part and the most rewarding part.
--

- **If you stuck, or it took so long*- it ok, we understand just send an email with the a link of your work in your github, tell us more about your comfort level out of 5 and how much did you actually completed from the task out of 7, where are you stuck or what took the most of your time
