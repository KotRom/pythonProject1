import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#MIME - Multipurpose Internet Mail Extension

#Here just add a SMTP details of your server
server = smtplib.SMTP('smtp.zone.eu', 587)
server.ehlo()
server.starttls()
server.ehlo()
#Next, log in to the server
server.login("python@mrartful.com", "dsf342asda")

fromaddr = "python@mrartful.com"
toaddr = "sample@example.com"  # Email address where email needs to be sent
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"
body = "Python test mail sent at " + str(datetime.now())
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

#Send the mail
#msg = "Hello!" # The /n separates the message from the headers
server.sendmail("python@mrartful.com", "sample@example.com", text)