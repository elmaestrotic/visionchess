import sys
import time
import random
from datetime import datetime
from visionchess import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QFileDialog

DURATION_INT = 30
global letras
global celda
global correctas
global erradas
global pulsadas
global evaluadas
global casilla
casilla = ""
evaluadas = []
pulsadas = []
celda = ""
erradas = ""
correctas = ""

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class visionchess(QWidget):
    def __init__(self):
        super(visionchess, self).__init__()
        self.my_qtimer = QtCore.QTimer(self)
        self.time_left_int = 10  # DURATION_INT
        self.widget_counter_int = 0
        central_widget = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.pintarmatriz()

        #self.timer_start()
        evaluadas = []
        #self.my_qtimer.stop()

    def iniciarReloj(self):
        self.timer_start()
        self.update_gui()
        self.timer_pause()
        self.preguntarCelda()

    def pintarmatriz(self):
        # armamos el cabezote la grilla incial
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(70)  # width super
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(70)  # height
        self.ui.tableWidget.setStyleSheet("QTableView {gridline-color:black;} ")
        self.ui.tableWidget.setHorizontalHeaderLabels(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))  # set
        self.ui.tableWidget.setVerticalHeaderLabels(('8', '7', '6', '5', '4', '3', '2', '1'))
        m = [[0] * 8 for i in range(8)]  # matriz de 8 *8
        fila = 1
        celda = 0
        for f in range(8):
            for c in range(8):
                celda += 1
                if (f + c) % 2 != 0:
                    self.ui.tableWidget.setItem(f, c, QTableWidgetItem())
                    self.ui.tableWidget.item(f, c).setBackground(QtGui.QColor("#A4E3C1"))  # lime green'''

        self.ui.lblErradas.setWordWrap(True)
        self.ui.lblCorrectas.setWordWrap(True)
        self.ui.btnStart.clicked.connect(self.timer_start)
        self.ui.tableWidget.clicked.connect(self.on_click)
        self.ui.checkCoordsNot.toggled.connect(self.hideCoords)
        self.ui.checkCoordsYes.toggled.connect(self.showCoords)

    def on_click(self, index):
        row = index.row()
        row = self.ui.tableWidget.verticalHeaderItem(row).text()
        column = index.column()
        column = self.ui.tableWidget.horizontalHeaderItem(column).text()
        celda = column + row
        pulsadas.append(celda)
        self.preguntarCelda()

    def preguntarCelda(self):
        # self.timer_start()
        numero = random.randint(1, 8)
        casilla = random.choice(letras) + str(numero)
        evaluadas.append(casilla)
        self.ui.lblCelda.setText(casilla)
        # casilla += casillActual

        global erradas
        global correctas
        if celda in evaluadas:
                correctas += celda + ","'''
            else:
                erradas += celda + ","'''

        # self.tiempo()

    def timer_start(self):
        global evaluadas
        evaluadas = []
        self.time_left_int = DURATION_INT
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        self.ui.tableWidget.setEnabled(True)
        self.preguntarCelda()
        self.update_gui()

    def timer_timeout(self):

        self.time_left_int -= 1
        if self.time_left_int == 0:
            # self.time_left_int = DURATION_INT
            # self.widget_counter_int = (self.widget_counter_int + 1) % 4
            self.my_qtimer.stop()
            self.ui.tableWidget.setEnabled(False)

            # self.pages_qsw.setCurrentIndex(self.widget_counter_int)'''

        self.update_gui()

    def update_gui(self):
        self.ui.lblTime.setText(str(self.time_left_int))
        self.ui.lblCorrectas.setText(str(evaluadas))
        self.ui.lblErradas.setText(str(pulsadas))

    def hideCoords(self):
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.lblCoords.hide()

    def showCoords(self):
        self.ui.tableWidget.horizontalHeader().show()
        self.ui.tableWidget.verticalHeader().show()
        self.ui.lblCoords.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = visionchess()
    application.show()
    sys.exit(app.exec())
