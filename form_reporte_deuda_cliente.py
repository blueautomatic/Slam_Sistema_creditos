# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_reporte_deuda_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_deuda_cliente(object):
    def setupUi(self, form_deuda_cliente):
        form_deuda_cliente.setObjectName("form_deuda_cliente")
        form_deuda_cliente.resize(400, 300)
        self.boton_reporte = QtWidgets.QPushButton(form_deuda_cliente)
        self.boton_reporte.setGeometry(QtCore.QRect(130, 50, 89, 25))
        self.boton_reporte.setObjectName("boton_reporte")

        self.retranslateUi(form_deuda_cliente)
        QtCore.QMetaObject.connectSlotsByName(form_deuda_cliente)

    def retranslateUi(self, form_deuda_cliente):
        _translate = QtCore.QCoreApplication.translate
        form_deuda_cliente.setWindowTitle(_translate("form_deuda_cliente", "Dialog"))
        self.boton_reporte.setText(_translate("form_deuda_cliente", "Reporte"))

