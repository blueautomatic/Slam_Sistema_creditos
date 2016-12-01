# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_nuevo.ui'
#
# Created: Thu Oct 20 17:57:49 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_nuevo(object):
    def setupUi(self, Form_clientes_nuevo):
        Form_clientes_nuevo.setObjectName("Form_clientes_nuevo")
        Form_clientes_nuevo.resize(1020, 596)
        Form_clientes_nuevo.setStyleSheet("font:  75 10Pt \"Century Schoolbook L\";\n"
"selection-background-color: rgb(218, 175, 158);\n"
"selection-color: rgb(0, 0, 0);\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_nuevo)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1001, 561))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 175, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font:  75 11Pt \"Century Schoolbook L\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 981, 461))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(13, 13, 951, 401))
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
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(509, 215, 131, 16))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(509, 152, 131, 16))
        self.label_11.setObjectName("label_11")
        self.lne_nombre_nuevo = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre_nuevo.setGeometry(QtCore.QRect(449, 46, 181, 23))
        self.lne_nombre_nuevo.setText("")
        self.lne_nombre_nuevo.setObjectName("lne_nombre_nuevo")
        self.cbx_ciudad = QtWidgets.QComboBox(self.groupBox)
        self.cbx_ciudad.setGeometry(QtCore.QRect(591, 183, 180, 22))
        self.cbx_ciudad.setObjectName("cbx_ciudad")
        self.cbx_ciudad.addItem("")
        self.cbx_ciudad.addItem("")
        self.cbx_ciudad.addItem("")
        self.lne_barrio = QtWidgets.QLineEdit(self.groupBox)
        self.lne_barrio.setGeometry(QtCore.QRect(590, 149, 300, 22))
        self.lne_barrio.setText("")
        self.lne_barrio.setObjectName("lne_barrio")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(649, 51, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(349, 117, 131, 16))
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(38, 117, 141, 16))
        self.label_7.setObjectName("label_7")
        self.lne_nro_doc = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc.setGeometry(QtCore.QRect(330, 78, 125, 23))
        self.lne_nro_doc.setText("")
        self.lne_nro_doc.setObjectName("lne_nro_doc")
        self.cbx_estado_civil = QtWidgets.QComboBox(self.groupBox)
        self.cbx_estado_civil.setGeometry(QtCore.QRect(479, 115, 180, 22))
        self.cbx_estado_civil.setObjectName("cbx_estado_civil")
        self.cbx_estado_civil.addItem("")
        self.cbx_estado_civil.addItem("")
        self.cbx_estado_civil.addItem("")
        self.cbx_estado_civil.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(38, 218, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 250, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lne_domicilio = QtWidgets.QLineEdit(self.groupBox)
        self.lne_domicilio.setGeometry(QtCore.QRect(179, 151, 300, 22))
        self.lne_domicilio.setText("")
        self.lne_domicilio.setObjectName("lne_domicilio")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(38, 185, 121, 16))
        self.label_8.setObjectName("label_8")
        self.lne_nro_cliente = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_cliente.setEnabled(False)
        self.lne_nro_cliente.setGeometry(QtCore.QRect(750, 47, 61, 23))
        self.lne_nro_cliente.setText("")
        self.lne_nro_cliente.setObjectName("lne_nro_cliente")
        self.label_50 = QtWidgets.QLabel(self.groupBox)
        self.label_50.setGeometry(QtCore.QRect(40, 80, 141, 16))
        self.label_50.setObjectName("label_50")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(375, 49, 71, 16))
        self.label.setObjectName("label")
        self.lne_telefono = QtWidgets.QLineEdit(self.groupBox)
        self.lne_telefono.setGeometry(QtCore.QRect(179, 183, 300, 22))
        self.lne_telefono.setText("")
        self.lne_telefono.setObjectName("lne_telefono")
        self.lne_email = QtWidgets.QLineEdit(self.groupBox)
        self.lne_email.setGeometry(QtCore.QRect(590, 216, 300, 22))
        self.lne_email.setText("")
        self.lne_email.setObjectName("lne_email")
        self.dte_nacimiento = QtWidgets.QDateEdit(self.groupBox)
        self.dte_nacimiento.setGeometry(QtCore.QRect(210, 110, 101, 25))
        self.dte_nacimiento.setMaximumDate(QtCore.QDate(7999, 12, 26))
        self.dte_nacimiento.setCalendarPopup(True)
        self.dte_nacimiento.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_nacimiento.setObjectName("dte_nacimiento")
        self.label_49 = QtWidgets.QLabel(self.groupBox)
        self.label_49.setGeometry(QtCore.QRect(259, 81, 71, 16))
        self.label_49.setObjectName("label_49")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(509, 186, 71, 16))
        self.label_10.setObjectName("label_10")
        self.cbx_tipo_doc = QtWidgets.QComboBox(self.groupBox)
        self.cbx_tipo_doc.setGeometry(QtCore.QRect(168, 77, 71, 23))
        self.cbx_tipo_doc.setObjectName("cbx_tipo_doc")
        self.cbx_tipo_doc.addItem("")
        self.cbx_tipo_doc.addItem("")
        self.cbx_tipo_doc.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 47, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lne_apellido = QtWidgets.QLineEdit(self.groupBox)
        self.lne_apellido.setGeometry(QtCore.QRect(150, 46, 191, 23))
        self.lne_apellido.setText("")
        self.lne_apellido.setObjectName("lne_apellido")
        self.lne_limite_credito = QtWidgets.QLineEdit(self.groupBox)
        self.lne_limite_credito.setGeometry(QtCore.QRect(179, 215, 300, 22))
        self.lne_limite_credito.setText("")
        self.lne_limite_credito.setObjectName("lne_limite_credito")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(38, 152, 101, 16))
        self.label_5.setObjectName("label_5")
        self.txte_observaciones = QtWidgets.QTextEdit(self.groupBox)
        self.txte_observaciones.setGeometry(QtCore.QRect(31, 268, 911, 121))
        self.txte_observaciones.setObjectName("txte_observaciones")
        self.cbx_estado = QtWidgets.QComboBox(self.groupBox)
        self.cbx_estado.setGeometry(QtCore.QRect(752, 84, 141, 23))
        self.cbx_estado.setObjectName("cbx_estado")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.setItemText(6, "")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(612, 84, 121, 20))
        self.label_37.setObjectName("label_37")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_4, icon, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setGeometry(QtCore.QRect(27, 27, 921, 241))
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
        self.lne_organismo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_organismo.setGeometry(QtCore.QRect(200, 90, 300, 20))
        self.lne_organismo.setText("")
        self.lne_organismo.setObjectName("lne_organismo")
        self.lne_sueldo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_sueldo.setGeometry(QtCore.QRect(670, 60, 101, 20))
        self.lne_sueldo.setObjectName("lne_sueldo")
        self.lne_categoria = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_categoria.setGeometry(QtCore.QRect(670, 120, 101, 20))
        self.lne_categoria.setText("")
        self.lne_categoria.setObjectName("lne_categoria")
        self.lne_telefono_laboral = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_telefono_laboral.setGeometry(QtCore.QRect(200, 120, 300, 20))
        self.lne_telefono_laboral.setText("")
        self.lne_telefono_laboral.setObjectName("lne_telefono_laboral")
        self.lne_ocupacion = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ocupacion.setGeometry(QtCore.QRect(200, 60, 300, 20))
        self.lne_ocupacion.setText("")
        self.lne_ocupacion.setObjectName("lne_ocupacion")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(530, 90, 131, 20))
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(59, 150, 161, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(59, 120, 141, 20))
        self.label_17.setObjectName("label_17")
        self.ckbx_recibo_sueldo_nuevo = QtWidgets.QCheckBox(self.groupBox_2)
        self.ckbx_recibo_sueldo_nuevo.setGeometry(QtCore.QRect(530, 150, 211, 21))
        self.ckbx_recibo_sueldo_nuevo.setChecked(True)
        self.ckbx_recibo_sueldo_nuevo.setObjectName("ckbx_recibo_sueldo_nuevo")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(530, 60, 80, 20))
        self.label_19.setObjectName("label_19")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(59, 90, 80, 20))
        self.label_15.setObjectName("label_15")
        self.lne_domicilio_laboral = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_domicilio_laboral.setGeometry(QtCore.QRect(200, 150, 300, 20))
        self.lne_domicilio_laboral.setText("")
        self.lne_domicilio_laboral.setObjectName("lne_domicilio_laboral")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(530, 120, 121, 20))
        self.label_21.setObjectName("label_21")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(59, 60, 80, 20))
        self.label_14.setObjectName("label_14")
        self.lne_antiguedad = QtWidgets.QDateEdit(self.groupBox_2)
        self.lne_antiguedad.setGeometry(QtCore.QRect(680, 90, 121, 24))
        self.lne_antiguedad.setCalendarPopup(True)
        self.lne_antiguedad.setObjectName("lne_antiguedad")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/hombre-en-el-escritorio-de-la-oficina-con-un-ordenador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_5, icon1, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_4.setGeometry(QtCore.QRect(23, 29, 931, 271))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_4.setFont(font)
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
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(128, 70, 80, 20))
        self.label_36.setObjectName("label_36")
        self.ckbx_veraz = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_veraz.setGeometry(QtCore.QRect(599, 130, 211, 21))
        self.ckbx_veraz.setChecked(False)
        self.ckbx_veraz.setObjectName("ckbx_veraz")
        self.lne_nro_beneficio = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_beneficio.setGeometry(QtCore.QRect(269, 160, 300, 20))
        self.lne_nro_beneficio.setText("")
        self.lne_nro_beneficio.setObjectName("lne_nro_beneficio")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(128, 160, 121, 20))
        self.label_35.setObjectName("label_35")
        self.ckbx_jub_pens = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_jub_pens.setGeometry(QtCore.QRect(599, 160, 211, 21))
        self.ckbx_jub_pens.setObjectName("ckbx_jub_pens")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(128, 100, 80, 20))
        self.label_33.setObjectName("label_33")
        self.lne_cbu = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cbu.setGeometry(QtCore.QRect(269, 130, 300, 20))
        self.lne_cbu.setText("")
        self.lne_cbu.setObjectName("lne_cbu")
        self.ckbx_facturas = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_facturas.setGeometry(QtCore.QRect(599, 100, 251, 21))
        self.ckbx_facturas.setChecked(False)
        self.ckbx_facturas.setObjectName("ckbx_facturas")
        self.lne_cuit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cuit.setGeometry(QtCore.QRect(269, 100, 300, 20))
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(128, 130, 141, 20))
        self.label_34.setObjectName("label_34")
        self.cbx_tipo_iva = QtWidgets.QComboBox(self.groupBox_4)
        self.cbx_tipo_iva.setGeometry(QtCore.QRect(270, 70, 231, 23))
        self.cbx_tipo_iva.setObjectName("cbx_tipo_iva")
        self.cbx_tipo_iva.addItem("")
        self.cbx_tipo_iva.addItem("")
        self.cbx_tipo_iva.addItem("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_7, icon2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 941, 411))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
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
"QPushButton{\n"
"background-color: rgb(253, 194, 179);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"}\n"
"\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tw_garantes_lista = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_garantes_lista.setGeometry(QtCore.QRect(10, 250, 911, 141))
        self.tw_garantes_lista.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(6)
        self.tw_garantes_lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(5, item)
        self.lne_garante_nro_cliente_nuevo = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_cliente_nuevo.setGeometry(QtCore.QRect(400, 20, 71, 20))
        self.lne_garante_nro_cliente_nuevo.setText("")
        self.lne_garante_nro_cliente_nuevo.setObjectName("lne_garante_nro_cliente_nuevo")
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(11, 21, 111, 20))
        self.label_51.setObjectName("label_51")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_22.setObjectName("label_22")
        self.txte_garante_observaciones = QtWidgets.QTextEdit(self.groupBox_3)
        self.txte_garante_observaciones.setGeometry(QtCore.QRect(10, 130, 911, 81))
        self.txte_garante_observaciones.setObjectName("txte_garante_observaciones")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(304, 24, 81, 16))
        self.label_31.setObjectName("label_31")
        self.boton_agregar_nuevo = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_agregar_nuevo.setGeometry(QtCore.QRect(840, 220, 80, 23))
        self.boton_agregar_nuevo.setObjectName("boton_agregar_nuevo")
        self.lne_garante_nro_doc_nuevo = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_doc_nuevo.setGeometry(QtCore.QRect(140, 20, 125, 23))
        self.lne_garante_nro_doc_nuevo.setText("")
        self.lne_garante_nro_doc_nuevo.setObjectName("lne_garante_nro_doc_nuevo")
        self.boton_buscar_garante_nuevo = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_buscar_garante_nuevo.setGeometry(QtCore.QRect(560, 20, 80, 23))
        self.boton_buscar_garante_nuevo.setObjectName("boton_buscar_garante_nuevo")
        self.lne_garante_apellido = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_apellido.setGeometry(QtCore.QRect(140, 50, 191, 23))
        self.lne_garante_apellido.setText("")
        self.lne_garante_apellido.setObjectName("lne_garante_apellido")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(34, 53, 61, 16))
        self.label_29.setObjectName("label_29")
        self.lne_garante_nombre = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nombre.setGeometry(QtCore.QRect(140, 80, 191, 23))
        self.lne_garante_nombre.setText("")
        self.lne_garante_nombre.setObjectName("lne_garante_nombre")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(390, 50, 61, 16))
        self.label_23.setObjectName("label_23")
        self.lne_garante_estado = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_estado.setGeometry(QtCore.QRect(480, 50, 181, 23))
        self.lne_garante_estado.setText("")
        self.lne_garante_estado.setObjectName("lne_garante_estado")
        self.cbx_tipo_garante = QtWidgets.QComboBox(self.groupBox_3)
        self.cbx_tipo_garante.setGeometry(QtCore.QRect(480, 80, 181, 23))
        self.cbx_tipo_garante.setObjectName("cbx_tipo_garante")
        self.cbx_tipo_garante.addItem("")
        self.cbx_tipo_garante.addItem("")
        self.cbx_tipo_garante.addItem("")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(350, 80, 101, 16))
        self.label_24.setObjectName("label_24")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(750, 20, 141, 23))
        self.pushButton.setObjectName("pushButton")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_6, icon3, "")
        self.boton_limpiar_nuevo = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar_nuevo.setGeometry(QtCore.QRect(820, 490, 80, 23))
        self.boton_limpiar_nuevo.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_limpiar_nuevo.setObjectName("boton_limpiar_nuevo")
        self.boton_guardar_nuevo = QtWidgets.QPushButton(self.tab)
        self.boton_guardar_nuevo.setGeometry(QtCore.QRect(910, 490, 80, 23))
        self.boton_guardar_nuevo.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_guardar_nuevo.setObjectName("boton_guardar_nuevo")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Íconos/silueta-masculina-de-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")

        self.retranslateUi(Form_clientes_nuevo)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_email.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_barrio.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_nro_cliente.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_nombre_nuevo.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_apellido.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_nro_doc.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_domicilio.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_telefono.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_limite_credito.clear)
        self.boton_limpiar_nuevo.clicked['bool'].connect(self.tw_garantes_lista.clearContents)
        self.boton_limpiar_nuevo.clicked['bool'].connect(self.tw_garantes_lista.reset)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_garante_nombre.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_garante_estado.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_garante_nro_cliente_nuevo.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_garante_nro_doc_nuevo.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_garante_apellido.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.txte_garante_observaciones.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_ocupacion.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_organismo.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_telefono_laboral.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_domicilio_laboral.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_sueldo.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_categoria.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_cuit.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_cbu.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.lne_nro_beneficio.clear)
        self.boton_limpiar_nuevo.clicked.connect(self.txte_observaciones.clear)
        self.pushButton.clicked.connect(self.lne_garante_nro_doc_nuevo.clear)
        self.pushButton.clicked.connect(self.lne_garante_apellido.clear)
        self.pushButton.clicked.connect(self.lne_garante_nombre.clear)
        self.pushButton.clicked.connect(self.lne_garante_estado.clear)
        self.pushButton.clicked.connect(self.lne_garante_nro_cliente_nuevo.clear)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_nuevo)
        Form_clientes_nuevo.setTabOrder(self.lne_apellido, self.lne_nombre_nuevo)
        Form_clientes_nuevo.setTabOrder(self.lne_nombre_nuevo, self.lne_nro_cliente)
        Form_clientes_nuevo.setTabOrder(self.lne_nro_cliente, self.cbx_tipo_doc)
        Form_clientes_nuevo.setTabOrder(self.cbx_tipo_doc, self.lne_nro_doc)
        Form_clientes_nuevo.setTabOrder(self.lne_nro_doc, self.cbx_estado)
        Form_clientes_nuevo.setTabOrder(self.cbx_estado, self.dte_nacimiento)
        Form_clientes_nuevo.setTabOrder(self.dte_nacimiento, self.cbx_estado_civil)
        Form_clientes_nuevo.setTabOrder(self.cbx_estado_civil, self.lne_domicilio)
        Form_clientes_nuevo.setTabOrder(self.lne_domicilio, self.lne_barrio)
        Form_clientes_nuevo.setTabOrder(self.lne_barrio, self.lne_telefono)
        Form_clientes_nuevo.setTabOrder(self.lne_telefono, self.cbx_ciudad)
        Form_clientes_nuevo.setTabOrder(self.cbx_ciudad, self.lne_limite_credito)
        Form_clientes_nuevo.setTabOrder(self.lne_limite_credito, self.lne_email)
        Form_clientes_nuevo.setTabOrder(self.lne_email, self.txte_observaciones)
        Form_clientes_nuevo.setTabOrder(self.txte_observaciones, self.lne_ocupacion)
        Form_clientes_nuevo.setTabOrder(self.lne_ocupacion, self.lne_sueldo)
        Form_clientes_nuevo.setTabOrder(self.lne_sueldo, self.lne_organismo)
        Form_clientes_nuevo.setTabOrder(self.lne_organismo, self.lne_telefono_laboral)
        Form_clientes_nuevo.setTabOrder(self.lne_telefono_laboral, self.lne_categoria)
        Form_clientes_nuevo.setTabOrder(self.lne_categoria, self.lne_domicilio_laboral)
        Form_clientes_nuevo.setTabOrder(self.lne_domicilio_laboral, self.ckbx_recibo_sueldo_nuevo)
        Form_clientes_nuevo.setTabOrder(self.ckbx_recibo_sueldo_nuevo, self.lne_garante_nro_doc_nuevo)
        Form_clientes_nuevo.setTabOrder(self.lne_garante_nro_doc_nuevo, self.lne_garante_nro_cliente_nuevo)
        Form_clientes_nuevo.setTabOrder(self.lne_garante_nro_cliente_nuevo, self.boton_buscar_garante_nuevo)
        Form_clientes_nuevo.setTabOrder(self.boton_buscar_garante_nuevo, self.lne_garante_apellido)
        Form_clientes_nuevo.setTabOrder(self.lne_garante_apellido, self.lne_garante_estado)
        Form_clientes_nuevo.setTabOrder(self.lne_garante_estado, self.lne_garante_nombre)
        Form_clientes_nuevo.setTabOrder(self.lne_garante_nombre, self.cbx_tipo_garante)
        Form_clientes_nuevo.setTabOrder(self.cbx_tipo_garante, self.txte_garante_observaciones)
        Form_clientes_nuevo.setTabOrder(self.txte_garante_observaciones, self.tw_garantes_lista)
        Form_clientes_nuevo.setTabOrder(self.tw_garantes_lista, self.cbx_tipo_iva)
        Form_clientes_nuevo.setTabOrder(self.cbx_tipo_iva, self.lne_cuit)
        Form_clientes_nuevo.setTabOrder(self.lne_cuit, self.ckbx_facturas)
        Form_clientes_nuevo.setTabOrder(self.ckbx_facturas, self.lne_cbu)
        Form_clientes_nuevo.setTabOrder(self.lne_cbu, self.ckbx_veraz)
        Form_clientes_nuevo.setTabOrder(self.ckbx_veraz, self.lne_nro_beneficio)
        Form_clientes_nuevo.setTabOrder(self.lne_nro_beneficio, self.ckbx_jub_pens)
        Form_clientes_nuevo.setTabOrder(self.ckbx_jub_pens, self.boton_limpiar_nuevo)
        Form_clientes_nuevo.setTabOrder(self.boton_limpiar_nuevo, self.boton_guardar_nuevo)
        Form_clientes_nuevo.setTabOrder(self.boton_guardar_nuevo, self.boton_agregar_nuevo)
        Form_clientes_nuevo.setTabOrder(self.boton_agregar_nuevo, self.tabWidget)
        Form_clientes_nuevo.setTabOrder(self.tabWidget, self.tabWidget_2)

    def retranslateUi(self, Form_clientes_nuevo):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_nuevo.setWindowTitle(_translate("Form_clientes_nuevo", "Alta Cliente"))
        self.label_12.setText(_translate("Form_clientes_nuevo", "Email:"))
        self.label_11.setText(_translate("Form_clientes_nuevo", "Barrio:"))
        self.cbx_ciudad.setItemText(0, _translate("Form_clientes_nuevo", "Viedma"))
        self.cbx_ciudad.setItemText(1, _translate("Form_clientes_nuevo", "Patagones"))
        self.cbx_ciudad.setItemText(2, _translate("Form_clientes_nuevo", "Otros"))
        self.label_3.setText(_translate("Form_clientes_nuevo", "N°  Cliente :"))
        self.label_13.setText(_translate("Form_clientes_nuevo", "Estado Civil:"))
        self.label_7.setText(_translate("Form_clientes_nuevo", "Fecha de Nacimiento:"))
        self.cbx_estado_civil.setItemText(0, _translate("Form_clientes_nuevo", "Soltero/a"))
        self.cbx_estado_civil.setItemText(1, _translate("Form_clientes_nuevo", "Casado/a"))
        self.cbx_estado_civil.setItemText(2, _translate("Form_clientes_nuevo", "Viudo/a"))
        self.cbx_estado_civil.setItemText(3, _translate("Form_clientes_nuevo", "Divorsiado/a"))
        self.label_6.setText(_translate("Form_clientes_nuevo", "Límite por Créditos:"))
        self.label_9.setText(_translate("Form_clientes_nuevo", "Observaciones: "))
        self.label_8.setText(_translate("Form_clientes_nuevo", "Teléfono:"))
        self.label_50.setText(_translate("Form_clientes_nuevo", "Tipo Documento:"))
        self.label.setText(_translate("Form_clientes_nuevo", "Nombre :"))
        self.dte_nacimiento.setDisplayFormat(_translate("Form_clientes_nuevo", "dd/M/yyyy"))
        self.label_49.setText(_translate("Form_clientes_nuevo", "Número:"))
        self.label_10.setText(_translate("Form_clientes_nuevo", "Ciudad:"))
        self.cbx_tipo_doc.setItemText(0, _translate("Form_clientes_nuevo", "DNI "))
        self.cbx_tipo_doc.setItemText(1, _translate("Form_clientes_nuevo", "CUIL"))
        self.cbx_tipo_doc.setItemText(2, _translate("Form_clientes_nuevo", "CUIT "))
        self.label_2.setText(_translate("Form_clientes_nuevo", "Apellido:"))
        self.label_5.setText(_translate("Form_clientes_nuevo", "Domicilio:"))
        self.txte_observaciones.setHtml(_translate("Form_clientes_nuevo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073; font-family:\'KacstOne\';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'KacstOne\';\"><br /></p></body></html>"))
        self.cbx_estado.setItemText(0, _translate("Form_clientes_nuevo", "Activo"))
        self.cbx_estado.setItemText(1, _translate("Form_clientes_nuevo", "Moroso"))
        self.cbx_estado.setItemText(2, _translate("Form_clientes_nuevo", "Inactivo"))
        self.cbx_estado.setItemText(3, _translate("Form_clientes_nuevo", "Judicial"))
        self.cbx_estado.setItemText(4, _translate("Form_clientes_nuevo", "Bloqueado"))
        self.cbx_estado.setItemText(5, _translate("Form_clientes_nuevo", "Cupo Cubierto"))
        self.label_37.setText(_translate("Form_clientes_nuevo", "Estado Persona"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form_clientes_nuevo", "Datos Personales"))
        self.lne_sueldo.setText(_translate("Form_clientes_nuevo", "0"))
        self.label_18.setText(_translate("Form_clientes_nuevo", "Antigüedad Laboral:"))
        self.label_16.setText(_translate("Form_clientes_nuevo", "Domicilio Laboral:"))
        self.label_17.setText(_translate("Form_clientes_nuevo", "Teléfono Laboral:"))
        self.ckbx_recibo_sueldo_nuevo.setText(_translate("Form_clientes_nuevo", "Posee Recibo de Sueldo"))
        self.label_19.setText(_translate("Form_clientes_nuevo", "Sueldo $:"))
        self.label_15.setText(_translate("Form_clientes_nuevo", "Organismo: "))
        self.label_21.setText(_translate("Form_clientes_nuevo", "Categoría laboral: "))
        self.label_14.setText(_translate("Form_clientes_nuevo", "Empresa:"))
        self.lne_antiguedad.setDisplayFormat(_translate("Form_clientes_nuevo", "dd/M/yyyy"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form_clientes_nuevo", "Datos laborales"))
        self.label_36.setText(_translate("Form_clientes_nuevo", "Tipo IVA:"))
        self.ckbx_veraz.setText(_translate("Form_clientes_nuevo", "Figura en el Veraz"))
        self.label_35.setText(_translate("Form_clientes_nuevo", "N° Beneficio:"))
        self.ckbx_jub_pens.setText(_translate("Form_clientes_nuevo", "Es Jubilado / Pensionado"))
        self.label_33.setText(_translate("Form_clientes_nuevo", "N° CUIT/CUIL:"))
        self.ckbx_facturas.setText(_translate("Form_clientes_nuevo", "Presentó Facturas de Luz, Gas"))
        self.label_34.setText(_translate("Form_clientes_nuevo", "N° CBU:"))
        self.cbx_tipo_iva.setItemText(0, _translate("Form_clientes_nuevo", "Consumidor final"))
        self.cbx_tipo_iva.setItemText(1, _translate("Form_clientes_nuevo", "Responsable inscripto"))
        self.cbx_tipo_iva.setItemText(2, _translate("Form_clientes_nuevo", "Monotributista"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form_clientes_nuevo", "Otros Datos"))
        item = self.tw_garantes_lista.horizontalHeaderItem(0)
        item.setText(_translate("Form_clientes_nuevo", "Estado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(1)
        item.setText(_translate("Form_clientes_nuevo", "Tipo Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(2)
        item.setText(_translate("Form_clientes_nuevo", "Nro. Cliente"))
        item = self.tw_garantes_lista.horizontalHeaderItem(3)
        item.setText(_translate("Form_clientes_nuevo", "Apellido"))
        item = self.tw_garantes_lista.horizontalHeaderItem(4)
        item.setText(_translate("Form_clientes_nuevo", "Nombre"))
        item = self.tw_garantes_lista.horizontalHeaderItem(5)
        item.setText(_translate("Form_clientes_nuevo", "Número Documento"))
        self.label_51.setText(_translate("Form_clientes_nuevo", "Nro Documento:"))
        self.label_22.setText(_translate("Form_clientes_nuevo", "Observaciones: "))
        self.txte_garante_observaciones.setHtml(_translate("Form_clientes_nuevo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KacstOne\';\">a</span></p></body></html>"))
        self.label_31.setText(_translate("Form_clientes_nuevo", "N°  Cliente :"))
        self.boton_agregar_nuevo.setText(_translate("Form_clientes_nuevo", "Agregar"))
        self.boton_buscar_garante_nuevo.setText(_translate("Form_clientes_nuevo", "Buscar"))
        self.label_4.setText(_translate("Form_clientes_nuevo", "Nombre :"))
        self.label_29.setText(_translate("Form_clientes_nuevo", "Apellido:"))
        self.label_23.setText(_translate("Form_clientes_nuevo", "Estado :"))
        self.cbx_tipo_garante.setItemText(0, _translate("Form_clientes_nuevo", "Garante Principal"))
        self.cbx_tipo_garante.setItemText(1, _translate("Form_clientes_nuevo", "Garante Secundario"))
        self.cbx_tipo_garante.setItemText(2, _translate("Form_clientes_nuevo", "Otro Garante"))
        self.label_24.setText(_translate("Form_clientes_nuevo", "Tipo Garante :"))
        self.pushButton.setText(_translate("Form_clientes_nuevo", "Limpiar Garante"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form_clientes_nuevo", "Datos Garante"))
        self.boton_limpiar_nuevo.setText(_translate("Form_clientes_nuevo", "Limpiar"))
        self.boton_guardar_nuevo.setText(_translate("Form_clientes_nuevo", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_nuevo", "Alta Persona"))

