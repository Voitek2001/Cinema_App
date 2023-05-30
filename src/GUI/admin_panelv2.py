from PyQt5 import QtCore, QtGui, QtWidgets
from admin.admin_utils import get_list_of_films, remove_film_at


class Ui_admin(object):

    def __init__(self, widget):
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        Form.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
                           "background-repeat: no-repeat;\n"
                           "")
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(10, 590, 221, 61))
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
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(80, 60, 600, 381))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget {\n"
                                      "background:rgba(255, 255, 255, 0.7);\n"
                                      "}")
        self.admin_info = QtWidgets.QLabel(Form)
        self.admin_info.setGeometry(QtCore.QRect(180, 10, 400, 41))
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 490, 200, 50))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(266, 490, 200, 50))
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
        self.pushButton_2.setObjectName("pushButton_3")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 490, 200, 50))
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

        self.stat_button_2 = QtWidgets.QPushButton(Form)
        self.stat_button_2.setGeometry(QtCore.QRect(510, 590, 221, 61))
        self.stat_button_2.setStyleSheet("QPushButton {\n"
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
        self.stat_button_2.setObjectName("stat_button_2")
        self.pushButton_2.clicked.connect(self.remove_film)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.load_films()

        self.return_button.clicked.connect(self.go_to_intro)
        self.pushButton.clicked.connect(self.go_to_add_new_film)
        self.pushButton_3.clicked.connect(self.go_to_modify)

    def remove_film(self):
        remove_film_at(self.listWidget.currentRow())
        self.load_films()

    def load_films(self):
        self.listWidget.clear()
        print(get_list_of_films())
        list_of_films = get_list_of_films()

        for curr_film_title in list_of_films:
            for data in list_of_films[curr_film_title]:
                info_str = f'Tytuł: {curr_film_title}     |||      Data i godzina: {data["date"]}      |||     Sala: {data["room"]}'
                self.listWidget.addItem(info_str)

    def go_to_intro(self):

        self.widget.setCurrentIndex(0)

    def go_to_modify(self):
        self.widget.widget(10).property('ui').load_film(self.listWidget.currentRow())
        self.widget.setCurrentIndex(10)

    def go_to_add_new_film(self):
        self.widget.setCurrentIndex(3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.return_button.setText(_translate("Form", "Powrót do strony głównej"))
        self.admin_info.setText(_translate("Form", "Panel administratora"))
        self.pushButton.setText(_translate("Form", "Dodaj nowy film"))
        self.pushButton_2.setText(_translate("Form", "Usuń film"))
        self.pushButton_3.setText(_translate("Form", "Modyfikuj film"))
        self.stat_button_2.setText(_translate("Form", "Analiza danych"))

