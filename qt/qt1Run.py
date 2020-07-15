#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sqlalchemy
import pandas as pd
import os.path
from qt1 import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import random
import sqlA
import io


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
 
class mywindow(QtWidgets.QMainWindow):

    def rand_result(self,kubs, maxR, i):
        res = 0
        while (kubs > 0):
            res += random.randint(1, maxR)
            kubs -= 1
        return res*i



    def atack_vall(self,text, label, label_2):
        try:
            i = 1
            k = 0
            if (text.find("|") > -1):
                k = text.find("|")
            else:
                k = 0
            if (k > 0):
                chanse_bonuse = int(text[0:k])
            else:
                chanse_bonuse = 0
            print(chanse_bonuse)
            res = 0
            chanse_res = random.randint(1,20)
            if (chanse_res == 1):
                label_2.setText('Неудача!')
            elif(chanse_res == 20):
                label_2.setText('Удача!')
                i = 2
            else :
                label_2.setText(str(chanse_res + chanse_bonuse))
            #print (chanse_res)
            if (k !=0): k +=2
            text = text [k:len(text)]
            print(text)
            list_atacks = text.split(', ')
            for at in list_atacks:
                kubs_num = at[0]
                plus_i = at.find("+")
                if (plus_i == -1):
                    kubs_w = str(at[2:len(at)])
                else:
                    kubs_w = at[2:plus_i:1]
                if (at.find('+') > -1):
                    bonus = at[len(at)-1]
                else :
                    bonus = str(0)
                if (kubs_num.isdigit() and kubs_w.isdigit() and bonus.isdigit()):
                    res += self.rand_result(int(kubs_num), int(kubs_w), i)
            label.setText(str(res + int(bonus)))
            print(' Урон ' + str(res))
        except:
            print("error")


    def read_enemies(self, table):
        res = sqlA.get_all_chars()
        for row in res:
            table.insertRow(0)
            for i in range(0, 4):
                table.setItem(0 , i,  QtWidgets.QTableWidgetItem(str (row[i+1])))
                
                """attaks = sqlA.get_char_atacks(row[0])
            combo = QtWidgets.QComboBox()
            for line in attaks:
                combo.addItem(str(line[3]) +'| ' + line[2])
                table.setCellWidget(0, 4, combo)"""
    
    def read_file(self):
        table = self.ui.tableWidget
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\')
        with io.open(fname[0], encoding='utf-8') as file:
            data = file.readline()
            while (data):
                print(data)
                table.insertRow(0)
                cells = data.split(";")                
                for i in range(0, len(cells)):
                    table.setItem(0 , i,  QtWidgets.QTableWidgetItem(str (cells[i])))
                data = file.readline()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start_table(self.ui.tableWidget, self.ui.pushButton_5)
        add_b = self.ui.pushButton_2
        add_b.setText("Добавить")
        add_b.clicked.connect(self.add_row)
        table = self.ui.tableWidget
        self.read_enemies(table)
        dell_b = self.ui.pushButton_3
        dell_b.clicked.connect(self.del_row)
        dell_b.setText("Удалить")

        strike_b = self.ui.pushButton
        strike_b.setText("Удар!")
        strike_b.clicked.connect(self.show_atack)

        add_file = self.ui.pushButton_4
        add_file.setText("Взять из файла")
        add_file.clicked.connect(self.read_file)

    def start_table(self, table, pushButton):
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["Имя", "Инициатива", "Ударили на", "Текущее ХП", "Урон атакой", "KD", "Описание"])
        table.setSortingEnabled(True)
        table.sortByColumn(1,1)
        def sum_hp(self):  
            try:
                row = table.currentRow()
                cell = table.item(row, 2)
                if (cell.text() != ""):
                    next_cell = table.item(row, 3)
                    val_1 = next_cell.text()
                    val_2 = cell.text()
                    if ((is_number(val_1)) & is_number(val_2)):
                        val_1 = int(val_1)
                        val_2 = int(val_2)                    
                        next_cell.setText(str(val_1 - val_2))
                cell.setText("")
            except:
                print("choose line")
        pushButton.clicked.connect(sum_hp)

    
    def add_row(self):
        table = self.ui.tableWidget
        i = table.rowCount() + 1
        table.setRowCount(i)
        """ combo = QtWidgets.QComboBox()
        combo.addItem("1d6+8")
        combo.addItem("2d6+10")
        table.setCellWidget(i-1, 4, combo)"""


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
        label_2 = self.ui.label_2
        if (str(type (cell)) == '<class \'NoneType\'>'):
            cell = table.cellWidget(row, 4)
            if (str(type (cell)) == '<class \'PyQt5.QtWidgets.QComboBox\'>'):
                self.atack_vall(cell.currentText(), label, label_2)
            else :
                label.setText('херн')
                
        elif (str(type (cell)) == '<class \'PyQt5.QtWidgets.QTableWidgetItem\'>'):
            #if (len(cell.text()) != 0): 
            self.atack_vall(cell.text(), label, label_2)
    



        
app = QtWidgets.QApplication([])
application = mywindow()
application.show() 
sys.exit(app.exec())

