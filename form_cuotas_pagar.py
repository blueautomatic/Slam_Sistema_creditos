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
        form_cuotas_pagar.resize(1449, 806)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_cuotas_pagar.sizePolicy().hasHeightForWidth())
        form_cuotas_pagar.setSizePolicy(sizePolicy)
        form_cuotas_pagar.setMinimumSize(QtCore.QSize(800, 450))
        form_cuotas_pagar.setMaximumSize(QtCore.QSize(1600, 900))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        form_cuotas_pagar.setFont(font)
        form_cuotas_pagar.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 1, 1);\n"
"\n"
"")
        self.tabWidget_4 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_4.setGeometry(QtCore.QRect(20, 340, 1081, 431))
        self.tabWidget_4.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tw_listado_cuotas = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_listado_cuotas.setEnabled(False)
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
        self.gridLayout_3.addWidget(self.tw_listado_cuotas, 3, 0, 1, 1)
        self.boton_historial_cuota = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_historial_cuota.setMinimumSize(QtCore.QSize(0, 25))
        self.boton_historial_cuota.setMaximumSize(QtCore.QSize(16777215, 25))
        self.boton_historial_cuota.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.boton_historial_cuota.setObjectName("boton_historial_cuota")
        self.gridLayout_3.addWidget(self.boton_historial_cuota, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_4.addTab(self.tab_3, icon, "")
        self.tabWidget_5 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_5.setGeometry(QtCore.QRect(1110, 50, 321, 461))
        self.tabWidget_5.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setMinimumSize(QtCore.QSize(300, 20))
        self.label_3.setMaximumSize(QtCore.QSize(300, 20))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_8.addWidget(self.line_2, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.dte_fecha_cobro = QtWidgets.QDateEdit(self.tab_5)
        self.dte_fecha_cobro.setEnabled(False)
        self.dte_fecha_cobro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fecha_cobro.setCalendarPopup(True)
        self.dte_fecha_cobro.setObjectName("dte_fecha_cobro")
        self.horizontalLayout_3.addWidget(self.dte_fecha_cobro)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.cbx_estado = QtWidgets.QComboBox(self.tab_5)
        self.cbx_estado.setEnabled(False)
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
        self.horizontalLayout_4.addWidget(self.cbx_estado)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_8.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setEnabled(True)
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
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_10.addWidget(self.line_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.lne_nro_cuota = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_cuota.setEnabled(False)
        self.lne_nro_cuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font:  75 11Pt \"Century Schoolbook L\";")
        self.lne_nro_cuota.setObjectName("lne_nro_cuota")
        self.horizontalLayout_5.addWidget(self.lne_nro_cuota)
        self.gridLayout_10.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.lne_importe_cuota = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_cuota.setEnabled(False)
        self.lne_importe_cuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font:  75 11Pt \"Century Schoolbook L\";")
        self.lne_importe_cuota.setObjectName("lne_importe_cuota")
        self.horizontalLayout_6.addWidget(self.lne_importe_cuota)
        self.gridLayout_10.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lne_punitorios = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_punitorios.setEnabled(False)
        self.lne_punitorios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_punitorios.setObjectName("lne_punitorios")
        self.horizontalLayout_7.addWidget(self.lne_punitorios)
        self.gridLayout_10.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lne_descuento = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_descuento.setEnabled(False)
        self.lne_descuento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descuento.setObjectName("lne_descuento")
        self.horizontalLayout_8.addWidget(self.lne_descuento)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lne_saldo = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_saldo.setEnabled(False)
        self.lne_saldo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_saldo.setObjectName("lne_saldo")
        self.horizontalLayout_9.addWidget(self.lne_saldo)
        self.gridLayout_10.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setStyleSheet("color: rgb(170, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_10.addWidget(self.line, 7, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.lne_importe_cobrar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_cobrar.setEnabled(False)
        self.lne_importe_cobrar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"border-color: rgb(170, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"font:  75 12Pt \"Century Schoolbook L\";")
        self.lne_importe_cobrar.setText("")
        self.lne_importe_cobrar.setObjectName("lne_importe_cobrar")
        self.horizontalLayout_10.addWidget(self.lne_importe_cobrar)
        self.gridLayout_10.addLayout(self.horizontalLayout_10, 8, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.boton_pagar = QtWidgets.QPushButton(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_pagar.setFont(font)
        self.boton_pagar.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"")
        self.boton_pagar.setObjectName("boton_pagar")
        self.horizontalLayout_11.addWidget(self.boton_pagar)
        self.boton_limpiar = QtWidgets.QPushButton(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.boton_limpiar.setFont(font)
        self.boton_limpiar.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.horizontalLayout_11.addWidget(self.boton_limpiar, 0, QtCore.Qt.AlignRight)
        self.boton_ticket = QtWidgets.QPushButton(self.tab_5)
        self.boton_ticket.setStyleSheet("background-color: rgb(251, 209, 209);")
        self.boton_ticket.setObjectName("boton_ticket")
        self.horizontalLayout_11.addWidget(self.boton_ticket)
        self.boton_re_ticket = QtWidgets.QPushButton(self.tab_5)
        self.boton_re_ticket.setStyleSheet("background-color: rgb(251, 209, 209);")
        self.boton_re_ticket.setObjectName("boton_re_ticket")
        self.horizontalLayout_11.addWidget(self.boton_re_ticket)
        self.gridLayout_8.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_5.addTab(self.tab_5, icon1, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 80, 1081, 241))
        self.tabWidget_3.setStyleSheet("background-color: rgb(252, 249, 247);")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_lista_creditos = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_lista_creditos.setEnabled(False)
        self.tw_lista_creditos.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_lista_creditos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tw_lista_creditos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_lista_creditos.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tw_lista_creditos.setObjectName("tw_lista_creditos")
        self.tw_lista_creditos.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos.setHorizontalHeaderItem(9, item)
        self.tw_lista_creditos.horizontalHeader().setDefaultSectionSize(125)
        self.gridLayout.addWidget(self.tw_lista_creditos, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_4, icon2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(form_cuotas_pagar)
        self.tabWidget_2.setGeometry(QtCore.QRect(1110, 525, 321, 241))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lne_descripcion = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descripcion.setObjectName("lne_descripcion")
        self.verticalLayout.addWidget(self.lne_descripcion)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.lne_cant_cuotas = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_cant_cuotas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cant_cuotas.setObjectName("lne_cant_cuotas")
        self.verticalLayout_4.addWidget(self.lne_cant_cuotas)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lne_total_cuotas = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_total_cuotas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_total_cuotas.setObjectName("lne_total_cuotas")
        self.verticalLayout_3.addWidget(self.lne_total_cuotas)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.layoutWidget = QtWidgets.QWidget(form_cuotas_pagar)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 120, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lne_capital = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_capital.setEnabled(False)
        self.lne_capital.setMinimumSize(QtCore.QSize(20, 20))
        self.lne_capital.setMaximumSize(QtCore.QSize(2, 20))
        self.lne_capital.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_capital.setObjectName("lne_capital")
        self.horizontalLayout_2.addWidget(self.lne_capital)
        self.lne_interes = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_interes.setEnabled(False)
        self.lne_interes.setMinimumSize(QtCore.QSize(20, 20))
        self.lne_interes.setMaximumSize(QtCore.QSize(20, 20))
        self.lne_interes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_interes.setObjectName("lne_interes")
        self.horizontalLayout_2.addWidget(self.lne_interes)
        self.lne_gastos = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_gastos.setEnabled(False)
        self.lne_gastos.setMinimumSize(QtCore.QSize(20, 20))
        self.lne_gastos.setMaximumSize(QtCore.QSize(20, 20))
        self.lne_gastos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_gastos.setObjectName("lne_gastos")
        self.horizontalLayout_2.addWidget(self.lne_gastos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(form_cuotas_pagar)
        self.label.setGeometry(QtCore.QRect(780, 10, 29, 16))
        self.label.setObjectName("label")
        self.lne_dni = QtWidgets.QLineEdit(form_cuotas_pagar)
        self.lne_dni.setGeometry(QtCore.QRect(830, 10, 125, 24))
        self.lne_dni.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_dni.setObjectName("lne_dni")
        self.boton_buscar_creditos = QtWidgets.QPushButton(form_cuotas_pagar)
        self.boton_buscar_creditos.setGeometry(QtCore.QRect(970, 10, 80, 23))
        self.boton_buscar_creditos.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.boton_buscar_creditos.setObjectName("boton_buscar_creditos")
        self.lne_nom_ape = QtWidgets.QLineEdit(form_cuotas_pagar)
        self.lne_nom_ape.setGeometry(QtCore.QRect(40, 10, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lne_nom_ape.setFont(font)
        self.lne_nom_ape.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Ubuntu\";\n"
"")
        self.lne_nom_ape.setText("")
        self.lne_nom_ape.setObjectName("lne_nom_ape")
        self.label.raise_()
        self.lne_dni.raise_()
        self.boton_buscar_creditos.raise_()
        self.lne_nom_ape.raise_()
        self.layoutWidget.raise_()
        self.tabWidget_4.raise_()
        self.tabWidget_5.raise_()
        self.tabWidget_2.raise_()
        self.tabWidget_3.raise_()

        self.retranslateUi(form_cuotas_pagar)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
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
        QtCore.QMetaObject.connectSlotsByName(form_cuotas_pagar)
        form_cuotas_pagar.setTabOrder(self.lne_dni, self.boton_buscar_creditos)
        form_cuotas_pagar.setTabOrder(self.boton_buscar_creditos, self.lne_nom_ape)
        form_cuotas_pagar.setTabOrder(self.lne_nom_ape, self.tabWidget_3)
        form_cuotas_pagar.setTabOrder(self.tabWidget_3, self.tw_lista_creditos)
        form_cuotas_pagar.setTabOrder(self.tw_lista_creditos, self.lne_capital)
        form_cuotas_pagar.setTabOrder(self.lne_capital, self.tabWidget_4)
        form_cuotas_pagar.setTabOrder(self.tabWidget_4, self.tw_listado_cuotas)
        form_cuotas_pagar.setTabOrder(self.tw_listado_cuotas, self.tabWidget_5)
        form_cuotas_pagar.setTabOrder(self.tabWidget_5, self.dte_fecha_cobro)
        form_cuotas_pagar.setTabOrder(self.dte_fecha_cobro, self.cbx_estado)
        form_cuotas_pagar.setTabOrder(self.cbx_estado, self.lne_nro_cuota)
        form_cuotas_pagar.setTabOrder(self.lne_nro_cuota, self.lne_importe_cuota)
        form_cuotas_pagar.setTabOrder(self.lne_importe_cuota, self.lne_punitorios)
        form_cuotas_pagar.setTabOrder(self.lne_punitorios, self.lne_descuento)
        form_cuotas_pagar.setTabOrder(self.lne_descuento, self.lne_saldo)
        form_cuotas_pagar.setTabOrder(self.lne_saldo, self.lne_importe_cobrar)
        form_cuotas_pagar.setTabOrder(self.lne_importe_cobrar, self.boton_pagar)
        form_cuotas_pagar.setTabOrder(self.boton_pagar, self.boton_limpiar)
        form_cuotas_pagar.setTabOrder(self.boton_limpiar, self.tabWidget_2)
        form_cuotas_pagar.setTabOrder(self.tabWidget_2, self.lne_descripcion)

    def retranslateUi(self, form_cuotas_pagar):
        _translate = QtCore.QCoreApplication.translate
        form_cuotas_pagar.setWindowTitle(_translate("form_cuotas_pagar", "Cuotas Pagar"))
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
        self.boton_historial_cuota.setText(_translate("form_cuotas_pagar", "Historial de Cuota"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_3), _translate("form_cuotas_pagar", "Cuotas del Crédito"))
        self.label_3.setText(_translate("form_cuotas_pagar", "Información a editar por el Usuario : "))
        self.label_11.setText(_translate("form_cuotas_pagar", "Fecha de Cobro : "))
        self.dte_fecha_cobro.setDisplayFormat(_translate("form_cuotas_pagar", "dd/M/yyyy"))
        self.label_12.setText(_translate("form_cuotas_pagar", "Estado : "))
        self.cbx_estado.setItemText(0, _translate("form_cuotas_pagar", "Pagada"))
        self.cbx_estado.setItemText(1, _translate("form_cuotas_pagar", "Pago Parcial"))
        self.cbx_estado.setItemText(2, _translate("form_cuotas_pagar", "Vencida 30 días"))
        self.cbx_estado.setItemText(3, _translate("form_cuotas_pagar", "Vencida 60 días"))
        self.cbx_estado.setItemText(4, _translate("form_cuotas_pagar", "Vencida 90 días"))
        self.cbx_estado.setItemText(5, _translate("form_cuotas_pagar", "Vencida 120 días"))
        self.cbx_estado.setItemText(6, _translate("form_cuotas_pagar", "Vencida 150 días"))
        self.cbx_estado.setItemText(7, _translate("form_cuotas_pagar", "Vencida 180 días"))
        self.cbx_estado.setItemText(8, _translate("form_cuotas_pagar", "En Judiciales"))
        self.label_13.setText(_translate("form_cuotas_pagar", "Detalle importes a Cobrar : "))
        self.label_15.setText(_translate("form_cuotas_pagar", "Nro de Cuota: "))
        self.label_16.setText(_translate("form_cuotas_pagar", "Importe de Cuota: "))
        self.label_8.setText(_translate("form_cuotas_pagar", "Punitorios :"))
        self.label_17.setText(_translate("form_cuotas_pagar", "Descuentos : "))
        self.label_9.setText(_translate("form_cuotas_pagar", "Saldo:"))
        self.label_6.setText(_translate("form_cuotas_pagar", "Importe a cobrar :"))
        self.boton_pagar.setText(_translate("form_cuotas_pagar", "Pagar"))
        self.boton_limpiar.setText(_translate("form_cuotas_pagar", "Limpiar"))
        self.boton_ticket.setText(_translate("form_cuotas_pagar", "TICKET"))
        self.boton_re_ticket.setText(_translate("form_cuotas_pagar", "Re-Tickect"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_5), _translate("form_cuotas_pagar", "Pago de Cuota"))
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
        item = self.tw_lista_creditos.horizontalHeaderItem(6)
        item.setText(_translate("form_cuotas_pagar", "Bloqueado"))
        item = self.tw_lista_creditos.horizontalHeaderItem(7)
        item.setText(_translate("form_cuotas_pagar", "Formula"))
        item = self.tw_lista_creditos.horizontalHeaderItem(8)
        item.setText(_translate("form_cuotas_pagar", "Tipo Vencimiento"))
        item = self.tw_lista_creditos.horizontalHeaderItem(9)
        item.setText(_translate("form_cuotas_pagar", "Observaciones"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("form_cuotas_pagar", "Historial de Cŕeditos"))
        self.label_2.setText(_translate("form_cuotas_pagar", "Descripción: "))
        self.label_14.setText(_translate("form_cuotas_pagar", "Cantidad de Cuotas Seleccionadas : "))
        self.label_5.setText(_translate("form_cuotas_pagar", "Calculo total de Cuotas Seleccionadas : "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_cuotas_pagar", "Detalle de Cuotas Cobradas"))
        self.label.setText(_translate("form_cuotas_pagar", "DNI: "))
        self.boton_buscar_creditos.setText(_translate("form_cuotas_pagar", "Buscar"))

