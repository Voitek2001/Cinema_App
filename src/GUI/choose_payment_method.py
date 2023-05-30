from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose_payment_method(object):
    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                           "background-repeat: no-repeat;\n"
                           "")

        # choose label
        self.choose_label = QtWidgets.QLabel(Form)
        self.choose_label.setGeometry(QtCore.QRect(180, 100, 400, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.choose_label.setFont(font)
        self.choose_label.setStyleSheet("\n"
                                        "QLabel {\n"
                                        "    background: rgb(0, 170, 255);\n"
                                        "    border: 2px solid rgb(0, 170, 255);\n"
                                        "    border-radius: 20px;\n"
                                        "    color: white;\n"
                                        "}")
        self.choose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_label.setObjectName("choose_label")

        # payment method radiobutton
        self.choose_radio1 = QtWidgets.QRadioButton(Form)
        self.choose_radio1.setGeometry(QtCore.QRect(220, 180, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_radio1.setFont(font)
        self.choose_radio1.setStyleSheet("QRadioButton {\n"
                                         "    background: rgba(255, 255, 255, 0.7);\n"
                                         "    padding-left: 10;\n"
                                         "}\n"
                                         "")

        self.choose_radio2 = QtWidgets.QRadioButton(Form)
        self.choose_radio2.setGeometry(QtCore.QRect(220, 230, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_radio2.setFont(font)
        self.choose_radio2.setStyleSheet("QRadioButton {\n"
                                         "    background: rgba(255, 255, 255, 0.7);\n"
                                         "    padding-left: 10;\n"
                                         "}\n"
                                         "")

        # go further button
        self.go_further = QtWidgets.QPushButton(Form)
        self.go_further.setGeometry(QtCore.QRect(180, 360, 400, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.go_further.setFont(font)
        self.go_further.setStyleSheet(
            "QPushButton {background: rgb(0, 170, 255);border: 2px solid rgb(0, 170, 255);border-radius: 20px;color: white;} QPushButton:hover {background-color: rgb(255, 0, 127);border: 2px solid rgb(255, 0, 127);}")
        self.go_further.setObjectName("go_further")
        self.go_further.clicked.connect(self.go_further_clicked)

        # return button
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(50, 590, 221, 51))
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
        font = QtGui.QFont()
        font.setPointSize(15)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(self.go_back)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def go_further_clicked(self):
        if self.choose_radio1.isChecked():
            self.widget.setCurrentIndex(0)
        else:
            self.widget.setCurrentIndex(9)
        

    def go_back(self):
        self.widget.setCurrentIndex(7)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.choose_label.setText(_translate("Form", "Wybierz sposób płatności"))
        self.choose_radio1.setText(_translate("Form", "Płacę przy wejściu"))
        self.choose_radio2.setText(_translate("Form", "Płacę teraz"))
        self.go_further.setText(_translate("show_film_window", "Potwierdzam i płacę"))
        self.return_button.setText(_translate("Form", "Powrót"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
