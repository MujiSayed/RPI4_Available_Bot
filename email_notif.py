import smtplib
import config as conf
from textwrap import dedent
import numpy as np

def email_notif(product_url, product_name):

    if conf.email_to != "" and conf.email_username != "":
        print(f"Sending email to {conf.email_to}")
        if np.array(conf.email_to).size == 1:
            To = conf.email_to
        else:
            To = ', '.join(conf.email_to)  

        From = conf.email_username
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
            server.login(conf.email_username, conf.email_pass)
            server.sendmail(From, To, email_msg)
            server.close()

            print(email_msg)
        except Exception as e:
            print("There's an issue with your email configs", e)
        
    else:
        print("No email sent")