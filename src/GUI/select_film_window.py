from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_utils import get_list_of_films


class Ui_show_film_window(object):
    def __init__(self, widget):
        self.widget = widget
        self.films = get_list_of_films()

    def setupUi(self, show_film_window):
        show_film_window.setObjectName("show_film_window")
        show_film_window.resize(760, 670)
        show_film_window.setWindowTitle("")
        show_film_window.setAutoFillBackground(False)
        show_film_window.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                                       "background-repeat: no-repeat;\n"
                                       "")
        self.centralwidget = QtWidgets.QWidget(show_film_window)
        self.centralwidget.setObjectName("centralwidget")

        # film comboBox
        self.select_film = QtWidgets.QComboBox(self.centralwidget)
        self.select_film.setEnabled(True)
        self.select_film.setGeometry(QtCore.QRect(200, 160, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_film.setFont(font)
        self.select_film.setIconSize(QtCore.QSize(20, 20))
        self.select_film.setObjectName("select_film")
        self.fill_films()
        self.select_film.activated.connect(self.film_checked)

        # date combobox
        self.select_date = QtWidgets.QComboBox(self.centralwidget)
        self.select_date.setEnabled(False)
        self.select_date.setGeometry(QtCore.QRect(200, 240, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_date.setFont(font)
        self.select_date.setIconSize(QtCore.QSize(20, 20))
        self.select_date.setObjectName("select_date")
        self.select_date.addItem("Wybierz datę")
        self.select_date.activated.connect(self.date_checked)

        # normal tickets
        self.normal_tickets_label = QtWidgets.QLabel(self.centralwidget)
        self.normal_tickets_label.setGeometry(QtCore.QRect(200, 316, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.normal_tickets_label.setFont(font)
        self.normal_tickets_label.setAutoFillBackground(False)
        self.normal_tickets_label.setStyleSheet("QLabel {\n"
                                                "    background: rgb(0, 170, 255);\n"
                                                "    border: 2px solid rgb(0, 170, 255);\n"
                                                "    border-radius: 10px;\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "")
        self.normal_tickets_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_tickets_label.setObjectName("normal_tickets_label")

        self.normal_tickets = QtWidgets.QSpinBox(show_film_window)
        self.normal_tickets.setGeometry(QtCore.QRect(330, 320, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.normal_tickets.setFont(font)
        self.normal_tickets.setMaximum(10)
        self.normal_tickets.setObjectName("normal_tickets")
        self.normal_tickets.valueChanged.connect(self.number_tickets_changed)

        # discounted tickets
        self.discounted_tickets_label = QtWidgets.QLabel(self.centralwidget)
        self.discounted_tickets_label.setGeometry(QtCore.QRect(383, 316, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discounted_tickets_label.setFont(font)
        self.discounted_tickets_label.setAutoFillBackground(False)
        self.discounted_tickets_label.setStyleSheet("QLabel {\n"
                                                    "    background: rgb(0, 170, 255);\n"
                                                    "    border: 2px solid rgb(0, 170, 255);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    color: white;\n"
                                                    "}\n"
                                                    "")
        self.discounted_tickets_label.setAlignment(QtCore.Qt.AlignCenter)
        self.discounted_tickets_label.setObjectName("discounted_tickets_label")

        self.discounted_tickets = QtWidgets.QSpinBox(show_film_window)
        self.discounted_tickets.setGeometry(QtCore.QRect(518, 320, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discounted_tickets.setFont(font)
        self.discounted_tickets.setMaximum(10)
        self.discounted_tickets.setObjectName("discounted_tickets")
        self.discounted_tickets.valueChanged.connect(self.number_tickets_changed)

        # go further button
        self.go_further = QtWidgets.QPushButton(self.centralwidget)
        self.go_further.setEnabled(False)
        self.go_further.setGeometry(QtCore.QRect(200, 400, 360, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.go_further.setFont(font)
        self.go_further.setStyleSheet(
            "QPushButton {background: rgb(0, 170, 255);border: 2px solid rgb(0, 170, 255);border-radius: 20px;color: white;} QPushButton:hover {background-color: rgb(255, 0, 127);border: 2px solid rgb(255, 0, 127);}")
        self.go_further.setObjectName("go_further")
        self.go_further.clicked.connect(self.go_further_clicked)

        # return button
        self.return_button = QtWidgets.QPushButton(show_film_window)
        self.return_button.setGeometry(QtCore.QRect(50, 520, 221, 51))
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
        self.return_button.clicked.connect(self.go_to_intro)

        self.retranslateUi(show_film_window)
        QtCore.QMetaObject.connectSlotsByName(show_film_window)

    def retranslateUi(self, show_film_window):
        _translate = QtCore.QCoreApplication.translate
        self.go_further.setText(_translate("show_film_window", "Przejdź dalej"))
        self.return_button.setText(_translate("show_film_window", "Powrót do strony głównej"))
        self.normal_tickets_label.setText(_translate("show_film_window", "Bilet normalny"))
        self.discounted_tickets_label.setText(_translate("show_film_window", "Bilet ulgowy"))

    def fill_films(self):
        self.select_film.addItem("Wybierz film")
        self.select_film.addItems(self.films.keys())

    def film_checked(self):
        checked = self.select_film.currentIndex()
        if checked == 0:
            self.select_date.setEnabled(False)
            self.select_date.clear()
            self.select_date.addItem("Wybierz datę i salę")
            self.go_further.setEnabled(False)
        else:
            self.fill_dates()
            self.select_date.setEnabled(True)
            self.go_further.setEnabled(False)

    def fill_dates(self):
        self.select_date.clear()
        self.select_date.addItem("Wybierz datę i salę")
        film = self.select_film.currentText()
        for event in self.films[film]:
            self.select_date.addItem(f'{str(event["date"])} sala {event["room"]}')
            self.select_date.setItemData(-1, event["price"])

    def date_checked(self):
        checked = self.select_date.currentIndex()
        if checked == 0:
            self.go_further.setEnabled(False)
        elif self.is_nonzero_tickets():
            self.go_further.setEnabled(True)

    def is_nonzero_tickets(self):
        return self.normal_tickets.value() + self.discounted_tickets.value() > 0

    def number_tickets_changed(self):
        if self.is_nonzero_tickets() and self.select_date.currentIndex() != 0:
            self.go_further.setEnabled(True)
        else:
            self.go_further.setEnabled(False)

    def go_further_clicked(self):
        film = self.select_film.currentText()
        event = self.films[film][self.select_date.currentIndex() - 1]
        tickets = {'normal': self.normal_tickets.value(), 'discounted': self.discounted_tickets.value()}
        print(f'Wybrano {film} {str(event["date"])} sala {event["room"]} cena {event["price"]}. Bilety: {tickets}')

        self.widget.widget(6).property('ui').set_number_of_tickets(sum(tickets.values()))
        self.widget.widget(6).property('ui').uncheck_seats()
        self.widget.currentWidget().setProperty('film', film)
        self.widget.currentWidget().setProperty('date', event['date'])
        self.widget.currentWidget().setProperty('room', event['room'])
        self.widget.currentWidget().setProperty('price', event['price'])
        self.widget.currentWidget().setProperty('tickets', tickets)
        self.widget.setCurrentIndex(6)

    def go_to_intro(self):
        self.widget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    show_film_window = QtWidgets.QMainWindow()
    ui = Ui_show_film_window()
    ui.setupUi(show_film_window)
    show_film_window.show()
    sys.exit(app.exec_())
