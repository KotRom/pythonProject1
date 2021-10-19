import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with smtplib.SMTP_SSL('smtp.zone.eu', 465) as server:
    server.login('python@mrartful.com', 'qwe576!sdf')

    msg = MIMEMultipart()
    msg['From'] = 'Python automatic script'
    msg['To'] = 'rkotenjov@gmail.com'
    msg['Subject'] = 'This is test mail'
    body = f'<h1 style="color:red;"> Hello world </h1>'

    msg.attach(MIMEText(body, 'html'))
    text = msg.as_string()

    server.sendmail('python@mrartful.com', 'rkotenjov@gmail.com', text)

