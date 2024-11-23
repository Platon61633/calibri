import sys

# from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt6.QtGui import QIcon, QAction

from Registration.style_ui import Ui_MainWindow

class Reg(QMainWindow):
    def __init__(self):
        super(Reg, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.name_label = self.ui.label_2
        self.surname_label = self.ui.label_3
        self.username_label = self.ui.label_4
        self.password_label = self.ui.label_5

        self.username_label.setText("")
        self.password_label.setText("")
        self.name_label.setText("")
        self.surname_label.setText("")

        self.name_input = self.ui.lineEdit
        self.surname_input = self.ui.lineEdit_2
        self.username_input = self.ui.lineEdit_3
        self.password_input = self.ui.lineEdit_4


        self.username_input.setPlaceholderText("Логин")
        self.password_input.setPlaceholderText("Пароль")
        self.name_input.setPlaceholderText("Имя")
        self.surname_input.setPlaceholderText("Фамилия")

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.username_input.setClearButtonEnabled(True)
        self.password_input.setClearButtonEnabled(True)
        self.name_input.setClearButtonEnabled(True)
        self.surname_input.setClearButtonEnabled(True)

        icon = QIcon('static/cross.svg')
        self.username_input.findChildren(QAction)[0].setIcon(icon)
        self.password_input.findChildren(QAction)[0].setIcon(icon)
        self.name_input.findChildren(QAction)[0].setIcon(icon)
        self.surname_input.findChildren(QAction)[0].setIcon(icon)


        self.username_input.textChanged.connect(self.do_username_label)
        self.password_input.textChanged.connect(self.do_password_label)
        self.name_input.textChanged.connect(self.do_name_label)
        self.surname_input.textChanged.connect(self.do_surname_label)

    def do_username_label(self, text):
        if text:
            self.username_label.setText("Логин")
        else:
            self.username_label.setText("")
    def do_password_label(self, text):
        if text:
            self.password_label.setText("Пароль")
        else:
            self.password_label.setText("")
    def do_name_label(self, text):
        if text:
            self.name_label.setText("Имя")
        else:
            self.name_label.setText("")
    def do_surname_label(self, text):
        if text:
            self.surname_label.setText("Фамилия")
        else:
            self.surname_label.setText("")
            


# app = QApplication(sys.argv)

# window = Reg()
# window.show()

# sys.exit(app.exec())