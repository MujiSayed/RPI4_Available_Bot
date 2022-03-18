
A simple HTML parser that checks to see if the raspberry pi 4 is in stock at adafruit.com

## Requirements

1. Discord Bot Token 
2. Python3 & pip
3. Email smtp, if you have a gmail with 2fa, check (This)[https://support.google.com/mail/answer/185833?hl=en]


To run this Bot, simply run the following commands:

```
$ apt-get install python3
$ apt-get install python3-pip
$ git clone https://git.mujisayed.com/basedmeezus/RPI4_Available_Bot.git
$ cd RPI4_Available_Bot
$ pip3 install -r requirements.txt
$ python3 scraper.py
```
NOTE: This has only been tested on debian based systems



SMS Carrier Settings:

    T-Mobile --- tmobile
    Virgin Mobile --- vmobile
    AT&T --- att
    Sprint --- sprint
    Verizon --- verizon
    Tracfone --- tracfone
    Ting --- ting
    Boost Mobile --- boost
    U.S. Cellular --- usc
    Metro PCS --- metro


Running via docker:

```
$ docker pull basedmeezus/rpi_availibility_bot:latest

$ docker run \
-e DISCORD_WEBHOOK= \
-e DISCORD_USER= \
-e EMAIL_TO= \
-e EMAIL_USERNAME= \
-e EMAIL_PASS= \
-e SMTP_SERVER= \
-e SMTP_SSL_PORT= \
-e INTERVAL=300 \
-e CARRIER= \
-e PHONE_NUMBER= \
basedmeezus/rpi_availibility_bot
```

## Guides

1. 2FA Gmail SMTP, check **[This](https://support.google.com/mail/answer/185833?hl=en)**
2. Discord Bot Token **[Guide](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot)**