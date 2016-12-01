# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_punitorios_generar.ui'
#
# Created: Thu Sep 29 11:53:47 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(678, 356)
        Form.setStyleSheet("selection-background-color: rgb(218, 175, 158);\n"
"selection-color: rgb(0, 0, 0);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"background-color: rgb(172, 55, 26);\n"
"")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 651, 331))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 621, 81))
        self.groupBox.setStyleSheet("QGroupBox{\n"
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
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(36, 32, 221, 16))
        self.label.setObjectName("label")
        self.dte_fecha_consumos_generados = QtWidgets.QDateEdit(self.groupBox)
        self.dte_fecha_consumos_generados.setGeometry(QtCore.QRect(266, 29, 110, 20))
        self.dte_fecha_consumos_generados.setCalendarPopup(True)
        self.dte_fecha_consumos_generados.setObjectName("dte_fecha_consumos_generados")
        self.boton_limpiar = QtWidgets.QPushButton(self.groupBox)
        self.boton_limpiar.setGeometry(QtCore.QRect(517, 29, 71, 20))
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_generar = QtWidgets.QPushButton(self.groupBox)
        self.boton_generar.setGeometry(QtCore.QRect(441, 29, 71, 20))
        self.boton_generar.setObjectName("boton_generar")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(13, 98, 241, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 621, 161))
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
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 581, 141))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.dte_fecha_consumos_generados.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Punitorios"))
        self.label.setText(_translate("Form", "Generar Punitorios  hasta Fecha:"))
        self.dte_fecha_consumos_generados.setDisplayFormat(_translate("Form", "dd/mm/yyyy"))
        self.boton_limpiar.setText(_translate("Form", "Limpiar"))
        self.boton_generar.setText(_translate("Form", "Generar"))
        self.label_2.setText(_translate("Form", "Historial de punitorios generados : "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Número"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Descripción"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fecha"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "Generar Punitorios"))

