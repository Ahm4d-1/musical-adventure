## Candidate (Ahmad Alturki) Phase 3 Feedback

- straightforward, had a small problem to execute the celery using python shell to test the task.
- had to update couple files from previous phases for better code quality.

## Setup
- make sure required services are running `make up`
- go to phase_3 directory `cd phase_3`
- open a pipenv shell `pipenv install`
- open a terminal and update pythonpath `export PYTHONPATH="$(pwd)/investor_bulletin"`
- move to celery worker dir `cd investor_bulletin/worker`
- run the celery worker `celery -A app worker --loglevel=INFO`
- open a new terminal window
- move to celery worker dir `cd investor_bulletin/worker`
- run the celery worker `celery -A app beat --loglevel=INFO`

## Explanation
This phase combines previous phases into a full application with background tasks and a scheduler. It improves efficiency, scalability, and reliability while providing real-time updates. However, it adds complexity, resource consumption, and potential concurrency issues.

# PHASE THREE (Background tasks)

![phase_three](../imgs/phase-three.jpg)

## Technology used

* Background task - [Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)
* Schedular - [celery beat](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html)

## Objectives

to be able to fetch the market data periodically every hour and check if any of any of the stocks crossed those thresholds that was sets by the users in our rules table and fire an event to alert the user based on that

## Functionality

* Background task to fetch market data for symbols mentioned in phase one

* publish event for each symbol synced with the new price

* schedule to trigger the task every hour

## TASKS Breakdown

- [x] **Copy all your work in phase two**
--
- [x] **Configure Celery app**
--
- [x] **Create a celery task that use the market_service.py to fetch the market data and use the rules_service.py to get all the users rules**
--
- [x] **Inside the celery publish `THRESHOLD_ALERT` event if there is a threshold crossover**
--
- [x] **Run the celery worker and make sure everything is working and the subscriber from phase two managed to consume the event**
--
- [x] **create a celery beat that runs the task every 5 min**

## What's next

* **If you complete the tasks**, just send an email with the a link of your work in your github, tell us more about your comfort level out of 5 and what was the most challenging part and the most rewarding part.
--

* **If you stuck, or it took so long** it ok, we understand just send an email with the a link of your work in your github, tell us more about your comfort level out of 5 and how much did you actually completed from the task out of 7, where are you stuck or what took the most of your time
