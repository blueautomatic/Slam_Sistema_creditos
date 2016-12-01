# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_creditos_agregar_nuevos.ui'
#
# Created: Mon Nov 14 11:21:19 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_agregar_nuevos_creditos(object):
    def setupUi(self, form_agregar_nuevos_creditos):
        form_agregar_nuevos_creditos.setObjectName("form_agregar_nuevos_creditos")
        form_agregar_nuevos_creditos.resize(1109, 820)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 207, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        form_agregar_nuevos_creditos.setPalette(palette)
        form_agregar_nuevos_creditos.setMouseTracking(False)
        form_agregar_nuevos_creditos.setStyleSheet("selection-background-color: rgb(218, 175, 158);\n"
"selection-color: rgb(0, 0, 0);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(form_agregar_nuevos_creditos)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1081, 671))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1051, 591))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 1011, 61))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
        self.label.setGeometry(QtCore.QRect(10, 24, 41, 16))
        self.label.setObjectName("label")
        self.lne_nro_doc_creditonuevo = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc_creditonuevo.setGeometry(QtCore.QRect(60, 20, 141, 20))
        self.lne_nro_doc_creditonuevo.setText("")
        self.lne_nro_doc_creditonuevo.setObjectName("lne_nro_doc_creditonuevo")
        self.boton_buscar_cliente_creditonuevo = QtWidgets.QPushButton(self.groupBox)
        self.boton_buscar_cliente_creditonuevo.setGeometry(QtCore.QRect(210, 20, 51, 23))
        self.boton_buscar_cliente_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"}\n"
"")
        self.boton_buscar_cliente_creditonuevo.setObjectName("boton_buscar_cliente_creditonuevo")
        self.lne_nro_creditonuevo_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_creditonuevo_2.setEnabled(False)
        self.lne_nro_creditonuevo_2.setGeometry(QtCore.QRect(660, 20, 41, 20))
        self.lne_nro_creditonuevo_2.setText("")
        self.lne_nro_creditonuevo_2.setObjectName("lne_nro_creditonuevo_2")
        self.lne_nom_ape = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nom_ape.setGeometry(QtCore.QRect(330, 20, 291, 23))
        self.lne_nom_ape.setObjectName("lne_nom_ape")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(24, 274, 1011, 281))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setMouseTracking(False)
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tw_lista_cuotas_creditonuevo = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_lista_cuotas_creditonuevo.setEnabled(False)
        self.tw_lista_cuotas_creditonuevo.setGeometry(QtCore.QRect(40, 9, 951, 201))
        self.tw_lista_cuotas_creditonuevo.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
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
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(37, 220, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(137, 220, 61, 16))
        self.label_12.setObjectName("label_12")
        self.lne_interes_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_interes_creditonuevo.setEnabled(False)
        self.lne_interes_creditonuevo.setGeometry(QtCore.QRect(37, 240, 81, 16))
        self.lne_interes_creditonuevo.setText("")
        self.lne_interes_creditonuevo.setObjectName("lne_interes_creditonuevo")
        self.lne_gastos_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_gastos_creditonuevo.setEnabled(False)
        self.lne_gastos_creditonuevo.setGeometry(QtCore.QRect(137, 240, 81, 16))
        self.lne_gastos_creditonuevo.setText("")
        self.lne_gastos_creditonuevo.setObjectName("lne_gastos_creditonuevo")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(530, 220, 91, 20))
        self.label_15.setObjectName("label_15")
        self.lne_credito_total_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_credito_total_creditonuevo.setEnabled(False)
        self.lne_credito_total_creditonuevo.setGeometry(QtCore.QRect(530, 240, 111, 21))
        self.lne_credito_total_creditonuevo.setText("")
        self.lne_credito_total_creditonuevo.setObjectName("lne_credito_total_creditonuevo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(24, 580, 1011, 51))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label_18.setObjectName("label_18")
        self.lne_observaciones_creditonuevo = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_observaciones_creditonuevo.setEnabled(False)
        self.lne_observaciones_creditonuevo.setGeometry(QtCore.QRect(140, 10, 851, 31))
        self.lne_observaciones_creditonuevo.setText("")
        self.lne_observaciones_creditonuevo.setObjectName("lne_observaciones_creditonuevo")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(34, 253, 281, 16))
        self.label_9.setObjectName("label_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(23, 159, 1011, 91))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.boton_generar_creditonuevo = QtWidgets.QPushButton(self.groupBox_4)
        self.boton_generar_creditonuevo.setEnabled(False)
        self.boton_generar_creditonuevo.setGeometry(QtCore.QRect(523, 54, 61, 23))
        self.boton_generar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"}\n"
"")
        self.boton_generar_creditonuevo.setObjectName("boton_generar_creditonuevo")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(23, 54, 221, 20))
        self.label_10.setObjectName("label_10")
        self.dte_vto_primer_cuota_creditonuevo = QtWidgets.QDateEdit(self.groupBox_4)
        self.dte_vto_primer_cuota_creditonuevo.setEnabled(False)
        self.dte_vto_primer_cuota_creditonuevo.setGeometry(QtCore.QRect(249, 50, 121, 24))
        self.dte_vto_primer_cuota_creditonuevo.setTime(QtCore.QTime(0, 0, 0))
        self.dte_vto_primer_cuota_creditonuevo.setCalendarPopup(True)
        self.dte_vto_primer_cuota_creditonuevo.setDate(QtCore.QDate(2000, 7, 31))
        self.dte_vto_primer_cuota_creditonuevo.setObjectName("dte_vto_primer_cuota_creditonuevo")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(289, 18, 131, 16))
        self.label_8.setObjectName("label_8")
        self.lne_importe_prestamo_creditonuevo = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_prestamo_creditonuevo.setEnabled(False)
        self.lne_importe_prestamo_creditonuevo.setGeometry(QtCore.QRect(173, 14, 81, 20))
        self.lne_importe_prestamo_creditonuevo.setObjectName("lne_importe_prestamo_creditonuevo")
        self.spbx_cantidad_cuotas_creditonuevo = QtWidgets.QSpinBox(self.groupBox_4)
        self.spbx_cantidad_cuotas_creditonuevo.setEnabled(False)
        self.spbx_cantidad_cuotas_creditonuevo.setGeometry(QtCore.QRect(434, 14, 47, 24))
        self.spbx_cantidad_cuotas_creditonuevo.setProperty("value", 3)
        self.spbx_cantidad_cuotas_creditonuevo.setObjectName("spbx_cantidad_cuotas_creditonuevo")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(13, 14, 151, 21))
        self.label_7.setObjectName("label_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(23, 101, 1011, 51))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(514, 16, 21, 20))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(539, 16, 59, 21))
        self.label_6.setObjectName("label_6")
        self.dte_fec_creditonuevo = QtWidgets.QDateEdit(self.groupBox_5)
        self.dte_fec_creditonuevo.setEnabled(False)
        self.dte_fec_creditonuevo.setGeometry(QtCore.QRect(309, 15, 101, 24))
        self.dte_fec_creditonuevo.setCalendarPopup(True)
        self.dte_fec_creditonuevo.setDate(QtCore.QDate(2007, 7, 23))
        self.dte_fec_creditonuevo.setObjectName("dte_fec_creditonuevo")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(199, 16, 111, 21))
        self.label_3.setObjectName("label_3")
        self.cbx_formula_creditonuevo = QtWidgets.QComboBox(self.groupBox_5)
        self.cbx_formula_creditonuevo.setEnabled(False)
        self.cbx_formula_creditonuevo.setGeometry(QtCore.QRect(599, 19, 79, 20))
        self.cbx_formula_creditonuevo.setObjectName("cbx_formula_creditonuevo")
        self.cbx_formula_creditonuevo.addItem("")
        self.spbx_tasa_creditonuevo = QtWidgets.QSpinBox(self.groupBox_5)
        self.spbx_tasa_creditonuevo.setEnabled(False)
        self.spbx_tasa_creditonuevo.setGeometry(QtCore.QRect(459, 16, 47, 24))
        self.spbx_tasa_creditonuevo.setProperty("value", 8)
        self.spbx_tasa_creditonuevo.setObjectName("spbx_tasa_creditonuevo")
        self.lne_nro_creditonuevo = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_nro_creditonuevo.setEnabled(False)
        self.lne_nro_creditonuevo.setGeometry(QtCore.QRect(147, 17, 41, 20))
        self.lne_nro_creditonuevo.setText("")
        self.lne_nro_creditonuevo.setObjectName("lne_nro_creditonuevo")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(419, 16, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 391, 16))
        self.label_13.setObjectName("label_13")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Descargas/Íconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(8, 22, 751, 111))
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
"")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.boton_agregar = QtWidgets.QPushButton(self.groupBox_6)
        self.boton_agregar.setEnabled(False)
        self.boton_agregar.setGeometry(QtCore.QRect(582, 71, 80, 23))
        self.boton_agregar.setStyleSheet("background-color: rgb(253, 194, 179);\n"
"")
        self.boton_agregar.setObjectName("boton_agregar")
        self.cbx_garante_creditonuevo = QtWidgets.QComboBox(self.groupBox_6)
        self.cbx_garante_creditonuevo.setGeometry(QtCore.QRect(194, 18, 471, 23))
        self.cbx_garante_creditonuevo.setObjectName("cbx_garante_creditonuevo")
        self.cbx_tipo_garante_creditonuevo = QtWidgets.QComboBox(self.groupBox_6)
        self.cbx_tipo_garante_creditonuevo.setGeometry(QtCore.QRect(196, 50, 181, 23))
        self.cbx_tipo_garante_creditonuevo.setObjectName("cbx_tipo_garante_creditonuevo")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(70, 22, 81, 16))
        self.label_17.setObjectName("label_17")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(67, 54, 101, 16))
        self.label_24.setObjectName("label_24")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(8, 160, 751, 221))
        self.groupBox_7.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
