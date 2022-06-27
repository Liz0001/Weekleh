"""
# UI for forgot password page.

-*- coding: utf-8 -*-
Created by: PyQt5 UI code generator 5.15.4
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.LoginUI import login
from src import create_account_login
from src import login_security

sys.path.insert(0, "../src")
path = os.path.dirname(os.path.abspath(f"{__file__}/.."))


class ResetPasswordWindowUI(object):
    """The Reset Password class."""

    def reset_pass_token(self):
        """Reset pass, send token to email."""
        go_on = True

        if self.email_input.text() == "":
            go_on = False

        elif not login_security.check_email(self.email_input.text()):
            go_on = False
            self.invalid_email_popup()
        
        elif not create_account_login.check_if_email_exists(self.email_input.text()):
            go_on = False
            self.not_in_db_popup()

        if go_on:
            self.token_sent_popup()
            # close the current window and continue to last window
            print("hehe, page open ....")

    def not_in_db_popup(self):
        """The user is not in our database."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Email")
        msg.setText("We cannot find your information.")
        msg.setText('Please sign up for an account or contact Customer Service: "jello.bello.marshmellow@gmail.com"')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        
    def invalid_email_popup(self):
        """Give a warning that email is not valid."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Email")
        msg.setText("You have entered invalid email address. Please check your email!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def token_sent_popup(self):
        """Token sent notice."""
        msg = QMessageBox()
        msg.setWindowTitle("Token sent.")
        msg.setText("Check Your Email.")
        msg.setInformativeText('We have sent a Token to your email for password reset. Token is valid for 30 minutes.')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def open_sign_in(self, ResetPasswordWindow):
        """Open the Sign In / Log In Window."""
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = login.LoginWindowUI()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.showMaximized()
        self.LoginWindow.setFocus()
        ResetPasswordWindow.close()

    def setupUi(self, ResetPasswordWindow):
        """UI setup."""
        ResetPasswordWindow.setObjectName("ResetPasswordWindow")
        ResetPasswordWindow.resize(1500, 820)
        ResetPasswordWindow.setStyleSheet("* {\n"
            "font: 22px \"Lato\";\n"
            "font-weight: bold;\n"
            "background-color: #f39766;\n"
            "color: #666;\n"
            "line-height: 1.6;\n"
            "}\n")

        self.centralwidget = QtWidgets.QWidget(ResetPasswordWindow)
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
        self.image.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/create_acc.jpg")))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image_frame, 0, 2, 1, 1)
        self.reset_frame_outer = QtWidgets.QFrame(self.frame_main)
        self.reset_frame_outer.setMinimumSize(QtCore.QSize(800, 800))
        self.reset_frame_outer.setMaximumSize(QtCore.QSize(800, 800))
        self.reset_frame_outer.setStyleSheet("border-radius: 5px;\n"
            "background: #f6f6f6;\n"
            "\n")

        self.reset_frame_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reset_frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reset_frame_outer.setObjectName("reset_frame_outer")
        self.reste_frame_inner = QtWidgets.QFrame(self.reset_frame_outer)
        self.reste_frame_inner.setGeometry(QtCore.QRect(50, 40, 700, 715))
        self.reste_frame_inner.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reste_frame_inner.setStyleSheet("")
        self.reste_frame_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reste_frame_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reste_frame_inner.setObjectName("reste_frame_inner")
        self.layoutWidget = QtWidgets.QWidget(self.reste_frame_inner)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 370, 380, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.email_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        self.email_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-2px;\n"
            "height:25px;")

        self.email_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.email_layout.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")

        self.email_input.setObjectName("email_input")
        self.email_layout.addWidget(self.email_input)
        self.logo = QtWidgets.QLabel(self.reste_frame_inner)
        self.logo.setGeometry(QtCore.QRect(150, 10, 400, 175))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/logo.PNG")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.send_token = QtWidgets.QPushButton(
            self.reste_frame_inner, clicked=lambda: self.reset_pass_token())
        self.send_token.setGeometry(QtCore.QRect(160, 500, 380, 50))
        self.send_token.setStyleSheet("#send_token {\n"
            "background: rgba(243,151,102, 0.9);\n"
            "color: #f6f6f6;\n"
            "border: none;\n"
            "}\n"

            "#send_token:hover {\n"
            "background: rgba(243,151,102, 1);\n"
            "}")

        self.send_token.setObjectName("send_token")
        self.back_button = QtWidgets.QPushButton(
            self.reste_frame_inner, clicked=lambda: self.open_sign_in(ResetPasswordWindow))

        self.back_button.setGeometry(QtCore.QRect(160, 585, 380, 20))
        self.back_button.setStyleSheet("*{\n"
            "font-size: 16px;\n"
            "color: #a3a3a3;\n"
            "padding-bottom:3px;\n"
            "}\n"
            "#back_button {\n"
            "border-bottom: solid 1px white;\n"
            "}\n"
            "#back_button:hover {\n"
            "color: #666;\n"
            "border-bottom: solid 1px #a3a3a3;\n"
            "}")

        self.back_button.setObjectName("back_button")
        self.widget = QtWidgets.QWidget(self.reste_frame_inner)
        self.widget.setGeometry(QtCore.QRect(160, 220, 400, 130))
        self.widget.setObjectName("widget")
        self.pass_layout = QtWidgets.QVBoxLayout(self.widget)
        self.pass_layout.setContentsMargins(0, 0, 0, 0)
        self.pass_layout.setObjectName("pass_layout")
        self.pass_caption = QtWidgets.QLabel(self.widget)
        self.pass_caption.setStyleSheet("font-size: 27px;\n"
            "margin-left:3px;")

        self.pass_caption.setAlignment(QtCore.Qt.AlignLeft)
        self.pass_caption.setObjectName("pass_caption")
        self.pass_layout.addWidget(self.pass_caption)
        self.pass_instruction = QtWidgets.QLabel(self.widget)
        self.pass_instruction.setStyleSheet("color: #a3a3a3;"
                                            "font-size: 18px;")
        self.pass_instruction.setWordWrap(True)
        self.pass_instruction.setObjectName("pass_instruction")
        self.pass_layout.addWidget(self.pass_instruction)
        self.gridLayout.addWidget(self.reset_frame_outer, 0, 1, 1, 1)
        self.reset_frame_outer.raise_()
        self.image_frame.raise_()
        self.gridLayout_2.addWidget(self.frame_main, 0, 0, 1, 1)
        ResetPasswordWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResetPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(ResetPasswordWindow)

    def retranslateUi(self, ResetPasswordWindow):
        """Labels."""
        _translate = QtCore.QCoreApplication.translate
        ResetPasswordWindow.setWindowTitle(_translate("ResetPasswordWindow", "MainWindow"))
        self.email_label.setText(_translate("ResetPasswordWindow", "Email"))
        self.email_input.setPlaceholderText(_translate("ResetPasswordWindow", "Enter your email"))
        self.send_token.setText(_translate("ResetPasswordWindow", "Send Token"))
        self.back_button.setText(_translate("ResetPasswordWindow", "<< Back"))
        self.pass_caption.setText(_translate("ResetPasswordWindow", "Reset Password"))
        self.pass_instruction.setText(_translate("ResetPasswordWindow", "Enter the email associated with your Weekleh account and we\'ll send an email with a token to reset your password."))


def reset_pass_main():
    """Run the window."""
    app = QtWidgets.QApplication(sys.argv)
    ResetPasswordWindow = QtWidgets.QMainWindow()
    ui = ResetPasswordWindowUI()
    ui.setupUi(ResetPasswordWindow)
    ResetPasswordWindow.showMaximized()
    ResetPasswordWindow.setFocus()
    sys.exit(app.exec_())


if __name__ == "__main__":
    reset_pass_main()
