from PyQt5 import QtCore, QtGui, QtWidgets
from user.payment_utils import check_if_valid_arguments, add_payment_details


class Ui_payment(object):

    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.pay_title = QtWidgets.QLabel(Form)
        self.pay_title.setGeometry(QtCore.QRect(235, 9, 290, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pay_title.setFont(font)
        self.pay_title.setStyleSheet("QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.pay_title.setAlignment(QtCore.Qt.AlignCenter)
        self.pay_title.setObjectName("pay_title")
        self.lineEdit_ban = QtWidgets.QLineEdit(Form)
        self.lineEdit_ban.setGeometry(QtCore.QRect(180, 110, 400, 40))
        self.lineEdit_ban.setObjectName("lineEdit_ban")
        self.ban_label = QtWidgets.QLabel(Form)
        self.ban_label.setGeometry(QtCore.QRect(305, 80, 150, 17))
        self.ban_label.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.ban_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ban_label.setObjectName("ban_label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(305, 180, 150, 17))
        self.label_3.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 160, 20))
        self.label_4.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(430, 280, 160, 20))
        self.label_5.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit2_ban = QtWidgets.QLineEdit(Form)
        self.lineEdit2_ban.setGeometry(QtCore.QRect(180, 210, 400, 40))
        self.lineEdit2_ban.setObjectName("lineEdit2_ban")
        self.lineEdit3_ban = QtWidgets.QLineEdit(Form)
        self.lineEdit3_ban.setGeometry(QtCore.QRect(180, 310, 160, 40))
        self.lineEdit3_ban.setObjectName("lineEdit3_ban")
        self.lineEdit4_ban = QtWidgets.QLineEdit(Form)
        self.lineEdit4_ban.setGeometry(QtCore.QRect(430, 310, 160, 40))
        self.lineEdit4_ban.setObjectName("lineEdit4_ban")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 370, 200, 40))
        self.label.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.8);\n"
"    color: black;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        self.label_info = QtWidgets.QLabel(Form)
        self.label_info.setGeometry(QtCore.QRect(250, 440, 260, 60))
        self.label_info.setStyleSheet("QLabel {\n"
                                 "    color: red;\n"
                                 "   background: rgba(204, 204, 204, 0);\n"

                                 "}")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label")


        self.payment_send = QtWidgets.QPushButton(Form)
        self.payment_send.setGeometry(QtCore.QRect(210, 510, 340, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.payment_send.setFont(font)
        self.payment_send.setStyleSheet("QPushButton {\n"
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
        self.payment_send.setObjectName("new_film_send")

        self.payment_send.clicked.connect(self.do_payment)

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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pay_title.setText(_translate("Form", "Podaj szczegóły płatności"))
        self.ban_label.setText(_translate("Form", "Numer konta:"))
        self.label_3.setText(_translate("Form", "Imie i nazwisko:"))
        self.label_4.setText(_translate("Form", "Data ważności:"))
        self.label_5.setText(_translate("Form", "CVC:"))
        self.label.setText(_translate("Form", "Kwota do zapłaty: "))
        self.payment_send.setText(_translate("Form", "Dokonaj płatności"))
        self.label_info.setText(_translate("Form", ""))
        self.return_button.setText(_translate("Form", "Powrót"))

    def do_payment(self):
        ban, person, date, cvc = self.lineEdit_ban.text(), self.lineEdit2_ban.text()\
            , self.lineEdit3_ban.text(), self.lineEdit4_ban.text()
        order_id = self.widget.currentWidget().property("order_id")
        payment_id = self.widget.currentWidget().property("payment_id")
        # text_res, is_valid = check_if_valid_arguments(
        #         ban,
        #         person,
        #         date,
        #         cvc
        # )
        # if is_valid:
            # def add_payment_details(ban, person, date, cvc, order_id, payment_id):
            # add_payment_details(ban, person, date, cvc, order_id, payment_id)

        try:
            text_res = add_payment_details(ban, person, date, cvc, order_id, payment_id)
            self.label_info.setText(text_res)

        except Exception as err_msg:
            print()
            self.label_info.setStyleSheet("QLabel {\n"
                                     "    background:rgba(255, 255, 255, 0.8);\n"
                                     "    color: red;\n"
                                     "}")
            self.label_info.setText(err_msg.args[0])
            return

        self.widget.setCurrentIndex(0)

    def go_back(self):
        self.widget.setCurrentIndex(7)

    def set_total_cost(self, total_price):
        self.label.setText(f"Kwota do zapłaty: {total_price}")
