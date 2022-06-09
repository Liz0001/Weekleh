"""Weekleh app."""
import sys

from src.LoginUI.login import LoginWindowUI
from PyQt5 import QtWidgets
sys.path.insert(0, "..")
# from src import main  # noqa: E402


def weekleh():
    """Run the app."""
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWindowUI()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    weekleh()
