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
from src.PasswordResetUI import reset_password_last
from src import forgot_password

sys.path.insert(0, "../src")
path = os.path.dirname(os.path.abspath(f"{__file__}/.."))


class Ui_ResetPasswordWindow(object):
    """The Reset Password class."""

    def enter_the_token(self, current_window):
        """Enter token."""
        value = True

        if self.token_input.text() == "":
            value = False

        elif not forgot_password.check_token(self.token_input.text()):
            value = False
            self.invalid_token_popup()

        if value:
            self.ResetPasswordWindow = QtWidgets.QMainWindow()
            self.ui = reset_password_last.Ui_ResetPasswordWindow()
            self.ui.setupUi(self.ResetPasswordWindow)
            self.ResetPasswordWindow.showMaximized()
            self.ResetPasswordWindow.setFocus
            current_window.close()

    def invalid_token_popup(self):
        """Give a warning that Token is not valid."""
        msg = QMessageBox()
        msg.setWindowTitle("Check your Token")
        msg.setText("It Token may be expired or invalid!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def open_sign_in(self, current_window):
        """Open the Sign In / Log In Window."""
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = login.LoginWindowUI()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.showMaximized()
        self.LoginWindow.setFocus()
        current_window.close()

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
        self.layoutWidget.setGeometry(QtCore.QRect(160, 300, 380, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.token_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.token_layout.setContentsMargins(0, 0, 0, 0)
        self.token_layout.setObjectName("token_layout")
        self.token_label = QtWidgets.QLabel(self.layoutWidget)
        self.token_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "height:35px;")

        self.token_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.token_label.setObjectName("token_label")
        self.token_layout.addWidget(self.token_label)
        self.token_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.token_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:35px;")

        self.token_input.setObjectName("token_input")
        self.token_layout.addWidget(self.token_input)
        self.logo = QtWidgets.QLabel(self.reste_frame_inner)
        self.logo.setGeometry(QtCore.QRect(150, 10, 400, 175))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(os.path.join(path + "/images/logo.PNG")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # Button
        self.send_token = QtWidgets.QPushButton(
            self.reste_frame_inner, clicked=lambda: self.enter_the_token(ResetPasswordWindow))
        self.send_token.setGeometry(QtCore.QRect(160, 425, 380, 50))
        self.send_token.setStyleSheet("#send_token {\n"
            "background: rgba(243,151,102, 0.9);\n"
            "color: #f6f6f6;\n"
            "border: none;\n"
            "}\n"

            "#send_token:hover {\n"
            "background: rgba(243,151,102, 1);\n"
            "}")

        self.send_token.setObjectName("send_token")
        # button
        self.back_button = QtWidgets.QPushButton(
            self.reste_frame_inner, clicked=lambda: self.open_sign_in(ResetPasswordWindow))
        self.back_button.setGeometry(QtCore.QRect(160, 500, 380, 20))
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
        self.pass_caption = QtWidgets.QLabel(self.reste_frame_inner)
        self.pass_caption.setGeometry(QtCore.QRect(160, 220, 380, 50))
        self.pass_caption.setStyleSheet("font-size: 27px;\n"
            "margin-left:3px;")
        self.pass_caption.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pass_caption.setObjectName("pass_caption")
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
        self.token_label.setText(_translate("ResetPasswordWindow", "Token"))
        self.token_input.setPlaceholderText(_translate("ResetPasswordWindow", "Enter your token here"))
        self.send_token.setText(_translate("ResetPasswordWindow", "Submit Token"))
        self.back_button.setText(_translate("ResetPasswordWindow", "<< Back"))
        self.pass_caption.setText(_translate("ResetPasswordWindow", "Enter Token"))


def reset_pass_main():
    """Run the window."""
    app = QtWidgets.QApplication(sys.argv)
    ResetPasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_ResetPasswordWindow()
    ui.setupUi(ResetPasswordWindow)
    ResetPasswordWindow.showMaximized()
    ResetPasswordWindow.setFocus()
    sys.exit(app.exec_())


if __name__ == "__main__":
    reset_pass_main()
