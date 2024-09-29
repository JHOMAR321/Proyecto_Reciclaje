import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sqlite3

class Administradorpre(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Administrador.ui', self)
        self.conn = sqlite3.connect('datos_residuos.db')
        self.c = self.conn.cursor()
        self.create_table()
        self.populate_table()
        self.bot_agregar.clicked.connect(self.agregar_elemento)
        self.modificar.clicked.connect(self.modificar_elemento)
        self.eliminar.clicked.connect(self.eliminar_elemento)

    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS inventario(codigo TEXT,tipo TEXT ,cantidad TEXT)")
        self.conn.commit()

    def populate_table(self):
        self.tabla_int.setRowCount(0)
        self.c.execute("SELECT * FROM administrador")
        rows = self.c.fetchall()
        for row_number, row_data in enumerate(rows):
            self.tabla_int.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Deshabilitar la edición de celdas
                self.tabla_int.setItem(row_number, column_number, item)

        self.tabla_int.cellClicked.connect(self.seleccionar_elemento)  # Conexión de señal y ranura

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

    def seleccionar_elemento(self, row, column):
        codigo = self.tabla_int.item(row, 0).text()
        tipo = self.tabla_int.item(row, 1).text()
        cantidad = self.tabla_int.item(row, 2).text()

        self.cod_bus.setText(codigo)
        self.tipo.setText(tipo)
        self.cant.setText(cantidad)

    def modificar_elemento(self):
        codigo_actual = self.cod_bus.text()
        tipo = self.nombre.text()
        cantidad = self.cant.text()

        self.c.execute("UPDATE administrador SET tipo = ?, cantidad = ? WHERE codigo = ?", (tipo, cantidad, codigo_actual))
        self.conn.commit()

        self.cod_bus.clear()
        self.tipo.clear()
        self.cant.clear()

        self.populate_table()

    def eliminar_elemento(self):
        codigo_actual = self.cod_bus.text()

        # Verificar si se seleccionó un elemento en la tabla
        if codigo_actual:
            # Mostrar un mensaje de confirmación antes de eliminar el elemento
            respuesta = QMessageBox.question(self, 'Confirmar Eliminación', '¿Estás seguro de eliminar este elemento?', QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                self.c.execute("DELETE FROM administrador WHERE codigo = ?", (codigo_actual,))
                self.conn.commit()

                self.cod_bus.clear()
                self.tipo.clear()
                self.cant.clear()

                self.populate_table()
        else:
            QMessageBox.warning(self, 'Elemento no seleccionado', 'No se ha seleccionado ningún elemento de la tabla.')
