from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
 
 
# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        #  метод супер класса
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))             # Устанавливаем размеры
        self.setWindowTitle("Работа с QTableWidget")    # Устанавливаем заголовок окна
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет
 
        grid_layout = QGridLayout()             # Создаём QGridLayout
        central_widget.setLayout(grid_layout)   # Устанавливаем данное размещение в центральный виджет
 
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(3)     # Устанавливаем три колонки
        table.setRowCount(1)        # и одну строку в таблице
 
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Имя", "Инициатива", "Полученый урон"])
 
        # Устанавливаем всплывающие подсказки на заголовки
        table.horizontalHeaderItem(0).setToolTip("Имя")
        table.horizontalHeaderItem(1).setToolTip("Инициатива")
        table.horizontalHeaderItem(2).setToolTip("Полученый урон")
 
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
 
        # заполняем первую строку
        table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
 
        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
 
        grid_layout.addWidget(table, 0, 0)   # Добавляем таблицу в сетку

    def add_item ():
        table.setItem(1, 0, QTableWidgetItem("Text in column 1"))
        table.setItem(1, 1, QTableWidgetItem("Text in column 2"))
        table.setItem(1, 2, QTableWidgetItem("Text in column 3"))

if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()

    sys.exit(app.exec())
    