import PyQt5.QtWidgets as qtw


class MainWindows(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cinema")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Select film")
        self.layout().addWidget(my_label)

        # create buttion
        my_button = qtw.QPushButton("1")
        self.layout().addWidget(my_button)

        self.show()

if __name__ == '__main__':
    app = qtw.QApplication([])
    main_win = MainWindows()
    app.exec_()
