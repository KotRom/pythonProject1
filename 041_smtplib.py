import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with smtplib.SMTP('smtp.zone.eu', 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('python@mrartful.com', 'qwe576!sdf')

    msg = MIMEMultipart()
    msg['From'] = 'Python automatic script'
    msg['To'] = 'rkotenjov@gmail.com'
    msg['Subject'] = 'This is test mail'
    body = f'<h1 style="colour: red;"> Hello world </h1>'

    msg.attach(MIMEText(body, 'html'))
    text = msg.as_string()

    server.sendmail('python@mrartful.com', 'rkotenjov@gmail.com', text)

