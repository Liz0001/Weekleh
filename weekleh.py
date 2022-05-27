"""Weekleh app."""
import sys
sys.path.insert(0, "../src")
from src import main    # noqa: E402


def weekleh():
    """Run the app."""
    main.main()


if __name__ == '__main__':
    weekleh()
