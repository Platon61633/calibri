import sys

import psycopg2
 
conn = psycopg2.connect(dbname="testDB", user="postgres", password="password", host="192.168.1.107", port="5432")
conn.autocommit = True
cursor = conn.cursor()

# from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt6.QtGui import QIcon, QAction

from style_ui import Ui_MainWindowL

from Registration.useRegistration import Reg

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        self.ui = Ui_MainWindowL()
        self.ui.setupUi(self)

        self.username_label = self.ui.label
        self.password_label = self.ui.label_2
        self.reg_button = self.ui.pushButton_2

        self.reg_button.clicked.connect(self.to_reg)

        self.username_label.setText("")
        self.password_label.setText("")
        # self.button_reg_label.setText("")

        self.username_input = self.ui.lineEdit
        self.password_input = self.ui.lineEdit_2

        self.login = self.ui.pushButton

        self.login.clicked.connect(self.do_login)

        self.username_input.setPlaceholderText("Логин")
        self.password_input.setPlaceholderText("Пароль")

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.username_input.setClearButtonEnabled(True)
        self.password_input.setClearButtonEnabled(True)

        icon = QIcon('static/cross.svg')
        self.username_input.findChildren(QAction)[0].setIcon(icon)
        self.password_input.findChildren(QAction)[0].setIcon(icon)


        self.username_input.textChanged.connect(self.do_username_label)
        self.password_input.textChanged.connect(self.do_password_label)

    def do_login(self):
        # print(self.username_input.text(), self.password_input.text())
        # q=cursor.execute("SELECT * FROM users WHERE login="+self.username_input.text())
        # print(q.fetchone())
        print(cursor.execute("SELECT * FROM users;").fetchone(), 3)
        

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
    def to_reg(self):
        for i in range(self.ui.gridLayout_2.count()): 
            while self.ui.gridLayout_2.count():
                child = self.ui.gridLayout_2.takeAt(0)
                if child.widget():
                  child.widget().deleteLater()
        self.ui.gridLayout_2.addWidget(Reg())

            


app = QApplication(sys.argv)

window = Login()
window.show()

app.exec()