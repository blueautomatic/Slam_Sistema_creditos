# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuotas_pagar_administrador.ui'
#
# Created: Thu Sep 29 11:55:53 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1001, 721)
        Form.setStyleSheet("selection-background-color: rgb(222, 222, 222);\n"
"selection-color: rgb(0, 0, 0);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
"background-color: rgb(172, 55, 26);\n"
"")
        self.tabWidget_4 = QtWidgets.QTabWidget(Form)
        self.tabWidget_4.setGeometry(QtCore.QRect(21, 261, 651, 441))
        self.tabWidget_4.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  10pt \"KacstOne\";\n"
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
        self.groupBox_3.setGeometry(QtCore.QRect(8, 10, 631, 391))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tw_listado_cuotas_cuotas_buscar = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_listado_cuotas_cuotas_buscar.setEnabled(True)
        self.tw_listado_cuotas_cuotas_buscar.setGeometry(QtCore.QRect(10, 15, 611, 361))
        self.tw_listado_cuotas_cuotas_buscar.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_listado_cuotas_cuotas_buscar.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tw_listado_cuotas_cuotas_buscar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_listado_cuotas_cuotas_buscar.setObjectName("tw_listado_cuotas_cuotas_buscar")
        self.tw_listado_cuotas_cuotas_buscar.setColumnCount(16)
        self.tw_listado_cuotas_cuotas_buscar.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_listado_cuotas_cuotas_buscar.setItem(5, 2, item)
        self.tw_listado_cuotas_cuotas_buscar.horizontalHeader().setDefaultSectionSize(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_4.addTab(self.tab_3, icon, "")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(424, 62, 551, 41))
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
        self.label.setGeometry(QtCore.QRect(15, 11, 41, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 11, 81, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(303, 10, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(470, 10, 61, 20))
        self.pushButton.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget_5 = QtWidgets.QTabWidget(Form)
        self.tabWidget_5.setEnabled(True)
        self.tabWidget_5.setGeometry(QtCore.QRect(684, 260, 291, 441))
        self.tabWidget_5.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  10pt \"KacstOne\";\n"
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
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 271, 261))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(37, 50, 57, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(143, 49, 81, 19))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(37, 74, 48, 18))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(143, 74, 81, 18))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(17, 220, 121, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(143, 98, 81, 18))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(37, 122, 52, 18))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(143, 122, 81, 18))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(37, 146, 64, 18))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(143, 146, 81, 18))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(143, 170, 81, 18))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(37, 170, 75, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(37, 98, 57, 18))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(143, 220, 81, 19))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(21, 200, 231, 20))
        self.line.setStyleSheet("color: rgb(170, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(10, 24, 231, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_5)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setGeometry(QtCore.QRect(137, 52, 101, 21))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.line_2 = QtWidgets.QFrame(self.tab_5)
        self.line_2.setGeometry(QtCore.QRect(2, 34, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(97, 79, 141, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(15, 53, 111, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(16, 79, 57, 18))
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(11, 9, 241, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(154, 380, 61, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"font: 10pt \"KacstOne\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 380, 61, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(252, 188, 188);\n"
"font: 10pt \"KacstOne\";")
        self.pushButton_2.setObjectName("pushButton_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_5.addTab(self.tab_5, icon1, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(Form)
        self.tabWidget_3.setGeometry(QtCore.QRect(22, 84, 951, 171))
        self.tabWidget_3.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  10pt \"KacstOne\";\n"
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 921, 121))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tw_lista_creditos_cuotas_buscar = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_lista_creditos_cuotas_buscar.setEnabled(True)
        self.tw_lista_creditos_cuotas_buscar.setGeometry(QtCore.QRect(10, 10, 901, 101))
        self.tw_lista_creditos_cuotas_buscar.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_lista_creditos_cuotas_buscar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_lista_creditos_cuotas_buscar.setObjectName("tw_lista_creditos_cuotas_buscar")
        self.tw_lista_creditos_cuotas_buscar.setColumnCount(10)
        self.tw_lista_creditos_cuotas_buscar.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_lista_creditos_cuotas_buscar.setItem(1, 0, item)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_4, icon2, "")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(19, 10, 261, 22))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 3, 241, 16))
        self.label_14.setStyleSheet("background-color: rgb(239, 235, 231);")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Form)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cuota"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Crédito"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Estado"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Capital"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "1° Vencimiento"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Importe 1°vto"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Saldo"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Fecha de Cobro"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Interes"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Importe Cobrado"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Cupon N°"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Gastos"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Seguros"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(13)
        item.setText(_translate("Form", "Impuestos"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Sellados"))
        item = self.tw_listado_cuotas_cuotas_buscar.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Mora"))
        __sortingEnabled = self.tw_listado_cuotas_cuotas_buscar.isSortingEnabled()
        self.tw_listado_cuotas_cuotas_buscar.setSortingEnabled(False)
        self.tw_listado_cuotas_cuotas_buscar.setSortingEnabled(__sortingEnabled)
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_3), _translate("Form", "Cuotas del Crédito"))
        self.label.setText(_translate("Form", "DNI: "))
        self.label_2.setText(_translate("Form", "N° Cliente : "))
        self.pushButton.setText(_translate("Form", "Buscar"))
        self.label_4.setText(_translate("Form", "Capital : "))
        self.label_5.setText(_translate("Form", "Saldo : "))
        self.label_6.setText(_translate("Form", "Importe a cobrar :"))
        self.label_7.setText(_translate("Form", "Gastos :"))
        self.label_8.setText(_translate("Form", "Seguros : "))
        self.label_9.setText(_translate("Form", "Impuestos :"))
        self.label_10.setText(_translate("Form", "Interes : "))
        self.label_13.setText(_translate("Form", "Detalle importes a Cobrar : "))
        self.dateEdit.setDisplayFormat(_translate("Form", "dd/mm/yyyy"))
        self.comboBox.setItemText(0, _translate("Form", "Vencida a 60 días"))
        self.comboBox.setItemText(1, _translate("Form", "A pagar"))
        self.comboBox.setItemText(2, _translate("Form", "Vencida a 30 días"))
        self.comboBox.setItemText(3, _translate("Form", "En judiciales"))
        self.label_11.setText(_translate("Form", "Fecha de Cobro : "))
        self.label_12.setText(_translate("Form", "Estado : "))
        self.label_3.setText(_translate("Form", "Información a editar por el Usuario : "))
        self.pushButton_3.setText(_translate("Form", "Limpiar"))
        self.pushButton_2.setText(_translate("Form", "Pagar"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_5), _translate("Form", "Pago de Cuota"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Crédito N°"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cliente"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fecha Crédito"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "N° Cuotas"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Capital"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Finalizado"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Bloqueado"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Formula"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Tipo Vencimiento"))
        item = self.tw_lista_creditos_cuotas_buscar.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Observaciones"))
        __sortingEnabled = self.tw_lista_creditos_cuotas_buscar.isSortingEnabled()
        self.tw_lista_creditos_cuotas_buscar.setSortingEnabled(False)
        self.tw_lista_creditos_cuotas_buscar.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("Form", "Historial de Cŕeditos"))
        self.label_14.setText(_translate("Form", "Cuotas Cobrar con Administrador "))

