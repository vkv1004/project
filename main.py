import sys
import os
import random

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPixmap, QFont
from PyQt5 import QtCore
import sqlite3


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        u = QGridLayout(self)

        self.label = QLabel(self)
        self.label.setText('Добавить:')
        self.label.setFont(QFont("Times", 16))
        self.label.setMaximumSize(140000, 140000)
        u.addWidget(self.label, 0, 0)
        
        self.btn = QPushButton('+', self)
        self.btn.clicked.connect(self.app)
        self.btn.setFont(QFont("Times", 16))
        self.btn.setStyleSheet(
            "background-color: {}".format('#00c8ff'))
        self.btn.setMaximumSize(140000, 140000)
        u.addWidget(self.btn, 0, 1)

        self.combo = QListWidget(self)
        self.combo.setFont(QFont("Times", 16))
        u.addWidget(self.combo, 1, 0, 1, 2)

        self.btn = QPushButton('Открыть', self)
        self.btn.clicked.connect(self.open)
        self.btn.setFont(QFont("Times", 16))
        self.btn.setStyleSheet(
            "background-color: {}".format('#00c8ff'))
        self.btn.setMaximumSize(140000, 140000)
        u.addWidget(self.btn, 2, 0, 1, 2)

        self.btn1 = QPushButton('Удалить', self)
        self.btn1.clicked.connect(self.dell)
        self.btn1.setFont(QFont("Times", 16))
        self.btn1.setStyleSheet(
            "background-color: {}".format('#00c8ff'))
        self.btn1.setMaximumSize(140000, 140000)
        u.addWidget(self.btn1, 3, 0, 1, 2)

        self.btn2 = QPushButton('Отправить', self)
        self.btn2.clicked.connect(self.otp)
        self.btn2.setFont(QFont("Times", 16))
        self.btn2.setStyleSheet(
            "background-color: {}".format('#00c8ff'))
        self.btn2.setMaximumSize(140000, 140000)
        u.addWidget(self.btn2, 4, 0, 1, 2)

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM files;")
        all_results = cur.fetchall()
        for i in all_results:
            s = i[0]
            # Нельзя добавлять файлы с пробелами
            #s007 = '.'.join((s.split('/')[-1]).split('.')[:-1]) + '.' + s.split('.')[-1]
            self.combo.addItems([s])
        
    def app(self):
        self.cwd = os.getcwd()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "Выбрать файл",  
                                    self.cwd, 
                                    "All Files (*);;Text Files (*.txt)")
        self.ftp = fileName_choose.split('.')[-1]
        self.f = fileName_choose
        self.nm = '.'.join((self.f.split('/')[-1]).split('.')[:-1])
        
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO files(fname) 
   VALUES('{self.f}');""")
        conn.commit()
        self.combo.addItems([self.f])
        #self.combo.addItems([self.nm + '.' + self.ftp])
        
    def open(self):
        a = self.combo.selectedItems()
        for i in a:
            self.name = i.text()
        os.system("start "+ self.name)

    def dell(self):
        a = self.combo.selectedItems()
        for i in a:
            self.name = i.text()
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM files WHERE fname='{self.name}';")
        conn.commit()
        for i in range(len(self.combo)):
            if self.combo.item(i).text() == self.name:
                c = i
                break
        self.combo.takeItem(c)

    def otp(self):
        print(0)
        #Я не знаю что писать
        
        

if __name__ == "__main__":
    app = Qt.QApplication([])
    t = Example()
    t.show()
    app.exec_()
