import smtplib
import config as conf


sent_from = conf.email_user
to = conf.to_address
subject = 'OMG Super Important Message 546464'
body = "Hey, what's up?\n\n- You"

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
