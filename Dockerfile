FROM python:3.8.0


COPY . /app

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean


WORKDIR app

RUN pip install -r requirements.txt

RUN echo 'import os\n\
discord_webhook = os.environ.get("DISCORD_WEBHOOK")\n\
discord_user = os.environ.get("DISCORD_USER")\n\
email_to = os.environ.get("EMAIL_TO")\n\
email_username = os.environ.get("EMAIL_USERNAME")\n\
email_pass = os.environ.get("EMAIL_PASS")\n\
smtp_server = os.environ.get("SMTP_SERVER")\n\
smtp_ssl_port = os.environ.get("SMTP_SSL_PORT")\n\
interval = os.environ.get("INTERVAL")\n\
carrier = os.environ.get("CARRIER")\n\
phone_number = os.environ.get("PHONE_NUMBER")' > ./config.py

CMD [ "python3", "scraper.py" ]