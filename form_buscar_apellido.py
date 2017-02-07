# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_buscar_apellido.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_buscar_apellido(object):
    def setupUi(self, Form_buscar_apellido):
        Form_buscar_apellido.setObjectName("Form_buscar_apellido")
        Form_buscar_apellido.resize(643, 483)
        Form_buscar_apellido.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(Form_buscar_apellido)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.tabWidget.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"KacstOne\";\n"
"background-color: rgb(172, 55, 26);\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(8, 70, 601, 351))
        self.tabWidget_2.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tw_resultado = QtWidgets.QTableWidget(self.tab_2)
        self.tw_resultado.setGeometry(QtCore.QRect(8, 10, 581, 301))
        self.tw_resultado.setStyleSheet("background-color: rgb(211, 203, 184);\n"
"")
        self.tw_resultado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_resultado.setObjectName("tw_resultado")
        self.tw_resultado.setColumnCount(4)
        self.tw_resultado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(3, item)
        self.tw_resultado.horizontalHeader().setDefaultSectionSize(150)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(2, 10, 431, 51))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(211, 211, 186);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 15, 71, 21))
        self.label.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.label.setObjectName("label")
        self.lne_apellido = QtWidgets.QLineEdit(self.groupBox)
        self.lne_apellido.setGeometry(QtCore.QRect(89, 16, 211, 21))
        self.lne_apellido.setObjectName("lne_apellido")
        self.boton_apellido_buscar = QtWidgets.QPushButton(self.groupBox)
        self.boton_apellido_buscar.setGeometry(QtCore.QRect(309, 16, 80, 23))
        self.boton_apellido_buscar.setObjectName("boton_apellido_buscar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")

        self.retranslateUi(Form_buscar_apellido)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_buscar_apellido)
        Form_buscar_apellido.setTabOrder(self.lne_apellido, self.boton_apellido_buscar)
        Form_buscar_apellido.setTabOrder(self.boton_apellido_buscar, self.tabWidget_2)
        Form_buscar_apellido.setTabOrder(self.tabWidget_2, self.tw_resultado)
        Form_buscar_apellido.setTabOrder(self.tw_resultado, self.tabWidget)

    def retranslateUi(self, Form_buscar_apellido):
        _translate = QtCore.QCoreApplication.translate
        Form_buscar_apellido.setWindowTitle(_translate("Form_buscar_apellido", "Buscar por Apellido"))
        item = self.tw_resultado.horizontalHeaderItem(0)
        item.setText(_translate("Form_buscar_apellido", "Apellido"))
        item = self.tw_resultado.horizontalHeaderItem(1)
        item.setText(_translate("Form_buscar_apellido", "Nombre"))
        item = self.tw_resultado.horizontalHeaderItem(2)
        item.setText(_translate("Form_buscar_apellido", "DNI"))
        item = self.tw_resultado.horizontalHeaderItem(3)
        item.setText(_translate("Form_buscar_apellido", "N° Cliente"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_buscar_apellido", "Resultado de Búsqueda"))
        self.label.setText(_translate("Form_buscar_apellido", "Apellido : "))
        self.boton_apellido_buscar.setText(_translate("Form_buscar_apellido", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_buscar_apellido", "Buscar por Apellido"))

