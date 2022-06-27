"""Here we create the user account."""

import sqlite3
from src import login_security
from cryptography.fernet import Fernet
import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


DATABASE = "src/database/weekleh.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


def create_database():
    """Connect to database."""
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS user (
                    user_email     text        PRIMARY KEY UNIQUE NOT NULL,
                    name           text        NOT NULL,
                    password       text        NOT NULL
                );""")


def check_if_email_exists(email):
    """Email must not exist in database and be accordance with email formatting."""
    email = email.lower()
    if login_security.check_email(email):
        create_database()
        with conn:
            c.execute("SELECT user_email FROM user WHERE user_email = ?", (email, ))

        res = c.fetchone()
        if res is None:
            return False
        return True
    else:
        return False


def create_account(name, email, password):
    """Recieve the data from the form."""
    pwd = encrypt(password)
    email = email.lower()
    with conn:
        c.execute("INSERT INTO user VALUES (?, ?, ?)", (email, name, pwd))


def encrypt(pwd):
    """Encrypt passwords."""
    try:
        with open("src/key.bin", "rb") as key_file:
            key = key_file.readline()
    except Exception as err:        # noqa
        pass
    fernet = Fernet(key)
    encryptedPWD = fernet.encrypt(pwd.encode())

    return encryptedPWD.decode()


def decrypt(email, password):
    """Decrypt the password."""
    email = email.lower()
    with conn:
        c.execute("SELECT password FROM user WHERE user_email = ?", (email,))

    res = c.fetchone()
    if res is None:
        return False

    try:
        with open("src/key.bin", "rb") as key_file:
            key = key_file.readline()
    except Exception as err:        # noqa
        pass

    fernet = Fernet(key)
    decpass = fernet.decrypt(res[0].encode())
    if password == decpass.decode():
        return True
    else:
        return False


def user_name(email):
    """Signed in sucessfully."""
    email = email.lower()
    with conn:
        c.execute("SELECT name FROM user WHERE user_email = ?", (email,))
    res = c.fetchone()
    return res[0]
