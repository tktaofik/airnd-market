# Job-Service

## Description

The Job service provides an API for creating, fetching, updating and deleting jobs

## Tasks

- [ ] Create a job
- [ ] Update a job
- [ ] Delete a job
- [ ] Get a job
- [ ] Get jobs owned by a user

## Data Sources

- N/A

## Logic/Rules

- Only authorized users can create jobs
- Only job owner can delete/update a job
- Job status (new, inProgress, cancelled, done)

## Health Endpoints

- `/health` App is up and running
- `/ready` App is up and all dependencies are up and avaialble

## API

`Link to swagger doc`

## Events Published

- `job.created`
- `job.updated`
- `job.deleted`

## Service Dependencies

- N/A

## Event Subscriptions

- N/A

## Key Metrics

- [ ] Succeful requests
- [ ] Internal server errors
- [ ] Unauthorized requests

## Non Functional Requirements

- 99.99% availability
- High usage

## Architecture

- Database `MongoDB`
- Framework Python `Django`
- Messaging `NATS`
- Metrics `??`
- Logging `??`

## Development

### Install dependencies and virtual environment

- Install _brew_ on your system
- Install _nodeJS_ globally on your system
- Install _nodemon_ globally on your system run `npm i -g nodemon`
- Install _pyenv_ to install multiple versions of python `brew install pyenv`
- Install virtual environment `make prepare-dev`
- Activate dev virtual environment run `source ./ENV/bin/activate`
- Install _dependencies_ run `make install`

### Run service

- Run service run `make run`
- Run service in watch mode run `make run_watch`

### Exit virtual environment

- While in virtual environment run `deactivate`
