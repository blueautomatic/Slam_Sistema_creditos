# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_egresos_diarios.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_egresos_diarios(object):
    def setupUi(self, form_egresos_diarios):
        form_egresos_diarios.setObjectName("form_egresos_diarios")
        form_egresos_diarios.resize(800, 800)
        form_egresos_diarios.setMaximumSize(QtCore.QSize(1600, 800))
        form_egresos_diarios.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 1, 1);\n"
"selection-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.gridLayout_4 = QtWidgets.QGridLayout(form_egresos_diarios)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(form_egresos_diarios)
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dte_fecha_egresos_mov = QtWidgets.QDateEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dte_fecha_egresos_mov.setFont(font)
        self.dte_fecha_egresos_mov.setStyleSheet("")
        self.dte_fecha_egresos_mov.setCalendarPopup(True)
        self.dte_fecha_egresos_mov.setObjectName("dte_fecha_egresos_mov")
        self.horizontalLayout.addWidget(self.dte_fecha_egresos_mov)
        self.boton_egresos_buscar = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_egresos_buscar.setFont(font)
        self.boton_egresos_buscar.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"")
        self.boton_egresos_buscar.setObjectName("boton_egresos_buscar")
        self.horizontalLayout.addWidget(self.boton_egresos_buscar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tw_ingresos_registros = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_ingresos_registros.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.tw_ingresos_registros.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tw_ingresos_registros.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_ingresos_registros.setObjectName("tw_ingresos_registros")
        self.tw_ingresos_registros.setColumnCount(6)
        self.tw_ingresos_registros.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(5, item)
        self.tw_ingresos_registros.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout_2.addWidget(self.tw_ingresos_registros, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lne_egresos_total = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_egresos_total.setStyleSheet("border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.lne_egresos_total.setObjectName("lne_egresos_total")
        self.gridLayout_2.addWidget(self.lne_egresos_total, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.boton_egresos_imprimir = QtWidgets.QPushButton(self.tab_2)
        self.boton_egresos_imprimir.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"")
        self.boton_egresos_imprimir.setObjectName("boton_egresos_imprimir")
        self.gridLayout_3.addWidget(self.boton_egresos_imprimir, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.gridLayout_4.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.retranslateUi(form_egresos_diarios)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_egresos_diarios)

    def retranslateUi(self, form_egresos_diarios):
        _translate = QtCore.QCoreApplication.translate
        form_egresos_diarios.setWindowTitle(_translate("form_egresos_diarios", "Egresos Diarios"))
        self.label.setText(_translate("form_egresos_diarios", "Fecha de movimientos a buscar :"))
        self.dte_fecha_egresos_mov.setDisplayFormat(_translate("form_egresos_diarios", "dd/M/yyyy"))
        self.boton_egresos_buscar.setText(_translate("form_egresos_diarios", "Buscar"))
        self.label_2.setText(_translate("form_egresos_diarios", "Registro de Egresos diarios"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(0)
        item.setText(_translate("form_egresos_diarios", "N° Orden"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(1)
        item.setText(_translate("form_egresos_diarios", "Creditos otorgados"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(2)
        item.setText(_translate("form_egresos_diarios", "Crédito"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(3)
        item.setText(_translate("form_egresos_diarios", "Cant. cuotas"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(4)
        item.setText(_translate("form_egresos_diarios", "Importe cuotas"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(5)
        item.setText(_translate("form_egresos_diarios", "Importe"))
        self.label_3.setText(_translate("form_egresos_diarios", "Total de Egresos del Día: "))
        self.boton_egresos_imprimir.setText(_translate("form_egresos_diarios", "Imprimir"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_egresos_diarios", "Egresos Diarios"))

