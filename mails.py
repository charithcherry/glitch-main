import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailing(receiver):
    sender = 'charith1tryout@gmail.com'
    password = 'charithcherry'
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'CONFIRMATION E-mail'
    text = 'Welcome To ChitChat Family , Hope You Have A Great Experience'
    part1 = MIMEText(text, 'plain')
    message.attach(part1)

    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com:587')
        smtpobj.starttls()
        smtpobj.login(sender, password)
        smtpobj.sendmail(sender, receiver, message.as_string())
        print("success")
    except Exception:
        print("error")