"")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.tw_garantes_lista_creditonuevo = QtWidgets.QTableWidget(self.groupBox_7)
        self.tw_garantes_lista_creditonuevo.setGeometry(QtCore.QRect(20, 40, 711, 101))
        self.tw_garantes_lista_creditonuevo.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_garantes_lista_creditonuevo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_garantes_lista_creditonuevo.setRowCount(0)
        self.tw_garantes_lista_creditonuevo.setColumnCount(5)
        self.tw_garantes_lista_creditonuevo.setObjectName("tw_garantes_lista_creditonuevo")
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_creditonuevo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_creditonuevo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_creditonuevo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_creditonuevo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_creditonuevo.setHorizontalHeaderItem(4, item)
        self.tw_garantes_lista_creditonuevo.horizontalHeader().setDefaultSectionSize(175)
        self.boton_limpiar = QtWidgets.QPushButton(self.tab_3)
        self.boton_limpiar.setGeometry(QtCore.QRect(680, 390, 80, 23))
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.boton_grabar_creditonuevo = QtWidgets.QPushButton(self.tab)
        self.boton_grabar_creditonuevo.setEnabled(False)
        self.boton_grabar_creditonuevo.setGeometry(QtCore.QRect(790, 610, 91, 23))
        self.boton_grabar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"font: 10pt \"KacstOne\";\n"
