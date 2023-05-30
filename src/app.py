from PyQt5 import QtWidgets
import sys
from GUI.login_window import Ui_login
from GUI.intro_window import Ui_intro
from GUI.admin_panel import Ui_AdminPanel
from GUI.new_film_window import Ui_NewFilm
from GUI.remove_film_window import Ui_remove_panel
from GUI.select_film_window import Ui_show_film_window
from GUI.select_seat_window import Ui_select_seats
from GUI.reservation_summary import Ui_reservation_summary
from GUI.choose_payment_method import Ui_choose_payment_method
from GUI.modify_window import Ui_modify
from GUI.payment_window import Ui_payment
from GUI.admin_panelv2 import Ui_admin
from GUI.data_analysis_window import Ui_data_analysis
from ID_generator import init_order_id, init_film_id, init_payment_id


if __name__ == '__main__':

    init_order_id()
    init_film_id()
    init_payment_id()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # init main window
    MainWindow = QtWidgets.QMainWindow()
    # MainWindow.show()
    intro_ui = Ui_intro(widget)
    intro_ui.setupUi(MainWindow)

    # init login window
    login_ui = QtWidgets.QWidget()
    ui = Ui_login(widget)
    ui.setupUi(login_ui)

    # init admin_panel window
    # admin_panel = QtWidgets.QWidget()
    # admin_ui = Ui_AdminPanel(widget)
    # admin_ui.setupUi(admin_panel)

    admin_panel = QtWidgets.QWidget()
    admin_ui = Ui_admin(widget)
    admin_ui.setupUi(admin_panel)
    admin_panel.setProperty('ui', admin_ui)

    # init create_new_film window
    create_new_film_window = QtWidgets.QWidget()
    new_film_ui = Ui_NewFilm(widget)
    new_film_ui.setupUi(create_new_film_window)

    #init remove_film window
    remove_film_window = QtWidgets.QWidget()
    remove_film_ui = Ui_remove_panel(widget)
    remove_film_ui.setupUi(remove_film_window)

    # init select_film window
    select_film_window = QtWidgets.QWidget()
    select_film_ui = Ui_show_film_window(widget)
    select_film_ui.setupUi(select_film_window)

    # init select_seat window
    select_seat_window = QtWidgets.QWidget()
    select_seat_ui = Ui_select_seats(widget)
    select_seat_ui.setupUi(select_seat_window)
    select_seat_window.setProperty('ui', select_seat_ui)

    # init reservation_summary window
    reservation_summary_window = QtWidgets.QWidget()
    reservation_summary_ui = Ui_reservation_summary(widget)
    reservation_summary_ui.setupUi(reservation_summary_window)
    reservation_summary_window.setProperty('ui', reservation_summary_ui)

    choose_payment_method_window = QtWidgets.QWidget()
    choose_payment_method_ui = Ui_choose_payment_method(widget)
    choose_payment_method_ui.setupUi(choose_payment_method_window)

    payment_window = QtWidgets.QWidget()
    payment_window_ui = Ui_payment(widget)
    payment_window_ui.setupUi(payment_window)
    payment_window.setProperty('ui', payment_window_ui)

    modify_window = QtWidgets.QWidget()
    modify_window_ui = Ui_modify(widget)
    modify_window_ui.setupUi(modify_window)
    modify_window.setProperty('ui', modify_window_ui)

    # init reservation_summary window
    data_analysis_window = QtWidgets.QWidget()
    data_analysis_ui = Ui_data_analysis(widget)
    data_analysis_ui.setupUi(data_analysis_window)

    # add windows to widget
    widget.addWidget(MainWindow)
    widget.addWidget(login_ui)
    widget.addWidget(admin_panel)
    widget.addWidget(create_new_film_window)
    widget.addWidget(remove_film_window)
    widget.addWidget(select_film_window)
    widget.addWidget(select_seat_window)
    widget.addWidget(reservation_summary_window)
    widget.addWidget(choose_payment_method_window)
    widget.addWidget(payment_window)
    widget.addWidget(modify_window)
    widget.addWidget(data_analysis_window)

    widget.setFixedWidth(760)
    widget.setFixedHeight(670)
    widget.show()
    #    MainWindow.show()
    sys.exit(app.exec_())

