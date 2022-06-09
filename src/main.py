"""Weekleh app."""
import sys
from LoginUI.login import LoginWindowUI
from PyQt5 import QtWidgets
sys.path.insert(0, "..")


def main():
    """Run the app."""
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWindowUI()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
