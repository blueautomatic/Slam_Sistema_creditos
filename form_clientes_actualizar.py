# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_actualizar.ui'
#
# Created: Wed Oct 26 10:50:11 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_actualizar(object):
    def setupUi(self, Form_clientes_actualizar):
        Form_clientes_actualizar.setObjectName("Form_clientes_actualizar")
        Form_clientes_actualizar.resize(1027, 679)
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_actualizar)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1001, 651))
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.boton_buscar_actualizar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_actualizar.setGeometry(QtCore.QRect(890, 30, 80, 30))
        self.boton_buscar_actualizar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_actualizar.setObjectName("boton_buscar_actualizar")
        self.label_122 = QtWidgets.QLabel(self.tab)
        self.label_122.setGeometry(QtCore.QRect(689, 34, 31, 20))
        self.label_122.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.label_122.setObjectName("label_122")
        self.lne_dni_filtro_actualizar = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_actualizar.setGeometry(QtCore.QRect(722, 34, 151, 20))
        self.lne_dni_filtro_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_actualizar.setText("")
        self.lne_dni_filtro_actualizar.setObjectName("lne_dni_filtro_actualizar")
        self.tab_widget_actualizar_cliente = QtWidgets.QTabWidget(self.tab)
        self.tab_widget_actualizar_cliente.setEnabled(False)
        self.tab_widget_actualizar_cliente.setGeometry(QtCore.QRect(20, 80, 951, 481))
        self.tab_widget_actualizar_cliente.setStyleSheet("background-color: rgb(239, 235, 231);\n"
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
        self.tab_widget_actualizar_cliente.setObjectName("tab_widget_actualizar_cliente")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.label_136 = QtWidgets.QLabel(self.tab_16)
        self.label_136.setGeometry(QtCore.QRect(19, 144, 71, 16))
        self.label_136.setObjectName("label_136")
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
        self.lne_email_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_email_actualizar.setGeometry(QtCore.QRect(550, 200, 300, 20))
        self.lne_email_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_email_actualizar.setText("")
        self.lne_email_actualizar.setObjectName("lne_email_actualizar")
        self.label_128 = QtWidgets.QLabel(self.groupBox)
        self.label_128.setGeometry(QtCore.QRect(21, 62, 103, 16))
        self.label_128.setObjectName("label_128")
        self.lne_domicilio_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_domicilio_actualizar.setGeometry(QtCore.QRect(160, 133, 301, 21))
        self.lne_domicilio_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_actualizar.setText("")
        self.lne_domicilio_actualizar.setObjectName("lne_domicilio_actualizar")
        self.cbx_tipo_doc_actualizar = QtWidgets.QComboBox(self.groupBox)
        self.cbx_tipo_doc_actualizar.setGeometry(QtCore.QRect(131, 62, 101, 23))
        self.cbx_tipo_doc_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_tipo_doc_actualizar.setObjectName("cbx_tipo_doc_actualizar")
        self.cbx_tipo_doc_actualizar.addItem("")
        self.cbx_tipo_doc_actualizar.addItem("")
        self.cbx_tipo_doc_actualizar.addItem("")
        self.lne_apellido_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_apellido_actualizar.setGeometry(QtCore.QRect(131, 28, 191, 23))
        self.lne_apellido_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_actualizar.setText("")
        self.lne_apellido_actualizar.setObjectName("lne_apellido_actualizar")
        self.cbx_estado_civil_actualizar = QtWidgets.QComboBox(self.groupBox)
        self.cbx_estado_civil_actualizar.setGeometry(QtCore.QRect(450, 98, 180, 21))
        self.cbx_estado_civil_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_estado_civil_actualizar.setObjectName("cbx_estado_civil_actualizar")
        self.cbx_estado_civil_actualizar.addItem("")
        self.cbx_estado_civil_actualizar.addItem("")
        self.cbx_estado_civil_actualizar.addItem("")
        self.cbx_estado_civil_actualizar.addItem("")
        self.label_147 = QtWidgets.QLabel(self.groupBox)
        self.label_147.setGeometry(QtCore.QRect(23, 137, 71, 16))
        self.label_147.setObjectName("label_147")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(473, 67, 121, 20))
        self.label_37.setObjectName("label_37")
        self.label_131 = QtWidgets.QLabel(self.groupBox)
        self.label_131.setGeometry(QtCore.QRect(263, 67, 52, 16))
        self.label_131.setObjectName("label_131")
        self.lne_nombre_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre_actualizar.setGeometry(QtCore.QRect(430, 28, 181, 23))
        self.lne_nombre_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre_actualizar.setText("")
        self.lne_nombre_actualizar.setObjectName("lne_nombre_actualizar")
        self.lne_telefono_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_telefono_actualizar.setGeometry(QtCore.QRect(160, 165, 300, 20))
        self.lne_telefono_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_actualizar.setText("")
        self.lne_telefono_actualizar.setObjectName("lne_telefono_actualizar")
        self.lne_nro_cliente = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_cliente.setGeometry(QtCore.QRect(716, 32, 71, 20))
        self.lne_nro_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cliente.setText("")
        self.lne_nro_cliente.setObjectName("lne_nro_cliente")
        self.label_130 = QtWidgets.QLabel(self.groupBox)
        self.label_130.setGeometry(QtCore.QRect(490, 197, 51, 16))
        self.label_130.setObjectName("label_130")
        self.lne_limite_credito_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_limite_credito_actualizar.setGeometry(QtCore.QRect(160, 197, 300, 20))
        self.lne_limite_credito_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_limite_credito_actualizar.setText("")
        self.lne_limite_credito_actualizar.setObjectName("lne_limite_credito_actualizar")
        self.lne_nro_doc_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc_actualizar.setGeometry(QtCore.QRect(323, 66, 125, 23))
        self.lne_nro_doc_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc_actualizar.setText("")
        self.lne_nro_doc_actualizar.setObjectName("lne_nro_doc_actualizar")
        self.label_126 = QtWidgets.QLabel(self.groupBox)
        self.label_126.setGeometry(QtCore.QRect(310, 98, 131, 16))
        self.label_126.setObjectName("label_126")
        self.label_132 = QtWidgets.QLabel(self.groupBox)
        self.label_132.setGeometry(QtCore.QRect(19, 230, 121, 16))
        self.label_132.setObjectName("label_132")
        self.cbx_ciudad_actualizar = QtWidgets.QComboBox(self.groupBox)
        self.cbx_ciudad_actualizar.setGeometry(QtCore.QRect(553, 157, 201, 31))
        self.cbx_ciudad_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_ciudad_actualizar.setObjectName("cbx_ciudad_actualizar")
        self.cbx_ciudad_actualizar.addItem("")
        self.cbx_ciudad_actualizar.addItem("")
        self.cbx_ciudad_actualizar.addItem("")
        self.label_129 = QtWidgets.QLabel(self.groupBox)
        self.label_129.setGeometry(QtCore.QRect(630, 33, 71, 16))
        self.label_129.setObjectName("label_129")
        self.label_124 = QtWidgets.QLabel(self.groupBox)
        self.label_124.setGeometry(QtCore.QRect(490, 134, 131, 16))
        self.label_124.setObjectName("label_124")
        self.label_135 = QtWidgets.QLabel(self.groupBox)
        self.label_135.setGeometry(QtCore.QRect(490, 168, 51, 16))
        self.label_135.setObjectName("label_135")
        self.lne_barrio_actualizar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_barrio_actualizar.setGeometry(QtCore.QRect(550, 130, 300, 20))
        self.lne_barrio_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_barrio_actualizar.setText("")
        self.lne_barrio_actualizar.setObjectName("lne_barrio_actualizar")
        self.label_127 = QtWidgets.QLabel(self.groupBox)
        self.label_127.setGeometry(QtCore.QRect(19, 167, 121, 16))
        self.label_127.setObjectName("label_127")
        self.label_133 = QtWidgets.QLabel(self.groupBox)
        self.label_133.setGeometry(QtCore.QRect(19, 200, 131, 16))
        self.label_133.setObjectName("label_133")
        self.dte_nacimiento_actualizar = QtWidgets.QDateEdit(self.groupBox)
        self.dte_nacimiento_actualizar.setGeometry(QtCore.QRect(163, 97, 101, 20))
        self.dte_nacimiento_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_nacimiento_actualizar.setDate(QtCore.QDate(1945, 5, 17))
        self.dte_nacimiento_actualizar.setObjectName("dte_nacimiento_actualizar")
        self.label_123 = QtWidgets.QLabel(self.groupBox)
        self.label_123.setGeometry(QtCore.QRect(19, 99, 141, 16))
        self.label_123.setObjectName("label_123")
        self.txte_observaciones_actualizar = QtWidgets.QTextEdit(self.groupBox)
        self.txte_observaciones_actualizar.setGeometry(QtCore.QRect(20, 248, 911, 161))
        self.txte_observaciones_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_observaciones_actualizar.setObjectName("txte_observaciones_actualizar")
        self.label_125 = QtWidgets.QLabel(self.groupBox)
        self.label_125.setGeometry(QtCore.QRect(360, 31, 71, 16))
        self.label_125.setObjectName("label_125")
        self.cbx_estado_actualizar = QtWidgets.QComboBox(self.groupBox)
        self.cbx_estado_actualizar.setGeometry(QtCore.QRect(613, 67, 141, 23))
        self.cbx_estado_actualizar.setObjectName("cbx_estado_actualizar")
        self.cbx_estado_actualizar.addItem("")
        self.cbx_estado_actualizar.addItem("")
        self.cbx_estado_actualizar.addItem("")
        self.cbx_estado_actualizar.addItem("")
        self.cbx_estado_actualizar.setItemText(3, "")
        self.label_134 = QtWidgets.QLabel(self.groupBox)
        self.label_134.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_134.setObjectName("label_134")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_widget_actualizar_cliente.addTab(self.tab_16, icon, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
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
        self.lne_telefono_laboral_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_telefono_laboral_actualizar.setGeometry(QtCore.QRect(200, 100, 300, 20))
        self.lne_telefono_laboral_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_laboral_actualizar.setText("")
        self.lne_telefono_laboral_actualizar.setObjectName("lne_telefono_laboral_actualizar")
        self.label_145 = QtWidgets.QLabel(self.groupBox_2)
        self.label_145.setGeometry(QtCore.QRect(533, 70, 131, 20))
        self.label_145.setObjectName("label_145")
        self.lne_categoria_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_categoria_actualizar.setGeometry(QtCore.QRect(670, 100, 101, 20))
        self.lne_categoria_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_categoria_actualizar.setText("")
        self.lne_categoria_actualizar.setObjectName("lne_categoria_actualizar")
        self.label_143 = QtWidgets.QLabel(self.groupBox_2)
        self.label_143.setGeometry(QtCore.QRect(780, 70, 41, 20))
        self.label_143.setObjectName("label_143")
        self.lne_ocupacion_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ocupacion_actualizar.setGeometry(QtCore.QRect(200, 40, 300, 20))
        self.lne_ocupacion_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_ocupacion_actualizar.setText("")
        self.lne_ocupacion_actualizar.setObjectName("lne_ocupacion_actualizar")
        self.lne_organismo_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_organismo_actualizar.setGeometry(QtCore.QRect(200, 70, 300, 20))
        self.lne_organismo_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_organismo_actualizar.setText("")
        self.lne_organismo_actualizar.setObjectName("lne_organismo_actualizar")
        self.label_140 = QtWidgets.QLabel(self.groupBox_2)
        self.label_140.setGeometry(QtCore.QRect(59, 40, 80, 20))
        self.label_140.setObjectName("label_140")
        self.label_139 = QtWidgets.QLabel(self.groupBox_2)
        self.label_139.setGeometry(QtCore.QRect(59, 70, 80, 20))
        self.label_139.setObjectName("label_139")
        self.label_141 = QtWidgets.QLabel(self.groupBox_2)
        self.label_141.setGeometry(QtCore.QRect(59, 130, 131, 20))
        self.label_141.setObjectName("label_141")
        self.ckbx_recibo_sueldo_actualizar = QtWidgets.QCheckBox(self.groupBox_2)
        self.ckbx_recibo_sueldo_actualizar.setGeometry(QtCore.QRect(533, 130, 211, 21))
        self.ckbx_recibo_sueldo_actualizar.setChecked(True)
        self.ckbx_recibo_sueldo_actualizar.setObjectName("ckbx_recibo_sueldo_actualizar")
        self.label_138 = QtWidgets.QLabel(self.groupBox_2)
        self.label_138.setGeometry(QtCore.QRect(59, 100, 141, 20))
        self.label_138.setObjectName("label_138")
        self.lne_sueldo_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_sueldo_actualizar.setGeometry(QtCore.QRect(670, 40, 101, 20))
        self.lne_sueldo_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_sueldo_actualizar.setText("")
        self.lne_sueldo_actualizar.setObjectName("lne_sueldo_actualizar")
        self.label_146 = QtWidgets.QLabel(self.groupBox_2)
        self.label_146.setGeometry(QtCore.QRect(533, 100, 131, 20))
        self.label_146.setObjectName("label_146")
        self.label_137 = QtWidgets.QLabel(self.groupBox_2)
        self.label_137.setGeometry(QtCore.QRect(530, 40, 80, 20))
        self.label_137.setObjectName("label_137")
        self.lne_antiguedad_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_antiguedad_actualizar.setGeometry(QtCore.QRect(670, 70, 101, 20))
        self.lne_antiguedad_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_antiguedad_actualizar.setText("")
        self.lne_antiguedad_actualizar.setObjectName("lne_antiguedad_actualizar")
        self.lne_domicilio_laboral_actualizar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_domicilio_laboral_actualizar.setGeometry(QtCore.QRect(200, 130, 300, 20))
        self.lne_domicilio_laboral_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_laboral_actualizar.setText("")
        self.lne_domicilio_laboral_actualizar.setObjectName("lne_domicilio_laboral_actualizar")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/hombre-en-el-escritorio-de-la-oficina-con-un-ordenador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_widget_actualizar_cliente.addTab(self.tab_17, icon1, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.label_162 = QtWidgets.QLabel(self.tab_19)
        self.label_162.setGeometry(QtCore.QRect(130, 30, 80, 20))
        self.label_162.setObjectName("label_162")
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
        self.cbx_tipo_iva_actualizar = QtWidgets.QComboBox(self.groupBox_4)
        self.cbx_tipo_iva_actualizar.setGeometry(QtCore.QRect(270, 30, 291, 23))
        self.cbx_tipo_iva_actualizar.setObjectName("cbx_tipo_iva_actualizar")
        self.cbx_tipo_iva_actualizar.addItem("")
        self.cbx_tipo_iva_actualizar.addItem("")
        self.cbx_tipo_iva_actualizar.addItem("")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(123, 34, 80, 20))
        self.label_36.setObjectName("label_36")
        self.ckbx_jub_pens_actualizar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_jub_pens_actualizar.setGeometry(QtCore.QRect(598, 120, 211, 21))
        self.ckbx_jub_pens_actualizar.setObjectName("ckbx_jub_pens_actualizar")
        self.lne_cuit_actualizar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cuit_actualizar.setGeometry(QtCore.QRect(268, 60, 300, 20))
        self.lne_cuit_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cuit_actualizar.setText("")
        self.lne_cuit_actualizar.setObjectName("lne_cuit_actualizar")
        self.label_160 = QtWidgets.QLabel(self.groupBox_4)
        self.label_160.setGeometry(QtCore.QRect(127, 90, 141, 20))
        self.label_160.setObjectName("label_160")
        self.label_159 = QtWidgets.QLabel(self.groupBox_4)
        self.label_159.setGeometry(QtCore.QRect(127, 60, 80, 20))
        self.label_159.setObjectName("label_159")
        self.lne_nro_beneficio_actualizar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_beneficio_actualizar.setGeometry(QtCore.QRect(268, 120, 300, 20))
        self.lne_nro_beneficio_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_beneficio_actualizar.setText("")
        self.lne_nro_beneficio_actualizar.setObjectName("lne_nro_beneficio_actualizar")
        self.ckbx_facturas_actualizar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_facturas_actualizar.setGeometry(QtCore.QRect(598, 60, 211, 21))
        self.ckbx_facturas_actualizar.setCheckable(True)
        self.ckbx_facturas_actualizar.setChecked(False)
        self.ckbx_facturas_actualizar.setObjectName("ckbx_facturas_actualizar")
        self.ckbx_veraz_actualizar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_veraz_actualizar.setGeometry(QtCore.QRect(598, 90, 211, 21))
        self.ckbx_veraz_actualizar.setCheckable(True)
        self.ckbx_veraz_actualizar.setChecked(False)
        self.ckbx_veraz_actualizar.setObjectName("ckbx_veraz_actualizar")
        self.lne_cbu_actualizar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cbu_actualizar.setGeometry(QtCore.QRect(268, 90, 300, 20))
        self.lne_cbu_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cbu_actualizar.setText("")
        self.lne_cbu_actualizar.setObjectName("lne_cbu_actualizar")
        self.label_161 = QtWidgets.QLabel(self.groupBox_4)
        self.label_161.setGeometry(QtCore.QRect(127, 120, 121, 20))
        self.label_161.setObjectName("label_161")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_widget_actualizar_cliente.addTab(self.tab_19, icon2, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 941, 561))
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
        self.boton_agregar_actualizar = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_agregar_actualizar.setGeometry(QtCore.QRect(850, 220, 80, 23))
        self.boton_agregar_actualizar.setObjectName("boton_agregar_actualizar")
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(17, 27, 111, 20))
        self.label_51.setObjectName("label_51")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(16, 116, 121, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(396, 56, 61, 16))
        self.label_23.setObjectName("label_23")
        self.txte_garante_observaciones_actualizar = QtWidgets.QTextEdit(self.groupBox_3)
        self.txte_garante_observaciones_actualizar.setGeometry(QtCore.QRect(16, 136, 911, 81))
        self.txte_garante_observaciones_actualizar.setObjectName("txte_garante_observaciones_actualizar")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(36, 86, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(356, 86, 101, 16))
        self.label_24.setObjectName("label_24")
        self.boton_buscar_garante_actualizar = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_buscar_garante_actualizar.setGeometry(QtCore.QRect(590, 20, 80, 30))
        self.boton_buscar_garante_actualizar.setObjectName("boton_buscar_garante_actualizar")
        self.lne_garante_nro_doc_actualizar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_doc_actualizar.setGeometry(QtCore.QRect(146, 26, 125, 23))
        self.lne_garante_nro_doc_actualizar.setText("")
        self.lne_garante_nro_doc_actualizar.setObjectName("lne_garante_nro_doc_actualizar")
        self.lne_garante_nro_cliente_actualizar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_cliente_actualizar.setGeometry(QtCore.QRect(406, 26, 91, 20))
        self.lne_garante_nro_cliente_actualizar.setText("")
        self.lne_garante_nro_cliente_actualizar.setObjectName("lne_garante_nro_cliente_actualizar")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(40, 59, 61, 16))
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(310, 30, 81, 16))
        self.label_31.setObjectName("label_31")
        self.tw_garantes_lista = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_garantes_lista.setGeometry(QtCore.QRect(10, 260, 911, 141))
        self.tw_garantes_lista.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(6)
        self.tw_garantes_lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(252, 227, 220))
        self.tw_garantes_lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(252, 227, 220))
        self.tw_garantes_lista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(252, 227, 220))
        self.tw_garantes_lista.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(252, 227, 220))
        self.tw_garantes_lista.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(252, 227, 220))
        self.tw_garantes_lista.setHorizontalHeaderItem(5, item)
        self.lne_garante_apellido_actualizar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_apellido_actualizar.setEnabled(False)
        self.lne_garante_apellido_actualizar.setGeometry(QtCore.QRect(146, 60, 125, 23))
        self.lne_garante_apellido_actualizar.setText("")
        self.lne_garante_apellido_actualizar.setObjectName("lne_garante_apellido_actualizar")
        self.lne_garante_nombre_actualizar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nombre_actualizar.setEnabled(False)
        self.lne_garante_nombre_actualizar.setGeometry(QtCore.QRect(145, 89, 125, 23))
        self.lne_garante_nombre_actualizar.setText("")
        self.lne_garante_nombre_actualizar.setObjectName("lne_garante_nombre_actualizar")
        self.lne_garante_estado_actualizar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_estado_actualizar.setEnabled(False)
        self.lne_garante_estado_actualizar.setGeometry(QtCore.QRect(460, 50, 125, 23))
        self.lne_garante_estado_actualizar.setText("")
        self.lne_garante_estado_actualizar.setObjectName("lne_garante_estado_actualizar")
        self.cbx_tipo_garante_actualizar = QtWidgets.QComboBox(self.groupBox_3)
        self.cbx_tipo_garante_actualizar.setGeometry(QtCore.QRect(460, 80, 171, 23))
        self.cbx_tipo_garante_actualizar.setObjectName("cbx_tipo_garante_actualizar")
        self.cbx_tipo_garante_actualizar.addItem("")
        self.cbx_tipo_garante_actualizar.setItemText(0, "")
        self.cbx_tipo_garante_actualizar.addItem("")
        self.cbx_tipo_garante_actualizar.addItem("")
        self.cbx_tipo_garante_actualizar.addItem("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_widget_actualizar_cliente.addTab(self.tab_18, icon3, "")
        self.boton_actualizar = QtWidgets.QPushButton(self.tab)
        self.boton_actualizar.setGeometry(QtCore.QRect(880, 570, 80, 20))
        self.boton_actualizar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_actualizar.setObjectName("boton_actualizar")
        self.boton_limpiar_actualizar_cliente = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar_actualizar_cliente.setGeometry(QtCore.QRect(790, 570, 80, 20))
        self.boton_limpiar_actualizar_cliente.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_limpiar_actualizar_cliente.setObjectName("boton_limpiar_actualizar_cliente")
        self.lne_id_party_actualizar = QtWidgets.QLineEdit(self.tab)
        self.lne_id_party_actualizar.setGeometry(QtCore.QRect(30, 570, 51, 20))
        self.lne_id_party_actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_id_party_actualizar.setText("")
        self.lne_id_party_actualizar.setObjectName("lne_id_party_actualizar")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Íconos/boton-actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")

        self.retranslateUi(Form_clientes_actualizar)
        self.tabWidget.setCurrentIndex(0)
        self.tab_widget_actualizar_cliente.setCurrentIndex(0)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.txte_observaciones_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_email_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_limite_credito_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_telefono_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_domicilio_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_barrio_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_apellido_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_nro_doc_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_nombre_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_nro_cliente.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_ocupacion_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_organismo_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_telefono_laboral_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_domicilio_laboral_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_sueldo_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_antiguedad_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_categoria_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_garante_nro_doc_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_garante_nro_cliente_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.txte_garante_observaciones_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_cuit_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_cbu_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_nro_beneficio_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_garante_apellido_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_garante_estado_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_garante_nombre_actualizar.clear)
        self.boton_limpiar_actualizar_cliente.clicked.connect(self.lne_dni_filtro_actualizar.clear)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_apellido_actualizar, self.lne_nombre_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_nombre_actualizar, self.cbx_tipo_doc_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_tipo_doc_actualizar, self.lne_nro_doc_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_nro_doc_actualizar, self.cbx_estado_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_estado_actualizar, self.dte_nacimiento_actualizar)
        Form_clientes_actualizar.setTabOrder(self.dte_nacimiento_actualizar, self.cbx_estado_civil_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_estado_civil_actualizar, self.lne_domicilio_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_domicilio_actualizar, self.lne_barrio_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_barrio_actualizar, self.lne_telefono_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_telefono_actualizar, self.cbx_ciudad_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_ciudad_actualizar, self.lne_limite_credito_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_limite_credito_actualizar, self.lne_email_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_email_actualizar, self.txte_observaciones_actualizar)
        Form_clientes_actualizar.setTabOrder(self.txte_observaciones_actualizar, self.lne_ocupacion_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_ocupacion_actualizar, self.lne_sueldo_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_sueldo_actualizar, self.lne_organismo_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_organismo_actualizar, self.lne_antiguedad_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_antiguedad_actualizar, self.lne_telefono_laboral_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_telefono_laboral_actualizar, self.lne_categoria_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_categoria_actualizar, self.lne_domicilio_laboral_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_domicilio_laboral_actualizar, self.ckbx_recibo_sueldo_actualizar)
        Form_clientes_actualizar.setTabOrder(self.ckbx_recibo_sueldo_actualizar, self.cbx_tipo_iva_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_tipo_iva_actualizar, self.lne_cuit_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_cuit_actualizar, self.ckbx_facturas_actualizar)
        Form_clientes_actualizar.setTabOrder(self.ckbx_facturas_actualizar, self.lne_cbu_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_cbu_actualizar, self.ckbx_veraz_actualizar)
        Form_clientes_actualizar.setTabOrder(self.ckbx_veraz_actualizar, self.lne_nro_beneficio_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_nro_beneficio_actualizar, self.ckbx_jub_pens_actualizar)
        Form_clientes_actualizar.setTabOrder(self.ckbx_jub_pens_actualizar, self.lne_garante_nro_doc_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_garante_nro_doc_actualizar, self.lne_garante_nro_cliente_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_garante_nro_cliente_actualizar, self.lne_garante_apellido_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_garante_apellido_actualizar, self.lne_garante_estado_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_garante_estado_actualizar, self.lne_garante_nombre_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_garante_nombre_actualizar, self.cbx_tipo_garante_actualizar)
        Form_clientes_actualizar.setTabOrder(self.cbx_tipo_garante_actualizar, self.txte_garante_observaciones_actualizar)
        Form_clientes_actualizar.setTabOrder(self.txte_garante_observaciones_actualizar, self.boton_agregar_actualizar)
        Form_clientes_actualizar.setTabOrder(self.boton_agregar_actualizar, self.boton_buscar_garante_actualizar)
        Form_clientes_actualizar.setTabOrder(self.boton_buscar_garante_actualizar, self.tw_garantes_lista)
        Form_clientes_actualizar.setTabOrder(self.tw_garantes_lista, self.boton_buscar_actualizar)
        Form_clientes_actualizar.setTabOrder(self.boton_buscar_actualizar, self.tabWidget)
        Form_clientes_actualizar.setTabOrder(self.tabWidget, self.lne_dni_filtro_actualizar)
        Form_clientes_actualizar.setTabOrder(self.lne_dni_filtro_actualizar, self.lne_nro_cliente)
        Form_clientes_actualizar.setTabOrder(self.lne_nro_cliente, self.tab_widget_actualizar_cliente)
        Form_clientes_actualizar.setTabOrder(self.tab_widget_actualizar_cliente, self.boton_actualizar)
        Form_clientes_actualizar.setTabOrder(self.boton_actualizar, self.boton_limpiar_actualizar_cliente)
        Form_clientes_actualizar.setTabOrder(self.boton_limpiar_actualizar_cliente, self.lne_id_party_actualizar)

    def retranslateUi(self, Form_clientes_actualizar):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_actualizar.setWindowTitle(_translate("Form_clientes_actualizar", "Actualizar Cliente"))
        self.boton_buscar_actualizar.setText(_translate("Form_clientes_actualizar", "Buscar"))
        self.label_122.setText(_translate("Form_clientes_actualizar", "DNI:"))
        self.label_136.setText(_translate("Form_clientes_actualizar", "Domicilio :"))
        self.label_128.setText(_translate("Form_clientes_actualizar", "Tipo Documento:"))
        self.cbx_tipo_doc_actualizar.setItemText(0, _translate("Form_clientes_actualizar", "DNI "))
        self.cbx_tipo_doc_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "CUIL"))
        self.cbx_tipo_doc_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "CUIT "))
        self.cbx_estado_civil_actualizar.setItemText(0, _translate("Form_clientes_actualizar", "Soltero/era"))
        self.cbx_estado_civil_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "Casado/ada"))
        self.cbx_estado_civil_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "Viudo/da"))
        self.cbx_estado_civil_actualizar.setItemText(3, _translate("Form_clientes_actualizar", "Divorsiado/ada"))
        self.label_147.setText(_translate("Form_clientes_actualizar", "Domicilio :"))
        self.label_37.setText(_translate("Form_clientes_actualizar", "Estado Persona"))
        self.label_131.setText(_translate("Form_clientes_actualizar", "Número:"))
        self.label_130.setText(_translate("Form_clientes_actualizar", "Email:"))
        self.label_126.setText(_translate("Form_clientes_actualizar", "Estado Civil:"))
        self.label_132.setText(_translate("Form_clientes_actualizar", "Observaciones: "))
        self.cbx_ciudad_actualizar.setItemText(0, _translate("Form_clientes_actualizar", "Viedma"))
        self.cbx_ciudad_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "Patagones"))
        self.cbx_ciudad_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "Otros"))
        self.label_129.setText(_translate("Form_clientes_actualizar", "N°  Cliente :"))
        self.label_124.setText(_translate("Form_clientes_actualizar", "Barrio:"))
        self.label_135.setText(_translate("Form_clientes_actualizar", "Ciudad:"))
        self.label_127.setText(_translate("Form_clientes_actualizar", "Teléfono:"))
        self.label_133.setText(_translate("Form_clientes_actualizar", "Límite por Créditos:"))
        self.dte_nacimiento_actualizar.setDisplayFormat(_translate("Form_clientes_actualizar", "yyyy/M/dd"))
        self.label_123.setText(_translate("Form_clientes_actualizar", "Fecha de Nacimiento:"))
        self.label_125.setText(_translate("Form_clientes_actualizar", "Nombre :"))
        self.cbx_estado_actualizar.setItemText(0, _translate("Form_clientes_actualizar", "Activo"))
        self.cbx_estado_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "Bloqueado"))
        self.cbx_estado_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "Cupo Cubierto"))
        self.label_134.setText(_translate("Form_clientes_actualizar", "Apellido:"))
        self.tab_widget_actualizar_cliente.setTabText(self.tab_widget_actualizar_cliente.indexOf(self.tab_16), _translate("Form_clientes_actualizar", "Datos Personales"))
        self.label_144.setText(_translate("Form_clientes_actualizar", "Categoría: "))
        self.label_145.setText(_translate("Form_clientes_actualizar", "Antigüedad Laboral:"))
        self.label_143.setText(_translate("Form_clientes_actualizar", "años"))
        self.label_140.setText(_translate("Form_clientes_actualizar", "Ocupación:"))
        self.label_139.setText(_translate("Form_clientes_actualizar", "Organismo: "))
        self.label_141.setText(_translate("Form_clientes_actualizar", "Domicilio Laboral:"))
        self.ckbx_recibo_sueldo_actualizar.setText(_translate("Form_clientes_actualizar", "Posee Recibo de Sueldo"))
        self.label_138.setText(_translate("Form_clientes_actualizar", "Teléfono Laboral:"))
        self.label_146.setText(_translate("Form_clientes_actualizar", "Categoria Laboral:"))
        self.label_137.setText(_translate("Form_clientes_actualizar", "Sueldo $:"))
        self.tab_widget_actualizar_cliente.setTabText(self.tab_widget_actualizar_cliente.indexOf(self.tab_17), _translate("Form_clientes_actualizar", "Datos laborales"))
        self.label_162.setText(_translate("Form_clientes_actualizar", "Tipo IVA:"))
        self.cbx_tipo_iva_actualizar.setItemText(0, _translate("Form_clientes_actualizar", "Consumidor final"))
        self.cbx_tipo_iva_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "Monotributista"))
        self.cbx_tipo_iva_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "Responsable inscripto"))
        self.label_36.setText(_translate("Form_clientes_actualizar", "Tipo IVA:"))
        self.ckbx_jub_pens_actualizar.setText(_translate("Form_clientes_actualizar", "Es Jubilado / Pensionado"))
        self.label_160.setText(_translate("Form_clientes_actualizar", "N° CBU:"))
        self.label_159.setText(_translate("Form_clientes_actualizar", "N° CUIT:"))
        self.ckbx_facturas_actualizar.setText(_translate("Form_clientes_actualizar", "Presentó Facturas de Luz, Gas"))
        self.ckbx_veraz_actualizar.setText(_translate("Form_clientes_actualizar", "Figura en el Veraz"))
        self.label_161.setText(_translate("Form_clientes_actualizar", "N° Beneficio:"))
        self.tab_widget_actualizar_cliente.setTabText(self.tab_widget_actualizar_cliente.indexOf(self.tab_19), _translate("Form_clientes_actualizar", "Otros Datos"))
        self.boton_agregar_actualizar.setText(_translate("Form_clientes_actualizar", "Agregar"))
        self.label_51.setText(_translate("Form_clientes_actualizar", "Nro Documento:"))
        self.label_22.setText(_translate("Form_clientes_actualizar", "Observaciones: "))
        self.label_23.setText(_translate("Form_clientes_actualizar", "Estado :"))
        self.txte_garante_observaciones_actualizar.setHtml(_translate("Form_clientes_actualizar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KacstOne\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a</p></body></html>"))
        self.label_4.setText(_translate("Form_clientes_actualizar", "Nombre :"))
        self.label_24.setText(_translate("Form_clientes_actualizar", "Tipo Garante :"))
        self.boton_buscar_garante_actualizar.setText(_translate("Form_clientes_actualizar", "Buscar"))
        self.label_29.setText(_translate("Form_clientes_actualizar", "Apellido:"))
        self.label_31.setText(_translate("Form_clientes_actualizar", "N°  Cliente :"))
        item = self.tw_garantes_lista.horizontalHeaderItem(0)
        item.setText(_translate("Form_clientes_actualizar", "Estado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(1)
        item.setText(_translate("Form_clientes_actualizar", "Tipo Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(2)
        item.setText(_translate("Form_clientes_actualizar", "Nro. Cliente"))
        item = self.tw_garantes_lista.horizontalHeaderItem(3)
        item.setText(_translate("Form_clientes_actualizar", "Apellido"))
        item = self.tw_garantes_lista.horizontalHeaderItem(4)
        item.setText(_translate("Form_clientes_actualizar", "Nombre"))
        item = self.tw_garantes_lista.horizontalHeaderItem(5)
        item.setText(_translate("Form_clientes_actualizar", "Número Documento"))
        self.cbx_tipo_garante_actualizar.setItemText(1, _translate("Form_clientes_actualizar", "Garante Principal"))
        self.cbx_tipo_garante_actualizar.setItemText(2, _translate("Form_clientes_actualizar", "Garante Secundario"))
        self.cbx_tipo_garante_actualizar.setItemText(3, _translate("Form_clientes_actualizar", "Otro Garante"))
        self.tab_widget_actualizar_cliente.setTabText(self.tab_widget_actualizar_cliente.indexOf(self.tab_18), _translate("Form_clientes_actualizar", "Datos Garante"))
        self.boton_actualizar.setText(_translate("Form_clientes_actualizar", "Actualizar"))
        self.boton_limpiar_actualizar_cliente.setText(_translate("Form_clientes_actualizar", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_actualizar", "Actualizar Cliente"))

