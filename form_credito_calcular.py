# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_credito_calcular.ui'
#
# Created: Wed Nov 30 19:58:40 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_credito_calcular(object):
    def setupUi(self, form_credito_calcular):
        form_credito_calcular.setObjectName("form_credito_calcular")
        form_credito_calcular.resize(671, 607)
        form_credito_calcular.setStyleSheet("selection-background-color: rgb(218, 175, 158);\n"
"selection-color: rgb(0, 0, 0);\n"
"font:  75 10Pt \"Century Schoolbook L\";")
        self.tabWidget = QtWidgets.QTabWidget(form_credito_calcular)
        self.tabWidget.setGeometry(QtCore.QRect(10, 7, 651, 591))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font:  75 10Pt \"Century Schoolbook L\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(8, 10, 631, 541))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.boton_limpiar_creditonuevo = QtWidgets.QPushButton(self.tab_2)
        self.boton_limpiar_creditonuevo.setEnabled(True)
        self.boton_limpiar_creditonuevo.setGeometry(QtCore.QRect(530, 409, 61, 23))
        self.boton_limpiar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"}")
        self.boton_limpiar_creditonuevo.setObjectName("boton_limpiar_creditonuevo")
        self.tw_lista_cuotas_creditonuevo = QtWidgets.QTableWidget(self.tab_2)
        self.tw_lista_cuotas_creditonuevo.setEnabled(True)
        self.tw_lista_cuotas_creditonuevo.setGeometry(QtCore.QRect(7, 194, 601, 181))
        self.tw_lista_cuotas_creditonuevo.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"font:  75 10Pt \"Century Schoolbook L\";")
        self.tw_lista_cuotas_creditonuevo.setObjectName("tw_lista_cuotas_creditonuevo")
        self.tw_lista_cuotas_creditonuevo.setColumnCount(6)
        self.tw_lista_cuotas_creditonuevo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_cuotas_creditonuevo.setHorizontalHeaderItem(5, item)
        self.tw_lista_cuotas_creditonuevo.horizontalHeader().setDefaultSectionSize(100)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(120, 383, 361, 121))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"font:  75 10Pt \"Century Schoolbook L\";}\n"
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
"}\n"
"\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lne_credito_total = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_credito_total.setEnabled(True)
        self.lne_credito_total.setGeometry(QtCore.QRect(170, 17, 171, 25))
        self.lne_credito_total.setText("")
        self.lne_credito_total.setObjectName("lne_credito_total")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 141, 18))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lne_interes_total = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_interes_total.setEnabled(True)
        self.lne_interes_total.setGeometry(QtCore.QRect(170, 48, 171, 25))
        self.lne_interes_total.setText("")
        self.lne_interes_total.setObjectName("lne_interes_total")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 51, 141, 18))
        self.label_13.setObjectName("label_13")
        self.lne_otros_total = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_otros_total.setEnabled(True)
        self.lne_otros_total.setGeometry(QtCore.QRect(170, 79, 171, 25))
        self.lne_otros_total.setText("")
        self.lne_otros_total.setObjectName("lne_otros_total")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(21, 82, 101, 18))
        self.label_14.setObjectName("label_14")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(7, 12, 371, 171))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 2px;\n"
