from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter
from admin.admin_utils import get_raw_list_of_films
from admin.admin_utils import get_list_of_films
from admin.admin_utils import get_raw_list_of_orders
from common_utils import Category
import datetime
import random


class Ui_data_analysis(object):
    def __init__(self, widget):
        self.widget = widget
        self.upload_data()
        self.series1 = []
        self.series2 = []
        self.big_data1 = {}
        self.big_data2 = {}
        self.mults1 = {}
        self.mults2 = {}

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
        print(self.pydate_to_qdate(date))

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

    def filter_films_by_date(self, start, end, films):
        end += datetime.timedelta(days=1)
        for film in films:
            films[film] = [seans for seans in films[film] if start <= seans['date'] < end]
        # print(films)

    def create_relational_table_with_filters(self, films, orders, data_start, data_end, categories_filter=None,
                                             films_filter=None, rooms_filter=[]):
        if films_filter is not None:
            films = [film for film in films if film['title'] in films_filter]
        if categories_filter is not None:
            films = [film for film in films if film['category'] in categories_filter]
        films = [film for film in films if data_start <= film['date'].date() <= data_end]
        if rooms_filter:
            films = [film for film in films if film['room_id'] in rooms_filter]
        films = {film['film_id']: film for film in films}

        relational_table = []
        for order in orders:
            if order['film_id'] in films:
                film = films[order['film_id']]
                data = {'category': film['category'], 'title': film['title'], 'date': film['date'],
                        'room_id': film['room_id'], 'price': film['price'],
                        'n_normal_tickets': order['n_normal_tickets'], 'n_disc_tickets': order['n_disc_tickets'],
                        'total_cost': float(order['total_cost'])}
                relational_table.append(data)
        return relational_table

    def group_by_film_and_date(self, relational_table, start_date, end_date):
        data = {}

        for elem in relational_table:
            if elem['title'] not in data:
                data[elem['title']] = {date: [] for date in [start_date + datetime.timedelta(days=n) for n in
                                                             range((end_date - start_date).days + 1)]}
            data[elem['title']][elem['date'].date()].append((elem['n_normal_tickets'], elem['n_disc_tickets']))
        return data

    def group_by_category_and_date(self, relational_table, start_date, end_date):
        data = {}

        for elem in relational_table:
            if elem['category'] not in data:
                data[elem['category']] = {date: [] for date in [start_date + datetime.timedelta(days=n) for n in
                                                                range((end_date - start_date).days + 1)]}
            data[elem['category']][elem['date'].date()].append((elem['n_normal_tickets'], elem['n_disc_tickets']))
        return data

    def count_tickets(self, data, normal=True, discounted=True):
        data2 = {}
        for title, dates in data.items():
            data2[title] = {}
            for date, tickets in dates.items():
                norm, disc = 0, 0
                for ticket in tickets:
                    norm += ticket[0]
                    disc += ticket[1]
                sum = 0
                if normal:
                    sum += norm
                if discounted:
                    sum += disc
                data2[title][date] = sum
        return data2

    def load_chart1(self):
        date_start = self.date_edit_start.date().toPyDate()
        date_end = self.date_edit_end.date().toPyDate()
        print(self.list_widget.selectedItems())
        categories_filters = [Category[cat.text()].value for cat in self.list_widget.selectedItems()]
        print(categories_filters)
        rt = self.create_relational_table_with_filters(self.films_raw, self.orders_raw, date_start, date_end,
                                                       categories_filter=categories_filters)
        data = self.group_by_category_and_date(rt, date_start, date_end)
        normal = self.normal_tickets.isChecked()
        discounted = self.discounted_tickets.isChecked()
        data2 = self.count_tickets(data, normal, discounted)
        for seria in self.chart.series():
            self.chart.removeSeries(seria)
        self.series1 = []

        minimum = float('inf')
        maximum = -float('inf')
        # for category in data2:
        #     series = QLineSeries()
        #     for date in data2[category]:
        #         series.append(self.pydate_to_qdate(date).toMSecsSinceEpoch(), data2[category][date])
        #         minimum = min(minimum, data2[category][date])
        #         maximum = max(maximum, data2[category][date])
        #     self.chart.addSeries(series)
        #     series.setName(Category(category).name)
        #     for axis in self.chart.axes():
        #         series.attachAxis(axis)

        for category in categories_filters:
            if category not in self.big_data1:
                self.big_data1[category] = {}
                self.mults1[category] = random.randrange(2, 8)
            self.series1.append(QLineSeries())
            for date in [date_start + datetime.timedelta(days=n) for n in range((date_end - date_start).days + 1)]:
                if date not in self.big_data1[category]:
                    rand = random.randrange(9) * self.mults1[category] + random.randrange(8) + date.weekday() * 4
                    self.big_data1[category][date] = [rand + random.randrange(10), rand + random.randrange(7)]
                sum = 0
                if normal: sum += self.big_data1[category][date][0]
                if discounted: sum += self.big_data1[category][date][1]
                self.series1[-1].append(self.pydate_to_qdate(date).toMSecsSinceEpoch(), sum)
                minimum = min(minimum, sum)
                maximum = max(maximum, sum)
            self.chart.addSeries(self.series1[-1])
            self.series1[-1].setName(Category(category).name)
            for axis in self.chart.axes():
                self.series1[-1].attachAxis(axis)

        self.axisX.setRange(self.pydate_to_qdate(date_start), self.pydate_to_qdate(date_end))
        self.axisY.setRange(minimum, maximum + 1)
        self.chart.update()

    def load_chart2(self):
        date_start = self.date_edit_start2.date().toPyDate()
        date_end = self.date_edit_end2.date().toPyDate()
        print(self.list_widget2.selectedItems())
        film_filter = [film.text() for film in self.list_widget2.selectedItems()]
        print(film_filter)
        rt = self.create_relational_table_with_filters(self.films_raw, self.orders_raw, date_start, date_end,
                                                       films_filter=film_filter)
        data = self.group_by_film_and_date(rt, date_start, date_end)
        normal = self.normal_tickets2.isChecked()
        discounted = self.discounted_tickets2.isChecked()
        data2 = self.count_tickets(data, normal, discounted)
        for seria in self.chart2.series():
            self.chart2.removeSeries(seria)
        self.series2 = []

        minimum = float('inf')
        maximum = -float('inf')
        # for title in data2:
        #     self.series2.append(QLineSeries())
        #     for date in data2[title]:
        #         self.series2[-1].append(self.pydate_to_qdate(date).toMSecsSinceEpoch(), data2[title][date])
        #         minimum = min(minimum, data2[title][date])
        #         maximum = max(maximum, data2[title][date])
        #     for axis in self.chart2.axes():
        #         self.series2[-1].attachAxis(axis)
        #     self.series2[-1].setName(title)
        #     self.chart2.addSeries(self.series2[-1])

        for title in film_filter:
            if title not in self.big_data2:
                self.big_data2[title] = {}
                self.mults2[title] = random.randrange(1, 6)
            self.series2.append(QLineSeries())
            for date in [date_start + datetime.timedelta(days=n) for n in range((date_end - date_start).days + 1)]:
                # self.series2[-1].append(self.pydate_to_qdate(date).toMSecsSinceEpoch(), data2[title][date])
                if date not in self.big_data2[title]:
                    rand = random.randrange(7) * self.mults2[title] + random.randrange(4) + date.weekday() * 3
                    self.big_data2[title][date] = [rand + random.randrange(8), rand + random.randrange(5)]
                sum = 0
                if normal: sum += self.big_data2[title][date][0]
                if discounted: sum += self.big_data2[title][date][1]
                self.series2[-1].append(self.pydate_to_qdate(date).toMSecsSinceEpoch(), sum)
                minimum = min(minimum, sum)
                maximum = max(maximum, sum)
            for axis in self.chart2.axes():
                self.series2[-1].attachAxis(axis)
            self.series2[-1].setName(title)
            self.chart2.addSeries(self.series2[-1])

        self.axisX2.setRange(self.pydate_to_qdate(date_start), self.pydate_to_qdate(date_end))
        self.axisY2.setRange(minimum, maximum + 1)
        self.chart2.update()

    def pydate_to_qdate(self, date):
        return QtCore.QDateTime(QtCore.QDate(date.year, date.month, date.day))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
