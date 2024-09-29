import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sqlite3
import pandas as pd
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Ciudadanopre(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ciudadano.ui', self)
        self.grafica.clicked.connect(self.codigo)
        self.pronosticar.clicked.connect(self.tipo)
        self.cambiar.clicked.connect(self.cantidad)
        self.df = None
        self.predicted_price = None # Variable de instancia para almacenar el DataFrame
        self.conn = sqlite3.connect('datos_residuos.db')
        self.c = self.conn.cursor()
        self.populate_table()

    def agregar_elemento(self):
        codigo = self.cod_bus.text()
        tipo = self.nombre.text()
        cantidad = self.cant.text()

        print("Codigo:", codigo)
        print("Tipo:", tipo)
        print("Cantidad:", cantidad)
        self.c.execute("INSERT INTO administrador (codigo,tipo,cantidad) values (?, ?, ?)", (codigo, tipo, cantidad))
        self.conn.commit()

        self.cod_bus.clear()
        self.tipo.clear()
        self.cant.clear()

        self.populate_table()

    def populate_table(self):
        self.tabla_int1.setRowCount(0)
        self.c.execute("SELECT * FROM administrador")
        rows = self.c.fetchall()
        for row_number, row_data in enumerate(rows):
            self.tabla_int1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Deshabilitar la edición de celdas
                self.tabla_int1.setItem(row_number, column_number, item)

        self.tabla_int1.cellClicked.connect(self.seleccionar_elemento)  # Conexión de señal y ranura





