"""
# UI for Create Account Page.

-*- coding: utf-8 -*-
Created by: PyQt5 UI code generator 5.15.4
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from qtwidgets import PasswordEdit

from src.LoginUI import login
from src import login_security
from src import create_account_login
sys.path.insert(0, "../src")
path = os.path.dirname(os.path.abspath(f"{__file__}/.."))


class CreateAccountWindowUI(object):
    """The Create Account Window Class."""

    def create_new_account(self, CreateAccountWindow):
        """Create new account."""
        __login_success = True

        if self.name_input.text() == "" and self.email_input.text() == "" and self.password_input.text() == "" and self.password_input_2.text() == "":
            self.all_fields_empty()
            __login_success = False

        elif not login_security.check_name(self.name_input.text()):
            self.invalid_name_popup()
            __login_success = False

        elif self.name_input.text() == "" or self.email_input.text() == "" or self.password_input.text() == "" or self.password_input_2.text() == "":
            __login_success = False

        elif not login_security.check_email(self.email_input.text()):
            self.invalid_email_popup()
            __login_success = False

        elif not login_security.check_password(self.password_input.text()):
            self.weak_password_popup()
            __login_success = False

        elif not login_security.check_password_match(self.password_input.text(), self.password_input_2.text()):
            self.passwords_not_matching_popup()
            __login_success = False

        elif create_account_login.check_if_email_exists(self.email_input.text()):
            __login_success = False

        if __login_success:
            create_account_login.create_account(self.name_input.text(), self.email_input.text(), self.password_input.text())
            action = self.account_created_popup()
            if action == 1024:
                self.LoginWindow = QtWidgets.QMainWindow()
                self.ui = login.LoginWindowUI()
                self.ui.setupUi(self.LoginWindow)
                self.LoginWindow.showMaximized()
                self.LoginWindow.setFocus()
                CreateAccountWindow.close()
            else:
                self.name_input.clear()
                self.email_input.clear()
                self.password_input.clear()
                self.password_input_2.clear()

    def all_fields_empty(self):
        """Give a warning that name is not valid."""
        msg = QMessageBox()
        msg.setWindowTitle("Nothing to create.")
        msg.setText("All fields are empty!\nYou need to fill the form in order to create an account.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def invalid_name_popup(self):
        """Give a warning that name is not valid."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Name")
        msg.setText("The name you entered is not valid. Make sure there are no special characters!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def invalid_email_popup(self):
        """Give a warning that email is not valid."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Email")
        msg.setText("You have entered invalid email address. Please check your email!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def weak_password_popup(self):
        """Give a warning that password is not good."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Password!")
        msg.setText("You have entered a weak password. Try again")
        msg.setInformativeText('- One Capital Letter\n- One Number\n- Special Character\n- Length Should be 6-30.')
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def passwords_not_matching_popup(self):
        """Give a warning that passwords are not matching."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Password!")
        msg.setText("Passwords entered do not match!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def account_created_popup(self):
        """Account created, go to 'Log In'."""
        msg = QMessageBox()
        msg.setWindowTitle("Account created!")
        msg.setText("Amazing! Account successfully created.")
        msg.setInformativeText('Go to "Log In".')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_action_ok)
        action = msg.exec_()
        return action

    def popup_action_ok(self):
        """."""
        pass

    def open_sign_in(self, CreateAccountWindow):
        """Open the Sign In / Log In Window."""
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = login.LoginWindowUI()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.showMaximized()
        self.LoginWindow.setFocus()
        CreateAccountWindow.close()

    # Create Account Window setup starts here
    def setupUi(self, CreateAccountWindow):
        """UI Setup."""
        CreateAccountWindow.setObjectName("CreateAccountWindow")
        CreateAccountWindow.resize(1500, 820)
        CreateAccountWindow.setStyleSheet("* {\n"
            "font: 22px \"Lato\";\n"
            "font-weight: bold;\n"
            "background-color: #f39766;\n"
            "color: #666;\n"
            "line-height: 1.6;\n"
            "}\n")

        self.centralwidget = QtWidgets.QWidget(CreateAccountWindow)
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
        self.image_frame = QtWidgets.QFrame(self.frame_main)
        self.image_frame.setMinimumSize(QtCore.QSize(400, 800))
        self.image_frame.setMaximumSize(QtCore.QSize(800, 800))
        self.image_frame.setAutoFillBackground(False)
        self.image_frame.setStyleSheet("")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image = QtWidgets.QLabel(self.image_frame)
        self.image.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.image.setStyleSheet("")
        self.image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/create_acc2.jpg")))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image_frame, 0, 2, 1, 1)
        self.create_acc_frame_outer = QtWidgets.QFrame(self.frame_main)
        self.create_acc_frame_outer.setMinimumSize(QtCore.QSize(800, 800))
        self.create_acc_frame_outer.setMaximumSize(QtCore.QSize(800, 800))
        self.create_acc_frame_outer.setStyleSheet("border-radius: 5px;\n"
            "background: #f6f6f6;\n"
            "\n")

        self.create_acc_frame_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_acc_frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_acc_frame_outer.setObjectName("create_acc_frame_outer")
        self.create_acc_frame_inner = QtWidgets.QFrame(self.create_acc_frame_outer)
        self.create_acc_frame_inner.setGeometry(QtCore.QRect(50, 40, 700, 730))

        self.create_acc_frame_inner.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.create_acc_frame_inner.setStyleSheet("")
        self.create_acc_frame_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_acc_frame_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_acc_frame_inner.setObjectName("create_acc_frame_inner")
        self.logo = QtWidgets.QLabel(self.create_acc_frame_inner)
        self.logo.setGeometry(QtCore.QRect(150, 10, 400, 175))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/logo.PNG")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # Create account
        self.create_account_button = QtWidgets.QPushButton(
            self.create_acc_frame_inner, clicked=lambda: self.create_new_account(CreateAccountWindow))
        self.create_account_button.setGeometry(QtCore.QRect(160, 620, 380, 50))
        self.create_account_button.setStyleSheet("#create_account_button {\n"
            "background: rgba(243,151,102, 0.9);\n"
            "color: #f6f6f6;\n"
            "outline: none;\n"
            "border: none;\n"
            "}\n"

            "#create_account_button:hover {\n"
            "background: rgba(243,151,102, 1);\n"
            "}")

        self.create_account_button.setObjectName("create_account_button")
        self.welcome_sentence = QtWidgets.QLabel(self.create_acc_frame_inner)
        self.welcome_sentence.setGeometry(QtCore.QRect(150, 200, 400, 25))
        self.welcome_sentence.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_sentence.setStyleSheet("font-size:18px;")
        self.welcome_sentence.setObjectName("welcome_sentence")
        self.layoutWidget = QtWidgets.QWidget(self.create_acc_frame_inner)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 450, 380, 140))
        self.layoutWidget.setObjectName("layoutWidget")
        self.password_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-3px;\n"
            "height:25px;")

        self.password_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.password_label.setObjectName("password_label")
        self.password_layout.addWidget(self.password_label)
        self.password_input = PasswordEdit()

        self.password_input.setStyleSheet("background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")
        # tooltip
        self.password_label.setToolTip('- One Capital Letter\n- One Number\n- Special Character\n- Length Should be 6-30.')
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.password_layout.addWidget(self.password_input)
        self.password_input_2 = PasswordEdit()
        self.password_input_2.setStyleSheet("background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")
        self.password_input_2.setText("")
        self.password_input_2.setObjectName("password_input_2")
        self.password_layout.addWidget(self.password_input_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.create_acc_frame_inner)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 705, 300, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.sig_in_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.sig_in_layout.setContentsMargins(0, 0, 0, 0)
        self.sig_in_layout.setObjectName("sig_in_layout")
        self.sign_in_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.sign_in_1.setMinimumSize(QtCore.QSize(0, 0))
        self.sign_in_1.setStyleSheet("font-size: 18px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;")

        self.sign_in_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_in_1.setObjectName("sign_in_1")
        self.sig_in_layout.addWidget(self.sign_in_1)

        # Sign in button
        self.sign_in_2 = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.open_sign_in(CreateAccountWindow))

        self.sign_in_2.setStyleSheet("*{\n"
            "font-size: 18px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;\n"
            "padding-left:5px;\n"
            "text-align:left;\n"
            "}\n"

            "#sign_in_2 {\n"
            "border-bottom: solid 1px white;\n"
            "}\n"

            "#sign_in_2:hover {\n"
            "color: #666;\n"
            "border-bottom: solid 1px #a3a3a3;\n"
            "}")

        self.sign_in_2.setObjectName("sign_in_2")
        self.sig_in_layout.addWidget(self.sign_in_2)
        self.widget = QtWidgets.QWidget(self.create_acc_frame_inner)
        self.widget.setGeometry(QtCore.QRect(160, 250, 380, 90))
        self.widget.setObjectName("widget")
        self.name_layout = QtWidgets.QVBoxLayout(self.widget)
        self.name_layout.setContentsMargins(0, 0, 0, 0)
        self.name_layout.setObjectName("name_layout")
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-3px;\n"
            "height:25px;")

        self.name_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.name_label.setObjectName("name_label")
        self.name_layout.addWidget(self.name_label)
        self.name_input = QtWidgets.QLineEdit(self.widget)
        self.name_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")

        self.name_input.setObjectName("name_input")
        self.name_layout.addWidget(self.name_input)

        self.widget1 = QtWidgets.QWidget(self.create_acc_frame_inner)
        self.widget1.setGeometry(QtCore.QRect(160, 350, 380, 90))
        self.widget1.setObjectName("widget1")
        self.email_layout = QtWidgets.QVBoxLayout(self.widget1)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.email_label = QtWidgets.QLabel(self.widget1)
        self.email_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-3px;\n"
            "height:25px;")

        self.email_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.email_layout.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.widget1)
        self.email_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")

        self.email_input.setClearButtonEnabled(False)
        self.email_input.setObjectName("email_input")
        self.email_layout.addWidget(self.email_input)
        self.gridLayout.addWidget(self.create_acc_frame_outer, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_main, 0, 0, 1, 1)
        CreateAccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateAccountWindow)

    def retranslateUi(self, CreateAccountWindow):
        """Labels."""
        _translate = QtCore.QCoreApplication.translate
        CreateAccountWindow.setWindowTitle(_translate("CreateAccountWindow", "Create an Account"))
        self.create_account_button.setText(_translate("CreateAccountWindow", "Create Account"))
        self.welcome_sentence.setText(_translate("CreateAccountWindow", "Create your Weekleh account and get going!"))
        self.password_label.setText(_translate("CreateAccountWindow", "Password*"))
        self.password_input.setPlaceholderText(_translate("CreateAccountWindow", "Password"))
        self.password_input_2.setPlaceholderText(_translate("CreateAccountWindow", "Confirm password"))
        self.sign_in_1.setText(_translate("CreateAccountWindow", "Already have an account?"))
        self.sign_in_2.setText(_translate("CreateAccountWindow", "Sign In"))
        self.name_label.setText(_translate("CreateAccountWindow", "Name*"))
        self.name_input.setPlaceholderText(_translate("CreateAccountWindow", "Enter your name"))
        self.email_label.setText(_translate("CreateAccountWindow", "Email*"))
        self.email_input.setPlaceholderText(_translate("CreateAccountWindow", "Enter your email"))


def create_account_main():
    """Run the window."""
    app = QtWidgets.QApplication(sys.argv)
    CreateAccountWindow = QtWidgets.QMainWindow()
    ui = CreateAccountWindowUI()
    ui.setupUi(CreateAccountWindow)
    CreateAccountWindow.showMaximized()
    CreateAccountWindow.setFocus()
    sys.exit(app.exec_())


if __name__ == "__main__":
    create_account_main()
