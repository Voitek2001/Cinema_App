from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_utils import get_list_of_orders


class Ui_select_seats(object):
    def __init__(self, widget):
        self.widget = widget
        self.number_of_tickets = 3
        self.checked = set()
        self.blocked = set()

    def setupUi(self, select_seats):
        select_seats.setObjectName("select_seats")
        select_seats.resize(760, 670)
        font = QtGui.QFont()
        font.setPointSize(12)
        select_seats.setFont(font)
        select_seats.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                                   "background-repeat: no-repeat;\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(select_seats)
        self.centralwidget.setObjectName("centralwidget")

        # "ekran" label
        self.label = QtWidgets.QLabel(select_seats)
        self.label.setGeometry(QtCore.QRect(200, 40, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # seat buttons
        self.seats = []
        for i in range(10):
            for j in range(10):
                self.seats.append(QtWidgets.QPushButton(select_seats))
                self.seats[-1].setGeometry(QtCore.QRect(137 + j * 50, 80 + i * 50, 40, 40))
                self.seats[-1].setText("")
                self.seats[-1].setProperty('row', i)
                self.seats[-1].setProperty('column', j)
                self.seats[-1].setCheckable(True)
                self.seats[-1].setChecked(False)
                self.seats[-1].setObjectName("seat")
                self.seats[-1].setStyleSheet("QPushButton {background: green; border:none}"
                                             "QPushButton:disabled {background: gray;}"
                                             "QPushButton:checked {background: orange;}")
                self.seats[-1].clicked.connect(lambda checked, seat=self.seats[-1]: self.seat_clicked(seat))

        # count of checked seats label
        self.label_2 = QtWidgets.QLabel(select_seats)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # go further button
        self.go_further = QtWidgets.QPushButton(self.centralwidget)
        self.go_further.setEnabled(False)
        self.go_further.setGeometry(QtCore.QRect(300, 590, 410, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.go_further.setFont(font)
        self.go_further.setStyleSheet(
            "QPushButton {background: rgb(0, 170, 255);border: 2px solid rgb(0, 170, 255);border-radius: 20px;color: white;} QPushButton:hover {background-color: rgb(255, 0, 127);border: 2px solid rgb(255, 0, 127);}")
        self.go_further.setObjectName("go_further")
        self.go_further.clicked.connect(self.go_further_clicked)

        # return button
        self.return_button = QtWidgets.QPushButton(select_seats)
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

        self.retranslateUi(select_seats)
        QtCore.QMetaObject.connectSlotsByName(select_seats)

    def retranslateUi(self, select_seats):
        _translate = QtCore.QCoreApplication.translate
        select_seats.setWindowTitle(_translate("select_seats", "Form"))
        self.label.setText(_translate("select_seats", "Ekran"))
        self.label_2.setText(
            _translate("select_seats", f'Wybrano 0/{self.number_of_tickets} miejsc.'))
        self.go_further.setText(_translate("select_seats", "Przejdź dalej"))
        self.return_button.setText(_translate("select_seats", "Powrót do wyboru filmu"))

    def set_number_of_tickets(self, number):
        _translate = QtCore.QCoreApplication.translate
        self.number_of_tickets = number
        self.label_2.setText(
            _translate("select_seats", f'Wybrano 0/{self.number_of_tickets} miejsc.'))

    def uncheck_seats(self):
        self.checked.clear()
        self.load_blocked()
        for seat in self.seats:
            if (seat.property('row'), seat.property('column')) in self.blocked:
                seat.setEnabled(False)
            else:
                seat.setEnabled(True)
            seat.setChecked(False)

    def seat_clicked(self, seat):
        row = seat.property('row')
        column = seat.property('column')
        if seat.isChecked():
            self.checked.add((row, column))
        else:
            self.checked.remove((row, column))
        number_of_clicked = len(self.checked)
        if number_of_clicked == self.number_of_tickets:
            self.go_further.setEnabled(True)
            self.set_button_enabled(False)
        else:
            self.go_further.setEnabled(False)
            self.set_button_enabled(True)
        self.label_2.setText(f'Wybrano {number_of_clicked}/{self.number_of_tickets} miejsc.')

    def set_button_enabled(self, value):
        for seat in self.seats:
            if not seat.isChecked() and (seat.property('row'), seat.property('column')) not in self.blocked:
                seat.setEnabled(value)

    def load_blocked(self):
        orders = get_list_of_orders()
        film_id = self.widget.widget(5).property('film_id')
        self.blocked.clear()
        for order in orders.values():
            if order['film_id'] == film_id:
                self.blocked.update(order['seats'])

    def go_further_clicked(self):
        self.widget.currentWidget().setProperty('seats', self.checked)
        self.widget.widget(7).property('ui').load_film_details()
        self.widget.widget(7).property('ui').fill_payment_table()
        self.widget.widget(7).property('ui').init_selected_seats(self.checked)
        self.widget.setCurrentIndex(7)

    def go_back(self):
        self.widget.setCurrentIndex(5)
        print(self.number_of_tickets)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    select_seats = QtWidgets.QWidget()
    ui = Ui_select_seats()
    ui.setupUi(select_seats)
    select_seats.show()
    sys.exit(app.exec_())