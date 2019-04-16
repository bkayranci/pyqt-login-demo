from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys


class MyDialog(QDialog):
    logined = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        uic.loadUi('Dialog.ui', self)
        self.btnLogin.clicked.connect(self.on_login)

    def on_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        if username == 'admin' and password == '123':
            self.logined.emit(True)
        else:
            self.logined.emit(False)
        self.close()


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.btnSec.clicked.connect(self.on_click)
        self.__giris_yapildi = False
        while(self.__giris_yapildi is False):
            d = MyDialog()
            d.logined.connect(self.on_logined)
            d.exec()

    def on_logined(self, status):
        self.__giris_yapildi = status
        

    def on_click(self):
        fd = QFileDialog()
        path = fd.getExistingDirectory()
        self.listview_doldur(path)

    def listview_doldur(self, path):
        import os
        files = os.listdir(path)
        model = self.get_model(files)
        self.lvDosya.setModel(model)
        
    def get_model(self, dosyalar):
        temp = QStandardItemModel()

        for dosya in dosyalar:
            item = QStandardItem(str(dosya))
            temp.appendRow(item)

        return temp

app = QApplication(sys.argv)
mw = MyMainWindow()
mw.show()
sys.exit(app.exec_())
