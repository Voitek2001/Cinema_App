import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_utils import add_new_film
from common_utils import get_timedelta_from_string, get_datetime_from_string
from common_utils import Category


class Ui_NewFilm(object):
    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, new_film):
        new_film.setObjectName("new_film")
        new_film.resize(760, 670)
        font = QtGui.QFont()
        font.setPointSize(9)
        new_film.setFont(font)
        new_film.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.listWidget = QtWidgets.QListWidget(new_film)
        self.listWidget.setGeometry(QtCore.QRect(360, 170, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.film_spec = QtWidgets.QLabel(new_film)
        self.film_spec.setGeometry(QtCore.QRect(160, 20, 440, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.film_spec.setFont(font)
        self.film_spec.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.film_spec.setAlignment(QtCore.Qt.AlignCenter)
        self.film_spec.setObjectName("film_spec")
        self.new_film_title = QtWidgets.QLabel(new_film)
        self.new_film_title.setGeometry(QtCore.QRect(110, 100, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_title.setFont(font)
        self.new_film_title.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_title.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_title.setObjectName("new_film_title")
        self.new_film_cat = QtWidgets.QLabel(new_film)
        self.new_film_cat.setGeometry(QtCore.QRect(110, 170, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_cat.setFont(font)
        self.new_film_cat.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_cat.setObjectName("new_film_cat")
        self.new_film_date = QtWidgets.QLabel(new_film)
        self.new_film_date.setGeometry(QtCore.QRect(110, 240, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_date.setFont(font)
        self.new_film_date.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_date.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_date.setObjectName("new_film_date")
        self.new_film_duration = QtWidgets.QLabel(new_film)
        self.new_film_duration.setGeometry(QtCore.QRect(110, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_duration.setFont(font)
        self.new_film_duration.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_duration.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_duration.setObjectName("new_film_duration")
        self.new_film_room_id = QtWidgets.QLabel(new_film)
        self.new_film_room_id.setGeometry(QtCore.QRect(110, 450, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_room_id.setFont(font)
        self.new_film_room_id.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_room_id.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_room_id.setObjectName("new_film_room_id")
        self.lineEdit = QtWidgets.QLineEdit(new_film)
        self.lineEdit.setGeometry(QtCore.QRect(360, 100, 300, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(new_film)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 240, 300, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(new_film)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 310, 300, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(new_film)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 450, 300, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.new_film_send = QtWidgets.QPushButton(new_film)
        self.new_film_send.setGeometry(QtCore.QRect(265, 570, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_send.setFont(font)
        self.new_film_send.setStyleSheet("QPushButton {\n"
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
        self.new_film_send.setObjectName("new_film_send")
        self.new_film_send.clicked.connect(self.submit_new_film)
        self.return_button = QtWidgets.QPushButton(new_film)
        self.return_button.setGeometry(QtCore.QRect(10, 600, 200, 40))
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
        self.return_button.clicked.connect(self.go_back_to_admin_panel)
        self.label = QtWidgets.QLabel(new_film)
        self.label.setGeometry(QtCore.QRect(340, 220, 300, 16))
        self.label.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(new_film)
        self.label_2.setGeometry(QtCore.QRect(340, 290, 321, 16))
        self.label_2.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.new_film_hour = QtWidgets.QLabel(new_film)
        self.new_film_hour.setGeometry(QtCore.QRect(110, 380, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_hour.setFont(font)
        self.new_film_hour.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_hour.setObjectName("new_film_hour")
        self.lineEdit_5 = QtWidgets.QLineEdit(new_film)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 380, 300, 40))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(new_film)
        self.label_3.setGeometry(QtCore.QRect(340, 360, 321, 16))
        self.label_3.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(new_film)
        self.label_4.setGeometry(QtCore.QRect(180, 510, 400, 40))
        self.label_4.setStyleSheet("QLabel {\n"
"background:rgba(255, 255, 255, 0);\n"
"color: red;\n"
"}")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(new_film)
        QtCore.QMetaObject.connectSlotsByName(new_film)


    def submit_new_film(self):
        selected_item = self.listWidget.currentItem()
        film_title = self.lineEdit.text()
        film_cat = switch_cat(selected_item.text())
        film_date = self.lineEdit_2.text()
        film_duration = self.lineEdit_3.text()
        film_hour = self.lineEdit_5.text()
        film_room_id = self.lineEdit_4.text()


        try:
            film_dur = get_timedelta_from_string(film_duration)
            newfilm_datetime = datetime.datetime.strptime(film_date, "%Y-%m-%d") + get_timedelta_from_string(film_hour)
            try:
                add_new_film(newfilm_datetime, film_dur, film_cat, film_title, film_room_id)
                self.label_4.setText("Dodano pomyślnie nowy film")
            except ValueError as err_msg:
                print(err_msg)
                self.label_4.setText(str(err_msg))
        except ValueError as err_msg:
            print(err_msg)
            print("Błedny format dla godziny lub daty!")
            self.label_4.setText("Błedny format dla godziny lub daty!")
        #2010-04-10 13:20:00, TRWAJACYM 2:00:00 W SALI 1]


    def go_back_to_admin_panel(self):
        self.widget.setCurrentIndex(2)

    def retranslateUi(self, new_film):
        _translate = QtCore.QCoreApplication.translate
        new_film.setWindowTitle(_translate("new_film", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("new_film", "Akcja"))
        item = self.listWidget.item(1)
        item.setText(_translate("new_film", "Komedia"))
        item = self.listWidget.item(2)
        item.setText(_translate("new_film", "Dramat"))
        item = self.listWidget.item(3)
        item.setText(_translate("new_film", "Fantasy"))
        item = self.listWidget.item(4)
        item.setText(_translate("new_film", "Horror"))
        item = self.listWidget.item(5)
        item.setText(_translate("new_film", "Mystery"))
        item = self.listWidget.item(6)
        item.setText(_translate("new_film", "Thriller"))
        item = self.listWidget.item(7)
        item.setText(_translate("new_film", "Western"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.film_spec.setText(_translate("new_film", "Podaj szczegóły nowego filmu"))
        self.new_film_title.setText(_translate("new_film", "Podaj tytuł:"))
        self.new_film_cat.setText(_translate("new_film", "Wybierz kategorie:"))
        self.new_film_date.setText(_translate("new_film", "Podaj date:"))
        self.new_film_duration.setText(_translate("new_film", "Podaj czas trwania:"))
        self.new_film_room_id.setText(_translate("new_film", "Podaj numer sali:"))
        self.new_film_send.setText(_translate("new_film", "Dodaj film"))
        self.return_button.setText(_translate("new_film", "Powrót do\n"
"panelu administratora"))
        self.label.setText(_translate("new_film", "Wymagany format: \"%Y-%M-%D\""))
        self.label_2.setText(_translate("new_film", "Wymagany format: \"%H:%M:%S\""))
        self.new_film_hour.setText(_translate("new_film", "Godzina:"))
        self.label_3.setText(_translate("new_film", "Wymagany format: \"%H:%M:%S\""))

def switch_cat(curr_cat):

    if curr_cat == "Akcja":
        return Category.ACTION
    elif curr_cat == "Komedia":
        return Category.COMEDY
    elif curr_cat == "Dramat":
        return Category.DRAMA
    elif curr_cat == "Fantasy":
        return Category.FANTASY
    elif curr_cat == "Mystery":
        return Category.MYSTERY
    elif curr_cat == "Thriller":
        return Category.THRILLER
    elif curr_cat == "Western":
        return Category.WESTERN



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_film = QtWidgets.QWidget()
    ui = Ui_new_film()
    ui.setupUi(new_film)
    new_film.show()
    sys.exit(app.exec_())
