"""Main."""

from src import create_account_login


def logged_in_user(user_email):
    """Get the email."""
    with open('src/active.txt', 'w') as f:
        f.write(user_email)


def greet():
    """Welcome the user."""
    with open('src/active.txt', 'r') as f:
        lines = f.readlines()
    user = create_account_login.user_name(lines[0])
    return user


def main():
    """Ze Main."""
    pass
