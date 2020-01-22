#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import pandas as pd
import os.path
from qt1 import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import random
 
 
class mywindow(QtWidgets.QMainWindow):
    def rand_result(self, kubs, max):
        res = 0
        while (kubs > 0):
            res += random.randint(1, max)
            print("res")
            print(res)
            kubs -= 1    
    
    def read_as(self, table):
        os.chdir('D:\GitHub\MorozovAP\qt')
        with open('./data.txt', 'r', encoding='utf-8') as f:
            csv_data = pd.read_csv(f, sep=';')
            for j in range(0, csv_data['name'].count()):
                table.insertRow(0)
                for i in range(0, 5):
                    table.setItem(0 , i,  QtWidgets.QTableWidgetItem(str (csv_data.loc[j][i])))


    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start_table(self.ui.tableWidget)
        add_b = self.ui.pushButton_2
        add_b.setText("Добавить")
        add_b.clicked.connect(self.add_row)
        table = self.ui.tableWidget
        self.read_as(table)
        dell_b = self.ui.pushButton_3
        dell_b.clicked.connect(self.del_row)
        dell_b.setText("Удалить")

        strike_b = self.ui.pushButton
        strike_b.setText("Рукопашный удар")
        strike_b.clicked.connect(self.show_atack)

    def start_table(self, table):
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Имя", "Инициатива", "Полученый урон", "Макс ХП", "Урон атакой"])
        table.setSortingEnabled(True)
        table.sortByColumn(1,1)

    def add_row(self):
        table = self.ui.tableWidget
        i = table.rowCount() + 1
        table.setRowCount(i)


    def del_row(self):
        table = self.ui.tableWidget
        i = self.ui.tableWidget.currentRow()
        if(i >= 0):
            table.removeRow(i)     

    def show_atack(self):
        table = self.ui.tableWidget
        row = table.currentRow()
        cell = table.item(row, 4)   
        label = self.ui.label
        #cel_text = cell.text()
        def rand_result(kubs, maxR):
            res = 0
            while (kubs > 0):
                res += random.randint(1, maxR)
                kubs -= 1
            return res    
        if (cell != None):
            kubs_num = cell.text()[0]
            plus_i = cell.text().find("+")
            kubs_w = cell.text()[2:plus_i:1]
            bonus = cell.text()[len(cell.text())-1]
            if (kubs_num.isdigit() and kubs_w.isdigit() and bonus.isdigit()):
                res = rand_result(int(kubs_num), int(kubs_w))
                label.setText(str(res + int(bonus)))
            #print(kubs_num)
            #print(kubs_w)
            #print(bonus)

        
app = QtWidgets.QApplication([])
application = mywindow()
application.show() 
sys.exit(app.exec())