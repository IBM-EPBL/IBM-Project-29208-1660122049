import smtplib
import sendgrid
import os
from dotenv import dotenv_values
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Interview Call"
s = smtplib.SMTP('smtp.gmail.com', 587)
envData=dotenv_values("./.env")
mailApi=envData['MAILAPI']

def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("il.prethi@gmail.com", "oms@1Ram")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("il.prethi@gmail.com", email, message)
    s.quit()
def sendgridmail(user,TEXT):
    sg = sendgrid.SendGridAPIClient(mailApi)
    from_email = Email("sankarannamalai01@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "Mail from IMS"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    

