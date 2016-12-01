# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_listado_morosos.ui'
#
# Created: Thu Sep 22 15:27:08 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_listado_morosos(object):
    def setupUi(self, form_listado_morosos):
        form_listado_morosos.setObjectName("form_listado_morosos")
        form_listado_morosos.resize(400, 300)
        self.boton_generar = QtWidgets.QPushButton(form_listado_morosos)
        self.boton_generar.setGeometry(QtCore.QRect(120, 130, 80, 23))
        self.boton_generar.setObjectName("boton_generar")
        self.label = QtWidgets.QLabel(form_listado_morosos)
        self.label.setGeometry(QtCore.QRect(110, 90, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(form_listado_morosos)
        QtCore.QMetaObject.connectSlotsByName(form_listado_morosos)

    def retranslateUi(self, form_listado_morosos):
        _translate = QtCore.QCoreApplication.translate
        form_listado_morosos.setWindowTitle(_translate("form_listado_morosos", "Dialog"))
        self.boton_generar.setText(_translate("form_listado_morosos", "Generar"))
        self.label.setText(_translate("form_listado_morosos", "Listado morosos"))

