# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -d --name server1-container -p 8000:8000 --mount source=fastapi-db,target=/app/db shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -d --name server2-container -p 8080:8080 --mount source=fastapi-db,target=/app/db shopping-server2:v1
```

