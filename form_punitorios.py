# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_punitorios.ui'
#
# Created: Fri Apr  7 23:15:30 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_punitorios(object):
    def setupUi(self, Form_punitorios):
        Form_punitorios.setObjectName("Form_punitorios")
        Form_punitorios.resize(589, 387)
        Form_punitorios.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(136, 3, 3);\n"
"font: 75 10pt \"KacstOne\";\n"
"\n"
"")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form_punitorios)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form_punitorios)
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
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dte_fecha_consumos_generados = QtWidgets.QDateEdit(self.groupBox)
        self.dte_fecha_consumos_generados.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fecha_consumos_generados.setCalendarPopup(True)
        self.dte_fecha_consumos_generados.setObjectName("dte_fecha_consumos_generados")
        self.horizontalLayout.addWidget(self.dte_fecha_consumos_generados)
        self.boton_generar = QtWidgets.QPushButton(self.groupBox)
        self.boton_generar.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"")
        self.boton_generar.setObjectName("boton_generar")
        self.horizontalLayout.addWidget(self.boton_generar)
        self.boton_limpiar = QtWidgets.QPushButton(self.groupBox)
        self.boton_limpiar.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.horizontalLayout.addWidget(self.boton_limpiar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setStyleSheet("background-color: rgb(247, 200, 193);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.gridLayout_4.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.retranslateUi(Form_punitorios)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_punitorios)

    def retranslateUi(self, Form_punitorios):
        _translate = QtCore.QCoreApplication.translate
        Form_punitorios.setWindowTitle(_translate("Form_punitorios", "Punitorios"))
        self.label.setText(_translate("Form_punitorios", "Generar Punitorios  hasta Fecha:"))
        self.dte_fecha_consumos_generados.setDisplayFormat(_translate("Form_punitorios", "dd/MM/yyyy"))
        self.boton_generar.setText(_translate("Form_punitorios", "Generar"))
        self.boton_limpiar.setText(_translate("Form_punitorios", "Limpiar"))
        self.label_2.setText(_translate("Form_punitorios", "Historial de punitorios generados : "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_punitorios", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_punitorios", "Descripción"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_punitorios", "Generar Punitorios"))

