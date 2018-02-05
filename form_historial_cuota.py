# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_historial_cuota.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1270, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1270, 300))
        Dialog.setMaximumSize(QtCore.QSize(1270, 300))
        Dialog.setStyleSheet("font: 75 11pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(136, 3, 3, 100);\n"
"\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_listado_cuotas = QtWidgets.QTableWidget(self.tab)
        self.tw_listado_cuotas.setEnabled(False)
        self.tw_listado_cuotas.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.tw_listado_cuotas.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tw_listado_cuotas.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tw_listado_cuotas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_listado_cuotas.setObjectName("tw_listado_cuotas")
        self.tw_listado_cuotas.setColumnCount(9)
        self.tw_listado_cuotas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(8, item)
        self.tw_listado_cuotas.horizontalHeader().setDefaultSectionSize(135)
        self.gridLayout.addWidget(self.tw_listado_cuotas, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Historial de Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Estado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "N° Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Vencimiento"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Importe Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Importe Cobrado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Fecha de Cobro"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Descripcion"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "N° Crédito"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Detalle Cuota"))

