# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_creditos_agregar_nuevos.ui'
#
# Created: Fri Feb 24 09:51:04 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_agregar_nuevos_creditos(object):
    def setupUi(self, form_agregar_nuevos_creditos):
        form_agregar_nuevos_creditos.setObjectName("form_agregar_nuevos_creditos")
        form_agregar_nuevos_creditos.resize(1299, 856)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_agregar_nuevos_creditos.sizePolicy().hasHeightForWidth())
        form_agregar_nuevos_creditos.setSizePolicy(sizePolicy)
        form_agregar_nuevos_creditos.setMinimumSize(QtCore.QSize(800, 450))
        form_agregar_nuevos_creditos.setMaximumSize(QtCore.QSize(1600, 856))
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
"font: 75 10pt \"KacstOne\";")
        self.gridLayout_14 = QtWidgets.QGridLayout(form_agregar_nuevos_creditos)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.tabWidget = QtWidgets.QTabWidget(form_agregar_nuevos_creditos)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(136, 3, 3, 100);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
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
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.lne_observaciones_creditonuevo = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_observaciones_creditonuevo.setEnabled(False)
        self.lne_observaciones_creditonuevo.setText("")
        self.lne_observaciones_creditonuevo.setObjectName("lne_observaciones_creditonuevo")
        self.horizontalLayout_3.addWidget(self.lne_observaciones_creditonuevo)
        self.gridLayout_12.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_3, 5, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.lne_nro_creditonuevo = QtWidgets.QLineEdit(self.groupBox_5)
        self.lne_nro_creditonuevo.setEnabled(False)
        self.lne_nro_creditonuevo.setText("")
        self.lne_nro_creditonuevo.setObjectName("lne_nro_creditonuevo")
        self.gridLayout_8.addWidget(self.lne_nro_creditonuevo, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 2, 1, 1)
        self.dte_fec_creditonuevo = QtWidgets.QDateEdit(self.groupBox_5)
        self.dte_fec_creditonuevo.setEnabled(False)
        self.dte_fec_creditonuevo.setCalendarPopup(True)
        self.dte_fec_creditonuevo.setDate(QtCore.QDate(2007, 7, 23))
        self.dte_fec_creditonuevo.setObjectName("dte_fec_creditonuevo")
        self.gridLayout_8.addWidget(self.dte_fec_creditonuevo, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 4, 1, 1)
        self.spbx_tasa_creditonuevo = QtWidgets.QSpinBox(self.groupBox_5)
        self.spbx_tasa_creditonuevo.setEnabled(False)
        self.spbx_tasa_creditonuevo.setProperty("value", 8)
        self.spbx_tasa_creditonuevo.setObjectName("spbx_tasa_creditonuevo")
        self.gridLayout_8.addWidget(self.spbx_tasa_creditonuevo, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 7, 1, 1)
        self.cbx_formula_creditonuevo = QtWidgets.QComboBox(self.groupBox_5)
        self.cbx_formula_creditonuevo.setEnabled(False)
        self.cbx_formula_creditonuevo.setObjectName("cbx_formula_creditonuevo")
        self.cbx_formula_creditonuevo.addItem("")
        self.gridLayout_8.addWidget(self.cbx_formula_creditonuevo, 0, 8, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_13.addWidget(self.label_13, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
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
"\n"
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.boton_imprimir = QtWidgets.QPushButton(self.groupBox_2)
        self.boton_imprimir.setObjectName("boton_imprimir")
        self.gridLayout_3.addWidget(self.boton_imprimir, 2, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.lne_interes_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_interes_creditonuevo.setEnabled(False)
        self.lne_interes_creditonuevo.setText("")
        self.lne_interes_creditonuevo.setObjectName("lne_interes_creditonuevo")
        self.verticalLayout.addWidget(self.lne_interes_creditonuevo)
        self.gridLayout_11.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.lne_gastos_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_gastos_creditonuevo.setEnabled(False)
        self.lne_gastos_creditonuevo.setText("")
        self.lne_gastos_creditonuevo.setObjectName("lne_gastos_creditonuevo")
        self.verticalLayout_2.addWidget(self.lne_gastos_creditonuevo)
        self.gridLayout_11.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.lne_credito_total_creditonuevo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_credito_total_creditonuevo.setEnabled(False)
        self.lne_credito_total_creditonuevo.setText("")
        self.lne_credito_total_creditonuevo.setObjectName("lne_credito_total_creditonuevo")
        self.verticalLayout_3.addWidget(self.lne_credito_total_creditonuevo)
        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.tw_lista_cuotas_creditonuevo = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_lista_cuotas_creditonuevo.setEnabled(False)
        self.tw_lista_cuotas_creditonuevo.setMinimumSize(QtCore.QSize(0, 250))
        self.tw_lista_cuotas_creditonuevo.setMaximumSize(QtCore.QSize(16777215, 250))
        self.tw_lista_cuotas_creditonuevo.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_lista_cuotas_creditonuevo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tw_lista_cuotas_creditonuevo.horizontalHeader().setDefaultSectionSize(130)
        self.gridLayout_3.addWidget(self.tw_lista_cuotas_creditonuevo, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_4, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
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
"\n"
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
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lne_nro_doc_creditonuevo = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc_creditonuevo.setText("")
        self.lne_nro_doc_creditonuevo.setObjectName("lne_nro_doc_creditonuevo")
        self.horizontalLayout_2.addWidget(self.lne_nro_doc_creditonuevo)
        self.boton_buscar_cliente_creditonuevo = QtWidgets.QPushButton(self.groupBox)
        self.boton_buscar_cliente_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"}\n"
"")
        self.boton_buscar_cliente_creditonuevo.setObjectName("boton_buscar_cliente_creditonuevo")
        self.horizontalLayout_2.addWidget(self.boton_buscar_cliente_creditonuevo)
        self.lne_nom_ape = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nom_ape.setObjectName("lne_nom_ape")
        self.horizontalLayout_2.addWidget(self.lne_nom_ape)
        self.lne_nro_creditonuevo_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_creditonuevo_2.setEnabled(False)
        self.lne_nro_creditonuevo_2.setText("")
        self.lne_nro_creditonuevo_2.setObjectName("lne_nro_creditonuevo_2")
        self.horizontalLayout_2.addWidget(self.lne_nro_creditonuevo_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)
        self.lne_importe_prestamo_creditonuevo = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_importe_prestamo_creditonuevo.setEnabled(False)
        self.lne_importe_prestamo_creditonuevo.setObjectName("lne_importe_prestamo_creditonuevo")
        self.gridLayout_9.addWidget(self.lne_importe_prestamo_creditonuevo, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 2, 1, 1)
        self.spbx_cantidad_cuotas_creditonuevo = QtWidgets.QSpinBox(self.groupBox_4)
        self.spbx_cantidad_cuotas_creditonuevo.setEnabled(False)
        self.spbx_cantidad_cuotas_creditonuevo.setProperty("value", 3)
        self.spbx_cantidad_cuotas_creditonuevo.setObjectName("spbx_cantidad_cuotas_creditonuevo")
        self.gridLayout_9.addWidget(self.spbx_cantidad_cuotas_creditonuevo, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)
        self.dte_vto_primer_cuota_creditonuevo = QtWidgets.QDateEdit(self.groupBox_4)
        self.dte_vto_primer_cuota_creditonuevo.setEnabled(False)
        self.dte_vto_primer_cuota_creditonuevo.setTime(QtCore.QTime(0, 0, 0))
        self.dte_vto_primer_cuota_creditonuevo.setCalendarPopup(True)
        self.dte_vto_primer_cuota_creditonuevo.setDate(QtCore.QDate(2000, 7, 31))
        self.dte_vto_primer_cuota_creditonuevo.setObjectName("dte_vto_primer_cuota_creditonuevo")
        self.gridLayout_10.addWidget(self.dte_vto_primer_cuota_creditonuevo, 0, 1, 1, 1)
        self.boton_generar_creditonuevo = QtWidgets.QPushButton(self.groupBox_4)
        self.boton_generar_creditonuevo.setEnabled(False)
        self.boton_generar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"}\n"
"")
        self.boton_generar_creditonuevo.setObjectName("boton_generar_creditonuevo")
        self.gridLayout_10.addWidget(self.boton_generar_creditonuevo, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_4, 3, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Descargas/Íconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
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
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(75, 25))
        self.label_17.setMaximumSize(QtCore.QSize(75, 25))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.cbx_garante_creditonuevo = QtWidgets.QComboBox(self.groupBox_6)
        self.cbx_garante_creditonuevo.setObjectName("cbx_garante_creditonuevo")
        self.horizontalLayout_8.addWidget(self.cbx_garante_creditonuevo)
        self.gridLayout_15.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.cbx_tipo_garante_creditonuevo = QtWidgets.QComboBox(self.groupBox_6)
        self.cbx_tipo_garante_creditonuevo.setObjectName("cbx_tipo_garante_creditonuevo")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.cbx_tipo_garante_creditonuevo.addItem("")
        self.horizontalLayout_9.addWidget(self.cbx_tipo_garante_creditonuevo)
        self.boton_agregar = QtWidgets.QPushButton(self.groupBox_6)
        self.boton_agregar.setEnabled(False)
        self.boton_agregar.setStyleSheet("background-color: rgb(253, 194, 179);\n"
"")
        self.boton_agregar.setObjectName("boton_agregar")
        self.horizontalLayout_9.addWidget(self.boton_agregar)
        self.gridLayout_15.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tw_garantes_lista_creditonuevo = QtWidgets.QTableWidget(self.groupBox_7)
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
        self.gridLayout_5.addWidget(self.tw_garantes_lista_creditonuevo, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.boton_limpiar = QtWidgets.QPushButton(self.tab_3)
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.gridLayout_16.addWidget(self.boton_limpiar, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lne_party_party = QtWidgets.QLineEdit(self.tab)
        self.lne_party_party.setMinimumSize(QtCore.QSize(50, 22))
        self.lne_party_party.setMaximumSize(QtCore.QSize(50, 22))
        self.lne_party_party.setObjectName("lne_party_party")
        self.horizontalLayout_7.addWidget(self.lne_party_party)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boton_limpiar_creditonuevo = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar_creditonuevo.setEnabled(False)
        self.boton_limpiar_creditonuevo.setMinimumSize(QtCore.QSize(100, 22))
        self.boton_limpiar_creditonuevo.setMaximumSize(QtCore.QSize(100, 22))
        self.boton_limpiar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"font: 10pt \"KacstOne\";\n"
"}")
        self.boton_limpiar_creditonuevo.setObjectName("boton_limpiar_creditonuevo")
        self.horizontalLayout.addWidget(self.boton_limpiar_creditonuevo)
        self.boton_grabar_creditonuevo = QtWidgets.QPushButton(self.tab)
        self.boton_grabar_creditonuevo.setEnabled(False)
        self.boton_grabar_creditonuevo.setMinimumSize(QtCore.QSize(100, 22))
        self.boton_grabar_creditonuevo.setMaximumSize(QtCore.QSize(100, 22))
        self.boton_grabar_creditonuevo.setStyleSheet("QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"font: 10pt \"KacstOne\";\n"
"}")
        self.boton_grabar_creditonuevo.setObjectName("boton_grabar_creditonuevo")
        self.horizontalLayout.addWidget(self.boton_grabar_creditonuevo)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.gridLayout_6.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Descargas/Íconos/icon(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.gridLayout_14.addWidget(self.tabWidget, 0, 0, 1, 1)

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
        form_agregar_nuevos_creditos.setTabOrder(self.tabWidget, self.tabWidget_2)
        form_agregar_nuevos_creditos.setTabOrder(self.tabWidget_2, self.lne_nro_doc_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_doc_creditonuevo, self.boton_buscar_cliente_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_buscar_cliente_creditonuevo, self.lne_nom_ape)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nom_ape, self.lne_nro_creditonuevo_2)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_creditonuevo_2, self.lne_nro_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_nro_creditonuevo, self.dte_fec_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.dte_fec_creditonuevo, self.spbx_tasa_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.spbx_tasa_creditonuevo, self.cbx_formula_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_formula_creditonuevo, self.lne_importe_prestamo_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_importe_prestamo_creditonuevo, self.spbx_cantidad_cuotas_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.spbx_cantidad_cuotas_creditonuevo, self.dte_vto_primer_cuota_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.dte_vto_primer_cuota_creditonuevo, self.boton_generar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_generar_creditonuevo, self.tw_lista_cuotas_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.tw_lista_cuotas_creditonuevo, self.lne_interes_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_interes_creditonuevo, self.lne_gastos_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_gastos_creditonuevo, self.lne_credito_total_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_credito_total_creditonuevo, self.boton_imprimir)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_imprimir, self.lne_observaciones_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_observaciones_creditonuevo, self.cbx_garante_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_garante_creditonuevo, self.cbx_tipo_garante_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.cbx_tipo_garante_creditonuevo, self.boton_agregar)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_agregar, self.tw_garantes_lista_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.tw_garantes_lista_creditonuevo, self.lne_party_party)
        form_agregar_nuevos_creditos.setTabOrder(self.lne_party_party, self.boton_limpiar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_limpiar_creditonuevo, self.boton_grabar_creditonuevo)
        form_agregar_nuevos_creditos.setTabOrder(self.boton_grabar_creditonuevo, self.boton_limpiar)

    def retranslateUi(self, form_agregar_nuevos_creditos):
        _translate = QtCore.QCoreApplication.translate
        form_agregar_nuevos_creditos.setWindowTitle(_translate("form_agregar_nuevos_creditos", "Créditos"))
        self.label_18.setText(_translate("form_agregar_nuevos_creditos", "Observaciones:"))
        self.label_2.setText(_translate("form_agregar_nuevos_creditos", "Credito N°:"))
        self.label_3.setText(_translate("form_agregar_nuevos_creditos", "Fecha de credito:"))
        self.dte_fec_creditonuevo.setDisplayFormat(_translate("form_agregar_nuevos_creditos", "dd/MM/yyyy"))
        self.label_4.setText(_translate("form_agregar_nuevos_creditos", "Tasa:"))
        self.label_5.setText(_translate("form_agregar_nuevos_creditos", "%"))
        self.label_6.setText(_translate("form_agregar_nuevos_creditos", "Formula:"))
        self.cbx_formula_creditonuevo.setItemText(0, _translate("form_agregar_nuevos_creditos", "Simple"))
        self.label_13.setText(_translate("form_agregar_nuevos_creditos", "Seleccione el cliente al cual le otorgaremos el crédito : "))
        self.label_9.setText(_translate("form_agregar_nuevos_creditos", "Lista de cuotas del nuevo credito"))
        self.boton_imprimir.setText(_translate("form_agregar_nuevos_creditos", "Imprimir"))
        self.label_11.setText(_translate("form_agregar_nuevos_creditos", "Interes $:"))
        self.label_12.setText(_translate("form_agregar_nuevos_creditos", "Gastos $:"))
        self.label_15.setText(_translate("form_agregar_nuevos_creditos", "Credito total $:"))
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
        self.label.setText(_translate("form_agregar_nuevos_creditos", "DNI: "))
        self.boton_buscar_cliente_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Buscar"))
        self.label_7.setText(_translate("form_agregar_nuevos_creditos", "Importe del prestamo $:"))
        self.lne_importe_prestamo_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "1000"))
        self.label_8.setText(_translate("form_agregar_nuevos_creditos", "Cantidad de cuotas:"))
        self.label_10.setText(_translate("form_agregar_nuevos_creditos", "Vencimiento de la primera cuota:"))
        self.dte_vto_primer_cuota_creditonuevo.setDisplayFormat(_translate("form_agregar_nuevos_creditos", "dd/MM/yyyy"))
        self.boton_generar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Generar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_agregar_nuevos_creditos", "Nuevo Crédito"))
        self.label_17.setText(_translate("form_agregar_nuevos_creditos", "Garante : "))
        self.label_24.setText(_translate("form_agregar_nuevos_creditos", "Tipo Garante :"))
        self.cbx_tipo_garante_creditonuevo.setItemText(0, _translate("form_agregar_nuevos_creditos", "Garante Principal"))
        self.cbx_tipo_garante_creditonuevo.setItemText(1, _translate("form_agregar_nuevos_creditos", "Garante Secundario"))
        self.cbx_tipo_garante_creditonuevo.setItemText(2, _translate("form_agregar_nuevos_creditos", "Otro Garante"))
        self.boton_agregar.setText(_translate("form_agregar_nuevos_creditos", "Agregar"))
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
        self.boton_limpiar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Limpiar"))
        self.boton_grabar_creditonuevo.setText(_translate("form_agregar_nuevos_creditos", "Grabar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_agregar_nuevos_creditos", "Créditos"))
