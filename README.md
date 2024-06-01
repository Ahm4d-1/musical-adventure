# Instructions from Candidate (Ahmad Alturki)
This repo contains 3 phases. added them all here for easier access,  visibility, and organization in my opinion.

You can find feedback about each phase in the corresponding README file.

It is reasonable to only test PHASE_3 since it includes all previous phases as well.

- [Phase One - Getting to know FastAPI](./phase_1/README.md)
- [Phase Two - Creating Publisher and Subscriber](./phase_2/README.md)
- [Phase Three - Background tasks](./phase_3/README.md)

## Overall Candidate feedback
- All 3 phases took me a total of around 4 to 5 hours to complete all tasks. which is a real commitment, I think only someone who is really interested in working with Malaa would commit to finishing this project.

- I was not able to start working on the project during the week, had very limited time, so I spent the weekend doing it.

- I think the project gives a slight view on how engineering is at the company, how focused on code quality, correct patterns and principles the team is. It comforts the candidate somewhat as well, everyone wants to work with great people who they could level up with.

- This project is focused on clear objectives, things like tests and authentication are important for real-world projects but are not relevant here.

---

# Investor Bulletin Project

![Welcome](./imgs/hello-welcome.gif)

> 🚨 This project doesn’t cover all tech/tools in Malaa stack and is only meant to give the initial boost and confidence to start working on Malaa’s codebase
>
## Objectives

You will create a simple API using FastAPI (python web framework), events published & consumed through RabbitMQ, and background tasks managed by Celery to sync stock market data and provide threshold alerting based on user interests.

## Project Context

Stock investments provide one of the highest returns in the market. Even though they are volatile in nature, one can visualize share prices and other statistical factors, which helps keen investors carefully decide on which company they want to spend their earnings on.

This project will allow users to retrieve the latest stock market prices and create alert rules by setting a threshold price for the stock they are interested in and receiving alerts if stocks cross those thresholds.

## High-Level Approach

![high-level](imgs/high-level.png)

## Project phases

- [Phase One - Getting to know FastAPI](./phase_1/README.md)
- [Phase Two - Creating Publisher and Subscriber](./phase_2/README.md)
- [Phase Three - Background tasks](./phase_3/README.md)

## Using Docker Setup

You can make your own setup / but to speed you up, you can use the provided setup. Just ensure you have the docker installed and the docker-compose, then run `make up` to start the containers.

## Deliverables

The solution should be submitted by phase as a GitHub repository with the following:

- Source code with clear comments and documentation.
- Instructions on how to run the code.
- A brief explanation of the solution and any trade-offs made.
## Evaluation

The solution will be evaluated based on the following criteria:

- Correctness and completeness of the solution.
- Code quality and engineering practices.
- Documentation and comments.
- Ease of setup and configuration.
- Solution architecture and design decisions.
- Adherence to the requirements.
