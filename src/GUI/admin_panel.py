from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):

    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 190, 360, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_create_new_film)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 300, 360, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.go_to_remove_film)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 410, 360, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.admin_info = QtWidgets.QLabel(Form)
        self.admin_info.setGeometry(QtCore.QRect(170, 60, 420, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.admin_info.setFont(font)
        self.admin_info.setStyleSheet("QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"")
        self.admin_info.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_info.setObjectName("admin_info")
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def go_to_intro(self):
        self.widget.setCurrentIndex(0)

    def go_to_create_new_film(self):
        self.widget.setCurrentIndex(3)

    def go_to_remove_film(self):
        self.widget.setCurrentIndex(4)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Dodaj nowy film"))
        self.pushButton_2.setText(_translate("Form", "Usuń film"))
        self.pushButton_3.setText(_translate("Form", "Wyświetl liste filmów"))
        self.admin_info.setText(_translate("Form", "Panel administratora"))
        self.return_button.setText(_translate("Form", "Powrót do strony głównej"))


