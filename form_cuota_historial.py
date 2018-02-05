# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuota_historial.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuota_historial(object):
    def setupUi(self, form_cuota_historial):
        form_cuota_historial.setObjectName("form_cuota_historial")
        form_cuota_historial.setEnabled(True)
        form_cuota_historial.resize(1270, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_cuota_historial.sizePolicy().hasHeightForWidth())
        form_cuota_historial.setSizePolicy(sizePolicy)
        form_cuota_historial.setMinimumSize(QtCore.QSize(1270, 300))
        form_cuota_historial.setMaximumSize(QtCore.QSize(1270, 300))
        form_cuota_historial.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 1, 1);\n"
"\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_cuota_historial)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(form_cuota_historial)
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

        self.retranslateUi(form_cuota_historial)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_cuota_historial)

    def retranslateUi(self, form_cuota_historial):
        _translate = QtCore.QCoreApplication.translate
        form_cuota_historial.setWindowTitle(_translate("form_cuota_historial", "Historial de Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(0)
        item.setText(_translate("form_cuota_historial", "Estado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(1)
        item.setText(_translate("form_cuota_historial", "N° Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(2)
        item.setText(_translate("form_cuota_historial", "Vencimiento"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(3)
        item.setText(_translate("form_cuota_historial", "Importe Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(4)
        item.setText(_translate("form_cuota_historial", "Importe Cobrado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(5)
        item.setText(_translate("form_cuota_historial", "Fecha de Cobro"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(6)
        item.setText(_translate("form_cuota_historial", "Descripcion"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(7)
        item.setText(_translate("form_cuota_historial", "N° Crédito"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(8)
        item.setText(_translate("form_cuota_historial", "id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_cuota_historial", "Detalle Cuota"))

