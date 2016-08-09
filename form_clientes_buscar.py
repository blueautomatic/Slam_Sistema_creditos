# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_buscar.ui'
#
# Created: Wed Aug  3 13:20:07 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_buscar(object):
    def setupUi(self, Form_clientes_buscar):
        Form_clientes_buscar.setObjectName("Form_clientes_buscar")
        Form_clientes_buscar.resize(1020, 720)
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_buscar)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 981, 691))
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 30, 951, 621))
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
        self.lne_telfono_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_telfono_buscar.setGeometry(QtCore.QRect(160, 175, 300, 20))
        self.lne_telfono_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telfono_buscar.setObjectName("lne_telfono_buscar")
        self.label_122 = QtWidgets.QLabel(self.tab_16)
        self.label_122.setGeometry(QtCore.QRect(19, 109, 141, 16))
        self.label_122.setObjectName("label_122")
        self.dte_nacimiento_buscar = QtWidgets.QDateEdit(self.tab_16)
        self.dte_nacimiento_buscar.setGeometry(QtCore.QRect(160, 108, 101, 20))
        self.dte_nacimiento_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_nacimiento_buscar.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_nacimiento_buscar.setObjectName("dte_nacimiento_buscar")
        self.cbx_estado_civil_buscar = QtWidgets.QComboBox(self.tab_16)
        self.cbx_estado_civil_buscar.setGeometry(QtCore.QRect(450, 108, 180, 20))
        self.cbx_estado_civil_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_estado_civil_buscar.setObjectName("cbx_estado_civil_buscar")
        self.cbx_estado_civil_buscar.addItem("")
        self.cbx_estado_civil_buscar.addItem("")
        self.cbx_estado_civil_buscar.addItem("")
        self.cbx_estado_civil_buscar.addItem("")
        self.label_123 = QtWidgets.QLabel(self.tab_16)
        self.label_123.setGeometry(QtCore.QRect(490, 144, 131, 16))
        self.label_123.setObjectName("label_123")
        self.lne_domicilio_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_domicilio_buscar.setGeometry(QtCore.QRect(160, 143, 300, 20))
        self.lne_domicilio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_buscar.setObjectName("lne_domicilio_buscar")
        self.label_124 = QtWidgets.QLabel(self.tab_16)
        self.label_124.setGeometry(QtCore.QRect(360, 41, 71, 16))
        self.label_124.setObjectName("label_124")
        self.label_125 = QtWidgets.QLabel(self.tab_16)
        self.label_125.setGeometry(QtCore.QRect(310, 108, 131, 16))
        self.label_125.setObjectName("label_125")
        self.lne_barrio_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_barrio_buscar.setGeometry(QtCore.QRect(630, 141, 300, 20))
        self.lne_barrio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_barrio_buscar.setObjectName("lne_barrio_buscar")
        self.label_126 = QtWidgets.QLabel(self.tab_16)
        self.label_126.setGeometry(QtCore.QRect(19, 177, 121, 16))
        self.label_126.setObjectName("label_126")
        self.cbx_ciudad_buscar = QtWidgets.QComboBox(self.tab_16)
        self.cbx_ciudad_buscar.setGeometry(QtCore.QRect(555, 178, 180, 20))
        self.cbx_ciudad_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_ciudad_buscar.setObjectName("cbx_ciudad_buscar")
        self.cbx_ciudad_buscar.addItem("")
        self.label_127 = QtWidgets.QLabel(self.tab_16)
        self.label_127.setGeometry(QtCore.QRect(21, 72, 103, 16))
        self.label_127.setObjectName("label_127")
        self.label_128 = QtWidgets.QLabel(self.tab_16)
        self.label_128.setGeometry(QtCore.QRect(630, 43, 71, 16))
        self.label_128.setObjectName("label_128")
        self.lne_nombre_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nombre_buscar.setGeometry(QtCore.QRect(430, 38, 181, 23))
        self.lne_nombre_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre_buscar.setObjectName("lne_nombre_buscar")
        self.lne_limite_credito_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_limite_credito_buscar.setGeometry(QtCore.QRect(160, 207, 300, 20))
        self.lne_limite_credito_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_limite_credito_buscar.setObjectName("lne_limite_credito_buscar")
        self.lne_nro_cliente_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nro_cliente_buscar.setGeometry(QtCore.QRect(716, 42, 71, 20))
        self.lne_nro_cliente_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cliente_buscar.setObjectName("lne_nro_cliente_buscar")
        self.label_129 = QtWidgets.QLabel(self.tab_16)
        self.label_129.setGeometry(QtCore.QRect(490, 207, 131, 16))
        self.label_129.setObjectName("label_129")
        self.cbx_tipo_doc_buscar = QtWidgets.QComboBox(self.tab_16)
        self.cbx_tipo_doc_buscar.setGeometry(QtCore.QRect(131, 72, 59, 23))
        self.cbx_tipo_doc_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_tipo_doc_buscar.setObjectName("cbx_tipo_doc_buscar")
        self.cbx_tipo_doc_buscar.addItem("")
        self.cbx_tipo_doc_buscar.addItem("")
        self.cbx_tipo_doc_buscar.addItem("")
        self.lne_apellido_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_apellido_buscar.setGeometry(QtCore.QRect(131, 38, 191, 23))
        self.lne_apellido_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_buscar.setObjectName("lne_apellido_buscar")
        self.label_130 = QtWidgets.QLabel(self.tab_16)
        self.label_130.setGeometry(QtCore.QRect(210, 75, 52, 16))
        self.label_130.setObjectName("label_130")
        self.label_131 = QtWidgets.QLabel(self.tab_16)
        self.label_131.setGeometry(QtCore.QRect(19, 240, 121, 16))
        self.label_131.setObjectName("label_131")
        self.label_132 = QtWidgets.QLabel(self.tab_16)
        self.label_132.setGeometry(QtCore.QRect(19, 210, 121, 16))
        self.label_132.setObjectName("label_132")
        self.label_133 = QtWidgets.QLabel(self.tab_16)
        self.label_133.setGeometry(QtCore.QRect(21, 39, 53, 16))
        self.label_133.setObjectName("label_133")
        self.label_134 = QtWidgets.QLabel(self.tab_16)
        self.label_134.setGeometry(QtCore.QRect(490, 178, 71, 16))
        self.label_134.setObjectName("label_134")
        self.lne_email_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_email_buscar.setGeometry(QtCore.QRect(630, 208, 300, 20))
        self.lne_email_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_email_buscar.setObjectName("lne_email_buscar")
        self.label_135 = QtWidgets.QLabel(self.tab_16)
        self.label_135.setGeometry(QtCore.QRect(19, 144, 71, 16))
        self.label_135.setObjectName("label_135")
        self.lne_nro_doc_buscar = QtWidgets.QLineEdit(self.tab_16)
        self.lne_nro_doc_buscar.setGeometry(QtCore.QRect(270, 74, 125, 23))
        self.lne_nro_doc_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc_buscar.setObjectName("lne_nro_doc_buscar")
        self.ckbx_activo_buscar = QtWidgets.QCheckBox(self.tab_16)
        self.ckbx_activo_buscar.setGeometry(QtCore.QRect(820, 38, 85, 21))
        self.ckbx_activo_buscar.setObjectName("ckbx_activo_buscar")
        self.ckbx_inactivo_buscar = QtWidgets.QCheckBox(self.tab_16)
        self.ckbx_inactivo_buscar.setGeometry(QtCore.QRect(820, 68, 85, 21))
        self.ckbx_inactivo_buscar.setObjectName("ckbx_inactivo_buscar")
        self.txte_observaciones_buscar = QtWidgets.QTextEdit(self.tab_16)
        self.txte_observaciones_buscar.setGeometry(QtCore.QRect(20, 258, 911, 161))
        self.txte_observaciones_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_observaciones_buscar.setObjectName("txte_observaciones_buscar")
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
        self.lne_organismo_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_organismo_buscar.setGeometry(QtCore.QRect(220, 70, 300, 20))
        self.lne_organismo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_organismo_buscar.setObjectName("lne_organismo_buscar")
        self.lne_ocupacion_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_ocupacion_buscar.setGeometry(QtCore.QRect(220, 40, 300, 20))
        self.lne_ocupacion_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_ocupacion_buscar.setObjectName("lne_ocupacion_buscar")
        self.lne_antiguedad_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_antiguedad_buscar.setGeometry(QtCore.QRect(690, 70, 101, 20))
        self.lne_antiguedad_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_antiguedad_buscar.setText("")
        self.lne_antiguedad_buscar.setObjectName("lne_antiguedad_buscar")
        self.label_136 = QtWidgets.QLabel(self.tab_17)
        self.label_136.setGeometry(QtCore.QRect(550, 40, 80, 20))
        self.label_136.setObjectName("label_136")
        self.label_137 = QtWidgets.QLabel(self.tab_17)
        self.label_137.setGeometry(QtCore.QRect(79, 100, 141, 20))
        self.label_137.setObjectName("label_137")
        self.lne_domicilio_laboral_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_domicilio_laboral_buscar.setGeometry(QtCore.QRect(220, 130, 300, 20))
        self.lne_domicilio_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_laboral_buscar.setObjectName("lne_domicilio_laboral_buscar")
        self.lne_telefono_laboral_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_telefono_laboral_buscar.setGeometry(QtCore.QRect(220, 100, 300, 20))
        self.lne_telefono_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_laboral_buscar.setObjectName("lne_telefono_laboral_buscar")
        self.lne_sueldo_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_sueldo_buscar.setGeometry(QtCore.QRect(690, 40, 101, 20))
        self.lne_sueldo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_sueldo_buscar.setText("")
        self.lne_sueldo_buscar.setObjectName("lne_sueldo_buscar")
        self.ckbx_recibo_sueldo_4 = QtWidgets.QCheckBox(self.tab_17)
        self.ckbx_recibo_sueldo_4.setGeometry(QtCore.QRect(550, 130, 211, 21))
        self.ckbx_recibo_sueldo_4.setChecked(True)
        self.ckbx_recibo_sueldo_4.setObjectName("ckbx_recibo_sueldo_4")
        self.label_138 = QtWidgets.QLabel(self.tab_17)
        self.label_138.setGeometry(QtCore.QRect(79, 70, 80, 20))
        self.label_138.setObjectName("label_138")
        self.label_139 = QtWidgets.QLabel(self.tab_17)
        self.label_139.setGeometry(QtCore.QRect(79, 40, 80, 20))
        self.label_139.setObjectName("label_139")
        self.label_140 = QtWidgets.QLabel(self.tab_17)
        self.label_140.setGeometry(QtCore.QRect(79, 130, 131, 20))
        self.label_140.setObjectName("label_140")
        self.label_141 = QtWidgets.QLabel(self.tab_17)
        self.label_141.setGeometry(QtCore.QRect(550, 70, 131, 20))
        self.label_141.setObjectName("label_141")
        self.label_142 = QtWidgets.QLabel(self.tab_17)
        self.label_142.setGeometry(QtCore.QRect(800, 70, 41, 20))
        self.label_142.setObjectName("label_142")
        self.lne_categoria_buscar = QtWidgets.QLineEdit(self.tab_17)
        self.lne_categoria_buscar.setGeometry(QtCore.QRect(690, 100, 101, 20))
        self.lne_categoria_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_categoria_buscar.setText("")
        self.lne_categoria_buscar.setObjectName("lne_categoria_buscar")
        self.label_143 = QtWidgets.QLabel(self.tab_17)
        self.label_143.setGeometry(QtCore.QRect(550, 100, 71, 20))
        self.label_143.setObjectName("label_143")
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
        self.lne_garante_domicilio_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_domicilio_buscar.setGeometry(QtCore.QRect(160, 135, 300, 20))
        self.lne_garante_domicilio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_domicilio_buscar.setObjectName("lne_garante_domicilio_buscar")
        self.label_144 = QtWidgets.QLabel(self.tab_18)
        self.label_144.setGeometry(QtCore.QRect(19, 232, 121, 16))
        self.label_144.setObjectName("label_144")
        self.lne_garante_nombre_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nombre_buscar.setGeometry(QtCore.QRect(430, 30, 181, 23))
        self.lne_garante_nombre_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nombre_buscar.setObjectName("lne_garante_nombre_buscar")
        self.label_145 = QtWidgets.QLabel(self.tab_18)
        self.label_145.setGeometry(QtCore.QRect(210, 67, 52, 16))
        self.label_145.setObjectName("label_145")
        self.label_146 = QtWidgets.QLabel(self.tab_18)
        self.label_146.setGeometry(QtCore.QRect(19, 169, 121, 16))
        self.label_146.setObjectName("label_146")
        self.label_147 = QtWidgets.QLabel(self.tab_18)
        self.label_147.setGeometry(QtCore.QRect(490, 169, 131, 16))
        self.label_147.setObjectName("label_147")
        self.lne_garante_barrio_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_barrio_buscar.setGeometry(QtCore.QRect(630, 133, 300, 20))
        self.lne_garante_barrio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_barrio_buscar.setObjectName("lne_garante_barrio_buscar")
        self.lne_garante_limite_credito_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_limite_credito_buscar.setGeometry(QtCore.QRect(160, 199, 300, 20))
        self.lne_garante_limite_credito_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_limite_credito_buscar.setObjectName("lne_garante_limite_credito_buscar")
        self.lne_garante_email_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_email_buscar.setGeometry(QtCore.QRect(630, 170, 300, 20))
        self.lne_garante_email_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_email_buscar.setObjectName("lne_garante_email_buscar")
        self.label_148 = QtWidgets.QLabel(self.tab_18)
        self.label_148.setGeometry(QtCore.QRect(19, 101, 141, 16))
        self.label_148.setObjectName("label_148")
        self.label_149 = QtWidgets.QLabel(self.tab_18)
        self.label_149.setGeometry(QtCore.QRect(19, 202, 121, 16))
        self.label_149.setObjectName("label_149")
        self.label_150 = QtWidgets.QLabel(self.tab_18)
        self.label_150.setGeometry(QtCore.QRect(21, 64, 103, 16))
        self.label_150.setObjectName("label_150")
        self.label_151 = QtWidgets.QLabel(self.tab_18)
        self.label_151.setGeometry(QtCore.QRect(490, 136, 131, 16))
        self.label_151.setObjectName("label_151")
        self.label_152 = QtWidgets.QLabel(self.tab_18)
        self.label_152.setGeometry(QtCore.QRect(280, 102, 71, 16))
        self.label_152.setObjectName("label_152")
        self.lne_garante_nro_cliente_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nro_cliente_buscar.setGeometry(QtCore.QRect(716, 34, 71, 20))
        self.lne_garante_nro_cliente_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente_buscar.setObjectName("lne_garante_nro_cliente_buscar")
        self.txte_garante_observaciones_buscar = QtWidgets.QTextEdit(self.tab_18)
        self.txte_garante_observaciones_buscar.setGeometry(QtCore.QRect(20, 260, 911, 81))
        self.txte_garante_observaciones_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_garante_observaciones_buscar.setObjectName("txte_garante_observaciones_buscar")
        self.label_153 = QtWidgets.QLabel(self.tab_18)
        self.label_153.setGeometry(QtCore.QRect(360, 33, 71, 16))
        self.label_153.setObjectName("label_153")
        self.label_154 = QtWidgets.QLabel(self.tab_18)
        self.label_154.setGeometry(QtCore.QRect(21, 31, 53, 16))
        self.label_154.setObjectName("label_154")
        self.label_155 = QtWidgets.QLabel(self.tab_18)
        self.label_155.setGeometry(QtCore.QRect(490, 202, 131, 16))
        self.label_155.setObjectName("label_155")
        self.cbx_garante_estado_civil_buscar = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_estado_civil_buscar.setGeometry(QtCore.QRect(630, 202, 180, 20))
        self.cbx_garante_estado_civil_buscar.setObjectName("cbx_garante_estado_civil_buscar")
        self.cbx_garante_estado_civil_buscar.addItem("")
        self.cbx_garante_estado_civil_buscar.addItem("")
        self.cbx_garante_estado_civil_buscar.addItem("")
        self.cbx_garante_estado_civil_buscar.addItem("")
        self.ckbx_garante_activo_buscar = QtWidgets.QCheckBox(self.tab_18)
        self.ckbx_garante_activo_buscar.setGeometry(QtCore.QRect(820, 30, 85, 21))
        self.ckbx_garante_activo_buscar.setObjectName("ckbx_garante_activo_buscar")
        self.cbx_garante_tipo_doc_buscar = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_tipo_doc_buscar.setGeometry(QtCore.QRect(131, 64, 59, 23))
        self.cbx_garante_tipo_doc_buscar.setObjectName("cbx_garante_tipo_doc_buscar")
        self.cbx_garante_tipo_doc_buscar.addItem("")
        self.cbx_garante_tipo_doc_buscar.addItem("")
        self.cbx_garante_tipo_doc_buscar.addItem("")
        self.lne_garante_apellido_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_apellido_buscar.setGeometry(QtCore.QRect(131, 30, 191, 23))
        self.lne_garante_apellido_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_apellido_buscar.setObjectName("lne_garante_apellido_buscar")
        self.lne__garante_telefono_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne__garante_telefono_buscar.setGeometry(QtCore.QRect(160, 167, 300, 20))
        self.lne__garante_telefono_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne__garante_telefono_buscar.setObjectName("lne__garante_telefono_buscar")
        self.cbx_garante_ciudad_buscar = QtWidgets.QComboBox(self.tab_18)
        self.cbx_garante_ciudad_buscar.setGeometry(QtCore.QRect(345, 102, 180, 20))
        self.cbx_garante_ciudad_buscar.setObjectName("cbx_garante_ciudad_buscar")
        self.cbx_garante_ciudad_buscar.addItem("")
        self.label_156 = QtWidgets.QLabel(self.tab_18)
        self.label_156.setGeometry(QtCore.QRect(630, 35, 71, 16))
        self.label_156.setObjectName("label_156")
        self.label_157 = QtWidgets.QLabel(self.tab_18)
        self.label_157.setGeometry(QtCore.QRect(19, 136, 71, 16))
        self.label_157.setObjectName("label_157")
        self.ckbx_garante_inactivo_buscar = QtWidgets.QCheckBox(self.tab_18)
        self.ckbx_garante_inactivo_buscar.setGeometry(QtCore.QRect(820, 60, 85, 21))
        self.ckbx_garante_inactivo_buscar.setObjectName("ckbx_garante_inactivo_buscar")
        self.lne_garante_nro_doc_buscar = QtWidgets.QLineEdit(self.tab_18)
        self.lne_garante_nro_doc_buscar.setGeometry(QtCore.QRect(270, 66, 125, 23))
        self.lne_garante_nro_doc_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_doc_buscar.setObjectName("lne_garante_nro_doc_buscar")
        self.dte_garante_nacimiento_buscar = QtWidgets.QDateEdit(self.tab_18)
        self.dte_garante_nacimiento_buscar.setGeometry(QtCore.QRect(160, 100, 101, 20))
        self.dte_garante_nacimiento_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_garante_nacimiento_buscar.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_garante_nacimiento_buscar.setObjectName("dte_garante_nacimiento_buscar")
        self.tw_garantes_lista_buscar = QtWidgets.QTableWidget(self.tab_18)
        self.tw_garantes_lista_buscar.setGeometry(QtCore.QRect(19, 388, 911, 151))
        self.tw_garantes_lista_buscar.setObjectName("tw_garantes_lista_buscar")
        self.tw_garantes_lista_buscar.setColumnCount(10)
        self.tw_garantes_lista_buscar.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Descargas/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon2)
        self.tw_garantes_lista_buscar.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tw_garantes_lista_buscar.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tw_garantes_lista_buscar.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista_buscar.setHorizontalHeaderItem(9, item)
        self.boton_agregar_buscar = QtWidgets.QPushButton(self.tab_18)
        self.boton_agregar_buscar.setGeometry(QtCore.QRect(849, 352, 80, 23))
        self.boton_agregar_buscar.setObjectName("boton_agregar_buscar")
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
        self.ckbx_veraz_buscar = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_veraz_buscar.setGeometry(QtCore.QRect(601, 90, 211, 21))
        self.ckbx_veraz_buscar.setChecked(True)
        self.ckbx_veraz_buscar.setObjectName("ckbx_veraz_buscar")
        self.ckbx_bloqueado_buscar = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_bloqueado_buscar.setGeometry(QtCore.QRect(602, 150, 211, 21))
        self.ckbx_bloqueado_buscar.setObjectName("ckbx_bloqueado_buscar")
        self.lne_iva_buscar = QtWidgets.QLineEdit(self.tab_19)
        self.lne_iva_buscar.setGeometry(QtCore.QRect(271, 30, 300, 20))
        self.lne_iva_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_iva_buscar.setObjectName("lne_iva_buscar")
        self.lne_cbu_buscar = QtWidgets.QLineEdit(self.tab_19)
        self.lne_cbu_buscar.setGeometry(QtCore.QRect(271, 90, 300, 20))
        self.lne_cbu_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cbu_buscar.setObjectName("lne_cbu_buscar")
        self.label_158 = QtWidgets.QLabel(self.tab_19)
        self.label_158.setGeometry(QtCore.QRect(130, 60, 80, 20))
        self.label_158.setObjectName("label_158")
        self.lne_nro_beneficio_buscar = QtWidgets.QLineEdit(self.tab_19)
        self.lne_nro_beneficio_buscar.setGeometry(QtCore.QRect(271, 120, 300, 20))
        self.lne_nro_beneficio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_beneficio_buscar.setObjectName("lne_nro_beneficio_buscar")
        self.label_159 = QtWidgets.QLabel(self.tab_19)
        self.label_159.setGeometry(QtCore.QRect(130, 90, 141, 20))
        self.label_159.setObjectName("label_159")
        self.label_160 = QtWidgets.QLabel(self.tab_19)
        self.label_160.setGeometry(QtCore.QRect(130, 120, 121, 20))
        self.label_160.setObjectName("label_160")
        self.lne_cuit_buscar = QtWidgets.QLineEdit(self.tab_19)
        self.lne_cuit_buscar.setGeometry(QtCore.QRect(271, 60, 300, 20))
        self.lne_cuit_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cuit_buscar.setObjectName("lne_cuit_buscar")
        self.label_161 = QtWidgets.QLabel(self.tab_19)
        self.label_161.setGeometry(QtCore.QRect(130, 30, 80, 20))
        self.label_161.setObjectName("label_161")
        self.ckbx_jub_pens_buscar = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_jub_pens_buscar.setGeometry(QtCore.QRect(601, 120, 211, 21))
        self.ckbx_jub_pens_buscar.setObjectName("ckbx_jub_pens_buscar")
        self.ckbx_facturas_buscar = QtWidgets.QCheckBox(self.tab_19)
        self.ckbx_facturas_buscar.setGeometry(QtCore.QRect(601, 60, 211, 21))
        self.ckbx_facturas_buscar.setChecked(True)
        self.ckbx_facturas_buscar.setObjectName("ckbx_facturas_buscar")
        self.rbt_monotributista_buscar = QtWidgets.QRadioButton(self.tab_19)
        self.rbt_monotributista_buscar.setGeometry(QtCore.QRect(600, 30, 111, 21))
        self.rbt_monotributista_buscar.setObjectName("rbt_monotributista_buscar")
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
        self.boton_buscar_buscar_2 = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_buscar_2.setGeometry(QtCore.QRect(880, -20, 80, 20))
        self.boton_buscar_buscar_2.setObjectName("boton_buscar_buscar_2")
        self.label_162 = QtWidgets.QLabel(self.tab)
        self.label_162.setGeometry(QtCore.QRect(660, -18, 59, 15))
        self.label_162.setObjectName("label_162")
        self.lne_dni_filtro_buscar_2 = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_buscar_2.setGeometry(QtCore.QRect(719, -20, 151, 20))
        self.lne_dni_filtro_buscar_2.setObjectName("lne_dni_filtro_buscar_2")
        self.boton_buscar_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_buscar.setGeometry(QtCore.QRect(869, 9, 80, 20))
        self.boton_buscar_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_buscar.setObjectName("boton_buscar_buscar")
        self.label_121 = QtWidgets.QLabel(self.tab)
        self.label_121.setGeometry(QtCore.QRect(678, 12, 31, 16))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("background-color: rgb(207, 100, 76);\n"
"font: 75 10pt \"KacstOne\";")
        self.label_121.setObjectName("label_121")
        self.lne_dni_filtro_buscar = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_buscar.setGeometry(QtCore.QRect(709, 10, 151, 20))
        self.lne_dni_filtro_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_buscar.setObjectName("lne_dni_filtro_buscar")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Íconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon5, "")

        self.retranslateUi(Form_clientes_buscar)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_buscar)

    def retranslateUi(self, Form_clientes_buscar):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_buscar.setWindowTitle(_translate("Form_clientes_buscar", "Form"))
        self.lne_telfono_buscar.setText(_translate("Form_clientes_buscar", "2920-000001"))
        self.label_122.setText(_translate("Form_clientes_buscar", "Fecha de Nacimiento:"))
        self.dte_nacimiento_buscar.setDisplayFormat(_translate("Form_clientes_buscar", "yyyy/M/dd"))
        self.cbx_estado_civil_buscar.setItemText(0, _translate("Form_clientes_buscar", "Soltero/era"))
        self.cbx_estado_civil_buscar.setItemText(1, _translate("Form_clientes_buscar", "Casado/ada"))
        self.cbx_estado_civil_buscar.setItemText(2, _translate("Form_clientes_buscar", "Viudo/da"))
        self.cbx_estado_civil_buscar.setItemText(3, _translate("Form_clientes_buscar", "Divorsiado/ada"))
        self.label_123.setText(_translate("Form_clientes_buscar", "Barrio:"))
        self.lne_domicilio_buscar.setText(_translate("Form_clientes_buscar", "Las violestas 68"))
        self.label_124.setText(_translate("Form_clientes_buscar", "Nombre :"))
        self.label_125.setText(_translate("Form_clientes_buscar", "Estado Civil:"))
        self.lne_barrio_buscar.setText(_translate("Form_clientes_buscar", "Las flores"))
        self.label_126.setText(_translate("Form_clientes_buscar", "Teléfono:"))
        self.cbx_ciudad_buscar.setItemText(0, _translate("Form_clientes_buscar", "Viedma"))
        self.label_127.setText(_translate("Form_clientes_buscar", "Tipo Documento:"))
        self.label_128.setText(_translate("Form_clientes_buscar", "N°  Cliente :"))
        self.lne_nombre_buscar.setText(_translate("Form_clientes_buscar", "Alejandro"))
        self.lne_limite_credito_buscar.setText(_translate("Form_clientes_buscar", "10000"))
        self.lne_nro_cliente_buscar.setText(_translate("Form_clientes_buscar", "00-001"))
        self.label_129.setText(_translate("Form_clientes_buscar", "Email:"))
        self.cbx_tipo_doc_buscar.setItemText(0, _translate("Form_clientes_buscar", "DNI "))
        self.cbx_tipo_doc_buscar.setItemText(1, _translate("Form_clientes_buscar", "CUIL"))
        self.cbx_tipo_doc_buscar.setItemText(2, _translate("Form_clientes_buscar", "CUIT "))
        self.lne_apellido_buscar.setText(_translate("Form_clientes_buscar", "Fernandez"))
        self.label_130.setText(_translate("Form_clientes_buscar", "Número:"))
        self.label_131.setText(_translate("Form_clientes_buscar", "Observaciones: "))
        self.label_132.setText(_translate("Form_clientes_buscar", "Límite por Créditos:"))
        self.label_133.setText(_translate("Form_clientes_buscar", "Apellido:"))
        self.label_134.setText(_translate("Form_clientes_buscar", "Ciudad:"))
        self.lne_email_buscar.setText(_translate("Form_clientes_buscar", "email@email.com"))
        self.label_135.setText(_translate("Form_clientes_buscar", "Domicilio :"))
        self.lne_nro_doc_buscar.setText(_translate("Form_clientes_buscar", "5678879"))
        self.ckbx_activo_buscar.setText(_translate("Form_clientes_buscar", "Activo"))
        self.ckbx_inactivo_buscar.setText(_translate("Form_clientes_buscar", "Inactivo"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), _translate("Form_clientes_buscar", "Datos Personales"))
        self.lne_organismo_buscar.setText(_translate("Form_clientes_buscar", "Ministerio de Educación"))
        self.lne_ocupacion_buscar.setText(_translate("Form_clientes_buscar", "Auxiliar"))
        self.label_136.setText(_translate("Form_clientes_buscar", "Sueldo $:"))
        self.label_137.setText(_translate("Form_clientes_buscar", "Teléfono Laboral:"))
        self.lne_domicilio_laboral_buscar.setText(_translate("Form_clientes_buscar", "Las violetas 45"))
        self.lne_telefono_laboral_buscar.setText(_translate("Form_clientes_buscar", "2920-000001"))
        self.ckbx_recibo_sueldo_4.setText(_translate("Form_clientes_buscar", "Posee Recibo de Sueldo"))
        self.label_138.setText(_translate("Form_clientes_buscar", "Organismo: "))
        self.label_139.setText(_translate("Form_clientes_buscar", "Ocupación:"))
        self.label_140.setText(_translate("Form_clientes_buscar", "Domicilio Laboral:"))
        self.label_141.setText(_translate("Form_clientes_buscar", "Antigüedad Laboral:"))
        self.label_142.setText(_translate("Form_clientes_buscar", "años"))
        self.label_143.setText(_translate("Form_clientes_buscar", "Categoría: "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), _translate("Form_clientes_buscar", "Datos laborales"))
        self.lne_garante_domicilio_buscar.setText(_translate("Form_clientes_buscar", "Las violestas 68"))
        self.label_144.setText(_translate("Form_clientes_buscar", "Observaciones: "))
        self.lne_garante_nombre_buscar.setText(_translate("Form_clientes_buscar", "Alejandro"))
        self.label_145.setText(_translate("Form_clientes_buscar", "Número:"))
        self.label_146.setText(_translate("Form_clientes_buscar", "Teléfono:"))
        self.label_147.setText(_translate("Form_clientes_buscar", "Email:"))
        self.lne_garante_barrio_buscar.setText(_translate("Form_clientes_buscar", "Las flores"))
        self.lne_garante_limite_credito_buscar.setText(_translate("Form_clientes_buscar", "10000"))
        self.lne_garante_email_buscar.setText(_translate("Form_clientes_buscar", "email@email.com"))
        self.label_148.setText(_translate("Form_clientes_buscar", "Fecha de Nacimiento:"))
        self.label_149.setText(_translate("Form_clientes_buscar", "Límite por Créditos:"))
        self.label_150.setText(_translate("Form_clientes_buscar", "Tipo Documento:"))
        self.label_151.setText(_translate("Form_clientes_buscar", "Barrio:"))
        self.label_152.setText(_translate("Form_clientes_buscar", "Ciudad:"))
        self.lne_garante_nro_cliente_buscar.setText(_translate("Form_clientes_buscar", "00-001"))
        self.label_153.setText(_translate("Form_clientes_buscar", "Nombre :"))
        self.label_154.setText(_translate("Form_clientes_buscar", "Apellido:"))
        self.label_155.setText(_translate("Form_clientes_buscar", "Estado Civil:"))
        self.cbx_garante_estado_civil_buscar.setItemText(0, _translate("Form_clientes_buscar", "Soltero/era"))
        self.cbx_garante_estado_civil_buscar.setItemText(1, _translate("Form_clientes_buscar", "Casado/ada"))
        self.cbx_garante_estado_civil_buscar.setItemText(2, _translate("Form_clientes_buscar", "Viudo/da"))
        self.cbx_garante_estado_civil_buscar.setItemText(3, _translate("Form_clientes_buscar", "Divorsiado/ada"))
        self.ckbx_garante_activo_buscar.setText(_translate("Form_clientes_buscar", "Activo"))
        self.cbx_garante_tipo_doc_buscar.setItemText(0, _translate("Form_clientes_buscar", "DNI "))
        self.cbx_garante_tipo_doc_buscar.setItemText(1, _translate("Form_clientes_buscar", "CUIL"))
        self.cbx_garante_tipo_doc_buscar.setItemText(2, _translate("Form_clientes_buscar", "CUIT "))
        self.lne_garante_apellido_buscar.setText(_translate("Form_clientes_buscar", "Fernandez"))
        self.lne__garante_telefono_buscar.setText(_translate("Form_clientes_buscar", "2920-000001"))
        self.cbx_garante_ciudad_buscar.setItemText(0, _translate("Form_clientes_buscar", "Viedma"))
        self.label_156.setText(_translate("Form_clientes_buscar", "N°  Cliente :"))
        self.label_157.setText(_translate("Form_clientes_buscar", "Domicilio :"))
        self.ckbx_garante_inactivo_buscar.setText(_translate("Form_clientes_buscar", "Inactivo"))
        self.lne_garante_nro_doc_buscar.setText(_translate("Form_clientes_buscar", "5678879"))
        self.dte_garante_nacimiento_buscar.setDisplayFormat(_translate("Form_clientes_buscar", "yyyy/M/dd"))
        item = self.tw_garantes_lista_buscar.verticalHeaderItem(0)
        item.setText(_translate("Form_clientes_buscar", "Garante Princ."))
        item = self.tw_garantes_lista_buscar.verticalHeaderItem(1)
        item.setText(_translate("Form_clientes_buscar", "Garante Sec."))
        item = self.tw_garantes_lista_buscar.verticalHeaderItem(2)
        item.setText(_translate("Form_clientes_buscar", "Otro Garante"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form_clientes_buscar", "Apellido"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form_clientes_buscar", "Nombre"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form_clientes_buscar", "Nro. Cliente"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form_clientes_buscar", "Tipo Doc."))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form_clientes_buscar", "Número"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(5)
        item.setText(_translate("Form_clientes_buscar", "F. Nacimiento"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(6)
        item.setText(_translate("Form_clientes_buscar", "Ciudad"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(7)
        item.setText(_translate("Form_clientes_buscar", "Domicilio"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(8)
        item.setText(_translate("Form_clientes_buscar", "Teléfono"))
        item = self.tw_garantes_lista_buscar.horizontalHeaderItem(9)
        item.setText(_translate("Form_clientes_buscar", "Estado"))
        self.boton_agregar_buscar.setText(_translate("Form_clientes_buscar", "Agregar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), _translate("Form_clientes_buscar", "Datos Garante"))
        self.ckbx_veraz_buscar.setText(_translate("Form_clientes_buscar", "Figura en el Veraz"))
        self.ckbx_bloqueado_buscar.setText(_translate("Form_clientes_buscar", "Cliente Bloqueado"))
        self.lne_iva_buscar.setText(_translate("Form_clientes_buscar", "Responsable Inscripto"))
        self.lne_cbu_buscar.setText(_translate("Form_clientes_buscar", "00451597859478396574780"))
        self.label_158.setText(_translate("Form_clientes_buscar", "N° CUIT:"))
        self.lne_nro_beneficio_buscar.setText(_translate("Form_clientes_buscar", "00345687"))
        self.label_159.setText(_translate("Form_clientes_buscar", "N° CBU:"))
        self.label_160.setText(_translate("Form_clientes_buscar", "N° Beneficio:"))
        self.lne_cuit_buscar.setText(_translate("Form_clientes_buscar", "00-5678879-00"))
        self.label_161.setText(_translate("Form_clientes_buscar", "Tipo IVA:"))
        self.ckbx_jub_pens_buscar.setText(_translate("Form_clientes_buscar", "Es Jubilado / Pensionado"))
        self.ckbx_facturas_buscar.setText(_translate("Form_clientes_buscar", "Presentó Facturas de Luz, Gas"))
        self.rbt_monotributista_buscar.setText(_translate("Form_clientes_buscar", "Monotributista"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("Form_clientes_buscar", "Otros Datos"))
        self.boton_buscar_buscar_2.setText(_translate("Form_clientes_buscar", "Buscar"))
        self.label_162.setText(_translate("Form_clientes_buscar", "DNI:"))
        self.boton_buscar_buscar.setText(_translate("Form_clientes_buscar", "Buscar"))
        self.label_121.setText(_translate("Form_clientes_buscar", "DNI:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_buscar", "Buscar Cliente"))

