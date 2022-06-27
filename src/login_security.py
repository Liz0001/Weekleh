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
    # Special characters: " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    __SpecialSym = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
                    '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
                    '|', '}', '~']
    __val = True

    # 'length should be at least 6'
    if len(pwd) < 6:
        __val = False

    # 'length should be not be greater than 30'
    if len(pwd) > 30:
        __val = False

    # 'Password should have at least one numeral'
    if not any(char.isdigit() for char in pwd):
        __val = False

    # 'Password should have at least one uppercase letter'
    if not any(char.isupper() for char in pwd):
        __val = False

    # 'Password should have at least one lowercase letter'
    if not any(char.islower() for char in pwd):
        __val = False

    # 'Password should have at least one of the symbols $@#'
    if not any(char in __SpecialSym for char in pwd):
        __val = False

    if __val:
        return __val


def check_password_match(pwd1, pwd2):
    """Check that passwords match."""
    return pwd1 == pwd2
