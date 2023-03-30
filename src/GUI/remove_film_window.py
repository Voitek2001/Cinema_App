from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_utils import get_list_of_films


class Ui_remove_panel(object):
    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(180, 20, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(80, 80, 600, 351))
        #rgb(7, 87, 247)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget {\n"
                                      "background:rgba(255, 255, 255, 0.7);\n"
                                      "}")

        self.remove_button = QtWidgets.QPushButton(Form)
        self.remove_button.setGeometry(QtCore.QRect(265, 500, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.remove_button.setFont(font)
        self.remove_button.setStyleSheet("QPushButton {\n"
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
        self.remove_button.setObjectName("remove_button")
        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setGeometry(QtCore.QRect(100, 450, 570, 31))
        self.info_label.setStyleSheet("QLabel {\n"
"    background: rgba(255, 255, 255, 0.9);\n"
"    color: red;\n"
"}\n"
"")
        self.info_label.setObjectName("info_label")
        self.info_about_remove = QtWidgets.QLabel(Form)
        self.info_about_remove.setGeometry(QtCore.QRect(100, 550, 570, 31))
        self.info_about_remove.setStyleSheet("QLabel {\n"
"    background: rgba(255, 255, 255, 0);\n"
"    color: red;\n"
"}\n"
"")
        self.info_about_remove.setText("")
        self.info_about_remove.setAlignment(QtCore.Qt.AlignCenter)
        self.info_about_remove.setObjectName("info_about_remove")
        self.return_button = QtWidgets.QPushButton(Form)
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
        self.return_button.clicked.connect(self.go_to_admin_panel)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.load_films()

    def go_to_admin_panel(self):
        self.widget.setCurrentIndex(2)

    def load_films(self):
        print(get_list_of_films())
        list_of_films = get_list_of_films()
        for _ in range(10):
            for curr_film_title in list_of_films:
                for data in list_of_films[curr_film_title]:
                    info_str = f'Tytuł: {curr_film_title}     |||      Data i godzina: {data["date"]}      |||     Sala: {data["room"]}'
                    self.listWidget.addItem(info_str)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "Wybierz film do usunięcia"))
        self.remove_button.setText(_translate("Form", "Usuń film"))
        self.info_label.setText(_translate("Form", "Usunięty film zostaje na zawsze usunięty z bazy danych"))
        self.return_button.setText(_translate("Form", "Powrót do\n"
"panelu administratora"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
