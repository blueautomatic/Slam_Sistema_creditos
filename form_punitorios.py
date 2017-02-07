# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_punitorios.ui'
#
# Created: Mon Jan  2 13:10:19 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_punitorios(object):
    def setupUi(self, Form_punitorios):
        Form_punitorios.setObjectName("Form_punitorios")
        Form_punitorios.resize(678, 356)
        Form_punitorios.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"KacstOne\";\n"
"background-color: rgb(172, 55, 26);\n"
"\n"
"")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form_punitorios)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 651, 331))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  11pt \"Century Schoolbook L\";")
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")

        self.retranslateUi(Form_punitorios)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_punitorios)

    def retranslateUi(self, Form_punitorios):
        _translate = QtCore.QCoreApplication.translate
        Form_punitorios.setWindowTitle(_translate("Form_punitorios", "Punitorios"))
        self.label.setText(_translate("Form_punitorios", "Generar Punitorios  hasta Fecha:"))
        self.dte_fecha_consumos_generados.setDisplayFormat(_translate("Form_punitorios", "dd/MM/yyyy"))
        self.boton_limpiar.setText(_translate("Form_punitorios", "Limpiar"))
        self.boton_generar.setText(_translate("Form_punitorios", "Generar"))
        self.label_2.setText(_translate("Form_punitorios", "Historial de punitorios generados : "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_punitorios", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_punitorios", "Descripción"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_punitorios", "Generar Punitorios"))

