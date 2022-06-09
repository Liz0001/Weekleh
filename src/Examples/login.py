"""Created by: PyQt6 UI code generator 6.1.0."""
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

sys.path.insert(0, "../src/LoginUI")
print(sys.path)


class LoginWindowUI(object):
    """Log in class."""

    def setupUi(self, LoginWindow):
        """UI setup."""
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1103, 621)
        LoginWindow.setStyleSheet("* {\n"
                                  "font: 15px \"Lato\";\n"
                                  "font-weight: bold;\n"
                                  "background-color: #f39766;\n"
                                  "color: #666;\n"
                                  "line-height: 1.6;\n"
                                  "}\n"
                                  ""
                                  )
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setMinimumSize(QtCore.QSize(1085, 603))
        self.frame_main.setMaximumSize(QtCore.QSize(1085, 603))
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout.setObjectName("gridLayout")
        self.image_frame = QtWidgets.QFrame(self.frame_main)
        self.image_frame.setMinimumSize(QtCore.QSize(529, 583))
        self.image_frame.setMaximumSize(QtCore.QSize(529, 583))
        self.image_frame.setAutoFillBackground(False)
        self.image_frame.setStyleSheet("")
        self.image_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image = QtWidgets.QLabel(self.image_frame)
        self.image.setGeometry(QtCore.QRect(0, 0, 531, 591))
        self.image.setStyleSheet("")
        self.image.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(":/login_img/img2.jpg"))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image_frame, 0, 2, 1, 1)
        self.sign_in_frame_outer = QtWidgets.QFrame(self.frame_main)
        self.sign_in_frame_outer.setMinimumSize(QtCore.QSize(530, 583))
        self.sign_in_frame_outer.setMaximumSize(QtCore.QSize(530, 583))
        self.sign_in_frame_outer.setStyleSheet("border-radius: 5px;\n"
                                               "background: #f6f6f6;\n"
                                               "\n"
                                               "")
        self.sign_in_frame_outer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sign_in_frame_outer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sign_in_frame_outer.setObjectName("sign_in_frame_outer")
        self.sign_in_frame_inner = QtWidgets.QFrame(self.sign_in_frame_outer)
        self.sign_in_frame_inner.setGeometry(QtCore.QRect(90, 20, 351, 561))
        self.sign_in_frame_inner.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.sign_in_frame_inner.setStyleSheet("")
        self.sign_in_frame_inner.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sign_in_frame_inner.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sign_in_frame_inner.setObjectName("sign_in_frame_inner")
        self.layoutWidget = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 470, 314, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.create_acc_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.create_acc_layout.setContentsMargins(0, 0, 0, 0)
        self.create_acc_layout.setObjectName("create_acc_layout")
        self.create_account_1 = QtWidgets.QLabel(self.layoutWidget)
        self.create_account_1.setMinimumSize(QtCore.QSize(0, 0))
        self.create_account_1.setStyleSheet("font-size: 13px;\n"
                                        "color: #a3a3a3;")
        self.create_account_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.create_account_1.setObjectName("create_account_1")
        self.create_acc_layout.addWidget(self.create_account_1)
        self.create_account_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.create_account_2.setStyleSheet("*{\n"
                                        "font-size: 13px;\n"
                                        "color: #a3a3a3;\n"
                                        "padding-bottom:3px;\n"
                                        "}\n"
                                        "\n"
                                        "#create_account_2 {\n"
                                        "border-bottom: solid 1px white;\n"
                                        "}\n"
                                        "\n"
                                        "#create_account_2:hover {\n"
                                        "color: #666;\n"
                                        "border-bottom: solid 1px #a3a3a3;\n"
                                        "}")
        self.create_account_2.setObjectName("create_account_2")
        self.create_acc_layout.addWidget(self.create_account_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 150, 311, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.email_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.email_label = QtWidgets.QLabel(self.layoutWidget1)
        self.email_label.setStyleSheet("\n"
                                "padding-left: 5px;\n"
                                "padding-bottom:-2px;\n"
                                "height:25px;")
        self.email_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.email_label.setObjectName("email_label")
        self.email_layout.addWidget(self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.email_input.setStyleSheet("\n"
                                "background: rgba(243,151,102, 0.05);\n"
                                "padding: 5px;\n"
                                "height:25px;")
        self.email_input.setObjectName("email_input")
        self.email_layout.addWidget(self.email_input)
        self.logo = QtWidgets.QLabel(self.sign_in_frame_inner)
        self.logo.setGeometry(QtCore.QRect(10, 10, 331, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/logo_sample1.PNG"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.layoutWidget2 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 250, 311, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.password_layout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.password_label = QtWidgets.QLabel(self.layoutWidget2)
        self.password_label.setStyleSheet("\n"
                                        "padding-left: 5px;\n"
                                        "padding-bottom:-2px;\n"
                                        "height:25px;")
        self.password_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBotto | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.password_label.setObjectName("password_label")
        self.password_layout.addWidget(self.password_label)
        self.password_input = QtWidgets.QLineEdit(self.layoutWidget2)
        self.password_input.setStyleSheet("background: rgba(243,151,102, 0.05);\n"
                                        "padding: 5px;\n"
                                        "height:25px;")
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.password_layout.addWidget(self.password_input)
        self.sign_in = QtWidgets.QPushButton(self.sign_in_frame_inner)
        self.sign_in.setGeometry(QtCore.QRect(20, 390, 311, 41))
        self.sign_in.setStyleSheet("#sign_in {\n"
                                "background: rgba(243,151,102, 0.9);\n"
                                "color: #f6f6f6;\n"
                                "cursor: pointer;\n"
                                "outline: none;\n"
                                "border: none;\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#sign_in:hover {\n"
                                "background: rgba(243,151,102, 1);\n"
                                "}")
        self.sign_in.setObjectName("sign_in")
        self.layoutWidget3 = QtWidgets.QWidget(self.sign_in_frame_inner)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 340, 311, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.remember_forgot_layout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.remember_forgot_layout.setContentsMargins(0, 0, 0, 0)
        self.remember_forgot_layout.setObjectName("remember_forgot_layout")
        self.remember_password = QtWidgets.QCheckBox(self.layoutWidget3)
        self.remember_password.setStyleSheet("font-size: 13px;\n"
                                        "color: #a3a3a3;\n"
                                        "padding-bottom:3px;")
        self.remember_password.setObjectName("remember_password")
        self.remember_forgot_layout.addWidget(self.remember_password)
        self.forgot_password = QtWidgets.QPushButton(self.layoutWidget3)
        self.forgot_password.setStyleSheet("*{\n"
                                        "font-size: 13px;\n"
                                        "color: #a3a3a3;\n"
                                        "padding-bottom:3px;\n"
                                        "}\n"
                                        "\n"
                                        "#forgot_password {\n"
                                        "border-bottom: solid 1px white;\n"
                                        "}\n"
                                        "\n"
                                        "#forgot_password:hover {\n"
                                        "color: #666;\n"
                                        "border-bottom: solid 1px #a3a3a3;\n"
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
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.create_account_1.setText(_translate("LoginWindow", "Don\'t have an account?"))
        self.create_account_2.setText(_translate("LoginWindow", "Create an Account"))
        self.email_label.setText(_translate("LoginWindow", "Email"))
        self.email_input.setPlaceholderText(_translate("LoginWindow", "Enter your email"))
        self.password_label.setText(_translate("LoginWindow", "Password"))
        self.password_input.setPlaceholderText(_translate("LoginWindow", "Enter your password"))
        self.sign_in.setText(_translate("LoginWindow", "Sign In"))
        self.remember_password.setText(_translate("LoginWindow", "Remember me"))
        self.forgot_password.setText(_translate("LoginWindow", "Forgot password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWindowUI()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
