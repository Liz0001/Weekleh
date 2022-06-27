"""Forgot the password reset."""
from email.message import EmailMessage
import ssl
import smtplib


sender_email = "jello.bello.marshmellow@gmail.com"
sender_password = "oalqqzoxsimgcipg"
receiver = "liis.usin@gmail.com"

subject = "Reset Weekleh PWD"
message = """\
    Heyy,
    Here's you Token, it will be valid for 30 mins.
    Copy and Paste the Token to the email reset field.

    Token: #1234#

    *A message from Weekleh!
    Weekleh
    """

em = EmailMessage()
em["From"] = sender_email
em["To"] = receiver
em["Subject"] = subject
em.set_content(message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver, em.as_string())
