# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_login.ui'
#
# Created: Mon Jan  2 10:35:09 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_login(object):
    def setupUi(self, Form_login):
        Form_login.setObjectName("Form_login")
        Form_login.resize(406, 225)
        Form_login.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font:  11pt \"KacstOne\";\n"
"background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.487, y2:0.977273, stop:0.188482 rgba(132, 0, 0, 255), stop:1 rgba(235, 0, 4, 255));")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form_login)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 201))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
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
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(6, 6, 361, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Íconos/credi1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 321, 101))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.487, y2:0.977273, stop:0.188482 rgba(132, 0, 0, 255), stop:1 rgba(235, 0, 4, 255));\n"
"border-radius: 8px;\n"
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
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 19, 59, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 45, 101, 16))
        self.label_3.setObjectName("label_3")
        self.lne_nombre = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre.setGeometry(QtCore.QRect(131, 15, 161, 23))
        self.lne_nombre.setObjectName("lne_nombre")
        self.lne_pass = QtWidgets.QLineEdit(self.groupBox)
        self.lne_pass.setGeometry(QtCore.QRect(131, 43, 161, 23))
        self.lne_pass.setObjectName("lne_pass")
        self.boton_aceptar = QtWidgets.QPushButton(self.groupBox)
        self.boton_aceptar.setGeometry(QtCore.QRect(209, 70, 80, 23))
        self.boton_aceptar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.487, y2:0.977273, stop:0.188482 rgba(132, 0, 0, 132), stop:1 rgba(235, 0, 4, 255));")
        self.boton_aceptar.setObjectName("boton_aceptar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")

        self.retranslateUi(Form_login)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_login)

    def retranslateUi(self, Form_login):
        _translate = QtCore.QCoreApplication.translate
        Form_login.setWindowTitle(_translate("Form_login", "LogIn"))
        self.label_2.setText(_translate("Form_login", "Usuario :"))
        self.label_3.setText(_translate("Form_login", "Contraseña : "))
        self.boton_aceptar.setText(_translate("Form_login", "Ingresar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_login", "Ingreso Usuario"))

