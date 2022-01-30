import smtplib
import config as conf


def email_notif(product_url, rpi_name):
    sent_from = conf.email_user
    to = conf.to_address
    subject = f"RPI{rpi_name} available"
    body = f"RPI{rpi_name} is now available at {product_url}"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL(conf.smtp_server, conf.smtp_ssl_port)
        server.ehlo()
        server.login(conf.email_user, conf.email_pass)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
    return