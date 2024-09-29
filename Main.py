
from time import strftime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys
from Administrador import Administradorpre
from Ciudadano import Ciudadanopre
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

timer = QTimer()
def hora():
    return dt.now().strftime('%H:%M:%S')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Inicio.ui', self)
        self.setWindowTitle('Sistema ECO-CLAS: Clasificación Eficiente de Residuos Sólidos')
        self.setWindowIcon(QIcon('Municipalidad.png'))
        self.Fecha.setText(strftime('%d/%m/%Y'))
        self.Hora.setText(self.actualizar_tiempo())
        self.administrador = Administradorpre()
        self.ciudadano1 = Ciudadanopre()
        self.Inventario.clicked.connect(self.administrador.show)
        self.pronostico.clicked.connect(self.ciudadano1.show)

    def actualizar_tiempo(self):
        timer.start(1000)
        timer.timeout.connect(self.set_tiempo)

    def set_tiempo(self):
        self.Hora.setText(hora())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())