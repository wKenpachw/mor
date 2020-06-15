from PyQt5 import QtWidgets
import sqlalchemy
import pandas as pd
import os.path
from ui1 import Ui_Dialog  # импорт нашего сгенерированного файла
import sys
import random
import sqlObr
import io
import raschet
import add
import add2


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.start_table(self.ui.tableWidget)
        self.start_table(self.ui.tableWidget_2)
        self.set_combobox(self.ui.comboBox)
        self.set_combobox(self.ui.comboBox_2)
        self.ui.pushButton.clicked.connect(self.add_collum)
        self.ui.pushButton_6.clicked.connect(self.add_collum_2)
        #self.ui.pushButton_2.clicked.connect(self.new_obr_bd)
        self.ui.pushButton_3.clicked.connect(self.get_column_info)
        self.ui.pushButton_4.clicked.connect(self.add_empty_coll)
        self.ui.pushButton_5.clicked.connect(self.dell_column)
        self.ui.pushButton_8.clicked.connect(self.add_empty_coll_2)
        self.ui.pushButton_9.clicked.connect(self.dell_column_2)
        
    def start_table(self, table):
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Наименование", "Значение", "Год"])
        """table.setRowCount(9)
        table.setVerticalHeaderLabels(["Наименование","Часовая производительность", "Материал на 1 шт", "Основная заработная плата", "Расход воды, сжатого воздуха", 
        "Расход технологической электр. энергии", "Расход по содержанию оборудования и износ инструмента", "Годовые расходы по наладке оборудования", "Содержание и износ оснастки за год"])
        """
    def set_combobox(self, combobox):
        search = sqlObr.get_Names()
        combobox.addItem("new")
        for row in search:
            combobox.addItem(row[0])

    def add_collum(self):
        table = self.ui.tableWidget
        combo = self.ui.comboBox
        #print(combo.currentText())
        name = combo.currentText()
        if (name == "new"):
            window3.show()
        else:
            obr = sqlObr.get_obr(name)
            for r in obr:
                self.ui.lineEdit.setText(str(r[0]))
                self.ui.lineEdit_2.setText(str(r[1]))
            res = sqlObr.get_year(combo.currentText())
            for row in res:
                table.insertRow(0)
                for i in range(0, 2):
                    table.setItem(0,i, QtWidgets.QTableWidgetItem(str (row[i])))
                table.setItem(0,2, QtWidgets.QTableWidgetItem(str ("+")))
            res = sqlObr.get_izd(combo.currentText())
            for row in res:
                table.insertRow(0)
                for i in range(0, 2):
                    table.setItem(0,i, QtWidgets.QTableWidgetItem(str (row[i])))
                table.setItem(0,2, QtWidgets.QTableWidgetItem(str ("-")))

    def add_collum_2(self):
        table = self.ui.tableWidget_2
        combo = self.ui.comboBox_2
        name = combo.currentText()
        if (name == "new"):
            window3.show()
        else:
            obr = sqlObr.get_obr(name)
            for r in obr:
                self.ui.lineEdit_3.setText(str(r[0]))
                self.ui.lineEdit_4.setText(str(r[1]))
            res = sqlObr.get_year(combo.currentText())
            for row in res:
                table.insertRow(0)
                for i in range(0, 2):
                    table.setItem(0,i, QtWidgets.QTableWidgetItem(str (row[i])))
                table.setItem(0,2, QtWidgets.QTableWidgetItem(str ("+")))
            res = sqlObr.get_izd(combo.currentText())
            for row in res:
                table.insertRow(0)
                for i in range(0, 2):
                    table.setItem(0,i, QtWidgets.QTableWidgetItem(str (row[i])))
                table.setItem(0,2, QtWidgets.QTableWidgetItem(str ("-")))

    def add_empty_coll(self):
        name = self.ui.comboBox.currentText()
        window2.set_name(name)
        window2.show()  # Показываем окно
        
    def dell_column(self):
        table = self.ui.tableWidget
        print(table.currentColumn())
        table.removeRow(table.currentRow())
    
    def add_empty_coll_2(self):
        #app2 = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
       # window2 = add.mywindow2()  # Создаём объект класса ExampleApp
        window2.set_name(self.ui.comboBox_2.currentText())
        window2.show()  # Показываем окно
        #app2.exec_()  # и запускаем приложение
        
        
    def dell_column_2(self):
        table = self.ui.tableWidget_2
        print(table.currentColumn())
        table.removeRow(table.currentRow())

    def get_column_info(self):
        table1 = self.ui.tableWidget
        table2 = self.ui.tableWidget_2
        textEdit = self.ui.textEdit
        izdH = self.ui.lineEdit.text()
        matIzd = self.ui.lineEdit_2.text()
        izdH2 = self.ui.lineEdit_3.text()
        matIzd2 = self.ui.lineEdit_4.text()
        c1 = 0.0
        v1 = 0.0
        c2 = 0.0
        v2 = 0.0

        try:
            for i in range (0 ,table1.rowCount()):
                if(table1.item(i,2).text() == '+'):
                    c1 += float(table1.item(i,1).text())
                else:
                    v1 += float(table1.item(i,1).text())
            for i in range (0 ,table2.rowCount()):
                if(table2.item(i,2).text() == '+'):
                    c2 += float(table2.item(i,1).text())
                else:
                    v2 += float(table2.item(i,1).text())
            v1 = v1/float(izdH) + float(matIzd)
            v2 = v2/float(izdH2) + float(matIzd2)
            n = raschet.nkp12(c1, v1, c2, v2)
            s1 = raschet.sTeh(c1, v1, n)
            s2 = raschet.sTeh(c2, v2, n)
            end = raschet.end_result(s1, s2, n)
            textEdit.append("v1 = " + str(v1) + " , c1 = " + str(c1))
            textEdit.append("v2 = " + str(v2) + " , c1 = " + str(c2))
            textEdit.append("N = " + str(n))
            textEdit.append("s1 = " + str(s1) + ", s2 = " + str (s2))
            textEdit.append(end)
        except:
            print("error")
        


app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = mywindow()  # Создаём объект класса ExampleApp
window2 = add.mywindow2()
window3 = add2.mywindow2()
window.show()  # Показываем окно
app.exec_()  # и запускаем приложение
