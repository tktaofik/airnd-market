# Job-Service

## Description
The Job service provides an API for creating, fetching, updating and deleting jobs

## Tasks           
- [ ] Create a job
- [ ] Update a job
- [ ] Delete a job
- [ ] Get  a job
- [ ] Get jobs for a user

## Data Sources
- N/A

## Logic/Rules
- Only authorized users can create jobs
- Only job owner can delete/update a job
- Job status (new, inProgress, cancelled, done)

## Health Endpoints
- `/health` App is up and running
- `/ready`  App is up and all dependencies are up and avaialble

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
- [ ] Order created
- [ ] Order deleted
- [ ] Order not found
- [ ] Internal server errors
- [ ] Unauthorized requests from users
                                              

## Non Functional Requirements 
- 99.99% availability
- High usage

## Architecture
- Database `MongoDB`
- Framework Python `Django` 
- Messaging `NATS`
- Metrics `??`
- Logging `??`
