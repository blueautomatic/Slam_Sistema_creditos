# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_buscar.ui'
#
# Created: Tue Oct 25 14:28:59 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_buscar(object):
    def setupUi(self, Form_clientes_buscar):
        Form_clientes_buscar.setObjectName("Form_clientes_buscar")
        Form_clientes_buscar.resize(983, 611)
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_buscar)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 961, 591))
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 951, 491))
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
        self.groupBox = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox.setGeometry(QtCore.QRect(3, 17, 941, 441))
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
        self.label_127 = QtWidgets.QLabel(self.groupBox)
        self.label_127.setGeometry(QtCore.QRect(21, 61, 121, 16))
        self.label_127.setObjectName("label_127")
        self.label_124 = QtWidgets.QLabel(self.groupBox)
        self.label_124.setGeometry(QtCore.QRect(360, 26, 71, 16))
        self.label_124.setObjectName("label_124")
        self.lne_barrio_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_barrio_buscar.setGeometry(QtCore.QRect(550, 130, 300, 20))
        self.lne_barrio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_barrio_buscar.setText("")
        self.lne_barrio_buscar.setObjectName("lne_barrio_buscar")
        self.lne_nro_cliente_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_cliente_buscar.setGeometry(QtCore.QRect(716, 25, 91, 23))
        self.lne_nro_cliente_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cliente_buscar.setText("")
        self.lne_nro_cliente_buscar.setObjectName("lne_nro_cliente_buscar")
        self.txte_observaciones_buscar = QtWidgets.QTextEdit(self.groupBox)
        self.txte_observaciones_buscar.setGeometry(QtCore.QRect(20, 245, 911, 161))
        self.txte_observaciones_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_observaciones_buscar.setObjectName("txte_observaciones_buscar")
        self.label_128 = QtWidgets.QLabel(self.groupBox)
        self.label_128.setGeometry(QtCore.QRect(630, 26, 71, 16))
        self.label_128.setObjectName("label_128")
        self.lne_domicilio_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_domicilio_buscar.setGeometry(QtCore.QRect(160, 130, 300, 20))
        self.lne_domicilio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_buscar.setText("")
        self.lne_domicilio_buscar.setObjectName("lne_domicilio_buscar")
        self.lne_fecha_nac = QtWidgets.QLineEdit(self.groupBox)
        self.lne_fecha_nac.setGeometry(QtCore.QRect(170, 92, 113, 23))
        self.lne_fecha_nac.setObjectName("lne_fecha_nac")
        self.label_133 = QtWidgets.QLabel(self.groupBox)
        self.label_133.setGeometry(QtCore.QRect(21, 26, 53, 16))
        self.label_133.setObjectName("label_133")
        self.label_122 = QtWidgets.QLabel(self.groupBox)
        self.label_122.setGeometry(QtCore.QRect(21, 97, 141, 16))
        self.label_122.setObjectName("label_122")
        self.label_132 = QtWidgets.QLabel(self.groupBox)
        self.label_132.setGeometry(QtCore.QRect(21, 197, 131, 16))
        self.label_132.setObjectName("label_132")
        self.lne_estado = QtWidgets.QLineEdit(self.groupBox)
        self.lne_estado.setGeometry(QtCore.QRect(725, 59, 113, 23))
        self.lne_estado.setObjectName("lne_estado")
        self.label_135 = QtWidgets.QLabel(self.groupBox)
        self.label_135.setGeometry(QtCore.QRect(21, 131, 71, 16))
        self.label_135.setObjectName("label_135")
        self.label_130 = QtWidgets.QLabel(self.groupBox)
        self.label_130.setGeometry(QtCore.QRect(360, 59, 61, 16))
        self.label_130.setObjectName("label_130")
        self.lne_telefono_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_telefono_buscar.setGeometry(QtCore.QRect(160, 162, 300, 20))
        self.lne_telefono_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_buscar.setText("")
        self.lne_telefono_buscar.setObjectName("lne_telefono_buscar")
        self.label_125 = QtWidgets.QLabel(self.groupBox)
        self.label_125.setGeometry(QtCore.QRect(360, 96, 91, 20))
        self.label_125.setObjectName("label_125")
        self.lne_apellido_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_apellido_buscar.setGeometry(QtCore.QRect(131, 25, 191, 23))
        self.lne_apellido_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_buscar.setText("")
        self.lne_apellido_buscar.setObjectName("lne_apellido_buscar")
        self.lne_tipo_doc_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_tipo_doc_buscar.setGeometry(QtCore.QRect(144, 57, 131, 23))
        self.lne_tipo_doc_buscar.setObjectName("lne_tipo_doc_buscar")
        self.lne_email_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_email_buscar.setGeometry(QtCore.QRect(550, 194, 300, 20))
        self.lne_email_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_email_buscar.setText("")
        self.lne_email_buscar.setObjectName("lne_email_buscar")
        self.lne_estado_civil = QtWidgets.QLineEdit(self.groupBox)
        self.lne_estado_civil.setGeometry(QtCore.QRect(446, 93, 113, 23))
        self.lne_estado_civil.setObjectName("lne_estado_civil")
        self.lne_nombre_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre_buscar.setGeometry(QtCore.QRect(430, 25, 181, 23))
        self.lne_nombre_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre_buscar.setText("")
        self.lne_nombre_buscar.setObjectName("lne_nombre_buscar")
        self.label_131 = QtWidgets.QLabel(self.groupBox)
        self.label_131.setGeometry(QtCore.QRect(21, 227, 121, 16))
        self.label_131.setObjectName("label_131")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(605, 59, 101, 20))
        self.label_37.setObjectName("label_37")
        self.lne_nro_doc_cliente = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc_cliente.setGeometry(QtCore.QRect(432, 59, 125, 23))
        self.lne_nro_doc_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc_cliente.setText("")
        self.lne_nro_doc_cliente.setObjectName("lne_nro_doc_cliente")
        self.lne_limite_credito_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_limite_credito_buscar.setGeometry(QtCore.QRect(160, 194, 300, 20))
        self.lne_limite_credito_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_limite_credito_buscar.setText("")
        self.lne_limite_credito_buscar.setObjectName("lne_limite_credito_buscar")
        self.label_134 = QtWidgets.QLabel(self.groupBox)
        self.label_134.setGeometry(QtCore.QRect(490, 165, 51, 16))
        self.label_134.setObjectName("label_134")
        self.label_126 = QtWidgets.QLabel(self.groupBox)
        self.label_126.setGeometry(QtCore.QRect(21, 164, 121, 16))
        self.label_126.setObjectName("label_126")
        self.label_129 = QtWidgets.QLabel(self.groupBox)
        self.label_129.setGeometry(QtCore.QRect(490, 194, 51, 16))
        self.label_129.setObjectName("label_129")
        self.label_123 = QtWidgets.QLabel(self.groupBox)
        self.label_123.setGeometry(QtCore.QRect(490, 131, 51, 16))
        self.label_123.setObjectName("label_123")
        self.lne_ciudad_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_ciudad_buscar.setGeometry(QtCore.QRect(550, 160, 113, 23))
        self.lne_ciudad_buscar.setObjectName("lne_ciudad_buscar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_16, icon, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
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
        self.label_139 = QtWidgets.QLabel(self.groupBox_2)
        self.label_139.setGeometry(QtCore.QRect(80, 40, 80, 20))
        self.label_139.setObjectName("label_139")
        self.label_140 = QtWidgets.QLabel(self.groupBox_2)
        self.label_140.setGeometry(QtCore.QRect(80, 130, 131, 20))
        self.label_140.setObjectName("label_140")
        self.lne_organismo_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_organismo_buscar.setGeometry(QtCore.QRect(221, 70, 300, 20))
        self.lne_organismo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_organismo_buscar.setText("")
        self.lne_organismo_buscar.setObjectName("lne_organismo_buscar")
        self.label_141 = QtWidgets.QLabel(self.groupBox_2)
        self.label_141.setGeometry(QtCore.QRect(551, 70, 131, 20))
        self.label_141.setObjectName("label_141")
        self.label_143 = QtWidgets.QLabel(self.groupBox_2)
        self.label_143.setGeometry(QtCore.QRect(551, 100, 71, 20))
        self.label_143.setObjectName("label_143")
        self.lne_ocupacion_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ocupacion_buscar.setGeometry(QtCore.QRect(221, 40, 300, 20))
        self.lne_ocupacion_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_ocupacion_buscar.setText("")
        self.lne_ocupacion_buscar.setObjectName("lne_ocupacion_buscar")
        self.ckbx_posee_sueldo_buscar = QtWidgets.QCheckBox(self.groupBox_2)
        self.ckbx_posee_sueldo_buscar.setGeometry(QtCore.QRect(551, 130, 211, 21))
        self.ckbx_posee_sueldo_buscar.setChecked(False)
        self.ckbx_posee_sueldo_buscar.setObjectName("ckbx_posee_sueldo_buscar")
        self.label_137 = QtWidgets.QLabel(self.groupBox_2)
        self.label_137.setGeometry(QtCore.QRect(80, 100, 141, 20))
        self.label_137.setObjectName("label_137")
        self.lne_sueldo_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_sueldo_buscar.setGeometry(QtCore.QRect(691, 40, 101, 20))
        self.lne_sueldo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_sueldo_buscar.setText("")
        self.lne_sueldo_buscar.setObjectName("lne_sueldo_buscar")
        self.label_138 = QtWidgets.QLabel(self.groupBox_2)
        self.label_138.setGeometry(QtCore.QRect(80, 70, 80, 20))
        self.label_138.setObjectName("label_138")
        self.label_136 = QtWidgets.QLabel(self.groupBox_2)
        self.label_136.setGeometry(QtCore.QRect(551, 40, 80, 20))
        self.label_136.setObjectName("label_136")
        self.lne_categoria_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_categoria_buscar.setGeometry(QtCore.QRect(691, 100, 101, 20))
        self.lne_categoria_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_categoria_buscar.setText("")
        self.lne_categoria_buscar.setObjectName("lne_categoria_buscar")
        self.lne_telefono_laboral_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_telefono_laboral_buscar.setGeometry(QtCore.QRect(221, 100, 300, 20))
        self.lne_telefono_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_laboral_buscar.setText("")
        self.lne_telefono_laboral_buscar.setObjectName("lne_telefono_laboral_buscar")
        self.lne_antiguedad_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_antiguedad_buscar.setGeometry(QtCore.QRect(691, 70, 101, 20))
        self.lne_antiguedad_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_antiguedad_buscar.setText("")
        self.lne_antiguedad_buscar.setObjectName("lne_antiguedad_buscar")
        self.lne_domicilio_laboral_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_domicilio_laboral_buscar.setGeometry(QtCore.QRect(221, 130, 300, 20))
        self.lne_domicilio_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_laboral_buscar.setText("")
        self.lne_domicilio_laboral_buscar.setObjectName("lne_domicilio_laboral_buscar")
        self.label_142 = QtWidgets.QLabel(self.groupBox_2)
        self.label_142.setGeometry(QtCore.QRect(801, 70, 41, 20))
        self.label_142.setObjectName("label_142")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/hombre-en-el-escritorio-de-la-oficina-con-un-ordenador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_17, icon1, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
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
        self.tw_garantes_lista = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_garantes_lista.setGeometry(QtCore.QRect(20, 20, 891, 141))
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(6, item)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_18, icon2, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
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
        self.ckbx_facturas_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_facturas_buscar.setGeometry(QtCore.QRect(580, 70, 251, 21))
        self.ckbx_facturas_buscar.setChecked(False)
        self.ckbx_facturas_buscar.setObjectName("ckbx_facturas_buscar")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(109, 40, 80, 20))
        self.label_36.setObjectName("label_36")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(109, 100, 141, 20))
        self.label_34.setObjectName("label_34")
        self.ckbx_veraz_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_veraz_buscar.setGeometry(QtCore.QRect(580, 100, 211, 21))
        self.ckbx_veraz_buscar.setChecked(False)
        self.ckbx_veraz_buscar.setObjectName("ckbx_veraz_buscar")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(109, 70, 80, 20))
        self.label_33.setObjectName("label_33")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(109, 130, 121, 20))
        self.label_35.setObjectName("label_35")
        self.ckbx_jub_pens_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_jub_pens_buscar.setGeometry(QtCore.QRect(580, 130, 211, 21))
        self.ckbx_jub_pens_buscar.setObjectName("ckbx_jub_pens_buscar")
        self.lne_cbu_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cbu_buscar.setGeometry(QtCore.QRect(250, 100, 300, 20))
        self.lne_cbu_buscar.setText("")
        self.lne_cbu_buscar.setObjectName("lne_cbu_buscar")
        self.lne_nro_beneficio_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_beneficio_buscar.setGeometry(QtCore.QRect(250, 130, 300, 20))
        self.lne_nro_beneficio_buscar.setText("")
        self.lne_nro_beneficio_buscar.setObjectName("lne_nro_beneficio_buscar")
        self.lne_cuit_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cuit_buscar.setGeometry(QtCore.QRect(250, 70, 300, 20))
        self.lne_cuit_buscar.setText("")
        self.lne_cuit_buscar.setObjectName("lne_cuit_buscar")
        self.lne_tipo_iva_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_tipo_iva_buscar.setGeometry(QtCore.QRect(250, 40, 300, 20))
        self.lne_tipo_iva_buscar.setText("")
        self.lne_tipo_iva_buscar.setObjectName("lne_tipo_iva_buscar")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Íconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_19, icon3, "")
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
        self.boton_buscar_buscar.setGeometry(QtCore.QRect(843, 9, 80, 30))
        self.boton_buscar_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_buscar.setObjectName("boton_buscar_buscar")
        self.label_121 = QtWidgets.QLabel(self.tab)
        self.label_121.setGeometry(QtCore.QRect(644, 12, 31, 16))
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
        self.lne_dni_filtro_buscar.setGeometry(QtCore.QRect(675, 10, 151, 20))
        self.lne_dni_filtro_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_buscar.setObjectName("lne_dni_filtro_buscar")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar.setGeometry(QtCore.QRect(860, 530, 80, 20))
        self.boton_limpiar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_limpiar.setObjectName("boton_limpiar")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Íconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")

        self.retranslateUi(Form_clientes_buscar)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_apellido_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_tipo_doc_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nombre_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_cliente_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_doc_cliente.clear)
        self.boton_limpiar.clicked.connect(self.lne_estado.clear)
        self.boton_limpiar.clicked.connect(self.lne_fecha_nac.clear)
        self.boton_limpiar.clicked.connect(self.lne_estado_civil.clear)
        self.boton_limpiar.clicked.connect(self.lne_domicilio_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_barrio_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_telefono_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_ciudad_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_limite_credito_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_email_buscar.clear)
        self.boton_limpiar.clicked.connect(self.txte_observaciones_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_dni_filtro_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_ocupacion_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_sueldo_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_antiguedad_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_categoria_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_organismo_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_telefono_laboral_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_domicilio_laboral_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_tipo_iva_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_cuit_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_cbu_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_beneficio_buscar.clear)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_buscar)

    def retranslateUi(self, Form_clientes_buscar):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_buscar.setWindowTitle(_translate("Form_clientes_buscar", "Buscar Cliente"))
        self.label_127.setText(_translate("Form_clientes_buscar", "Tipo Documento:"))
        self.label_124.setText(_translate("Form_clientes_buscar", "Nombre :"))
        self.label_128.setText(_translate("Form_clientes_buscar", "N°  Cliente :"))
        self.label_133.setText(_translate("Form_clientes_buscar", "Apellido:"))
        self.label_122.setText(_translate("Form_clientes_buscar", "Fecha de Nacimiento:"))
        self.label_132.setText(_translate("Form_clientes_buscar", "Límite por Créditos:"))
        self.label_135.setText(_translate("Form_clientes_buscar", "Domicilio :"))
        self.label_130.setText(_translate("Form_clientes_buscar", "Número:"))
        self.label_125.setText(_translate("Form_clientes_buscar", "Estado Civil:"))
        self.label_131.setText(_translate("Form_clientes_buscar", "Observaciones: "))
        self.label_37.setText(_translate("Form_clientes_buscar", "Estado Persona"))
        self.label_134.setText(_translate("Form_clientes_buscar", "Ciudad:"))
        self.label_126.setText(_translate("Form_clientes_buscar", "Teléfono:"))
        self.label_129.setText(_translate("Form_clientes_buscar", "Email:"))
        self.label_123.setText(_translate("Form_clientes_buscar", "Barrio:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), _translate("Form_clientes_buscar", "Datos Personales"))
        self.label_139.setText(_translate("Form_clientes_buscar", "Ocupación:"))
        self.label_140.setText(_translate("Form_clientes_buscar", "Domicilio Laboral:"))
        self.label_141.setText(_translate("Form_clientes_buscar", "Antigüedad Laboral:"))
        self.label_143.setText(_translate("Form_clientes_buscar", "Categoría: "))
        self.ckbx_posee_sueldo_buscar.setText(_translate("Form_clientes_buscar", "Posee Recibo de Sueldo"))
        self.label_137.setText(_translate("Form_clientes_buscar", "Teléfono Laboral:"))
        self.label_138.setText(_translate("Form_clientes_buscar", "Organismo: "))
        self.label_136.setText(_translate("Form_clientes_buscar", "Sueldo $:"))
        self.label_142.setText(_translate("Form_clientes_buscar", "años"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), _translate("Form_clientes_buscar", "Datos laborales"))
        item = self.tw_garantes_lista.horizontalHeaderItem(0)
        item.setText(_translate("Form_clientes_buscar", "Estado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(1)
        item.setText(_translate("Form_clientes_buscar", "Tipo Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(2)
        item.setText(_translate("Form_clientes_buscar", "Nro. Cliente"))
        item = self.tw_garantes_lista.horizontalHeaderItem(3)
        item.setText(_translate("Form_clientes_buscar", "Apellido"))
        item = self.tw_garantes_lista.horizontalHeaderItem(4)
        item.setText(_translate("Form_clientes_buscar", "Nombre"))
        item = self.tw_garantes_lista.horizontalHeaderItem(5)
        item.setText(_translate("Form_clientes_buscar", "Número Documento"))
        item = self.tw_garantes_lista.horizontalHeaderItem(6)
        item.setText(_translate("Form_clientes_buscar", "Comentario"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), _translate("Form_clientes_buscar", "Datos Garante"))
        self.ckbx_facturas_buscar.setText(_translate("Form_clientes_buscar", "Presentó Facturas de Luz, Gas"))
        self.label_36.setText(_translate("Form_clientes_buscar", "Tipo IVA:"))
        self.label_34.setText(_translate("Form_clientes_buscar", "N° CBU:"))
        self.ckbx_veraz_buscar.setText(_translate("Form_clientes_buscar", "Figura en el Veraz"))
        self.label_33.setText(_translate("Form_clientes_buscar", "N° CUIT:"))
        self.label_35.setText(_translate("Form_clientes_buscar", "N° Beneficio:"))
        self.ckbx_jub_pens_buscar.setText(_translate("Form_clientes_buscar", "Es Jubilado / Pensionado"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("Form_clientes_buscar", "Otros Datos"))
        self.boton_buscar_buscar_2.setText(_translate("Form_clientes_buscar", "Buscar"))
        self.label_162.setText(_translate("Form_clientes_buscar", "DNI:"))
        self.boton_buscar_buscar.setText(_translate("Form_clientes_buscar", "Buscar"))
        self.label_121.setText(_translate("Form_clientes_buscar", "DNI:"))
        self.boton_limpiar.setText(_translate("Form_clientes_buscar", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_buscar", "Buscar Cliente"))

