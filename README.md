# Telegram API Cleaner
This is a simple script to clear messages from the Telegram API. But, since its not possible to completely delete those, this software just marks messages as "confirmed", which makes them not appear on the default API responses. It also deletes any webhook associated with the bot to ensure that no old messages will get delivered that way either.

## How to use
Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and run the following:

```
docker run --env TELEGRAM_TOKEN=<your_token> laury/telegram-api-cleaner:latest
```

## Development
To develop locally, I recommend building a local image and running it with a volume mounted to get code changes.

```
docker build -t telegram-api-cleaner:dev .

docker run -it --env-file .env -v ${PWD}:/app telegram-api-cleaner:dev bash
```
