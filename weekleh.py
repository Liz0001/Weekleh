"""Weekleh app."""
import sys

from src.LoginUI import login
sys.path.insert(0, "..")


def weekleh():
    """Run the app."""
    login.run_login_page()


if __name__ == "__main__":
    weekleh()
