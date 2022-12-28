# Telegram Wikipedia Bot

## Description
A bot for using wikipedia right in the telegram app

## How to use the bot

This bot receives your message and does a quick wikipedia search, giving you a short summary.
Available commands:

- `/start` — exchange greetings with the bot:

  ![](img/start.png)

- `/help` — see available commands:

  ![](img/help.png)

- `/eng` search articles in English:

  ![](img/fate_eng.png)

- `/rus` — search articles in Russian:

  ![](img/fate_rus.png)


## Getting started

### Setting up credentials

First, go to the [BotFather](https://t.me/BotFather) and get your own bot token.
After that, you need to input it to `API_TOKEN` variable in `main.py`.

### Run the app with Docker

To run the bot with Docker, just follow this steps.

First, build Docker image:

```
docker build -t telepediabot .
```

Then, run the application:

```
docker run telepediabot
```

### Running without Docker

To begin, clone this repository:
```
git clone https://github.com/denis-shvetcov/telegram-wikipedia.git
```
Then follow this steps:
- Get Python `ver. 3.10` or newer
- Run the requirements installation `pip install -r requirements.txt`
- Run the main file `python main.py`

Now you're all set. Have fun.

