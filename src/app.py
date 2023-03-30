from PyQt5 import QtWidgets
import sys
from GUI.login_window import Ui_login
from GUI.intro_window import Ui_intro
from GUI.admin_panel import Ui_AdminPanel
from GUI.new_film_window import Ui_NewFilm
from GUI.remove_film_window import Ui_remove_panel


if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # init main window
    MainWindow = QtWidgets.QMainWindow()
    intro_ui = Ui_intro(widget)
    intro_ui.setupUi(MainWindow)

    # init login window
    login_ui = QtWidgets.QWidget()
    ui = Ui_login(widget)
    ui.setupUi(login_ui)

    # init admin_panel window
    admin_panel = QtWidgets.QWidget()
    admin_ui = Ui_AdminPanel(widget)
    admin_ui.setupUi(admin_panel)

    # init create_new_film window
    create_new_film_window = QtWidgets.QWidget()
    new_film_ui = Ui_NewFilm(widget)
    new_film_ui.setupUi(create_new_film_window)

    #init remove_film window
    remove_film_window = QtWidgets.QWidget()
    remove_film_ui = Ui_remove_panel(widget)
    remove_film_ui.setupUi(remove_film_window)

    # add windows to widget
    widget.addWidget(MainWindow)
    widget.addWidget(login_ui)
    widget.addWidget(admin_panel)
    widget.addWidget(create_new_film_window)
    widget.addWidget(remove_film_window)

    widget.setFixedWidth(760)
    widget.setFixedHeight(670)
    widget.show()
    #    MainWindow.show()
    sys.exit(app.exec_())

