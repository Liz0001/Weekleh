"""
# UI for forgot password page.

-*- coding: utf-8 -*-
Created by: PyQt5 UI code generator 5.15.4
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


sys.path.insert(0, "../src")
path = os.path.dirname(os.path.abspath(f"{__file__}/.."))


class ResetPasswordWindowUI(object):
    """The Reset Password class."""

    def setupUi(self, ResetPasswordWindow):
        """UI setup."""
        ResetPasswordWindow.setObjectName("ResetPasswordWindow")
        ResetPasswordWindow.resize(1103, 621)
        ResetPasswordWindow.setStyleSheet("* {\n"
            "font: 15px \"Lato\";\n"
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
        self.frame_main.setMinimumSize(QtCore.QSize(1085, 603))
        self.frame_main.setMaximumSize(QtCore.QSize(1085, 603))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout.setObjectName("gridLayout")
        self.image_frame = QtWidgets.QFrame(self.frame_main)
        self.image_frame.setMinimumSize(QtCore.QSize(529, 583))
        self.image_frame.setMaximumSize(QtCore.QSize(529, 583))
        self.image_frame.setAutoFillBackground(False)
        self.image_frame.setStyleSheet("")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image = QtWidgets.QLabel(self.image_frame)
        self.image.setGeometry(QtCore.QRect(0, 0, 531, 591))
        self.image.setStyleSheet("")
        self.image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("C:/Users/liisu/Desktop/Weekleh/src/PasswordResetUI\\../images/create_acc.jpg"))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image_frame, 0, 2, 1, 1)
        self.reset_frame_outer = QtWidgets.QFrame(self.frame_main)
        self.reset_frame_outer.setMinimumSize(QtCore.QSize(530, 583))
        self.reset_frame_outer.setMaximumSize(QtCore.QSize(530, 583))
        self.reset_frame_outer.setStyleSheet("border-radius: 5px;\n"
            "background: #f6f6f6;\n"
            "\n")

        self.reset_frame_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reset_frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reset_frame_outer.setObjectName("reset_frame_outer")
        self.reste_frame_inner = QtWidgets.QFrame(self.reset_frame_outer)
        self.reste_frame_inner.setGeometry(QtCore.QRect(90, 20, 351, 561))
        self.reste_frame_inner.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reste_frame_inner.setStyleSheet("")
        self.reste_frame_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reste_frame_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reste_frame_inner.setObjectName("reste_frame_inner")
        self.layoutWidget = QtWidgets.QWidget(self.reste_frame_inner)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 280, 311, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.email_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        self.email_label.setStyleSheet("\n"
            "padding-left: 5px;\n"
            "padding-bottom:-2px;\n"
            "height:25px;")

        self.email_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.email_layout.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_input.setStyleSheet("\n"
            "background: rgba(243,151,102, 0.05);\n"
            "padding: 5px;\n"
            "height:25px;")

        self.email_input.setObjectName("email_input")
        self.email_layout.addWidget(self.email_input)
        self.logo = QtWidgets.QLabel(self.reste_frame_inner)
        self.logo.setGeometry(QtCore.QRect(10, 10, 331, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:/Users/liisu/Desktop/Weekleh/src/PasswordResetUI\\../images/logo.PNG"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.send_token = QtWidgets.QPushButton(self.reste_frame_inner)
        self.send_token.setGeometry(QtCore.QRect(20, 400, 311, 41))
        self.send_token.setStyleSheet("#send_token {\n"
            "background: rgba(243,151,102, 0.9);\n"
            "color: #f6f6f6;\n"
            "outline: none;\n"
            "border: none;\n"
            "}\n"

            "#send_token:hover {\n"
            "background: rgba(243,151,102, 1);\n"
            "}")

        self.send_token.setObjectName("send_token")
        self.back_button = QtWidgets.QPushButton(self.reste_frame_inner)
        self.back_button.setGeometry(QtCore.QRect(20, 470, 312, 19))
        self.back_button.setStyleSheet("*{\n"
            "font-size: 13px;\n"
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
        self.widget.setGeometry(QtCore.QRect(21, 160, 308, 96))
        self.widget.setObjectName("widget")
        self.pass_layout = QtWidgets.QVBoxLayout(self.widget)
        self.pass_layout.setContentsMargins(0, 0, 0, 0)
        self.pass_layout.setObjectName("pass_layout")
        self.pass_caption = QtWidgets.QLabel(self.widget)
        self.pass_caption.setStyleSheet("font-size: 20px;\n"
            "margin-bottom:10px;")

        self.pass_caption.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_caption.setObjectName("pass_caption")
        self.pass_layout.addWidget(self.pass_caption)
        self.pass_instruction = QtWidgets.QLabel(self.widget)
        self.pass_instruction.setStyleSheet("color: #a3a3a3;")
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
