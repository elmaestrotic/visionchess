# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visionchess.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1077, 806)
        Form.setStyleSheet("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(100, 60, 591, 591))
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.lblCoords = QtWidgets.QLabel(Form)
        self.lblCoords.setGeometry(QtCore.QRect(120, 640, 741, 91))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lblCoords.setFont(font)
        self.lblCoords.setObjectName("lblCoords")
        self.lblCelda = QtWidgets.QLabel(Form)
        self.lblCelda.setGeometry(QtCore.QRect(780, 490, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblCelda.setFont(font)
        self.lblCelda.setStyleSheet("color: rgb(0, 170, 255);")
        self.lblCelda.setObjectName("lblCelda")
        self.btnStart = QtWidgets.QPushButton(Form)
        self.btnStart.setGeometry(QtCore.QRect(720, 600, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.lblTime = QtWidgets.QLabel(Form)
        self.lblTime.setGeometry(QtCore.QRect(750, 0, 251, 141))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setObjectName("lblTime")
        self.lblCorrectas = QtWidgets.QLabel(Form)
        self.lblCorrectas.setGeometry(QtCore.QRect(710, 140, 91, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblCorrectas.setFont(font)
        self.lblCorrectas.setStyleSheet("color: rgb(85, 0, 255);")
        self.lblCorrectas.setObjectName("lblCorrectas")
        self.lblErradas = QtWidgets.QLabel(Form)
        self.lblErradas.setGeometry(QtCore.QRect(960, 150, 91, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblErradas.setFont(font)
        self.lblErradas.setStyleSheet("color: rgb(255, 0, 127);")
        self.lblErradas.setObjectName("lblErradas")
        self.checkCoordsYes = QtWidgets.QCheckBox(Form)
        self.checkCoordsYes.setGeometry(QtCore.QRect(790, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkCoordsYes.setFont(font)
        self.checkCoordsYes.setAutoExclusive(True)
        self.checkCoordsYes.setObjectName("checkCoordsYes")
        self.checkCoordsNot = QtWidgets.QCheckBox(Form)
        self.checkCoordsNot.setGeometry(QtCore.QRect(790, 700, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkCoordsNot.setFont(font)
        self.checkCoordsNot.setAutoExclusive(True)
        self.checkCoordsNot.setObjectName("checkCoordsNot")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Semillero de Ajedrez UCN - VisionChess  - Fundación Universitaria Católica del Norte - Desarrollado por Alexander Narváez - anarvaez@ucn.edu.co"))
        self.lblCoords.setText(_translate("Form", "A  B  C  D  E  F  G  H"))
        self.lblCelda.setText(_translate("Form", "¿Listo?"))
        self.btnStart.setText(_translate("Form", "Comenzar"))
        self.lblTime.setText(_translate("Form", "Tiempo"))
        self.lblCorrectas.setText(_translate("Form", "Correctas"))
        self.lblErradas.setText(_translate("Form", "Erradas"))
        self.checkCoordsYes.setText(_translate("Form", "Mostrar Coordenadas"))
        self.checkCoordsNot.setText(_translate("Form", "Ocultar Coordenadas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
