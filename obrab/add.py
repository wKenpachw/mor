from PyQt5 import QtWidgets
import sqlalchemy
import pandas as pd
import os.path
from ui2 import Ui_Dialog2  # импорт нашего сгенерированного файла
import sys
import random
import sqlObr
import io


class mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        self.ui.comboBox_2.addItem("Год")
        self.ui.comboBox_2.addItem("Изделие")
        self.ui.buttonBox.clicked.connect(self.add)

    def set_name(self, name):
        self.ui.label_3.setText(name)
    
    def add(self):
        name = self.ui.lineEdit.text()
        cost = self.ui.lineEdit_2.text()
        table = self.ui.comboBox_2.currentText()
        obrName = self.ui.label_3.text()
        if ((name != "") & (cost != "")):
            id = sqlObr.get_id(obrName)
            if (table == "Год"):
                print("year")
                sqlObr.set_year(name, cost, id)
            else :
                print("izd")
                sqlObr.set_izd(name, cost, id)



"""app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window2 = mywindow2()  # Создаём объект класса ExampleApp
window2.show()  # Показываем окно
app.exec_()  # и запускаем приложение"""