
from email.message import EmailMessage
import ssl
import smtplib

email_sender="**************"
email_password="***************" #this password is generated from google account. see resource
email_receiver="*************"

subject="Send email with python"
body='''A SMOOTH SEA NEVER MADE A SKILLED SAILOR'''

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


#Resource: https://www.youtube.com/watch?v=zxFXnLEmnb4