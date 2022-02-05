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


def sms_notif(product_url, product_name):
    if conf.phone_number != "" and conf.carrier != "":

        print(f"Sending SMS to {conf.phone_number}")

        for carrier in conf.carrier:
            if conf.carrier == "tmobile":
                phone_number = conf.phone_number + "@tmomail.net"
            elif conf.carrier == "vmobile":
                phone_number = conf.phone_number + "@vmobl.com"
            elif conf.carrier == "att":
                phone_number = conf.phone_number + "@txt.att.net"
            elif conf.carrier == "sprint":
                phone_number = conf.phone_number + "@messaging.sprintpcs.com"
            elif conf.carrier == "verizon":
                phone_number = conf.phone_number + "@vtext.com"
            elif conf.carrier == "tracfone":
                phone_number = conf.phone_number + "@mmst5.tracfone.com"
            elif conf.carrier == "ting":
                phone_number = conf.phone_number + "@message.ting.com"
            elif conf.carrier == "boost":
                phone_number = conf.phone_number + "@myboostmobile.com"
            elif conf.carrier == "usc":
                phone_number = conf.phone_number + "@email.uscc.net"
            elif conf.carrier == "metro":
                phone_number = conf.phone_number + "@mymetropcs.com"

        From = conf.email_username
        To = phone_number
        Subject = f"RPI{product_name} available"
        Body = f"RPI{product_name} is now available at {product_url}"
        Msg = dedent(f"""
        From: {From}
        To: {To}
        Subject: {Subject}
        \n""") + Body
        sms_msg = Msg.strip()

        try:
            server = smtplib.SMTP_SSL(conf.smtp_server, conf.smtp_ssl_port)
            server.login(conf.email_username, conf.email_pass)
            server.sendmail(From, To, sms_msg)
            server.close()
            print('SMS Text sent successfully')
        except Exception as e:
            print("failed to send sms, check email settings", e)

    else:
        print("Phone or carrier not set")