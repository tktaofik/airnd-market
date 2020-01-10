# User-Service

## Description

The User service provides an API for managing and authenticating users in the system

## API

- [ ] Create a user
- [ ] Update a user
- [ ] Login user
- [ ] Get a user
- [ ] Authenticate user
- [ ] Renew user token

## Model

```json
{
  "id": String,
  "firstName": String,
  "lastName": String,
  "email": String,
  "createdAt": Date,
  "updatedAt": Date
}
```

## Data Sources

- N/A

## Logic/Rules

- N/A

## Health Endpoints

- `/health` App is up and running
- `/ready` App is up and all dependencies are up and avaialble

## API

`Link to swagger doc`

## Events Published

- `user.created`

## Event Subscriptions

- N/A

## Service Dependencies

- N/A

## Key Metrics

- N/A

## Non Functional Requirements

- 99.99% availability
- High usage

## Architecture

- Database `MongoDB`
- HTTP server `aiohttp`
- Messaging `Nats`
- Metrics `??`
- Monitoring `Sentry`
- Logging `Sentry`

## Development

- Navigate into service directory `services/user`
- Add environment variables by creating file `.env` and add the following

```
PORT=8082
```

- Install _dependencies_ `make install`
- Start _postgreSQL_ `make database`
- Start service `make start`
