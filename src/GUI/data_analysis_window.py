from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter
from admin.admin_utils import get_raw_list_of_films
from admin.admin_utils import get_list_of_films
from admin.admin_utils import get_raw_list_of_orders
from common_utils import Category
from data_analysis import *
import datetime
import random


class Ui_data_analysis(object):
    def __init__(self, widget):
        self.widget = widget
        self.upload_data()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 670)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setStyleSheet("background-color: #ddd;")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 760, 670))
        self.tabWidget.setObjectName("tabWidget")
        font_small = QtGui.QFont()
        font_small.setPointSize(8)
        font_medium = QtGui.QFont()  # tytuł wykresu
        font_medium.setPointSize(12)

        # tab1 - by categories
        self.tab1 = QtWidgets.QWidget(self.tabWidget)
        self.tab1.setObjectName("tab1")

        # === CHART
        self.chart = QChart()
        self.chart.setTitle("Ilość sprzedanych biletów według kategorii")
        self.chart.setTitleFont(font_medium)
        self.chart.createDefaultAxes()

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.chart_widget = QtWidgets.QWidget(self.tab1)
        self.chart_widget.setGeometry(QtCore.QRect(0, 0, 720, 450))

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.chart_view)
        self.chart_widget.setLayout(self.vbox)

        # Tworzenie osi x
        self.axisX = QDateTimeAxis()
        self.axisX.setFormat("dd/MM/yyyy")  # Format daty dla osi x
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)

        # Tworzenie osi y
        self.axisY = QValueAxis()
        self.axisY.setLabelFormat("%.0f")
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        self.chart.legend().setVisible(True)

        # === CATEGORIES BOX
        self.categories_label = QtWidgets.QLabel(self.tab1)
        self.categories_label.setGeometry(QtCore.QRect(30, 460, 150, 40))
        self.categories_label.setFont(font_small)

        self.list_widget = QtWidgets.QListWidget(self.tab1)
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.MultiSelection)
        self.list_widget.setGeometry(QtCore.QRect(30, 500, 140, 140))
        for member in Category:
            self.list_widget.addItem(member.name)
        for i in range(self.list_widget.count()):
            self.list_widget.item(i).setSelected(True)
        self.list_widget.setFont(font_small)

        # === DATES ===
        self.date_range_label = QtWidgets.QLabel(self.tab1)
        self.date_range_label.setGeometry(QtCore.QRect(200, 460, 100, 40))
        self.date_range_label.setFont(font_small)

        self.date_edit_start = QtWidgets.QDateEdit(self.tab1)
        self.date_edit_start.setGeometry(QtCore.QRect(300, 460, 140, 40))
        self.date_edit_start.setObjectName("date_edit_start")
        self.date_edit_start.setFont(font_small)
        self.date_start = QtCore.QDate(2025, 5, 1)
        self.date_edit_start.setDate(self.date_start)

        self.date_range_label2 = QtWidgets.QLabel(self.tab1)
        self.date_range_label2.setGeometry(QtCore.QRect(200, 560, 30, 40))
        self.date_range_label2.setFont(font_small)

        self.date_edit_end = QtWidgets.QDateEdit(self.tab1)
        self.date_edit_end.setGeometry(QtCore.QRect(300, 560, 140, 40))
        self.date_edit_end.setObjectName("date_edit_end")
        self.date_edit_end.setFont(font_small)
        self.date_end = QtCore.QDate(2025, 5, 31)
        self.date_edit_end.setDate(self.date_end)

        # === DICOUNTED / NORMAL ===
        self.ticket_type_label = QtWidgets.QLabel(self.tab1)
        self.ticket_type_label.setGeometry(QtCore.QRect(480, 460, 100, 40))
        self.ticket_type_label.setFont(font_small)

        self.normal_tickets = QtWidgets.QCheckBox(self.tab1)
        self.normal_tickets.setChecked(True)
        self.normal_tickets.setGeometry(QtCore.QRect(480, 536, 12, 12))

        self.ticket_type_normal_label = QtWidgets.QLabel(self.tab1)
        self.ticket_type_normal_label.setGeometry(QtCore.QRect(500, 520, 80, 40))
        self.ticket_type_normal_label.setFont(font_small)

        self.discounted_tickets = QtWidgets.QCheckBox(self.tab1)
        self.discounted_tickets.setChecked(True)
        self.discounted_tickets.setGeometry(QtCore.QRect(480, 596, 12, 12))

        self.ticket_type_discounted_label = QtWidgets.QLabel(self.tab1)
        self.ticket_type_discounted_label.setGeometry(QtCore.QRect(500, 580, 60, 40))
        self.ticket_type_discounted_label.setFont(font_small)

        # === RELOAD BUTTON ===
        self.reload_button = QtWidgets.QPushButton(self.tab1)
        self.reload_button.setGeometry(QtCore.QRect(600, 580, 100, 30))
        self.reload_button.setFont(font_small)
        self.reload_button.clicked.connect(self.load_chart1)

        self.tabWidget.addTab(self.tab1, "")

        # tab2 - by films
        self.tab2 = QtWidgets.QWidget(self.tabWidget)
        self.tab2.setObjectName("tab2")

        # === CHART
        self.chart2 = QChart()
        self.chart2.setTitle("Ilość sprzedanych biletów według filmów")
        self.chart2.setTitleFont(font_medium)
        self.chart2.createDefaultAxes()

        self.chart2_view = QChartView(self.chart2)
        self.chart2_view.setRenderHint(QPainter.Antialiasing)

        self.chart2_widget = QtWidgets.QWidget(self.tab2)
        self.chart2_widget.setGeometry(QtCore.QRect(0, 0, 720, 450))

        self.vbox2 = QtWidgets.QVBoxLayout()
        self.vbox2.addWidget(self.chart2_view)
        self.chart2_widget.setLayout(self.vbox2)

        # Tworzenie osi x
        self.axisX2 = QDateTimeAxis()
        self.axisX2.setFormat("dd/MM/yyyy")  # Format daty dla osi x
        self.chart2.addAxis(self.axisX2, QtCore.Qt.AlignBottom)

        # Tworzenie osi y
        self.axisY2 = QValueAxis()
        self.axisY2.setLabelFormat("%.0f")
        self.chart2.addAxis(self.axisY2, QtCore.Qt.AlignLeft)

        self.chart2.legend().setVisible(True)

        # === CATEGORIES BOX
        self.categories_label2 = QtWidgets.QLabel(self.tab2)
        self.categories_label2.setGeometry(QtCore.QRect(20, 460, 180, 40))
        self.categories_label2.setFont(font_small)

        self.list_widget2 = QtWidgets.QListWidget(self.tab2)
        self.list_widget2.setSelectionMode(QtWidgets.QListWidget.MultiSelection)
        self.list_widget2.setGeometry(QtCore.QRect(20, 500, 190, 140))
        for title in get_list_of_films():
            self.list_widget2.addItem(title)
        for i in range(self.list_widget2.count()):
            if random.random() < 0.2:
                self.list_widget2.item(i).setSelected(True)
        self.list_widget2.setFont(font_small)

        # === DATES ===
        self.date_range_label_2 = QtWidgets.QLabel(self.tab2)
        self.date_range_label_2.setGeometry(QtCore.QRect(230, 460, 100, 40))
        self.date_range_label_2.setFont(font_small)

        self.date_edit_start2 = QtWidgets.QDateEdit(self.tab2)
        self.date_edit_start2.setGeometry(QtCore.QRect(320, 460, 140, 40))
        self.date_edit_start2.setObjectName("date_edit_start")
        self.date_edit_start2.setFont(font_small)
        self.date_start2 = QtCore.QDate(2025, 5, 1)
        self.date_edit_start2.setDate(self.date_start2)

        self.date_range_label_22 = QtWidgets.QLabel(self.tab2)
        self.date_range_label_22.setGeometry(QtCore.QRect(230, 560, 30, 40))
        self.date_range_label_22.setFont(font_small)

        self.date_edit_end2 = QtWidgets.QDateEdit(self.tab2)
        self.date_edit_end2.setGeometry(QtCore.QRect(320, 560, 140, 40))
        self.date_edit_end2.setObjectName("date_edit_end")
        self.date_edit_end2.setFont(font_small)
        self.date_end2 = QtCore.QDate(2025, 5, 31)
        self.date_edit_end2.setDate(self.date_end2)

        # === DICOUNTED / NORMAL ===
        self.ticket_type_label2 = QtWidgets.QLabel(self.tab2)
        self.ticket_type_label2.setGeometry(QtCore.QRect(480, 460, 100, 40))
        self.ticket_type_label2.setFont(font_small)

        self.normal_tickets2 = QtWidgets.QCheckBox(self.tab2)
        self.normal_tickets2.setChecked(True)
        self.normal_tickets2.setGeometry(QtCore.QRect(480, 536, 12, 12))

        self.ticket_type_normal_label2 = QtWidgets.QLabel(self.tab2)
        self.ticket_type_normal_label2.setGeometry(QtCore.QRect(500, 520, 80, 40))
        self.ticket_type_normal_label2.setFont(font_small)

        self.discounted_tickets2 = QtWidgets.QCheckBox(self.tab2)
        self.discounted_tickets2.setChecked(True)
        self.discounted_tickets2.setGeometry(QtCore.QRect(480, 596, 12, 12))

        self.ticket_type_discounted_label2 = QtWidgets.QLabel(self.tab2)
        self.ticket_type_discounted_label2.setGeometry(QtCore.QRect(500, 580, 60, 40))
        self.ticket_type_discounted_label2.setFont(font_small)

        # === RELOAD BUTTON ===
        self.reload_button2 = QtWidgets.QPushButton(self.tab2)
        self.reload_button2.setGeometry(QtCore.QRect(600, 580, 100, 30))
        self.reload_button2.setFont(font_small)
        self.reload_button2.clicked.connect(self.load_chart2)

        self.tabWidget.addTab(self.tab2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.load_chart1()
        self.load_chart2()
        date = datetime.date(2020, 10, 12)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "Tab 2"))
        self.date_range_label.setText(_translate("data_analysis_window", "Zakres dat od: "))
        self.date_range_label2.setText(_translate("data_analysis_window", "do: "))
        self.categories_label.setText(_translate("data_analysis_window", "Wybierz kategorie: "))
        self.ticket_type_label.setText(_translate("data_analysis_window", "Rodzaj biletu: "))
        self.ticket_type_normal_label.setText(_translate("data_analysis_window", "Normalny "))
        self.ticket_type_discounted_label.setText(_translate("data_analysis_window", "Ulgowy "))
        self.reload_button.setText(_translate("data_analysis_window", "Zastosuj filtry "))
        self.date_range_label_2.setText(_translate("data_analysis_window", "Zakres dat od: "))
        self.date_range_label_22.setText(_translate("data_analysis_window", "do: "))
        self.categories_label2.setText(_translate("data_analysis_window", "Wybierz filmy: "))
        self.ticket_type_label2.setText(_translate("data_analysis_window", "Rodzaj biletu: "))
        self.ticket_type_normal_label2.setText(_translate("data_analysis_window", "Normalny "))
        self.ticket_type_discounted_label2.setText(_translate("data_analysis_window", "Ulgowy "))
        self.reload_button2.setText(_translate("data_analysis_window", "Zastosuj filtry "))

    def upload_data(self):
        self.orders_raw = get_raw_list_of_orders()
        self.films_raw = get_raw_list_of_films()

    def load_chart1(self):
        date_start = self.date_edit_start.date().toPyDate()
        date_end = self.date_edit_end.date().toPyDate()
        categories_filters = [Category[cat.text()].value for cat in self.list_widget.selectedItems()]
        rt = create_relational_table_with_filters(self.films_raw, self.orders_raw, date_start, date_end,
                                                  categories_filter=categories_filters)
        data = group_by_category_and_date(rt, date_start, date_end)
        normal = self.normal_tickets.isChecked()
        discounted = self.discounted_tickets.isChecked()
        data2 = count_tickets(data, normal, discounted)
        for seria in self.chart.series():
            self.chart.removeSeries(seria)
        self.series1 = []

        minimum = float('inf')
        maximum = -float('inf')
        for category in data2:
            series = QLineSeries()
            for date in data2[category]:
                series.append(pydate_to_qdate(date).toMSecsSinceEpoch(), data2[category][date])
                minimum = min(minimum, data2[category][date])
                maximum = max(maximum, data2[category][date])
            self.chart.addSeries(series)
            series.setName(Category(category).name)
            for axis in self.chart.axes():
                series.attachAxis(axis)

        self.axisX.setRange(pydate_to_qdate(date_start), pydate_to_qdate(date_end))
        self.axisY.setRange(minimum, maximum + 1)
        self.chart.update()

    def load_chart2(self):
        date_start = self.date_edit_start2.date().toPyDate()
        date_end = self.date_edit_end2.date().toPyDate()
        film_filter = [film.text() for film in self.list_widget2.selectedItems()]
        rt = create_relational_table_with_filters(self.films_raw, self.orders_raw, date_start, date_end,
                                                  films_filter=film_filter)
        data = group_by_film_and_date(rt, date_start, date_end)
        normal = self.normal_tickets2.isChecked()
        discounted = self.discounted_tickets2.isChecked()
        data2 = count_tickets(data, normal, discounted)
        for seria in self.chart2.series():
            self.chart2.removeSeries(seria)
        self.series2 = []

        minimum = float('inf')
        maximum = -float('inf')
        for title in data2:
            self.series2.append(QLineSeries())
            for date in data2[title]:
                self.series2[-1].append(pydate_to_qdate(date).toMSecsSinceEpoch(), data2[title][date])
                minimum = min(minimum, data2[title][date])
                maximum = max(maximum, data2[title][date])
            for axis in self.chart2.axes():
                self.series2[-1].attachAxis(axis)
            self.series2[-1].setName(title)
            self.chart2.addSeries(self.series2[-1])

        self.axisX2.setRange(pydate_to_qdate(date_start), pydate_to_qdate(date_end))
        self.axisY2.setRange(minimum, maximum + 1)
        self.chart2.update()
