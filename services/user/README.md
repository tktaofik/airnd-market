# User-Service

## Description

The User service provides an API for managing users, authenticating requests from the client and service to service communication.

## API

- [ ] Create user
- [ ] Update user
- [ ] Get user
- [ ] Login
- [ ] Logout
- [ ] Authenticate requests (Create JWT)
- [ ] Expire JWT after 5 min
- [ ] Extend JWT if used under 5 min

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
