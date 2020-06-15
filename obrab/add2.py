from PyQt5 import QtWidgets
import sqlalchemy
import pandas as pd
import os.path
from ui3 import Ui_Dialog3  # импорт нашего сгенерированного файла
import sys
import random
import sqlObr
import io


class mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.set_name)


    def set_name(self):
        name = self.ui.lineEdit.text()
        hour = self.ui.lineEdit_2.text()
        cost = self.ui.lineEdit_3.text()
        if (name != ""):
            sqlObr.set_obr(name, hour, cost)

        



"""app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window2 = mywindow2()  # Создаём объект класса ExampleApp
window2.show()  # Показываем окно
app.exec_()  # и запускаем приложение"""