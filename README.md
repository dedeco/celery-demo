# How to run this project

## Build the images and run the containers:

```
docker-compose up -d --build
```

## Components running on docker:
- scheduler: celery
- worker: celery
- api: using flask api
- redis: backend and broker celery 


## Examples

### Add numbers

Request:
```
curl --location --request GET 'http://0.0.0.0:8000/numbers?a=4&b=71'
```

Response:
```
{
    "url": "/tasks?task_id=7564b6c0-1b1f-478f-b2d3-a57a318c82f8"
}
```

### Get result of this long-running task

Request:
```
curl --location --request GET 'http://0.0.0.0:8000/tasks?task_id=dc023ce4-2a20-4c21-8078-c65a5af9515a'
```

After just 1 second will be:

Response:
```
{
    "state": "PENDING",
    "result": null
}
```

After 30 seconds:

Response:
```
{
    "state": "SUCCESS",
    "result": 75
}
```
