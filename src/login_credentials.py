"""Create account functionality."""
import re


def check_name(name):
    """Name format check."""
    __regex_name = re.compile(r'[A-Za-z]{2,25}( [A-Za-z]{2,35})?')
    if re.fullmatch(__regex_name, name):
        return True
    return False


def check_email(email):
    """Check that email has a correct format."""
    __regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(__regex_email, email):
        return True
    return False


def check_password(pwd):
    """Check that passwords are correct."""
    __regex_pass = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,32}$')
    if re.fullmatch(__regex_pass, pwd):
        return True
    return False


def check_password_match(pwd1, pwd2):
    """Check that passwords match."""
    return pwd1 == pwd2
