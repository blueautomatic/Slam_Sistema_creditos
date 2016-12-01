# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_empresa_datos_actualizar.ui'
#
# Created: Thu Oct 20 17:29:13 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_empresa_datos_actualizar(object):
    def setupUi(self, form_empresa_datos_actualizar):
        form_empresa_datos_actualizar.setObjectName("form_empresa_datos_actualizar")
        form_empresa_datos_actualizar.resize(653, 555)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 207, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        form_empresa_datos_actualizar.setPalette(palette)
        form_empresa_datos_actualizar.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"background-color: rgb(239, 235, 231);")
        self.tabWidget = QtWidgets.QTabWidget(form_empresa_datos_actualizar)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 491))
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font:  11pt \"KacstOne\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 571, 411))
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
"}\n"
"\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(24, 16, 521, 341))
        self.groupBox.setAcceptDrops(True)
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
        self.lne_ciudad = QtWidgets.QLineEdit(self.groupBox)
        self.lne_ciudad.setGeometry(QtCore.QRect(200, 60, 171, 20))
        self.lne_ciudad.setText("")
        self.lne_ciudad.setObjectName("lne_ciudad")
        self.lne_ingresos_brutos = QtWidgets.QLineEdit(self.groupBox)
        self.lne_ingresos_brutos.setGeometry(QtCore.QRect(200, 240, 171, 20))
        self.lne_ingresos_brutos.setText("")
        self.lne_ingresos_brutos.setObjectName("lne_ingresos_brutos")
        self.lne_website = QtWidgets.QLineEdit(self.groupBox)
        self.lne_website.setGeometry(QtCore.QRect(200, 180, 181, 20))
        self.lne_website.setText("")
        self.lne_website.setObjectName("lne_website")
        self.lne_telefono = QtWidgets.QLineEdit(self.groupBox)
        self.lne_telefono.setGeometry(QtCore.QRect(200, 120, 171, 20))
        self.lne_telefono.setText("")
        self.lne_telefono.setObjectName("lne_telefono")
        self.label_48 = QtWidgets.QLabel(self.groupBox)
        self.label_48.setGeometry(QtCore.QRect(24, 300, 141, 16))
        self.label_48.setObjectName("label_48")
        self.lne_email = QtWidgets.QLineEdit(self.groupBox)
        self.lne_email.setGeometry(QtCore.QRect(200, 150, 261, 20))
        self.lne_email.setText("")
        self.lne_email.setObjectName("lne_email")
        self.label_40 = QtWidgets.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(30, 60, 141, 16))
        self.label_40.setObjectName("label_40")
        self.btn_actualizar = QtWidgets.QPushButton(self.groupBox)
        self.btn_actualizar.setGeometry(QtCore.QRect(530, 390, 85, 31))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.label_47 = QtWidgets.QLabel(self.groupBox)
        self.label_47.setGeometry(QtCore.QRect(30, 270, 141, 16))
        self.label_47.setObjectName("label_47")
        self.label_42 = QtWidgets.QLabel(self.groupBox)
        self.label_42.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_42.setObjectName("label_42")
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setGeometry(QtCore.QRect(30, 30, 151, 16))
        self.label_39.setObjectName("label_39")
        self.lne_direccion = QtWidgets.QLineEdit(self.groupBox)
        self.lne_direccion.setGeometry(QtCore.QRect(200, 90, 300, 20))
        self.lne_direccion.setText("")
        self.lne_direccion.setObjectName("lne_direccion")
        self.lne_nombre = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre.setGeometry(QtCore.QRect(200, 30, 301, 20))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lne_nombre.setFont(font)
        self.lne_nombre.setText("")
        self.lne_nombre.setObjectName("lne_nombre")
        self.label_43 = QtWidgets.QLabel(self.groupBox)
        self.label_43.setGeometry(QtCore.QRect(30, 150, 141, 16))
        self.label_43.setObjectName("label_43")
        self.lne_cuit = QtWidgets.QLineEdit(self.groupBox)
        self.lne_cuit.setGeometry(QtCore.QRect(200, 270, 181, 20))
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.cbx_tipo_iva = QtWidgets.QComboBox(self.groupBox)
        self.cbx_tipo_iva.setGeometry(QtCore.QRect(200, 210, 161, 23))
        self.cbx_tipo_iva.setObjectName("cbx_tipo_iva")
        self.cbx_tipo_iva.addItem("")
        self.cbx_tipo_iva.addItem("")
        self.cbx_tipo_iva.addItem("")
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        self.label_41.setGeometry(QtCore.QRect(30, 90, 141, 16))
        self.label_41.setObjectName("label_41")
        self.label_45 = QtWidgets.QLabel(self.groupBox)
        self.label_45.setGeometry(QtCore.QRect(30, 210, 141, 16))
        self.label_45.setObjectName("label_45")
        self.label_44 = QtWidgets.QLabel(self.groupBox)
        self.label_44.setGeometry(QtCore.QRect(30, 180, 141, 16))
        self.label_44.setObjectName("label_44")
        self.label_46 = QtWidgets.QLabel(self.groupBox)
        self.label_46.setGeometry(QtCore.QRect(30, 240, 141, 16))
        self.label_46.setObjectName("label_46")
        self.lne_nombre_fantasia = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre_fantasia.setGeometry(QtCore.QRect(200, 300, 181, 20))
        self.lne_nombre_fantasia.setText("")
        self.lne_nombre_fantasia.setObjectName("lne_nombre_fantasia")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab, icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/boton-actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.btn_actualizarr = QtWidgets.QPushButton(form_empresa_datos_actualizar)
        self.btn_actualizarr.setGeometry(QtCore.QRect(550, 510, 71, 23))
        self.btn_actualizarr.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"font:  10pt \"KacstOne\";")
        self.btn_actualizarr.setObjectName("btn_actualizarr")

        self.retranslateUi(form_empresa_datos_actualizar)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_empresa_datos_actualizar)

    def retranslateUi(self, form_empresa_datos_actualizar):
        _translate = QtCore.QCoreApplication.translate
        form_empresa_datos_actualizar.setWindowTitle(_translate("form_empresa_datos_actualizar", "Datos empresa actualizar"))
        self.label_48.setText(_translate("form_empresa_datos_actualizar", "Nombre de  fantasia:"))
        self.label_40.setText(_translate("form_empresa_datos_actualizar", "Ciudad:"))
        self.btn_actualizar.setText(_translate("form_empresa_datos_actualizar", "actualizar"))
        self.label_47.setText(_translate("form_empresa_datos_actualizar", "N° de CUIT:"))
        self.label_42.setText(_translate("form_empresa_datos_actualizar", "Teléfono/Fax:"))
        self.label_39.setText(_translate("form_empresa_datos_actualizar", "Nombre de la Empresa:"))
        self.label_43.setText(_translate("form_empresa_datos_actualizar", "E-mail:"))
        self.cbx_tipo_iva.setItemText(0, _translate("form_empresa_datos_actualizar", "Responsable inscripto"))
        self.cbx_tipo_iva.setItemText(1, _translate("form_empresa_datos_actualizar", "Exento"))
        self.cbx_tipo_iva.setItemText(2, _translate("form_empresa_datos_actualizar", "Monotributo"))
        self.label_41.setText(_translate("form_empresa_datos_actualizar", "Dirección:"))
        self.label_45.setText(_translate("form_empresa_datos_actualizar", "Tipo de IVA:"))
        self.label_44.setText(_translate("form_empresa_datos_actualizar", "Website:"))
        self.label_46.setText(_translate("form_empresa_datos_actualizar", "Ingresos Brutos:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("form_empresa_datos_actualizar", "Actualizar Datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("form_empresa_datos_actualizar", "Actualizar Empresa"))
        self.btn_actualizarr.setText(_translate("form_empresa_datos_actualizar", "Actualizar"))

