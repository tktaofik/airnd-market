# Job-Service

## Description

The Job service provides an API for creating, fetching, updating and deleting jobs

## Tasks

- [ ] Create a job
- [ ] Update a job
- [ ] Delete a job
- [ ] Get a job
- [ ] Get jobs owned by a user

## Model

```json
{
  "id": String,
  "userId": String,
  "riderId": String,
  "title": String,
  "status": new | inProgress | cancelled | done,
  "address": String,
  "description": String,
  "createdAt": Date,
  "updatedAt": Date
}
```

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

- Database `PostgreSQL`
- HTTP server `aiohttp`
- Messaging `kafka`
- Metrics `??`
- Logging `??`

## Development

- Navigate into service directory `services/job`
- Add environment variables by creating file `.env` and add the following

```
PORT=8081
HOST=localhost

DATABASE=job
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
DB_PORT=5432
DB_POOL_MIN_SIZE=1
DB_POOL_MAX_SIZE=5
```

- Install service _dependencies_ and initialize _postgreSQL_ database run `make install`
- Start service run `make start`
