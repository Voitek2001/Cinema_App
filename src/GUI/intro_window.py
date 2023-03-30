from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_intro(object):
    def __init__(self, widget):
        self.widget = widget


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 670)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(\"resources/home_background.png\");\n"
"background-repeat: no-repeat;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_film = QtWidgets.QPushButton(self.centralwidget)
        self.select_film.setGeometry(QtCore.QRect(200, 250, 360, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_film.setFont(font)
        self.select_film.setStyleSheet("QPushButton {\n"
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
        self.select_film.setObjectName("select_film")
        self.admin_panel = QtWidgets.QPushButton(self.centralwidget)
        self.admin_panel.setGeometry(QtCore.QRect(200, 380, 360, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.admin_panel.setFont(font)
        self.admin_panel.setStyleSheet("QPushButton {\n"
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
        self.admin_panel.setObjectName("admin_panel")
        self.admin_panel.clicked.connect(self.go_to_admin_panel)
        self.cinema_intro = QtWidgets.QLabel(self.centralwidget)
        self.cinema_intro.setGeometry(QtCore.QRect(170, 70, 420, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cinema_intro.setFont(font)
        self.cinema_intro.setAutoFillBackground(False)
        self.cinema_intro.setStyleSheet("QLabel {\n"
"    background: rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"")
        self.cinema_intro.setAlignment(QtCore.Qt.AlignCenter)
        self.cinema_intro.setObjectName("cinema_intro")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def go_to_select_film(self):
        pass
    def go_to_admin_panel(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_film.setText(_translate("MainWindow", "Wybierz film"))
        self.admin_panel.setText(_translate("MainWindow", "Panel administratora"))
        self.cinema_intro.setText(_translate("MainWindow", "Witamy w kinie!"))



