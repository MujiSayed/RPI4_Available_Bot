import smtplib
import config as conf
from textwrap import dedent

def email_notif(product_url, product_name):
    From = conf.email_user
    To = conf.to_address
    print(To)
    Subject = f"RPI{product_name} available"
    Body = f"RPI{product_name} is now available at {product_url}"
    Msg = dedent(f"""
    From: {From}
    To: {To}
    Subject: {Subject}
    \n""") + Body
    email_msg = Msg.strip()

    try:
        server = smtplib.SMTP_SSL(conf.smtp_server, conf.smtp_ssl_port)
        server.login(conf.email_user, conf.email_pass)
        server.sendmail(From, To, email_msg)
        server.close()

        print(email_msg)
    except Exception as e:
        print("There's an issue with your email configs", e)
