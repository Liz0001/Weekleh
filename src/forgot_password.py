"""Forgot the password reset."""
from email.message import EmailMessage
import smtplib
import ssl
import datetime
import string
import secrets
from src import create_account_login


def generate_token():
    """Generate token."""
    alphabet = string.ascii_letters + string.digits
    while True:
        token = ''.join(secrets.choice(alphabet) for i in range(8))
        if (sum(c.isupper() for c in token) >= 1 and sum(c.isdigit() for c in token) >= 2):
            break
    return token


def generate_date():
    """Save time: 2022-07-01 >> 20220701."""
    now = datetime.datetime.now()
    now = now.strftime("%Y%m%d")
    return now


def generate_time():
    """Save date in seconds."""
    s = datetime.datetime.now().strftime('%S')
    s = int(s)
    m = datetime.datetime.now().strftime('%M')
    m = int(m) * 60
    h = datetime.datetime.now().strftime('%H')
    h = int(h) * 3600
    time = h + m + s
    return str(time)


def send_token_email(receiver):
    """Email received from reset password screen."""
    sender_email = "jello.bello.marshmellow@gmail.com"
    sender_password = "oalqqzoxsimgcipg"

    token = generate_token()
    date = generate_date()
    time = generate_time()

    create_account_login.reset_account_pass(receiver, token, time, date)
    subject = "Reset your Weekleh password."
    message = f"""\
    Heyy you,
    Here's your Token, it will be valid for 30 mins.
    Copy and Paste the Token to the token field and create new password.

    Your Token: {token}

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


def check_token(token):
    """Lets check if token is true."""
    if create_account_login.decrypt_token(get_user_email(), token):
        db_time, db_date = create_account_login.date_time_token(get_user_email())

        if int(db_date) == int(generate_date()) and not (int(generate_time()) - int(db_time) > 1800):
            return True
    else:
        return False


def save_new_password(new_password):
    """Save the newly created password to database."""
    create_account_login.reset_pass(get_user_email(), new_password)
    create_account_login.delete_old_token(get_user_email())
    user_pass_reset()


def user_forgot_the_password(user_email):
    """Write the email."""
    with open('src/PasswordResetUI/forgot.txt', 'w') as f:
        f.write(user_email)


def get_user_email():
    """Get the user email."""
    with open('src/PasswordResetUI/forgot.txt', 'r') as f:
        email = f.readlines()
        email = email[0].rstrip('\n')
    return email


def user_pass_reset():
    """Delete the email."""
    with open('src/PasswordResetUI/forgot.txt', 'w') as f:
        f.write("")
