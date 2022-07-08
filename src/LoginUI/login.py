"""
# UI for Login Page.

-*- coding: utf-8 -*-
Created by: PyQt5 UI code generator 5.15.4
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from qtwidgets import PasswordEdit

from src.CreateAccountUI.create_account import CreateAccountWindowUI
from src.PasswordResetUI.password_reset_screen import ResetPasswordWindowUI
from src import create_account_login
from src import main_main
from src import remember_me

# Only for testing
from src.MainUI.main_window import Ui_MainWindow

sys.path.insert(0, "../src")
path = os.path.dirname(os.path.abspath(f"{__file__}/.."))


class LoginWindowUI(object):
    """The Login Window Class."""

    def open_main(self, LoginWindow):
        """Open MainWindow, after successful login."""
        __login_success = True

        if self.email_input.text() == "" and self.password_input.text() == "":
            __login_success = False

        elif self.email_input.text() == "" or self.password_input.text() == "":
            __login_success = False
            self.error_popup()

        elif not create_account_login.check_if_email_exists(self.email_input.text()) or not create_account_login.decrypt(self.email_input.text(), self.password_input.text()):
            __login_success = False
            self.login_error_popup()

        if __login_success:
            main_main.logged_in_user(self.email_input.text())    # noqa
            if self.remember_password.isChecked():
                remember_me.remember_user(self.email_input.text(), self.password_input.text())
            elif not self.remember_password.isChecked():
                remember_me.forget_me()
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.showMaximized()
            LoginWindow.close()

    def remember_me_popup(self):
        """Remember me."""
        if self.remember_password.isChecked():
            msg = QMessageBox()
            msg.setWindowTitle("Remember me.")
            msg.setText("Please do not store your username and password, if the computer is easily accessible to other people!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def login_error_popup(self):
        """Wrong Email or Password."""
        msg = QMessageBox()
        msg.setWindowTitle("Wrong Email or Password.")
        msg.setText("You have entered a wrong Email address or Password. Try again")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def error_popup(self):
        """Something went wrong."""
        msg = QMessageBox()
        msg.setWindowTitle("Something went wrong.")
        msg.setText("Please check that all fields are properly filled and try again!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def open_forgot_pass(self, LoginWindow):
        """Forgot password."""
        self.ResetPasswordWindow = QtWidgets.QMainWindow()
        self.ui = ResetPasswordWindowUI()
        self.ui.setupUi(self.ResetPasswordWindow)
        self.ResetPasswordWindow.showMaximized()
        self.ResetPasswordWindow.setFocus()
        LoginWindow.close()

    def open_create_acc(self, LoginWindow):
        """Open the Create Account window."""
        self.CreateAccountWindow = QtWidgets.QMainWindow()
        self.ui = CreateAccountWindowUI()
        self.ui.setupUi(self.CreateAccountWindow)
        self.CreateAccountWindow.showMaximized()
        self.CreateAccountWindow.setFocus()
        LoginWindow.close()

    def setupUi(self, LoginWindow):
        """UI Setup."""
        email, password = remembered()
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1500, 820)
        LoginWindow.setStyleSheet("* {\n"
            "font: 22px \"Lato\";\n"
            "font-weight: bold;\n"
            "background-color: #f39766;\n"
            "color: #666;\n"
            "line-height: 1.6;\n"
            "}")

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setMinimumSize(QtCore.QSize(1300, 820))
        self.frame_main.setMaximumSize(QtCore.QSize(1700, 820))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout.setObjectName("gridLayout")

        # Image frame
        self.image_frame = QtWidgets.QFrame(self.frame_main)
        self.image_frame.setMinimumSize(QtCore.QSize(400, 800))
        self.image_frame.setMaximumSize(QtCore.QSize(800, 800))
        self.image_frame.setAutoFillBackground(False)
        self.image_frame.setStyleSheet("border-radius: 5px;")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")

        # Image
        self.image = QtWidgets.QLabel(self.image_frame)
        self.image.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.image.setStyleSheet("border-radius: 5px;")
        self.image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/login.jpg")))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image_frame, 0, 2, 1, 1)

        # Outer login frame
        self.sign_in_frame_outer = QtWidgets.QFrame(self.frame_main)
        self.sign_in_frame_outer.setMinimumSize(QtCore.QSize(800, 800))
        self.sign_in_frame_outer.setMaximumSize(QtCore.QSize(800, 800))
        self.sign_in_frame_outer.setStyleSheet("border-radius:5px;\n"
            "background: #f6f6f6;")
        self.sign_in_frame_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sign_in_frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sign_in_frame_outer.setObjectName("sign_in_frame_outer")

        # Inner login frame
        self.sign_in_frame_inner = QtWidgets.QFrame(self.sign_in_frame_outer)
        self.sign_in_frame_inner.setGeometry(QtCore.QRect(50, 40, 700, 715))
        self.sign_in_frame_inner.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sign_in_frame_inner.setStyleSheet("")
        self.sign_in_frame_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sign_in_frame_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sign_in_frame_inner.setObjectName("sign_in_frame_inner")

        # Create an account
        self.layoutWidget = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 590, 380, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.create_acc_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.create_acc_layout.setContentsMargins(0, 0, 0, 0)
        self.create_acc_layout.setObjectName("create_acc_layout")
        self.create_account_1 = QtWidgets.QLabel(self.layoutWidget)
        self.create_account_1.setMinimumSize(QtCore.QSize(0, 0))
        self.create_account_1.setStyleSheet("font-size: 18px;\n"
            "color: #a3a3a3;")

        self.create_account_1.setAlignment(QtCore.Qt.AlignCenter)
        self.create_account_1.setObjectName("create_account_1")
        self.create_acc_layout.addWidget(self.create_account_1)

        # Button
        self.create_account_2 = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.open_create_acc(LoginWindow))
        self.create_account_2.setStyleSheet("*{\n"
            "font-size: 18px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;\n"
            "}\n"

            "#create_account_2 {\n"
            "border-bottom: solid 1px white;\n"
            "}\n"

            "#create_account_2:hover {\n"
            "color: #666;\n"
            "border-bottom: solid 1px #a3a3a3;\n"
            "}")

        self.create_account_2.setObjectName("create_account_2")
        self.create_acc_layout.addWidget(self.create_account_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 210, 380, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.email_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.email_label = QtWidgets.QLabel(self.layoutWidget1)
        self.email_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-2px;\n"
            "height:25px;")

        self.email_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.email_layout.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.email_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")

        self.email_input.setText(f"{email}")
        self.email_input.setObjectName("email_input")
        self.email_layout.addWidget(self.email_input)
        self.logo = QtWidgets.QLabel(self.sign_in_frame_inner)
        self.logo.setGeometry(QtCore.QRect(150, 10, 400, 175))

        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/logo.PNG")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.layoutWidget2 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget2.setGeometry(QtCore.QRect(160, 325, 380, 100))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.password_layout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.password_label = QtWidgets.QLabel(self.layoutWidget2)
        self.password_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-2px;\n"
            "height:25px;")

        self.password_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.password_label.setObjectName("password_label")
        self.password_layout.addWidget(self.password_label)

        # password hide/show
        self.password_input = PasswordEdit()
        self.password_input.setStyleSheet("background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height: 35px;")

        self.password_input.setText(f"{password}")
        self.password_input.setObjectName("password_input")
        self.password_layout.addWidget(self.password_input)
        self.sign_in = QtWidgets.QPushButton(
            self.sign_in_frame_inner, clicked=lambda: self.open_main(LoginWindow))
        self.sign_in.setGeometry(QtCore.QRect(160, 500, 380, 50))
        self.sign_in.setStyleSheet("#sign_in {\n"
            "background: rgba(243,151,102, 0.9);\n"
            "color: #f6f6f6;\n"
            "border: none;\n"
            "}\n"

            "#sign_in:hover {\n"
            "background: rgba(243,151,102, 1);\n"
            "border: none;\n"
            "}")

        self.sign_in.setObjectName("sign_in")
        self.layoutWidget3 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget3.setGeometry(QtCore.QRect(170, 440, 380, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.remember_forgot_layout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.remember_forgot_layout.setContentsMargins(0, 0, 0, 0)
        self.remember_forgot_layout.setObjectName("remember_forgot_layout")
        self.remember_password = QtWidgets.QCheckBox(
            self.layoutWidget3, clicked=lambda: self.remember_me_popup())
        if remember_me.check_if_user_remembered():
            self.remember_password.setChecked(True)

        self.remember_password.setStyleSheet("font-size: 16px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;")

        self.remember_password.setObjectName("remember_password")
        self.remember_forgot_layout.addWidget(self.remember_password)
        self.forgot_password = QtWidgets.QPushButton(
            self.layoutWidget3, clicked=lambda: self.open_forgot_pass(LoginWindow))
        self.forgot_password.setStyleSheet("*{\n"
            "font-size: 16px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;\n"
            "border: none;\n"
            "}\n"

            "#forgot_password {\n"
            "border-bottom: solid 1px white;\n"
            "}\n"

            "#forgot_password:hover {\n"
            "color: #666;\n"
            "border-bottom: solid 1px #a3a3a3;\n"
            "border: none;\n"
            "}")

        self.forgot_password.setObjectName("forgot_password")
        self.remember_forgot_layout.addWidget(self.forgot_password)
        self.gridLayout.addWidget(self.sign_in_frame_outer, 0, 1, 1, 1)
        self.sign_in_frame_outer.raise_()
        self.image_frame.raise_()
        self.gridLayout_2.addWidget(self.frame_main, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        """Labels."""
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Weekleh"))
        self.create_account_1.setText(_translate("LoginWindow", "Don\'t have an account?"))
        self.create_account_2.setText(_translate("LoginWindow", "Create an Account"))
        self.email_label.setText(_translate("LoginWindow", "Email"))
        self.email_input.setPlaceholderText(_translate("LoginWindow", "Enter your email"))
        self.password_label.setText(_translate("LoginWindow", "Password"))
        self.password_input.setPlaceholderText(_translate("LoginWindow", "Enter your password"))
        self.sign_in.setText(_translate("LoginWindow", "Sign In"))
        self.remember_password.setText(_translate("LoginWindow", "Remember me"))
        self.forgot_password.setText(_translate("LoginWindow", "Forgot password?"))


def remembered():
    """This checks if the user has previously wanted to remember their user."""
    remember = remember_me.check_if_user_remembered()
    if remember:
        email, passw = remember_me.get_name_pwd()
        return email, passw
    else:
        return "", ""


def login_main():
    """Run the window."""
    remembered()
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWindowUI()
    ui.setupUi(LoginWindow)
    LoginWindow.showMaximized()
    LoginWindow.setFocus()
    sys.exit(app.exec_())


if __name__ == "__main__":
    login_main()
