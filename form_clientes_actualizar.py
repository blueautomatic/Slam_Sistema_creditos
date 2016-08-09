# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_actualizar.ui'
#
# Created: Wed Aug  3 13:20:49 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_actualizar(object):
    def setupUi(self, Form_clientes_actualizar):
        Form_clientes_actualizar.setObjectName("Form_clientes_actualizar")
        Form_clientes_actualizar.resize(1020, 720)
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_actualizar)
        self.tabWidget.setGeometry(QtCore.QRect(12, 15, 1001, 701))
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.boton_buscar_actualizar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_actualizar.setGeometry(QtCore.QRect(890, 11, 80, 20))
        self.boton_buscar_actualizar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_actualizar.setObjectName("boton_buscar_actualizar")
        self.label_122 = QtWidgets.QLabel(self.tab)
        self.label_122.setGeometry(QtCore.QRect(697, 11, 31, 20))
        self.label_122.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.label_122.setObjectName("label_122")
        self.lne_dni_filtro_actualizar = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_actualizar.setGeometry(QtCore.QRect(730, 11, 151, 20))
        self.lne_dni_filtro_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_actualizar.setObjectName("lne_dni_filtro_actualizar")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(23, 22, 951, 611))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font: 75 10pt \"KacstOne\";\n"
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
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.lne_telfono_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_telfono_buscar_2.setGeometry(QtCore.QRect(160, 175, 300, 20))
        self.lne_telfono_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telfono_buscar_2.setObjectName("lne_telfono_buscar_2")
        self.label_123 = QtWidgets.QLabel(self.tab_16)
        self.label_123.setGeometry(QtCore.QRect(19, 109, 141, 16))
        self.label_123.setObjectName("label_123")
        self.dte_nacimiento_buscar_2 = QtWidgets.QDateEdit(self.tab_16)
        self.dte_nacimiento_buscar_2.setGeometry(QtCore.QRect(160, 108, 101, 20))
        self.dte_nacimiento_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_nacimiento_buscar_2.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_nacimiento_buscar_2.setObjectName("dte_nacimiento_buscar_2")
        self.cbx_estado_civil_buscar_2 = QtWidgets.QComboBox(self.tab_16)
        self.cbx_estado_civil_buscar_2.setGeometry(QtCore.QRect(450, 108, 180, 20))
        self.cbx_estado_civil_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_estado_civil_buscar_2.setObjectName("cbx_estado_civil_buscar_2")
        self.cbx_estado_civil_buscar_2.addItem("")
        self.cbx_estado_civil_buscar_2.addItem("")
        self.cbx_estado_civil_buscar_2.addItem("")
        self.cbx_estado_civil_buscar_2.addItem("")
        self.label_124 = QtWidgets.QLabel(self.tab_16)
        self.label_124.setGeometry(QtCore.QRect(490, 144, 131, 16))
        self.label_124.setObjectName("label_124")
        self.lne_domicilio_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_domicilio_buscar_2.setGeometry(QtCore.QRect(160, 143, 300, 20))
        self.lne_domicilio_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_buscar_2.setObjectName("lne_domicilio_buscar_2")
        self.label_125 = QtWidgets.QLabel(self.tab_16)
        self.label_125.setGeometry(QtCore.QRect(360, 41, 71, 16))
        self.label_125.setObjectName("label_125")
        self.label_126 = QtWidgets.QLabel(self.tab_16)
        self.label_126.setGeometry(QtCore.QRect(310, 108, 131, 16))
        self.label_126.setObjectName("label_126")
        self.lne_barrio_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_barrio_buscar_2.setGeometry(QtCore.QRect(630, 141, 300, 20))
        self.lne_barrio_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_barrio_buscar_2.setObjectName("lne_barrio_buscar_2")
        self.label_127 = QtWidgets.QLabel(self.tab_16)
        self.label_127.setGeometry(QtCore.QRect(19, 177, 121, 16))
        self.label_127.setObjectName("label_127")
        self.cbx_ciudad_4 = QtWidgets.QComboBox(self.tab_16)
        self.cbx_ciudad_4.setGeometry(QtCore.QRect(555, 178, 180, 20))
        self.cbx_ciudad_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_ciudad_4.setObjectName("cbx_ciudad_4")
        self.cbx_ciudad_4.addItem("")
        self.label_128 = QtWidgets.QLabel(self.tab_16)
        self.label_128.setGeometry(QtCore.QRect(21, 72, 103, 16))
        self.label_128.setObjectName("label_128")
        self.label_129 = QtWidgets.QLabel(self.tab_16)
        self.label_129.setGeometry(QtCore.QRect(630, 43, 71, 16))
        self.label_129.setObjectName("label_129")
        self.lne_nombre_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nombre_buscar_2.setGeometry(QtCore.QRect(430, 38, 181, 23))
        self.lne_nombre_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre_buscar_2.setObjectName("lne_nombre_buscar_2")
        self.lne_limite_credito_4 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_limite_credito_4.setGeometry(QtCore.QRect(160, 207, 300, 20))
        self.lne_limite_credito_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_limite_credito_4.setObjectName("lne_limite_credito_4")
        self.lne_nro_cliente_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nro_cliente_buscar_2.setGeometry(QtCore.QRect(716, 42, 71, 20))
        self.lne_nro_cliente_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cliente_buscar_2.setObjectName("lne_nro_cliente_buscar_2")
        self.label_130 = QtWidgets.QLabel(self.tab_16)
        self.label_130.setGeometry(QtCore.QRect(490, 207, 131, 16))
        self.label_130.setObjectName("label_130")
        self.cbx_tipo_doc_buscar_2 = QtWidgets.QComboBox(self.tab_16)
        self.cbx_tipo_doc_buscar_2.setGeometry(QtCore.QRect(131, 72, 59, 23))
        self.cbx_tipo_doc_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_tipo_doc_buscar_2.setObjectName("cbx_tipo_doc_buscar_2")
        self.cbx_tipo_doc_buscar_2.addItem("")
        self.cbx_tipo_doc_buscar_2.addItem("")
        self.cbx_tipo_doc_buscar_2.addItem("")
        self.lne_apellido_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_apellido_buscar_2.setGeometry(QtCore.QRect(131, 38, 191, 23))
        self.lne_apellido_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_buscar_2.setObjectName("lne_apellido_buscar_2")
        self.label_131 = QtWidgets.QLabel(self.tab_16)
        self.label_131.setGeometry(QtCore.QRect(210, 75, 52, 16))
        self.label_131.setObjectName("label_131")
        self.label_132 = QtWidgets.QLabel(self.tab_16)
        self.label_132.setGeometry(QtCore.QRect(19, 240, 121, 16))
        self.label_132.setObjectName("label_132")
        self.label_133 = QtWidgets.QLabel(self.tab_16)
        self.label_133.setGeometry(QtCore.QRect(19, 210, 121, 16))
        self.label_133.setObjectName("label_133")
        self.label_134 = QtWidgets.QLabel(self.tab_16)
        self.label_134.setGeometry(QtCore.QRect(21, 39, 53, 16))
        self.label_134.setObjectName("label_134")
        self.label_135 = QtWidgets.QLabel(self.tab_16)
        self.label_135.setGeometry(QtCore.QRect(490, 178, 71, 16))
        self.label_135.setObjectName("label_135")
        self.lne_email_4 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_email_4.setGeometry(QtCore.QRect(630, 208, 300, 20))
        self.lne_email_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_email_4.setObjectName("lne_email_4")
        self.label_136 = QtWidgets.QLabel(self.tab_16)
        self.label_136.setGeometry(QtCore.QRect(19, 144, 71, 16))
        self.label_136.setObjectName("label_136")
        self.lne_nro_doc_buscar_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nro_doc_buscar_2.setGeometry(QtCore.QRect(270, 74, 125, 23))
        self.lne_nro_doc_buscar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc_buscar_2.setObjectName("lne_nro_doc_buscar_2")
        self.ckbx_activo_buscar_2 = QtWidgets.QCheckBox(self.tab_16)
        self.ckbx_activo_buscar_2.setGeometry(QtCore.QRect(820, 38, 85, 21))
        self.ckbx_activo_buscar_2.setObjectName("ckbx_activo_buscar_2")
        self.ckbx_inactivo_buscar_2 = QtWidgets.QCheckBox(self.tab_16)
        self.ckbx_inactivo_buscar_2.setGeometry(QtCore.QRect(820, 68, 85, 21))
        self.ckbx_inactivo_buscar_2.setObjectName("ckbx_inactivo_buscar_2")
        self.txte_observaciones_4 = QtWidgets.QTextEdit(self.tab_16)
        self.txte_observaciones_4.setGeometry(QtCore.QRect(20, 258, 911, 161))
        self.txte_observaciones_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_observaciones_4.setObjectName("txte_observaciones_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox.setGeometry(QtCore.QRect(3, 17, 941, 421))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_16, icon, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.lne_organismo_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_organismo_4.setGeometry(QtCore.QRect(220, 70, 300, 20))
        self.lne_organismo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_organismo_4.setObjectName("lne_organismo_4")
        self.lne_ocupacion_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_ocupacion_4.setGeometry(QtCore.QRect(220, 40, 300, 20))
        self.lne_ocupacion_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_ocupacion_4.setObjectName("lne_ocupacion_4")
        self.lne_antiguedad_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_antiguedad_4.setGeometry(QtCore.QRect(690, 70, 101, 20))
        self.lne_antiguedad_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_antiguedad_4.setText("")
        self.lne_antiguedad_4.setObjectName("lne_antiguedad_4")
        self.label_137 = QtWidgets.QLabel(self.tab_17)
        self.label_137.setGeometry(QtCore.QRect(550, 40, 80, 20))
        self.label_137.setObjectName("label_137")
        self.label_138 = QtWidgets.QLabel(self.tab_17)
        self.label_138.setGeometry(QtCore.QRect(79, 100, 141, 20))
        self.label_138.setObjectName("label_138")
        self.lne_domicilio_laboral_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_domicilio_laboral_4.setGeometry(QtCore.QRect(220, 130, 300, 20))
        self.lne_domicilio_laboral_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_laboral_4.setObjectName("lne_domicilio_laboral_4")
        self.lne_telefono_laboral_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_telefono_laboral_4.setGeometry(QtCore.QRect(220, 100, 300, 20))
        self.lne_telefono_laboral_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_laboral_4.setObjectName("lne_telefono_laboral_4")
        self.lne_sueldo_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_sueldo_4.setGeometry(QtCore.QRect(690, 40, 101, 20))
        self.lne_sueldo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_sueldo_4.setText("")
        self.lne_sueldo_4.setObjectName("lne_sueldo_4")
        self.ckbx_recibo_sueldo_4 = QtWidgets.QCheckBox(self.tab_17)
        self.ckbx_recibo_sueldo_4.setGeometry(QtCore.QRect(550, 130, 211, 21))
        self.ckbx_recibo_sueldo_4.setChecked(True)
        self.ckbx_recibo_sueldo_4.setObjectName("ckbx_recibo_sueldo_4")
        self.label_139 = QtWidgets.QLabel(self.tab_17)
        self.label_139.setGeometry(QtCore.QRect(79, 70, 80, 20))
        self.label_139.setObjectName("label_139")
        self.label_140 = QtWidgets.QLabel(self.tab_17)
        self.label_140.setGeometry(QtCore.QRect(79, 40, 80, 20))
        self.label_140.setObjectName("label_140")
        self.label_141 = QtWidgets.QLabel(self.tab_17)
        self.label_141.setGeometry(QtCore.QRect(79, 130, 131, 20))
        self.label_141.setObjectName("label_141")
        self.label_142 = QtWidgets.QLabel(self.tab_17)
        self.label_142.setGeometry(QtCore.QRect(550, 70, 131, 20))
        self.label_142.setObjectName("label_142")
        self.label_143 = QtWidgets.QLabel(self.tab_17)
        self.label_143.setGeometry(QtCore.QRect(800, 70, 41, 20))
        self.label_143.setObjectName("label_143")
        self.lne_categoria_4 = QtWidgets.QLineEdit(self.tab_17)
        self.lne_categoria_4.setGeometry(QtCore.QRect(690, 100, 101, 20))
        self.lne_categoria_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_categoria_4.setText("")
        self.lne_categoria_4.setObjectName("lne_categoria_4")
        self.label_144 = QtWidgets.QLabel(self.tab_17)
        self.label_144.setGeometry(QtCore.QRect(550, 100, 71, 20))
        self.label_144.setObjectName("label_144")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_2.setGeometry(QtCore.QRect(3, 10, 941, 411))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/hombre-en-el-escritorio-de-la-oficina-con-un-ordenador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_17, icon1, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.lne_garante_domicilio_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_domicilio_4.setGeometry(QtCore.QRect(160, 135, 300, 20))
        self.lne_garante_domicilio_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_domicilio_4.setObjectName("lne_garante_domicilio_4")
        self.label_145 = QtWidgets.QLabel(self.tab_18)
        self.label_145.setGeometry(QtCore.QRect(19, 232, 121, 16))
        self.label_145.setObjectName("label_145")
        self.lne_garante_nombre_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nombre_4.setGeometry(QtCore.QRect(430, 30, 181, 23))
        self.lne_garante_nombre_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nombre_4.setObjectName("lne_garante_nombre_4")
        self.label_146 = QtWidgets.QLabel(self.tab_18)
        self.label_146.setGeometry(QtCore.QRect(210, 67, 52, 16))
        self.label_146.setObjectName("label_146")
        self.label_147 = QtWidgets.QLabel(self.tab_18)
        self.label_147.setGeometry(QtCore.QRect(19, 169, 121, 16))
        self.label_147.setObjectName("label_147")
        self.label_148 = QtWidgets.QLabel(self.tab_18)
        self.label_148.setGeometry(QtCore.QRect(490, 169, 131, 16))
        self.label_148.setObjectName("label_148")
        self.lne_garante_barrio_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_barrio_4.setGeometry(QtCore.QRect(630, 133, 300, 20))
        self.lne_garante_barrio_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_barrio_4.setObjectName("lne_garante_barrio_4")
        self.lne_garante_limite_credito_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_limite_credito_4.setGeometry(QtCore.QRect(160, 199, 300, 20))
        self.lne_garante_limite_credito_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_limite_credito_4.setObjectName("lne_garante_limite_credito_4")
        self.lne_garante_email_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_email_4.setGeometry(QtCore.QRect(630, 170, 300, 20))
        self.lne_garante_email_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_email_4.setObjectName("lne_garante_email_4")
        self.label_149 = QtWidgets.QLabel(self.tab_18)
        self.label_149.setGeometry(QtCore.QRect(19, 101, 141, 16))
        self.label_149.setObjectName("label_149")
        self.label_150 = QtWidgets.QLabel(self.tab_18)
        self.label_150.setGeometry(QtCore.QRect(19, 202, 121, 16))
        self.label_150.setObjectName("label_150")
        self.label_151 = QtWidgets.QLabel(self.tab_18)
        self.label_151.setGeometry(QtCore.QRect(21, 64, 103, 16))
        self.label_151.setObjectName("label_151")
        self.label_152 = QtWidgets.QLabel(self.tab_18)
        self.label_152.setGeometry(QtCore.QRect(490, 136, 131, 16))
        self.label_152.setObjectName("label_152")
        self.label_153 = QtWidgets.QLabel(self.tab_18)
        self.label_153.setGeometry(QtCore.QRect(280, 102, 71, 16))
        self.label_153.setObjectName("label_153")
        self.lne_garante_nro_cliente_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nro_cliente_4.setGeometry(QtCore.QRect(716, 34, 71, 20))
        self.lne_garante_nro_cliente_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente_4.setObjectName("lne_garante_nro_cliente_4")
        self.txte_garante_observaciones_4 = QtWidgets.QTextEdit(self.tab_18)
        self.txte_garante_observaciones_4.setGeometry(QtCore.QRect(20, 260, 911, 81))
        self.txte_garante_observaciones_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_garante_observaciones_4.setObjectName("txte_garante_observaciones_4")
        self.label_154 = QtWidgets.QLabel(self.tab_18)
        self.label_154.setGeometry(QtCore.QRect(360, 33, 71, 16))
        self.label_154.setObjectName("label_154")
        self.label_155 = QtWidgets.QLabel(self.tab_18)
        self.label_155.setGeometry(QtCore.QRect(21, 31, 53, 16))
        self.label_155.setObjectName("label_155")
        self.label_156 = QtWidgets.QLabel(self.tab_18)
        self.label_156.setGeometry(QtCore.QRect(490, 202, 131, 16))
        self.label_156.setObjectName("label_156")
        self.cbx_garante_estado_civil_4 = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_estado_civil_4.setGeometry(QtCore.QRect(630, 202, 180, 20))
        self.cbx_garante_estado_civil_4.setObjectName("cbx_garante_estado_civil_4")
        self.cbx_garante_estado_civil_4.addItem("")
        self.cbx_garante_estado_civil_4.addItem("")
        self.cbx_garante_estado_civil_4.addItem("")
        self.cbx_garante_estado_civil_4.addItem("")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_18)
        self.checkBox_10.setGeometry(QtCore.QRect(820, 30, 85, 21))
        self.checkBox_10.setObjectName("checkBox_10")
        self.cbx_garante_tipo_doc_4 = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_tipo_doc_4.setGeometry(QtCore.QRect(131, 64, 59, 23))
        self.cbx_garante_tipo_doc_4.setObjectName("cbx_garante_tipo_doc_4")
        self.cbx_garante_tipo_doc_4.addItem("")
        self.cbx_garante_tipo_doc_4.addItem("")
        self.cbx_garante_tipo_doc_4.addItem("")
        self.lne_garante_apellido_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_apellido_4.setGeometry(QtCore.QRect(131, 30, 191, 23))
        self.lne_garante_apellido_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_apellido_4.setObjectName("lne_garante_apellido_4")
        self.lne__garante_telefono_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne__garante_telefono_4.setGeometry(QtCore.QRect(160, 167, 300, 20))
        self.lne__garante_telefono_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne__garante_telefono_4.setObjectName("lne__garante_telefono_4")
        self.cbx_garante_ciudad_4 = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_ciudad_4.setGeometry(QtCore.QRect(345, 102, 180, 20))
        self.cbx_garante_ciudad_4.setObjectName("cbx_garante_ciudad_4")
        self.cbx_garante_ciudad_4.addItem("")
        self.label_157 = QtWidgets.QLabel(self.tab_18)
        self.label_157.setGeometry(QtCore.QRect(630, 35, 71, 16))
        self.label_157.setObjectName("label_157")
        self.label_158 = QtWidgets.QLabel(self.tab_18)
        self.label_158.setGeometry(QtCore.QRect(19, 136, 71, 16))
        self.label_158.setObjectName("label_158")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_18)
        self.checkBox_11.setGeometry(QtCore.QRect(820, 60, 85, 21))
        self.checkBox_11.setObjectName("checkBox_11")
        self.lne_garante_nro_doc_4 = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nro_doc_4.setGeometry(QtCore.QRect(270, 66, 125, 23))
        self.lne_garante_nro_doc_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_doc_4.setObjectName("lne_garante_nro_doc_4")
        self.dte_garante_nacimiento_4 = QtWidgets.QDateEdit(self.tab_18)
        self.dte_garante_nacimiento_4.setGeometry(QtCore.QRect(160, 100, 101, 20))
        self.dte_garante_nacimiento_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_garante_nacimiento_4.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_garante_nacimiento_4.setObjectName("dte_garante_nacimiento_4")
        self.tw_garantes_lista_4 = QtWidgets.QTableWidget(self.tab_18)
        self.tw_garantes_lista_4.setGeometry(QtCore.QRect(19, 388, 911, 151))
        self.tw_garantes_lista_4.setObjectName("tw_garantes_lista_4")
        self.tw_garantes_lista_4.setColumnCount(10)
        self.tw_garantes_lista_4.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Descargas/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon2)
        self.tw_garantes_lista_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tw_garantes_lista_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tw_garantes_lista_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_4.setHorizontalHeaderItem(9, item)
        self.boton_agregar_4 = QtWidgets.QPushButton(self.tab_18)
        self.boton_agregar_4.setGeometry(QtCore.QRect(849, 352, 80, 23))
        self.boton_agregar_4.setObjectName("boton_agregar_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_3.setGeometry(QtCore.QRect(3, 10, 941, 561))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_18, icon3, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.ckbx_veraz_4 = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_veraz_4.setGeometry(QtCore.QRect(601, 90, 211, 21))
        self.ckbx_veraz_4.setChecked(True)
        self.ckbx_veraz_4.setObjectName("ckbx_veraz_4")
        self.ckbx_bloqueado_4 = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_bloqueado_4.setGeometry(QtCore.QRect(602, 150, 211, 21))
        self.ckbx_bloqueado_4.setObjectName("ckbx_bloqueado_4")
        self.lne_iva_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lne_iva_4.setGeometry(QtCore.QRect(271, 30, 300, 20))
        self.lne_iva_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_iva_4.setObjectName("lne_iva_4")
        self.lne_cbu_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lne_cbu_4.setGeometry(QtCore.QRect(271, 90, 300, 20))
        self.lne_cbu_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cbu_4.setObjectName("lne_cbu_4")
        self.label_159 = QtWidgets.QLabel(self.tab_19)
        self.label_159.setGeometry(QtCore.QRect(130, 60, 80, 20))
        self.label_159.setObjectName("label_159")
        self.lne_nro_beneficio_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lne_nro_beneficio_4.setGeometry(QtCore.QRect(271, 120, 300, 20))
        self.lne_nro_beneficio_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_beneficio_4.setObjectName("lne_nro_beneficio_4")
        self.label_160 = QtWidgets.QLabel(self.tab_19)
        self.label_160.setGeometry(QtCore.QRect(130, 90, 141, 20))
        self.label_160.setObjectName("label_160")
        self.label_161 = QtWidgets.QLabel(self.tab_19)
        self.label_161.setGeometry(QtCore.QRect(130, 120, 121, 20))
        self.label_161.setObjectName("label_161")
        self.lne_cuit_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lne_cuit_4.setGeometry(QtCore.QRect(271, 60, 300, 20))
        self.lne_cuit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cuit_4.setObjectName("lne_cuit_4")
        self.label_162 = QtWidgets.QLabel(self.tab_19)
        self.label_162.setGeometry(QtCore.QRect(130, 30, 80, 20))
        self.label_162.setObjectName("label_162")
        self.ckbx_jub_pens_4 = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_jub_pens_4.setGeometry(QtCore.QRect(601, 120, 211, 21))
        self.ckbx_jub_pens_4.setObjectName("ckbx_jub_pens_4")
        self.ckbx_facturas_4 = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_facturas_4.setGeometry(QtCore.QRect(601, 60, 211, 21))
        self.ckbx_facturas_4.setChecked(True)
        self.ckbx_facturas_4.setObjectName("ckbx_facturas_4")
        self.rbt_monotributista_4 = QtWidgets.QRadioButton(self.tab_19)
        self.rbt_monotributista_4.setGeometry(QtCore.QRect(600, 30, 111, 21))
        self.rbt_monotributista_4.setObjectName("rbt_monotributista_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_19)
        self.groupBox_4.setGeometry(QtCore.QRect(3, 10, 941, 411))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Íconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_19, icon4, "")
        self.boton_buscar_actualizar_2 = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_actualizar_2.setGeometry(QtCore.QRect(896, 639, 80, 20))
        self.boton_buscar_actualizar_2.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_actualizar_2.setObjectName("boton_buscar_actualizar_2")
        self.boton_buscar_actualizar_3 = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_actualizar_3.setGeometry(QtCore.QRect(806, 639, 80, 20))
        self.boton_buscar_actualizar_3.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_actualizar_3.setObjectName("boton_buscar_actualizar_3")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Íconos/boton-actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon5, "")

        self.retranslateUi(Form_clientes_actualizar)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_actualizar)

    def retranslateUi(self, Form_clientes_actualizar):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_actualizar.setWindowTitle(_translate("Form_clientes_actualizar", "Form"))
        self.boton_buscar_actualizar.setText(_translate("Form_clientes_actualizar", "Buscar"))
        self.label_122.setText(_translate("Form_clientes_actualizar", "DNI:"))
        self.lne_telfono_buscar_2.setText(_translate("Form_clientes_actualizar", "2920-000001"))
        self.label_123.setText(_translate("Form_clientes_actualizar", "Fecha de Nacimiento:"))
        self.dte_nacimiento_buscar_2.setDisplayFormat(_translate("Form_clientes_actualizar", "yyyy/M/dd"))
        self.cbx_estado_civil_buscar_2.setItemText(0, _translate("Form_clientes_actualizar", "Soltero/era"))
        self.cbx_estado_civil_buscar_2.setItemText(1, _translate("Form_clientes_actualizar", "Casado/ada"))
        self.cbx_estado_civil_buscar_2.setItemText(2, _translate("Form_clientes_actualizar", "Viudo/da"))
        self.cbx_estado_civil_buscar_2.setItemText(3, _translate("Form_clientes_actualizar", "Divorsiado/ada"))
        self.label_124.setText(_translate("Form_clientes_actualizar", "Barrio:"))
        self.lne_domicilio_buscar_2.setText(_translate("Form_clientes_actualizar", "Las violestas 68"))
        self.label_125.setText(_translate("Form_clientes_actualizar", "Nombre :"))
        self.label_126.setText(_translate("Form_clientes_actualizar", "Estado Civil:"))
        self.lne_barrio_buscar_2.setText(_translate("Form_clientes_actualizar", "Las flores"))
        self.label_127.setText(_translate("Form_clientes_actualizar", "Teléfono:"))
        self.cbx_ciudad_4.setItemText(0, _translate("Form_clientes_actualizar", "Viedma"))
        self.label_128.setText(_translate("Form_clientes_actualizar", "Tipo Documento:"))
        self.label_129.setText(_translate("Form_clientes_actualizar", "N°  Cliente :"))
        self.lne_nombre_buscar_2.setText(_translate("Form_clientes_actualizar", "Alejandro"))
        self.lne_limite_credito_4.setText(_translate("Form_clientes_actualizar", "10000"))
        self.lne_nro_cliente_buscar_2.setText(_translate("Form_clientes_actualizar", "00-001"))
        self.label_130.setText(_translate("Form_clientes_actualizar", "Email:"))
        self.cbx_tipo_doc_buscar_2.setItemText(0, _translate("Form_clientes_actualizar", "DNI "))
        self.cbx_tipo_doc_buscar_2.setItemText(1, _translate("Form_clientes_actualizar", "CUIL"))
        self.cbx_tipo_doc_buscar_2.setItemText(2, _translate("Form_clientes_actualizar", "CUIT "))
        self.lne_apellido_buscar_2.setText(_translate("Form_clientes_actualizar", "Fernandez"))
        self.label_131.setText(_translate("Form_clientes_actualizar", "Número:"))
        self.label_132.setText(_translate("Form_clientes_actualizar", "Observaciones: "))
        self.label_133.setText(_translate("Form_clientes_actualizar", "Límite por Créditos:"))
        self.label_134.setText(_translate("Form_clientes_actualizar", "Apellido:"))
        self.label_135.setText(_translate("Form_clientes_actualizar", "Ciudad:"))
        self.lne_email_4.setText(_translate("Form_clientes_actualizar", "email@email.com"))
        self.label_136.setText(_translate("Form_clientes_actualizar", "Domicilio :"))
        self.lne_nro_doc_buscar_2.setText(_translate("Form_clientes_actualizar", "5678879"))
        self.ckbx_activo_buscar_2.setText(_translate("Form_clientes_actualizar", "Activo"))
        self.ckbx_inactivo_buscar_2.setText(_translate("Form_clientes_actualizar", "Inactivo"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), _translate("Form_clientes_actualizar", "Datos Personales"))
        self.lne_organismo_4.setText(_translate("Form_clientes_actualizar", "Ministerio de Educación"))
        self.lne_ocupacion_4.setText(_translate("Form_clientes_actualizar", "Auxiliar"))
        self.label_137.setText(_translate("Form_clientes_actualizar", "Sueldo $:"))
        self.label_138.setText(_translate("Form_clientes_actualizar", "Teléfono Laboral:"))
        self.lne_domicilio_laboral_4.setText(_translate("Form_clientes_actualizar", "Las violetas 45"))
        self.lne_telefono_laboral_4.setText(_translate("Form_clientes_actualizar", "2920-000001"))
        self.ckbx_recibo_sueldo_4.setText(_translate("Form_clientes_actualizar", "Posee Recibo de Sueldo"))
        self.label_139.setText(_translate("Form_clientes_actualizar", "Organismo: "))
        self.label_140.setText(_translate("Form_clientes_actualizar", "Ocupación:"))
        self.label_141.setText(_translate("Form_clientes_actualizar", "Domicilio Laboral:"))
        self.label_142.setText(_translate("Form_clientes_actualizar", "Antigüedad Laboral:"))
        self.label_143.setText(_translate("Form_clientes_actualizar", "años"))
        self.label_144.setText(_translate("Form_clientes_actualizar", "Categoría: "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), _translate("Form_clientes_actualizar", "Datos laborales"))
        self.lne_garante_domicilio_4.setText(_translate("Form_clientes_actualizar", "Las violestas 68"))
        self.label_145.setText(_translate("Form_clientes_actualizar", "Observaciones: "))
        self.lne_garante_nombre_4.setText(_translate("Form_clientes_actualizar", "Alejandro"))
        self.label_146.setText(_translate("Form_clientes_actualizar", "Número:"))
        self.label_147.setText(_translate("Form_clientes_actualizar", "Teléfono:"))
        self.label_148.setText(_translate("Form_clientes_actualizar", "Email:"))
        self.lne_garante_barrio_4.setText(_translate("Form_clientes_actualizar", "Las flores"))
        self.lne_garante_limite_credito_4.setText(_translate("Form_clientes_actualizar", "10000"))
        self.lne_garante_email_4.setText(_translate("Form_clientes_actualizar", "email@email.com"))
        self.label_149.setText(_translate("Form_clientes_actualizar", "Fecha de Nacimiento:"))
        self.label_150.setText(_translate("Form_clientes_actualizar", "Límite por Créditos:"))
        self.label_151.setText(_translate("Form_clientes_actualizar", "Tipo Documento:"))
        self.label_152.setText(_translate("Form_clientes_actualizar", "Barrio:"))
        self.label_153.setText(_translate("Form_clientes_actualizar", "Ciudad:"))
        self.lne_garante_nro_cliente_4.setText(_translate("Form_clientes_actualizar", "00-001"))
        self.label_154.setText(_translate("Form_clientes_actualizar", "Nombre :"))
        self.label_155.setText(_translate("Form_clientes_actualizar", "Apellido:"))
        self.label_156.setText(_translate("Form_clientes_actualizar", "Estado Civil:"))
        self.cbx_garante_estado_civil_4.setItemText(0, _translate("Form_clientes_actualizar", "Soltero/era"))
        self.cbx_garante_estado_civil_4.setItemText(1, _translate("Form_clientes_actualizar", "Casado/ada"))
        self.cbx_garante_estado_civil_4.setItemText(2, _translate("Form_clientes_actualizar", "Viudo/da"))
        self.cbx_garante_estado_civil_4.setItemText(3, _translate("Form_clientes_actualizar", "Divorsiado/ada"))
        self.checkBox_10.setText(_translate("Form_clientes_actualizar", "Activo"))
        self.cbx_garante_tipo_doc_4.setItemText(0, _translate("Form_clientes_actualizar", "DNI "))
        self.cbx_garante_tipo_doc_4.setItemText(1, _translate("Form_clientes_actualizar", "CUIL"))
        self.cbx_garante_tipo_doc_4.setItemText(2, _translate("Form_clientes_actualizar", "CUIT "))
        self.lne_garante_apellido_4.setText(_translate("Form_clientes_actualizar", "Fernandez"))
        self.lne__garante_telefono_4.setText(_translate("Form_clientes_actualizar", "2920-000001"))
        self.cbx_garante_ciudad_4.setItemText(0, _translate("Form_clientes_actualizar", "Viedma"))
        self.label_157.setText(_translate("Form_clientes_actualizar", "N°  Cliente :"))
        self.label_158.setText(_translate("Form_clientes_actualizar", "Domicilio :"))
        self.checkBox_11.setText(_translate("Form_clientes_actualizar", "Inactivo"))
        self.lne_garante_nro_doc_4.setText(_translate("Form_clientes_actualizar", "5678879"))
        self.dte_garante_nacimiento_4.setDisplayFormat(_translate("Form_clientes_actualizar", "yyyy/M/dd"))
        item = self.tw_garantes_lista_4.verticalHeaderItem(0)
        item.setText(_translate("Form_clientes_actualizar", "Garante Princ."))
        item = self.tw_garantes_lista_4.verticalHeaderItem(1)
        item.setText(_translate("Form_clientes_actualizar", "Garante Sec."))
        item = self.tw_garantes_lista_4.verticalHeaderItem(2)
        item.setText(_translate("Form_clientes_actualizar", "Otro Garante"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(0)
        item.setText(_translate("Form_clientes_actualizar", "Apellido"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(1)
        item.setText(_translate("Form_clientes_actualizar", "Nombre"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(2)
        item.setText(_translate("Form_clientes_actualizar", "Nro. Cliente"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(3)
        item.setText(_translate("Form_clientes_actualizar", "Tipo Doc."))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(4)
        item.setText(_translate("Form_clientes_actualizar", "Número"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(5)
        item.setText(_translate("Form_clientes_actualizar", "F. Nacimiento"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(6)
        item.setText(_translate("Form_clientes_actualizar", "Ciudad"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(7)
        item.setText(_translate("Form_clientes_actualizar", "Domicilio"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(8)
        item.setText(_translate("Form_clientes_actualizar", "Teléfono"))
        item = self.tw_garantes_lista_4.horizontalHeaderItem(9)
        item.setText(_translate("Form_clientes_actualizar", "Estado"))
        self.boton_agregar_4.setText(_translate("Form_clientes_actualizar", "Agregar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), _translate("Form_clientes_actualizar", "Datos Garante"))
        self.ckbx_veraz_4.setText(_translate("Form_clientes_actualizar", "Figura en el Veraz"))
        self.ckbx_bloqueado_4.setText(_translate("Form_clientes_actualizar", "Cliente Bloqueado"))
        self.lne_iva_4.setText(_translate("Form_clientes_actualizar", "Responsable Inscripto"))
        self.lne_cbu_4.setText(_translate("Form_clientes_actualizar", "00451597859478396574780"))
        self.label_159.setText(_translate("Form_clientes_actualizar", "N° CUIT:"))
        self.lne_nro_beneficio_4.setText(_translate("Form_clientes_actualizar", "00345687"))
        self.label_160.setText(_translate("Form_clientes_actualizar", "N° CBU:"))
        self.label_161.setText(_translate("Form_clientes_actualizar", "N° Beneficio:"))
        self.lne_cuit_4.setText(_translate("Form_clientes_actualizar", "00-5678879-00"))
        self.label_162.setText(_translate("Form_clientes_actualizar", "Tipo IVA:"))
        self.ckbx_jub_pens_4.setText(_translate("Form_clientes_actualizar", "Es Jubilado / Pensionado"))
        self.ckbx_facturas_4.setText(_translate("Form_clientes_actualizar", "Presentó Facturas de Luz, Gas"))
        self.rbt_monotributista_4.setText(_translate("Form_clientes_actualizar", "Monotributista"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("Form_clientes_actualizar", "Otros Datos"))
        self.boton_buscar_actualizar_2.setText(_translate("Form_clientes_actualizar", "Actualizar"))
        self.boton_buscar_actualizar_3.setText(_translate("Form_clientes_actualizar", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_actualizar", "Actualizar Cliente"))

