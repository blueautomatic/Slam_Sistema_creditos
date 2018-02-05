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
        Form_buscar_apellido.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_buscar_apellido.sizePolicy().hasHeightForWidth())
        Form_buscar_apellido.setSizePolicy(sizePolicy)
        Form_buscar_apellido.setMinimumSize(QtCore.QSize(800, 400))
        Form_buscar_apellido.setMaximumSize(QtCore.QSize(1600, 800))
        Form_buscar_apellido.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"background-color: rgb(81, 1, 1);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form_buscar_apellido)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Form_buscar_apellido)
        self.tabWidget.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(9, 60, 751, 235))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_resultado = QtWidgets.QTableWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_resultado.sizePolicy().hasHeightForWidth())
        self.tw_resultado.setSizePolicy(sizePolicy)
        self.tw_resultado.setMinimumSize(QtCore.QSize(451, 181))
        self.tw_resultado.setMaximumSize(QtCore.QSize(1000, 181))
        self.tw_resultado.setStyleSheet("background-color: rgb(247, 200, 193);")
        self.tw_resultado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_resultado.setObjectName("tw_resultado")
        self.tw_resultado.setColumnCount(3)
        self.tw_resultado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_resultado.setHorizontalHeaderItem(2, item)
        self.tw_resultado.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tw_resultado, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.boton_apellido_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_apellido_buscar.setGeometry(QtCore.QRect(690, 10, 80, 25))
        self.boton_apellido_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_apellido_buscar.setObjectName("boton_apellido_buscar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(408, 12, 64, 25))
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.lne_apellido = QtWidgets.QLineEdit(self.tab)
        self.lne_apellido.setGeometry(QtCore.QRect(478, 12, 200, 25))
        self.lne_apellido.setMinimumSize(QtCore.QSize(200, 25))
        self.lne_apellido.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_apellido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_apellido.setObjectName("lne_apellido")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_buscar_apellido", "Resultado de Búsqueda"))
        self.boton_apellido_buscar.setText(_translate("Form_buscar_apellido", "Buscar"))
        self.label.setText(_translate("Form_buscar_apellido", "Apellido : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_buscar_apellido", "Buscar por Apellido"))

