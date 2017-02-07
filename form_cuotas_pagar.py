# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuotas_pagar.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuotas_pagar(object):
    def setupUi(self, form_cuotas_pagar):
        form_cuotas_pagar.setObjectName("form_cuotas_pagar")
        form_cuotas_pagar.resize(1188, 949)
        form_cuotas_pagar.setStyleSheet("selection-background-color: rgb(218, 175, 158);\n"
"selection-color: rgb(0, 0, 0);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
"background-color: rgb(172, 55, 26);\n"
"\n"
"")
        self.tabWidget_3 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_3.setGeometry(QtCore.QRect(11, 20, 1141, 281))
        self.tabWidget_3.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
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
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 1111, 221))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tw_lista_creditos = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_lista_creditos.setEnabled(False)
        self.tw_lista_creditos.setGeometry(QtCore.QRect(10, 10, 1091, 191))
        self.tw_lista_creditos.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_lista_creditos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tw_lista_creditos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_lista_creditos.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tw_lista_creditos.setObjectName("tw_lista_creditos")
        self.tw_lista_creditos.setColumnCount(6)
        self.tw_lista_creditos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(5, item)
        self.tw_lista_creditos.horizontalHeader().setDefaultSectionSize(125)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_4, icon, "")
        self.groupBox = QtWidgets.QGroupBox(form_cuotas_pagar)
        self.groupBox.setGeometry(QtCore.QRect(437, 4, 551, 41))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
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
"}\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 20))
        self.label.setObjectName("label")
        self.lne_nom_ape = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nom_ape.setGeometry(QtCore.QRect(270, 10, 201, 20))
        self.lne_nom_ape.setObjectName("lne_nom_ape")
        self.boton_buscar_creditos = QtWidgets.QPushButton(self.groupBox)
        self.boton_buscar_creditos.setGeometry(QtCore.QRect(190, 10, 61, 20))
        self.boton_buscar_creditos.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.boton_buscar_creditos.setObjectName("boton_buscar_creditos")
        self.lne_dni = QtWidgets.QLineEdit(self.groupBox)
        self.lne_dni.setGeometry(QtCore.QRect(60, 10, 121, 20))
        self.lne_dni.setObjectName("lne_dni")
        self.tabWidget_4 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_4.setGeometry(QtCore.QRect(10, 340, 841, 421))
        self.tabWidget_4.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
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
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(8, 10, 821, 371))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tw_listado_cuotas = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_listado_cuotas.setEnabled(False)
        self.tw_listado_cuotas.setGeometry(QtCore.QRect(10, 15, 791, 341))
        self.tw_listado_cuotas.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.tw_listado_cuotas.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tw_listado_cuotas.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tw_listado_cuotas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_listado_cuotas.setObjectName("tw_listado_cuotas")
        self.tw_listado_cuotas.setColumnCount(15)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas.setHorizontalHeaderItem(14, item)
        self.tw_listado_cuotas.horizontalHeader().setDefaultSectionSize(100)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_4.addTab(self.tab_3, icon1, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 770, 831, 161))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 11Pt \"Century Schoolbook L\"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(7, 10, 801, 111))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(11, 14, 91, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 48, 281, 16))
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(9, 78, 251, 16))
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.lne_total_cuotas = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_total_cuotas.setGeometry(QtCore.QRect(290, 44, 101, 23))
        self.lne_total_cuotas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_total_cuotas.setObjectName("lne_total_cuotas")
        self.lne_cant_cuotas = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_cant_cuotas.setGeometry(QtCore.QRect(290, 75, 101, 23))
        self.lne_cant_cuotas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cant_cuotas.setObjectName("lne_cant_cuotas")
        self.lne_descripcion = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_descripcion.setGeometry(QtCore.QRect(110, 12, 501, 23))
        self.lne_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descripcion.setObjectName("lne_descripcion")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.lne_capital = QtWidgets.QLineEdit(form_cuotas_pagar)
        self.lne_capital.setEnabled(False)
        self.lne_capital.setGeometry(QtCore.QRect(230, 310, 16, 20))
        self.lne_capital.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_capital.setObjectName("lne_capital")
        self.lne_interes = QtWidgets.QLineEdit(form_cuotas_pagar)
        self.lne_interes.setEnabled(False)
        self.lne_interes.setGeometry(QtCore.QRect(270, 310, 20, 20))
        self.lne_interes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_interes.setObjectName("lne_interes")
        self.lne_gastos = QtWidgets.QLineEdit(form_cuotas_pagar)
        self.lne_gastos.setEnabled(False)
        self.lne_gastos.setGeometry(QtCore.QRect(320, 310, 20, 20))
        self.lne_gastos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_gastos.setObjectName("lne_gastos")
        self.tabWidget_5 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_5.setGeometry(QtCore.QRect(870, 310, 291, 511))
        self.tabWidget_5.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
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
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 100, 271, 321))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font:  75 12Pt \"Century Schoolbook L\";\n"
"font: 11pt \"Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.lne_importe_cobrar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_cobrar.setEnabled(False)
        self.lne_importe_cobrar.setGeometry(QtCore.QRect(146, 250, 111, 41))
        self.lne_importe_cobrar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"font:  75 12Pt \"Century Schoolbook L\";")
        self.lne_importe_cobrar.setText("")
        self.lne_importe_cobrar.setObjectName("lne_importe_cobrar")
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(21, 230, 231, 20))
        self.line.setStyleSheet("color: rgb(170, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 201, 16))
        self.label_13.setStyleSheet("font:  75 11Pt \"Century Schoolbook L\";")
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(10, 34, 231, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(20, 138, 81, 18))
        self.label_8.setObjectName("label_8")
        self.lne_punitorios = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_punitorios.setEnabled(False)
        self.lne_punitorios.setGeometry(QtCore.QRect(158, 137, 81, 18))
        self.lne_punitorios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_punitorios.setObjectName("lne_punitorios")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(20, 200, 61, 21))
        self.label_9.setObjectName("label_9")
        self.lne_saldo = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_saldo.setEnabled(False)
        self.lne_saldo.setGeometry(QtCore.QRect(158, 200, 81, 18))
        self.lne_saldo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_saldo.setObjectName("lne_saldo")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(20, 78, 111, 20))
        self.label_15.setObjectName("label_15")
        self.lne_nro_cuota = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_cuota.setEnabled(False)
        self.lne_nro_cuota.setGeometry(QtCore.QRect(158, 77, 81, 19))
        self.lne_nro_cuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font:  75 11Pt \"Century Schoolbook L\";")
        self.lne_nro_cuota.setObjectName("lne_nro_cuota")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(20, 108, 131, 20))
        self.label_16.setObjectName("label_16")
        self.lne_importe_cuota = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_cuota.setEnabled(False)
        self.lne_importe_cuota.setGeometry(QtCore.QRect(158, 107, 81, 19))
        self.lne_importe_cuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font:  75 11Pt \"Century Schoolbook L\";")
        self.lne_importe_cuota.setObjectName("lne_importe_cuota")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 170, 101, 20))
        self.label_17.setObjectName("label_17")
        self.lne_descuento = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_descuento.setEnabled(False)
        self.lne_descuento.setGeometry(QtCore.QRect(158, 166, 81, 19))
        self.lne_descuento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descuento.setObjectName("lne_descuento")
        self.dte_fecha_cobro = QtWidgets.QDateEdit(self.tab_5)
        self.dte_fecha_cobro.setEnabled(False)
        self.dte_fecha_cobro.setGeometry(QtCore.QRect(142, 43, 111, 23))
        self.dte_fecha_cobro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fecha_cobro.setCalendarPopup(True)
        self.dte_fecha_cobro.setObjectName("dte_fecha_cobro")
        self.line_2 = QtWidgets.QFrame(self.tab_5)
        self.line_2.setGeometry(QtCore.QRect(3, 26, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.cbx_estado = QtWidgets.QComboBox(self.tab_5)
        self.cbx_estado.setEnabled(False)
        self.cbx_estado.setGeometry(QtCore.QRect(112, 70, 141, 20))
        self.cbx_estado.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.cbx_estado.setObjectName("cbx_estado")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(15, 42, 121, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(40, 69, 57, 18))
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(10, 2, 251, 31))
        self.label_3.setStyleSheet("font:  75 11Pt \"Century Schoolbook L\";")
        self.label_3.setObjectName("label_3")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab_5)
        self.boton_limpiar.setGeometry(QtCore.QRect(107, 440, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_limpiar.setFont(font)
        self.boton_limpiar.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"")
        self.boton_limpiar.setObjectName("boton_limpiar")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_5.addTab(self.tab_5, icon2, "")
        self.boton_pagar = QtWidgets.QPushButton(form_cuotas_pagar)
        self.boton_pagar.setGeometry(QtCore.QRect(590, 310, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_pagar.setFont(font)
        self.boton_pagar.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"")
        self.boton_pagar.setObjectName("boton_pagar")
        self.boton_ticket = QtWidgets.QPushButton(form_cuotas_pagar)
        self.boton_ticket.setGeometry(QtCore.QRect(720, 310, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_ticket.setFont(font)
        self.boton_ticket.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"")
        self.boton_ticket.setObjectName("boton_ticket")

        self.retranslateUi(form_cuotas_pagar)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_interes.clear)
        self.boton_limpiar.clicked.connect(self.lne_gastos.clear)
        self.boton_limpiar.clicked.connect(self.lne_capital.clear)
        self.boton_limpiar.clicked.connect(self.lne_importe_cobrar.clear)
        self.boton_limpiar.clicked.connect(self.lne_punitorios.clear)
        self.boton_limpiar.clicked.connect(self.lne_importe_cuota.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_cuota.clear)
        self.boton_limpiar.clicked.connect(self.lne_cant_cuotas.clear)
        self.boton_limpiar.clicked.connect(self.lne_total_cuotas.clear)
        self.boton_limpiar.clicked.connect(self.lne_descripcion.clear)
        self.boton_limpiar.clicked.connect(self.lne_descuento.clear)
        self.boton_limpiar.clicked.connect(self.lne_nom_ape.clear)
        self.boton_limpiar.clicked.connect(self.lne_dni.clear)
        QtCore.QMetaObject.connectSlotsByName(form_cuotas_pagar)
        form_cuotas_pagar.setTabOrder(self.lne_nom_ape, self.boton_buscar_creditos)
        form_cuotas_pagar.setTabOrder(self.boton_buscar_creditos, self.tw_lista_creditos)
        form_cuotas_pagar.setTabOrder(self.tw_lista_creditos, self.tw_listado_cuotas)
        form_cuotas_pagar.setTabOrder(self.tw_listado_cuotas, self.dte_fecha_cobro)
        form_cuotas_pagar.setTabOrder(self.dte_fecha_cobro, self.cbx_estado)
        form_cuotas_pagar.setTabOrder(self.cbx_estado, self.lne_nro_cuota)
        form_cuotas_pagar.setTabOrder(self.lne_nro_cuota, self.lne_importe_cuota)
        form_cuotas_pagar.setTabOrder(self.lne_importe_cuota, self.lne_punitorios)
        form_cuotas_pagar.setTabOrder(self.lne_punitorios, self.lne_descuento)
        form_cuotas_pagar.setTabOrder(self.lne_descuento, self.lne_capital)
        form_cuotas_pagar.setTabOrder(self.lne_capital, self.lne_interes)
        form_cuotas_pagar.setTabOrder(self.lne_interes, self.lne_gastos)
        form_cuotas_pagar.setTabOrder(self.lne_gastos, self.lne_saldo)
        form_cuotas_pagar.setTabOrder(self.lne_saldo, self.lne_importe_cobrar)
        form_cuotas_pagar.setTabOrder(self.lne_importe_cobrar, self.lne_descripcion)
        form_cuotas_pagar.setTabOrder(self.lne_descripcion, self.lne_total_cuotas)
        form_cuotas_pagar.setTabOrder(self.lne_total_cuotas, self.lne_cant_cuotas)
        form_cuotas_pagar.setTabOrder(self.lne_cant_cuotas, self.boton_limpiar)
        form_cuotas_pagar.setTabOrder(self.boton_limpiar, self.tabWidget_5)
        form_cuotas_pagar.setTabOrder(self.tabWidget_5, self.tabWidget_3)
        form_cuotas_pagar.setTabOrder(self.tabWidget_3, self.lne_dni)
        form_cuotas_pagar.setTabOrder(self.lne_dni, self.tabWidget_4)
        form_cuotas_pagar.setTabOrder(self.tabWidget_4, self.tabWidget_2)

    def retranslateUi(self, form_cuotas_pagar):
        _translate = QtCore.QCoreApplication.translate
        form_cuotas_pagar.setWindowTitle(_translate("form_cuotas_pagar", "Cuotas Pagar"))
        item = self.tw_lista_creditos.horizontalHeaderItem(0)
        item.setText(_translate("form_cuotas_pagar", "Crédito N°"))
        item = self.tw_lista_creditos.horizontalHeaderItem(1)
        item.setText(_translate("form_cuotas_pagar", "Cliente"))
        item = self.tw_lista_creditos.horizontalHeaderItem(2)
        item.setText(_translate("form_cuotas_pagar", "Fecha Crédito"))
        item = self.tw_lista_creditos.horizontalHeaderItem(3)
        item.setText(_translate("form_cuotas_pagar", "N° Cuotas"))
        item = self.tw_lista_creditos.horizontalHeaderItem(4)
        item.setText(_translate("form_cuotas_pagar", "Capital"))
        item = self.tw_lista_creditos.horizontalHeaderItem(5)
        item.setText(_translate("form_cuotas_pagar", "Finalizado"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("form_cuotas_pagar", "Historial de Cŕeditos"))
        self.label.setText(_translate("form_cuotas_pagar", "DNI: "))
        self.boton_buscar_creditos.setText(_translate("form_cuotas_pagar", "Buscar"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(0)
        item.setText(_translate("form_cuotas_pagar", "Estado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(1)
        item.setText(_translate("form_cuotas_pagar", "N° Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(2)
        item.setText(_translate("form_cuotas_pagar", "Vencimiento"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(3)
        item.setText(_translate("form_cuotas_pagar", "Importe Cuota"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(4)
        item.setText(_translate("form_cuotas_pagar", "Punitorio"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(5)
        item.setText(_translate("form_cuotas_pagar", "Descuento"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(6)
        item.setText(_translate("form_cuotas_pagar", "Cuota pagar"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(7)
        item.setText(_translate("form_cuotas_pagar", "Importe Cobrado"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(8)
        item.setText(_translate("form_cuotas_pagar", "Saldo"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(9)
        item.setText(_translate("form_cuotas_pagar", "Fecha de Cobro"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(10)
        item.setText(_translate("form_cuotas_pagar", "Capital"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(11)
        item.setText(_translate("form_cuotas_pagar", "Interes"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(12)
        item.setText(_translate("form_cuotas_pagar", "Gastos"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(13)
        item.setText(_translate("form_cuotas_pagar", "Descripcion"))
        item = self.tw_listado_cuotas.horizontalHeaderItem(14)
        item.setText(_translate("form_cuotas_pagar", "id"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_3), _translate("form_cuotas_pagar", "Cuotas del Crédito"))
        self.label_2.setText(_translate("form_cuotas_pagar", "Descripción: "))
        self.label_5.setText(_translate("form_cuotas_pagar", "Calculo total de Cuotas Seleccionadas : "))
        self.label_14.setText(_translate("form_cuotas_pagar", "Cantidad de Cuotas Seleccionadas : "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_cuotas_pagar", "Detalle de Cuotas Cobradas"))
        self.label_6.setText(_translate("form_cuotas_pagar", "Importe a cobrar :"))
        self.label_13.setText(_translate("form_cuotas_pagar", "Detalle importes a Cobrar : "))
        self.label_8.setText(_translate("form_cuotas_pagar", "Punitorios :"))
        self.label_9.setText(_translate("form_cuotas_pagar", "Saldo:"))
        self.label_15.setText(_translate("form_cuotas_pagar", "Nro de Cuota: "))
        self.label_16.setText(_translate("form_cuotas_pagar", "Importe de Cuota: "))
        self.label_17.setText(_translate("form_cuotas_pagar", "Descuentos : "))
        self.dte_fecha_cobro.setDisplayFormat(_translate("form_cuotas_pagar", "dd/M/yyyy"))
        self.cbx_estado.setItemText(0, _translate("form_cuotas_pagar", "Pagada"))
        self.cbx_estado.setItemText(1, _translate("form_cuotas_pagar", "Pago Parcial"))
        self.cbx_estado.setItemText(2, _translate("form_cuotas_pagar", "A pagar"))
        self.cbx_estado.setItemText(3, _translate("form_cuotas_pagar", "Vencida 30 días"))
        self.cbx_estado.setItemText(4, _translate("form_cuotas_pagar", "Vencida 60 días"))
        self.cbx_estado.setItemText(5, _translate("form_cuotas_pagar", "Vencida 90 días"))
        self.cbx_estado.setItemText(6, _translate("form_cuotas_pagar", "Vencida 120 días"))
        self.cbx_estado.setItemText(7, _translate("form_cuotas_pagar", "Vencida 150 días"))
        self.cbx_estado.setItemText(8, _translate("form_cuotas_pagar", "Vencida 180 días"))
        self.cbx_estado.setItemText(9, _translate("form_cuotas_pagar", "En Judiciales"))
        self.label_11.setText(_translate("form_cuotas_pagar", "Fecha de Cobro : "))
        self.label_12.setText(_translate("form_cuotas_pagar", "Estado : "))
        self.label_3.setText(_translate("form_cuotas_pagar", "Información a editar por el Usuario : "))
        self.boton_limpiar.setText(_translate("form_cuotas_pagar", "Limpiar"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_5), _translate("form_cuotas_pagar", "Pago de Cuota"))
        self.boton_pagar.setText(_translate("form_cuotas_pagar", "Pagar"))
        self.boton_ticket.setText(_translate("form_cuotas_pagar", "Ticket"))

