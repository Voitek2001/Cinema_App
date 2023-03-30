from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_authentication import authenticate_password


class Ui_login(object):

    def __init__(self, widget):
        self.widget = widget
        self.wrong_pass_cnt = 0


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.log_in_button = QtWidgets.QPushButton(Form)
        self.log_in_button.setGeometry(QtCore.QRect(220, 320, 321, 41))
        self.log_in_button.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 127);\n"
"    border: 2px solid rgb(255, 0, 127);\n"
"}")
        self.log_in_button.setObjectName("log_in_button")
        self.log_in_button.clicked.connect(self.go_to_admin_panel)
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(50, 520, 221, 61))
        self.return_button.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 127);\n"
"    border: 2px solid rgb(255, 0, 127);\n"
"}")
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(self.go_to_intro)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 240, 321, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 160, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 390, 291, 41))
        self.label_2.setStyleSheet("QLabel {\n"
"    background: rgba(204, 204, 204, 0);\n"
"    color: red;\n"
"}")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def go_to_admin_panel(self):

        if authenticate_password(self.lineEdit.text()):
            self.label_2.setText("")
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            self.label_2.setText("Nieprawidłowe hasło\n Spróbuj ponownie")
        self.lineEdit.setText("")


    def go_to_intro(self):

        self.label_2.setText("")
        self.widget.setCurrentIndex(0)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.log_in_button.setText(_translate("Form", "Zaloguj się"))
        self.return_button.setText(_translate("Form", "Powrót do strony głównej"))
        self.label.setText(_translate("Form", "Podaj hasło do panelu administratora"))



