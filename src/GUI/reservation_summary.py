from PyQt5 import QtCore, QtGui, QtWidgets
from user.user_utils import add_order_details
from ID_generator import get_and_inc_order, get_and_inc_payment_id


class Ui_reservation_summary(object):
    def __init__(self, widget):
        self.widget = widget
        self.selected_seats = []
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                           "background-repeat: no-repeat;\n"
                           "")

        # title label
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(180, 50, 400, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("\n"
                                       "QLabel {\n"
                                       "    background: rgb(0, 170, 255);\n"
                                       "    border: 2px solid rgb(0, 170, 255);\n"
                                       "    border-radius: 20px;\n"
                                       "    color: white;\n"
                                       "}")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        # film info
        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setGeometry(QtCore.QRect(100, 110, 570, 31))
        self.info_label.setStyleSheet("QLabel {\n"
                                      "    background: rgba(255, 255, 255, 0.7);\n"
                                      "    padding-left: 10;\n"
                                      "}\n"
                                      "")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")

        # table details
        self.table_widget = QtWidgets.QTableWidget(Form)
        self.table_widget.setGeometry(QtCore.QRect(100, 160, 550, 120))
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.verticalHeader().setStretchLastSection(True)
        self.table_widget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.verticalHeader().hide()
        self.table_widget.horizontalHeader().hide()
        self.table_widget.setStyleSheet("QTableWidget {\n"
                                        "    background: rgba(255, 255, 255, 0.7);\n"
                                        "}\n"
                                        "")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.table_widget.setFont(font)
        self.table_widget.setObjectName('table_widget')

        # price info
        self.price_label = QtWidgets.QLabel(Form)
        self.price_label.setGeometry(QtCore.QRect(100, 320, 570, 31))
        self.price_label.setStyleSheet("QLabel {\n"
                                       "    background: rgba(255, 255, 255, 0.7);\n"
                                       "    padding-left: 10;\n"
                                       "}\n"
                                       "")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")

        # go further button
        self.go_further = QtWidgets.QPushButton(Form)
        self.go_further.setGeometry(QtCore.QRect(200, 400, 360, 51))
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.return_button.setFont(font)
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
        self.return_button.clicked.connect(self.go_back)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def load_film_details(self):
        film = self.widget.widget(5).property('film')
        date = self.widget.widget(5).property('date')
        room = self.widget.widget(5).property('room')

        film_details = f'{film}     |||      Data i godzina: {date}      |||     Sala: {room}'
        self.info_label.setText(film_details)

    def fill_payment_table(self):
        self.table_widget.setRowCount(0)
        self.table_widget.insertRow(0)
        self.table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem("Rodzaj biletu"))
        self.table_widget.setItem(0, 1, QtWidgets.QTableWidgetItem("Liczba biletów"))
        self.table_widget.setItem(0, 2, QtWidgets.QTableWidgetItem("Cena"))
        price = self.widget.widget(5).property('price')
        tickets = self.widget.widget(5).property('tickets')
        if tickets['normal'] > 0:
            row = self.table_widget.rowCount()
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem("Bilet normalny"))
            self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(tickets['normal'])))
            self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(price['normal'])))
        if tickets['discounted'] > 0:
            row = self.table_widget.rowCount()
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem("Bilet ulgowy"))
            self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(tickets['discounted'])))
            self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(price['discounted'])))
        total_price = tickets['normal'] * int(price['normal']) + tickets['discounted'] * int(price['discounted'])
        self.price_label.setText(f'Łączna wartość zamówienia: {total_price}')

        self.widget.widget(9).property("ui").set_total_cost(total_price)


    def go_further_clicked(self):

        order_id = get_and_inc_order()
        film_id = self.widget.widget(5).property('film_id')
        payment_id = get_and_inc_payment_id()
        self.widget.widget(9).setProperty('payment_id', payment_id)
        self.widget.widget(9).setProperty("order_id", order_id)
        tickets = self.widget.widget(5).property('tickets')
        price = self.widget.widget(5).property('price')
        total_price = tickets['normal'] * price['normal'] + tickets['discounted'] * price['discounted']
        try:
            add_order_details(order_id, film_id,
                              payment_id, tickets['normal'],
                              tickets['discounted'], total_price, self.selected_seats)
        except Exception as err_msg:
            print(err_msg)
            print("Bład podczas zapisywania do bazy danych")
            self.widget.setCurrentIndex(0)
            return

        self.widget.setCurrentIndex(8)

    def go_back(self):
        self.widget.setCurrentIndex(6)

    def init_selected_seats(self, seats):
        self.selected_seats = seats

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "Podsumowanie rezerwacji"))
        self.info_label.setText(_translate("Form", "Informacja o wybranym seansie"))
        self.go_further.setText(_translate("show_film_window", "Przejdź do wyboru płatności"))
        self.return_button.setText(_translate("Form", "Powrót do wyboru miejsc"))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