"}")
        self.boton_grabar_creditonuevo.setObjectName("boton_grabar_creditonuevo")
        self.boton_limpiar_creditonuevo = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar_creditonuevo.setEnabled(False)
        self.boton_limpiar_creditonuevo.setGeometry(QtCore.QRect(692, 610, 80, 23))
        self.boton_limpiar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"font: 10pt \"KacstOne\";\n"
"}")
        self.boton_limpiar_creditonuevo.setObjectName("boton_limpiar_creditonuevo")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Descargas/Íconos/icon(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")

        self.retranslateUi(form_agregar_nuevos_creditos)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_nro_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_importe_prestamo_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_nro_doc_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_nro_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_interes_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_gastos_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_credito_total_creditonuevo.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_nom_ape.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_nro_creditonuevo_2.clear)
        self.boton_limpiar_creditonuevo.clicked.connect(self.lne_observaciones_creditonuevo.clear)
        QtCore.QMetaObject.connectSlotsByName(form_agregar_nuevos_creditos)
        form_agregar_nuevos_creditos.setTabOrder(self.tabWidget_2, self.lne_nro_creditonuevo_2)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_creditonuevo_2, self.lne_nro_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_creditonuevo, self.lne_nro_doc_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_doc_creditonuevo, self.boton_buscar_cliente_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_buscar_cliente_creditonuevo, self.dte_fec_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.dte_fec_creditonuevo, self.lne_importe_prestamo_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_importe_prestamo_creditonuevo, self.spbx_cantidad_cuotas_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.spbx_cantidad_cuotas_creditonuevo, self.dte_vto_primer_cuota_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.dte_vto_primer_cuota_creditonuevo, self.boton_generar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_generar_creditonuevo, self.cbx_garante_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_garante_creditonuevo, self.cbx_tipo_garante_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_tipo_garante_creditonuevo, self.boton_agregar)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_agregar, self.boton_limpiar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_limpiar_creditonuevo, self.boton_grabar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_grabar_creditonuevo, self.spbx_tasa_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.spbx_tasa_creditonuevo, self.tw_lista_cuotas_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.tw_lista_cuotas_creditonuevo, self.lne_observaciones_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_observaciones_creditonuevo, self.lne_gastos_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_gastos_creditonuevo, self.lne_credito_total_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_credito_total_creditonuevo, self.tw_garantes_lista_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.tw_garantes_lista_creditonuevo, self.lne_interes_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_interes_creditonuevo, self.cbx_formula_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_formula_creditonuevo, self.tabWidget)
        form_agregar_nuevos_creditos.setTabOrder(self.tabWidget, self.lne_nom_ape)

    def retranslateUi(self, form_agregar_nuevos_creditos):
        _translate = QtCore.QCoreApplication.translate
        form_agregar_nuevos_creditos.setWindowTitle(_translate("form_agregar_nuevos_creditos", "Créditos"))
        self.label.setText(_translate("form_agregar_nuevos_creditos", "DNI: "))
        self.boton_buscar_cliente_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Buscar"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(0)
        item.setText(_translate("form_agregar_nuevos_creditos", "N° Cuota "))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(1)
        item.setText(_translate("form_agregar_nuevos_creditos", "Capital"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(2)
        item.setText(_translate("form_agregar_nuevos_creditos", "Interés"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(3)
        item.setText(_translate("form_agregar_nuevos_creditos", "Gastos"))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(4)
        item.setText(_translate("form_agregar_nuevos_creditos", "1er Venc."))
        item = self.tw_lista_cuotas_creditonuevo.horizontalHeaderItem(5)
        item.setText(_translate("form_agregar_nuevos_creditos", "Importe 1er Venc."))
        self.label_11.setText(_translate("form_agregar_nuevos_creditos", "Interes $:"))
        self.label_12.setText(_translate("form_agregar_nuevos_creditos", "Gastos $:"))
        self.label_15.setText(_translate("form_agregar_nuevos_creditos", "Credito total $:"))
        self.label_18.setText(_translate("form_agregar_nuevos_creditos", "Observaciones:"))
        self.label_9.setText(_translate("form_agregar_nuevos_creditos", "Lista de cuotas del nuevo credito"))
        self.boton_generar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Generar"))
        self.label_10.setText(_translate("form_agregar_nuevos_creditos", "Vencimiento de la primera cuota:"))
        self.dte_vto_primer_cuota_creditonuevo.setDisplayFormat(_translate("form_agregar_nuevos_creditos", "dd/M/yyyy"))
        self.label_8.setText(_translate("form_agregar_nuevos_creditos", "Cantidad de cuotas:"))
        self.lne_importe_prestamo_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "1000"))
        self.label_7.setText(_translate("form_agregar_nuevos_creditos", "Importe del prestamo $:"))
        self.label_5.setText(_translate("form_agregar_nuevos_creditos", "%"))
        self.label_2.setText(_translate("form_agregar_nuevos_creditos", "Credito N°:"))
        self.label_6.setText(_translate("form_agregar_nuevos_creditos", "Formula:"))
        self.dte_fec_creditonuevo.setDisplayFormat(_translate("form_agregar_nuevos_creditos", "dd/M/yyyy"))
        self.label_3.setText(_translate("form_agregar_nuevos_creditos", "Fecha de credito:"))
        self.cbx_formula_creditonuevo.setItemText(0, _translate("form_agregar_nuevos_creditos", "Simple"))
        self.label_4.setText(_translate("form_agregar_nuevos_creditos", "Tasa:"))
        self.label_13.setText(_translate("form_agregar_nuevos_creditos", "Seleccione el cliente al cual le otorgaremos el crédito : "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_agregar_nuevos_creditos", "Nuevo Crédito"))
        self.boton_agregar.setText(_translate("form_agregar_nuevos_creditos", "Agregar"))
        self.cbx_tipo_garante_creditonuevo.setItemText(0, _translate("form_agregar_nuevos_creditos", "Garante Principal"))
        self.cbx_tipo_garante_creditonuevo.setItemText(1, _translate("form_agregar_nuevos_creditos", "Garante Secundario"))
        self.cbx_tipo_garante_creditonuevo.setItemText(2, _translate("form_agregar_nuevos_creditos", "Otro Garante"))
        self.label_17.setText(_translate("form_agregar_nuevos_creditos", "Garante : "))
        self.label_24.setText(_translate("form_agregar_nuevos_creditos", "Tipo Garante :"))
        item = self.tw_garantes_lista_creditonuevo.horizontalHeaderItem(0)
        item.setText(_translate("form_agregar_nuevos_creditos", "id"))
        item = self.tw_garantes_lista_creditonuevo.horizontalHeaderItem(1)
        item.setText(_translate("form_agregar_nuevos_creditos", "Nombre"))
        item = self.tw_garantes_lista_creditonuevo.horizontalHeaderItem(2)
        item.setText(_translate("form_agregar_nuevos_creditos", "Apellido"))
        item = self.tw_garantes_lista_creditonuevo.horizontalHeaderItem(3)
        item.setText(_translate("form_agregar_nuevos_creditos", "DNI"))
        item = self.tw_garantes_lista_creditonuevo.horizontalHeaderItem(4)
        item.setText(_translate("form_agregar_nuevos_creditos", "Tipo garante"))
        self.boton_limpiar.setText(_translate("form_agregar_nuevos_creditos", "Limpiar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("form_agregar_nuevos_creditos", "Garantes del Crédito"))
        self.boton_grabar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Grabar"))
        self.boton_limpiar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_agregar_nuevos_creditos", "Créditos"))

