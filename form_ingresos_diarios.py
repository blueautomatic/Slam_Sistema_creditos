# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_ingresos_diarios.ui'
#
# Created: Sun Nov 20 17:20:19 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_ingresos_diarios(object):
    def setupUi(self, form_ingresos_diarios):
        form_ingresos_diarios.setObjectName("form_ingresos_diarios")
        form_ingresos_diarios.resize(856, 825)
        form_ingresos_diarios.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"KacstOne\";\n"
"background-color: rgb(172, 55, 26);\n"
"\n"
"")
        self.tabWidget_2 = QtWidgets.QTabWidget(form_ingresos_diarios)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 831, 801))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font: 11pt \"Century Schoolbook L\";")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(110, 10, 621, 81))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(239, 235, 231);\n"
"}\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"font: 10pt \"KacstOne\";\n"
"}\n"
"QDateEdit{\n"
"background-color: rgb(239, 235, 231);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(36, 32, 231, 16))
        self.label.setStyleSheet("font: 75 11pt \"Century Schoolbook L\";")
        self.label.setObjectName("label")
        self.boton_ingresos_buscar = QtWidgets.QPushButton(self.groupBox)
        self.boton_ingresos_buscar.setGeometry(QtCore.QRect(490, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.boton_ingresos_buscar.setFont(font)
        self.boton_ingresos_buscar.setStyleSheet("font:  12pt \"Century Schoolbook L\";\n"
"background-color: rgb(251, 204, 193);\n"
"border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.boton_ingresos_buscar.setObjectName("boton_ingresos_buscar")
        self.dte_fecha_ingresos_mov = QtWidgets.QDateEdit(self.groupBox)
        self.dte_fecha_ingresos_mov.setGeometry(QtCore.QRect(300, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dte_fecha_ingresos_mov.setFont(font)
        self.dte_fecha_ingresos_mov.setStyleSheet("font: 75 12pt \"Century Schoolbook L\";\n"
"border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.dte_fecha_ingresos_mov.setCalendarPopup(True)
        self.dte_fecha_ingresos_mov.setObjectName("dte_fecha_ingresos_mov")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(13, 98, 241, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 801, 561))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"font: 10pt \"KacstOne\";\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(239, 235, 231);\n"
"}\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"font: 10pt \"KacstOne\";\n"
"}\n"
"QDateEdit{\n"
"background-color: rgb(239, 235, 231);\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(450, 480, 171, 31))
        self.label_3.setObjectName("label_3")
        self.lne_ingresos_total = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ingresos_total.setGeometry(QtCore.QRect(630, 470, 151, 51))
        self.lne_ingresos_total.setStyleSheet("border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.lne_ingresos_total.setObjectName("lne_ingresos_total")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 480, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lne_ingresos_nro_planilla = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ingresos_nro_planilla.setGeometry(QtCore.QRect(110, 480, 61, 31))
        self.lne_ingresos_nro_planilla.setStyleSheet("border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.lne_ingresos_nro_planilla.setObjectName("lne_ingresos_nro_planilla")
        self.tw_ingresos_registros = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_ingresos_registros.setGeometry(QtCore.QRect(20, 20, 761, 331))
        self.tw_ingresos_registros.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.tw_ingresos_registros.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tw_ingresos_registros.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_ingresos_registros.setObjectName("tw_ingresos_registros")
        self.tw_ingresos_registros.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_ingresos_registros.setHorizontalHeaderItem(6, item)
        self.tw_ingresos_registros.horizontalHeader().setDefaultSectionSize(150)
        self.boton_ingresos_imprimir = QtWidgets.QPushButton(self.groupBox_2)
        self.boton_ingresos_imprimir.setGeometry(QtCore.QRect(280, 360, 151, 51))
        self.boton_ingresos_imprimir.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;")
        self.boton_ingresos_imprimir.setObjectName("boton_ingresos_imprimir")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")

        self.retranslateUi(form_ingresos_diarios)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_ingresos_diarios)

    def retranslateUi(self, form_ingresos_diarios):
        _translate = QtCore.QCoreApplication.translate
        form_ingresos_diarios.setWindowTitle(_translate("form_ingresos_diarios", "Ingresos Diarios"))
        self.label.setText(_translate("form_ingresos_diarios", "Fecha de movimientos a buscar :"))
        self.boton_ingresos_buscar.setText(_translate("form_ingresos_diarios", "Buscar"))
        self.dte_fecha_ingresos_mov.setDisplayFormat(_translate("form_ingresos_diarios", "dd/M/yyyy"))
        self.label_2.setText(_translate("form_ingresos_diarios", "Registro de Ingresos diarios"))
        self.label_3.setText(_translate("form_ingresos_diarios", "Total de Ingresos del Día: "))
        self.label_4.setText(_translate("form_ingresos_diarios", "N° Planilla :"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(0)
        item.setText(_translate("form_ingresos_diarios", "Nombre y Apellido"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(1)
        item.setText(_translate("form_ingresos_diarios", "Cuota"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(2)
        item.setText(_translate("form_ingresos_diarios", "Número "))
        item = self.tw_ingresos_registros.horizontalHeaderItem(3)
        item.setText(_translate("form_ingresos_diarios", "Importe"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(4)
        item.setText(_translate("form_ingresos_diarios", "Punitorios"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(5)
        item.setText(_translate("form_ingresos_diarios", "Descuento"))
        item = self.tw_ingresos_registros.horizontalHeaderItem(6)
        item.setText(_translate("form_ingresos_diarios", "Estado"))
        self.boton_ingresos_imprimir.setText(_translate("form_ingresos_diarios", "Imprimir"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_ingresos_diarios", "Ingresos Diarios"))