"    font: 10pt \"KacstOne\";\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"    font: 10pt \"KacstOne\";\n"
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
"}\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.spbx_cantidad_cuotas_creditonuevo = QtWidgets.QSpinBox(self.groupBox)
        self.spbx_cantidad_cuotas_creditonuevo.setEnabled(True)
        self.spbx_cantidad_cuotas_creditonuevo.setGeometry(QtCore.QRect(189, 88, 51, 25))
        self.spbx_cantidad_cuotas_creditonuevo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spbx_cantidad_cuotas_creditonuevo.setProperty("value", 3)
        self.spbx_cantidad_cuotas_creditonuevo.setObjectName("spbx_cantidad_cuotas_creditonuevo")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(23, 24, 155, 18))
        self.label_7.setObjectName("label_7")
        self.lne_importe_prestamo_creditonuevo = QtWidgets.QLineEdit(self.groupBox)
        self.lne_importe_prestamo_creditonuevo.setEnabled(True)
        self.lne_importe_prestamo_creditonuevo.setGeometry(QtCore.QRect(189, 22, 51, 26))
        self.lne_importe_prestamo_creditonuevo.setObjectName("lne_importe_prestamo_creditonuevo")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(23, 87, 129, 18))
        self.label_8.setObjectName("label_8")
        self.lne_interes_creditonuevo = QtWidgets.QLineEdit(self.groupBox)
        self.lne_interes_creditonuevo.setEnabled(True)
        self.lne_interes_creditonuevo.setGeometry(QtCore.QRect(189, 57, 21, 25))
        self.lne_interes_creditonuevo.setObjectName("lne_interes_creditonuevo")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(23, 55, 60, 18))
        self.label_11.setObjectName("label_11")
        self.dte_fec_creditonuevo = QtWidgets.QDateEdit(self.groupBox)
        self.dte_fec_creditonuevo.setEnabled(True)
        self.dte_fec_creditonuevo.setGeometry(QtCore.QRect(189, 119, 101, 25))
        self.dte_fec_creditonuevo.setCalendarPopup(True)
        self.dte_fec_creditonuevo.setDate(QtCore.QDate(2007, 7, 23))
        self.dte_fec_creditonuevo.setObjectName("dte_fec_creditonuevo")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(23, 118, 112, 18))
        self.label_3.setObjectName("label_3")
        self.boton_generar_creditonuevo = QtWidgets.QPushButton(self.groupBox)
        self.boton_generar_creditonuevo.setEnabled(True)
        self.boton_generar_creditonuevo.setGeometry(QtCore.QRect(290, 75, 61, 23))
        self.boton_generar_creditonuevo.setStyleSheet("background-color: rgb(253, 194, 179);\n"
"font:  75 10Pt \"Century Schoolbook L\";")
        self.boton_generar_creditonuevo.setObjectName("boton_generar_creditonuevo")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/calculadora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.tabWidget.addTab(self.tab, icon, "")

        self.retranslateUi(form_credito_calcular)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_credito_total.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_interes_total.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_otros_total.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.spbx_cantidad_cuotas_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.dte_fec_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_importe_prestamo_creditonuevo.clear)
        QtCore.QMetaObject.connectSlotsByName(form_credito_calcular)

    def retranslateUi(self, form_credito_calcular):
        _translate = QtCore.QCoreApplication.translate
        form_credito_calcular.setWindowTitle(_translate("form_credito_calcular", "Calcular Crédito"))
        self.boton_limpiar_creditonuevo.setText(_translate("form_credito_calcular", "Limpiar"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(0)
        item.setText(_translate("form_credito_calcular", "Cuota N°"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(1)
        item.setText(_translate("form_credito_calcular", "Capital"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(2)
        item.setText(_translate("form_credito_calcular", "Interés"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(3)
        item.setText(_translate("form_credito_calcular", "Gastos"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(4)
        item.setText(_translate("form_credito_calcular", "1er Venc"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(5)
        item.setText(_translate("form_credito_calcular", "Importe 1er Venc"))
        self.label_12.setText(_translate("form_credito_calcular", "Total Crédito : "))
        self.label_13.setText(_translate("form_credito_calcular", "Total Intereses : "))
        self.label_14.setText(_translate("form_credito_calcular", "Total Otros  : "))
        self.label_7.setText(_translate("form_credito_calcular", "Importe del prestamo $:"))
        self.lne_importe_prestamo_creditonuevo.setText(_translate("form_credito_calcular", "1000"))
        self.label_8.setText(_translate("form_credito_calcular", "Cantidad de cuotas:"))
        self.lne_interes_creditonuevo.setText(_translate("form_credito_calcular", "8"))
        self.label_11.setText(_translate("form_credito_calcular", "Interes %:"))
        self.dte_fec_creditonuevo.setDisplayFormat(_translate("form_credito_calcular", "dd/M/yyyy"))
        self.label_3.setText(_translate("form_credito_calcular", "Fecha de credito:"))
        self.boton_generar_creditonuevo.setText(_translate("form_credito_calcular", "Calcular"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_credito_calcular", "Calcular"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_credito_calcular", "Cálculo de Crédito"))

