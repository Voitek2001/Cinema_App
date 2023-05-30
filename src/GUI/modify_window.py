import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

from admin.admin_utils import add_new_film, load_film_at, replace_film_at, remove_film_at
from common_utils import get_timedelta_from_string, get_datetime_from_string
from common_utils import Category
class Ui_modify(object):


    def __init__(self, widget):
            self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                           "background-repeat: no-repeat;\n"
                           "")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 100, 231, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.new_film_duration = QtWidgets.QLabel(Form)
        self.new_film_duration.setGeometry(QtCore.QRect(30, 310, 200, 40))
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
        self.new_film_hour = QtWidgets.QLabel(Form)
        self.new_film_hour.setGeometry(QtCore.QRect(30, 380, 200, 40))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 450, 231, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 290, 251, 16))
        self.label_2.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(20, 600, 200, 40))
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
        self.film_spec = QtWidgets.QLabel(Form)
        self.film_spec.setGeometry(QtCore.QRect(80, 20, 440, 40))
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
        self.new_film_cat = QtWidgets.QLabel(Form)
        self.new_film_cat.setGeometry(QtCore.QRect(30, 170, 200, 40))
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
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 380, 231, 40))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 240, 231, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.new_film_room_id = QtWidgets.QLabel(Form)
        self.new_film_room_id.setGeometry(QtCore.QRect(30, 450, 200, 40))
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
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(260, 170, 231, 40))
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
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 360, 251, 16))
        self.label_3.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.new_film_date = QtWidgets.QLabel(Form)
        self.new_film_date.setGeometry(QtCore.QRect(30, 240, 200, 40))
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
        self.new_film_title = QtWidgets.QLabel(Form)
        self.new_film_title.setGeometry(QtCore.QRect(30, 100, 200, 40))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 310, 231, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.new_film_send = QtWidgets.QPushButton(Form)
        self.new_film_send.setGeometry(QtCore.QRect(275, 570, 200, 40))
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
        self.new_film_send.clicked.connect(self.modify_film)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 220, 251, 16))
        self.label.setStyleSheet("QLabel {\n"
"    background:rgba(255, 255, 255, 0.3);\n"
"    color: black;\n"
"}")
        self.label.setObjectName("label")
        self.new_film_title_2 = QtWidgets.QLabel(Form)
        self.new_film_title_2.setGeometry(QtCore.QRect(530, 40, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_title_2.setFont(font)
        self.new_film_title_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_title_2.setObjectName("new_film_title_2")
        self.new_film_room_id_2 = QtWidgets.QLabel(Form)
        self.new_film_room_id_2.setGeometry(QtCore.QRect(530, 450, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_room_id_2.setFont(font)
        self.new_film_room_id_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_room_id_2.setText("")
        self.new_film_room_id_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_room_id_2.setObjectName("new_film_room_id_2")






        # self.lineEdit_6.setGeometry(QtCore.QRect(260, 520, 230, 40))

        self.price_2 = QtWidgets.QLabel(Form)
        self.price_2.setGeometry(QtCore.QRect(530, 520, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_2.setFont(font)
        self.price_2.setStyleSheet("\n"
                                              "QLabel {\n"
                                              "    background: rgb(0, 170, 255);\n"
                                              "    border: 2px solid rgb(0, 170, 255);\n"
                                              "    border-radius: 20px;\n"
                                              "    color: white;\n"
                                              "}")
        self.price_2.setText("")
        self.price_2.setAlignment(QtCore.Qt.AlignCenter)
        self.price_2.setObjectName("price_2")

        self.price_1 = QtWidgets.QLabel(Form)
        self.price_1.setGeometry(QtCore.QRect(30, 520, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_1.setFont(font)
        self.price_1.setStyleSheet("\n"
                                   "QLabel {\n"
                                   "    background: rgb(0, 170, 255);\n"
                                   "    border: 2px solid rgb(0, 170, 255);\n"
                                   "    border-radius: 20px;\n"
                                   "    color: white;\n"
                                   "}")
        self.price_1.setText("")
        self.price_1.setAlignment(QtCore.Qt.AlignCenter)
        self.price_1.setObjectName("price_1")

        self.new_film_hour_2 = QtWidgets.QLabel(Form)
        self.new_film_hour_2.setGeometry(QtCore.QRect(530, 380, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_hour_2.setFont(font)
        self.new_film_hour_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_hour_2.setText("")
        self.new_film_hour_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_hour_2.setObjectName("new_film_hour_2")
        self.new_film_cat_2 = QtWidgets.QLabel(Form)
        self.new_film_cat_2.setGeometry(QtCore.QRect(530, 170, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_cat_2.setFont(font)
        self.new_film_cat_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_cat_2.setText("")
        self.new_film_cat_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_cat_2.setObjectName("new_film_cat_2")
        self.new_film_title_3 = QtWidgets.QLabel(Form)
        self.new_film_title_3.setGeometry(QtCore.QRect(530, 100, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_title_3.setFont(font)
        self.new_film_title_3.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_title_3.setText("")
        self.new_film_title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_title_3.setObjectName("new_film_title_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 610, 400, 40))
        self.label_4.setStyleSheet("QLabel {\n"
                                   "background:rgba(255, 255, 255, 0);\n"
                                   "color: red;\n"
                                   "}")
        self.label_4.setObjectName("label_4")




        self.new_film_duration_2 = QtWidgets.QLabel(Form)
        self.new_film_duration_2.setGeometry(QtCore.QRect(530, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_duration_2.setFont(font)
        self.new_film_duration_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.new_film_duration_2.setText("")
        self.new_film_duration_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_duration_2.setObjectName("new_film_duration_2")






        self.new_film_date_2 = QtWidgets.QLabel(Form)
        self.new_film_date_2.setGeometry(QtCore.QRect(530, 240, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_film_date_2.setFont(font)
        self.new_film_date_2.setStyleSheet("\n"
"QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 520, 230, 40))
        # self.lineEdit_3.setGeometry(QtCore.QRect(260, 310, 231, 40))

        self.lineEdit_6.setObjectName("lineEdit_5")
        self.new_film_date_2.setText("")
        self.new_film_date_2.setAlignment(QtCore.Qt.AlignCenter)
        self.new_film_date_2.setObjectName("new_film_date_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.return_button.clicked.connect(self.go_to_admin)
        self.mod_row = -1
    def go_to_admin(self):
        self.widget.setCurrentIndex(2)


    def load_film(self, row):
        self.mod_row = row

        film = load_film_at(row)
        self.new_film_date_2.setText(film['film_datetime'][:10])
        self.new_film_cat_2.setText(rev_switch_cat(film['category']))
        self.new_film_duration_2.setText(film['duration'])
        self.new_film_hour_2.setText(film['film_datetime'][11:])
        self.new_film_room_id_2.setText(str(film['room_id']))
        self.new_film_title_3.setText(film['title'])
        self.price_2.setText(str(film['price']['normal']))


        self.listWidget.setCurrentItem(self.listWidget.item(film['category']-1))
        self.lineEdit.setText(film['title'])
        self.lineEdit_2.setText(film['film_datetime'][:10])
        self.lineEdit_3.setText(film['duration'])
        self.lineEdit_4.setText(str(film['room_id']))
        self.lineEdit_5.setText(film['film_datetime'][11:])
        self.lineEdit_6.setText(str(film['price']['normal']))


    def modify_film(self):
            selected_item = self.listWidget.currentItem()
            if selected_item is None:
                self.label_4.setText("Wybierz kategorie!")
                return
            film_title = self.lineEdit.text()
            film_cat = switch_cat(selected_item.text())
            film_date = self.lineEdit_2.text()
            film_duration = self.lineEdit_3.text()
            film_hour = self.lineEdit_5.text()
            film_room_id = self.lineEdit_4.text()
            ticket_price = self.lineEdit_6.text()
            try:
                    _ = int(film_room_id)
            except ValueError as err_msg:
                    print(err_msg)
                    self.label_4.setText("Numer sali musi być liczbą")
                    return
            try:
                    _ = int(ticket_price)
            except ValueError as err_msg:
                    print(err_msg)
                    self.label_4.setText("Cena musi być liczbą")
                    return
            try:
                    film_dur = get_timedelta_from_string(film_duration)
                    newfilm_datetime = datetime.datetime.strptime(film_date, "%Y-%m-%d") + get_timedelta_from_string(
                            film_hour)

            except ValueError as err_msg:
                    print(err_msg)
                    print("Błedny format dla godziny lub daty!")
                    self.label_4.setText("Błedny format dla godziny lub daty!")
                    # 2010-04-10 13:20:00, TRWAJACYM 2:00:00 W SALI 1]
                    return

            try:
                    _ = int(ticket_price)
                    remove_film_at(self.mod_row)
                    add_new_film(newfilm_datetime, film_dur, film_cat, film_title, film_room_id, ticket_price)
                    self.label_4.setText("Zmodyfikowano pomyślnie nowy film")
            except ValueError as err_msg:
                    print(err_msg)
                    self.label_4.setText(str(err_msg))

            self.widget.widget(2).property('ui').load_films()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.new_film_duration.setText(_translate("Form", "Podaj czas trwania:"))
        self.new_film_hour.setText(_translate("Form", "Godzina:"))
        self.label_2.setText(_translate("Form", "Wymagany format: \"%H:%M:%S\""))
        self.return_button.setText(_translate("Form", "Powrót do\n"
"panelu administratora"))
        self.film_spec.setText(_translate("Form", "Modyfikowanie filmu"))
        self.new_film_cat.setText(_translate("Form", "Wybierz kategorie:"))
        self.new_film_room_id.setText(_translate("Form", "Podaj numer sali:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Akcja"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Komedia"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Dramat"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Fantasy"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "Horror"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "Mystery"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "Thriller"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "Western"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "Wymagany format: \"%H:%M:%S\""))
        self.new_film_date.setText(_translate("Form", "Podaj date:"))
        self.new_film_title.setText(_translate("Form", "Podaj tytuł:"))
        self.new_film_send.setText(_translate("Form", "Modyfikuj film"))
        self.label.setText(_translate("Form", "Wymagany format: \"%Y-%M-%D\""))
        self.new_film_title_2.setText(_translate("Form", "Obecne dane:"))
        self.price_1.setText(_translate("Form", "Cena biletu:"))

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


def rev_switch_cat(id):
    if id == 1:
        return "Akcja"
    if id == 2:
        return "Komedia"
    if id == 3:
        return "Dramat"
    if id == 4:
        return "Fantasy"
    if id == 5:
        return "Mystery"
    if id == 6:
        return "Thriller"
    if id == 7:
        return "Western"



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
