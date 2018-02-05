# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_clientes_buscar.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_clientes_buscar(object):
    def setupUi(self, Form_clientes_buscar):
        Form_clientes_buscar.setObjectName("Form_clientes_buscar")
        Form_clientes_buscar.resize(983, 604)
        Form_clientes_buscar.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 1, 1);\n"
"selection-color: rgb(0, 0, 0);\n"
"")
        self.gridLayout_7 = QtWidgets.QGridLayout(Form_clientes_buscar)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Form_clientes_buscar)
        self.tabWidget.setStyleSheet("background-color: rgba(136, 3, 3);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.label_145 = QtWidgets.QLabel(self.tab)
        self.label_145.setStyleSheet("font: 75 10pt \"KacstOne\";")
        self.label_145.setObjectName("label_145")
        self.horizontalLayout_15.addWidget(self.label_145)
        self.lne_dni_filtro_buscar = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_buscar.setMinimumSize(QtCore.QSize(130, 0))
        self.lne_dni_filtro_buscar.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lne_dni_filtro_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_buscar.setText("")
        self.lne_dni_filtro_buscar.setObjectName("lne_dni_filtro_buscar")
        self.horizontalLayout_15.addWidget(self.lne_dni_filtro_buscar)
        self.boton_buscar_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_buscar.setObjectName("boton_buscar_buscar")
        self.horizontalLayout_15.addWidget(self.boton_buscar_buscar)
        self.gridLayout_6.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
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
        self.gridLayout = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_16)
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_133 = QtWidgets.QLabel(self.groupBox)
        self.label_133.setObjectName("label_133")
        self.horizontalLayout.addWidget(self.label_133)
        self.lne_apellido_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_apellido_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_buscar.setText("")
        self.lne_apellido_buscar.setObjectName("lne_apellido_buscar")
        self.horizontalLayout.addWidget(self.lne_apellido_buscar)
        self.label_124 = QtWidgets.QLabel(self.groupBox)
        self.label_124.setObjectName("label_124")
        self.horizontalLayout.addWidget(self.label_124)
        self.lne_nombre_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nombre_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre_buscar.setText("")
        self.lne_nombre_buscar.setObjectName("lne_nombre_buscar")
        self.horizontalLayout.addWidget(self.lne_nombre_buscar)
        self.label_128 = QtWidgets.QLabel(self.groupBox)
        self.label_128.setObjectName("label_128")
        self.horizontalLayout.addWidget(self.label_128)
        self.lne_nro_cliente_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_cliente_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cliente_buscar.setText("")
        self.lne_nro_cliente_buscar.setObjectName("lne_nro_cliente_buscar")
        self.horizontalLayout.addWidget(self.lne_nro_cliente_buscar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_127 = QtWidgets.QLabel(self.groupBox)
        self.label_127.setObjectName("label_127")
        self.horizontalLayout_2.addWidget(self.label_127)
        self.lne_tipo_doc_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_tipo_doc_buscar.setObjectName("lne_tipo_doc_buscar")
        self.horizontalLayout_2.addWidget(self.lne_tipo_doc_buscar)
        self.label_130 = QtWidgets.QLabel(self.groupBox)
        self.label_130.setObjectName("label_130")
        self.horizontalLayout_2.addWidget(self.label_130)
        self.lne_nro_doc_cliente = QtWidgets.QLineEdit(self.groupBox)
        self.lne_nro_doc_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc_cliente.setText("")
        self.lne_nro_doc_cliente.setObjectName("lne_nro_doc_cliente")
        self.horizontalLayout_2.addWidget(self.lne_nro_doc_cliente)
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_2.addWidget(self.label_37)
        self.lne_estado = QtWidgets.QLineEdit(self.groupBox)
        self.lne_estado.setObjectName("lne_estado")
        self.horizontalLayout_2.addWidget(self.lne_estado)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_122 = QtWidgets.QLabel(self.groupBox)
        self.label_122.setObjectName("label_122")
        self.horizontalLayout_3.addWidget(self.label_122)
        self.lne_fecha_nac = QtWidgets.QLineEdit(self.groupBox)
        self.lne_fecha_nac.setObjectName("lne_fecha_nac")
        self.horizontalLayout_3.addWidget(self.lne_fecha_nac)
        self.label_125 = QtWidgets.QLabel(self.groupBox)
        self.label_125.setObjectName("label_125")
        self.horizontalLayout_3.addWidget(self.label_125)
        self.lne_estado_civil = QtWidgets.QLineEdit(self.groupBox)
        self.lne_estado_civil.setObjectName("lne_estado_civil")
        self.horizontalLayout_3.addWidget(self.lne_estado_civil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_135 = QtWidgets.QLabel(self.groupBox)
        self.label_135.setObjectName("label_135")
        self.horizontalLayout_4.addWidget(self.label_135)
        self.lne_domicilio_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_domicilio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_buscar.setText("")
        self.lne_domicilio_buscar.setObjectName("lne_domicilio_buscar")
        self.horizontalLayout_4.addWidget(self.lne_domicilio_buscar)
        self.label_123 = QtWidgets.QLabel(self.groupBox)
        self.label_123.setObjectName("label_123")
        self.horizontalLayout_4.addWidget(self.label_123)
        self.lne_barrio_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_barrio_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_barrio_buscar.setText("")
        self.lne_barrio_buscar.setObjectName("lne_barrio_buscar")
        self.horizontalLayout_4.addWidget(self.lne_barrio_buscar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_126 = QtWidgets.QLabel(self.groupBox)
        self.label_126.setObjectName("label_126")
        self.horizontalLayout_5.addWidget(self.label_126)
        self.lne_telefono_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_telefono_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_buscar.setText("")
        self.lne_telefono_buscar.setObjectName("lne_telefono_buscar")
        self.horizontalLayout_5.addWidget(self.lne_telefono_buscar)
        self.label_134 = QtWidgets.QLabel(self.groupBox)
        self.label_134.setObjectName("label_134")
        self.horizontalLayout_5.addWidget(self.label_134)
        self.lne_ciudad_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_ciudad_buscar.setObjectName("lne_ciudad_buscar")
        self.horizontalLayout_5.addWidget(self.lne_ciudad_buscar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_132 = QtWidgets.QLabel(self.groupBox)
        self.label_132.setObjectName("label_132")
        self.horizontalLayout_6.addWidget(self.label_132)
        self.lne_limite_credito_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_limite_credito_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_limite_credito_buscar.setText("")
        self.lne_limite_credito_buscar.setObjectName("lne_limite_credito_buscar")
        self.horizontalLayout_6.addWidget(self.lne_limite_credito_buscar)
        self.label_129 = QtWidgets.QLabel(self.groupBox)
        self.label_129.setObjectName("label_129")
        self.horizontalLayout_6.addWidget(self.label_129)
        self.lne_email_buscar = QtWidgets.QLineEdit(self.groupBox)
        self.lne_email_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_email_buscar.setText("")
        self.lne_email_buscar.setObjectName("lne_email_buscar")
        self.horizontalLayout_6.addWidget(self.lne_email_buscar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_131 = QtWidgets.QLabel(self.groupBox)
        self.label_131.setObjectName("label_131")
        self.verticalLayout.addWidget(self.label_131)
        self.txte_observaciones_buscar = QtWidgets.QTextEdit(self.groupBox)
        self.txte_observaciones_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txte_observaciones_buscar.setObjectName("txte_observaciones_buscar")
        self.verticalLayout.addWidget(self.txte_observaciones_buscar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/tarjeta-personal-de-datos-de-contacto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_16, icon, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_17)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_17)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_138 = QtWidgets.QLabel(self.groupBox_2)
        self.label_138.setObjectName("label_138")
        self.horizontalLayout_8.addWidget(self.label_138)
        self.lne_organismo_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_organismo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_organismo_buscar.setText("")
        self.lne_organismo_buscar.setObjectName("lne_organismo_buscar")
        self.horizontalLayout_8.addWidget(self.lne_organismo_buscar)
        self.label_141 = QtWidgets.QLabel(self.groupBox_2)
        self.label_141.setObjectName("label_141")
        self.horizontalLayout_8.addWidget(self.label_141)
        self.lne_antiguedad_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_antiguedad_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_antiguedad_buscar.setText("")
        self.lne_antiguedad_buscar.setObjectName("lne_antiguedad_buscar")
        self.horizontalLayout_8.addWidget(self.lne_antiguedad_buscar)
        self.label_142 = QtWidgets.QLabel(self.groupBox_2)
        self.label_142.setObjectName("label_142")
        self.horizontalLayout_8.addWidget(self.label_142)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_139 = QtWidgets.QLabel(self.groupBox_2)
        self.label_139.setObjectName("label_139")
        self.horizontalLayout_7.addWidget(self.label_139)
        self.lne_ocupacion_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_ocupacion_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lne_ocupacion_buscar.setText("")
        self.lne_ocupacion_buscar.setObjectName("lne_ocupacion_buscar")
        self.horizontalLayout_7.addWidget(self.lne_ocupacion_buscar)
        self.label_136 = QtWidgets.QLabel(self.groupBox_2)
        self.label_136.setObjectName("label_136")
        self.horizontalLayout_7.addWidget(self.label_136)
        self.lne_sueldo_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_sueldo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_sueldo_buscar.setText("")
        self.lne_sueldo_buscar.setObjectName("lne_sueldo_buscar")
        self.horizontalLayout_7.addWidget(self.lne_sueldo_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_137 = QtWidgets.QLabel(self.groupBox_2)
        self.label_137.setObjectName("label_137")
        self.horizontalLayout_9.addWidget(self.label_137)
        self.lne_telefono_laboral_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_telefono_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_telefono_laboral_buscar.setText("")
        self.lne_telefono_laboral_buscar.setObjectName("lne_telefono_laboral_buscar")
        self.horizontalLayout_9.addWidget(self.lne_telefono_laboral_buscar)
        self.label_143 = QtWidgets.QLabel(self.groupBox_2)
        self.label_143.setObjectName("label_143")
        self.horizontalLayout_9.addWidget(self.label_143)
        self.lne_categoria_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_categoria_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_categoria_buscar.setText("")
        self.lne_categoria_buscar.setObjectName("lne_categoria_buscar")
        self.horizontalLayout_9.addWidget(self.lne_categoria_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_140 = QtWidgets.QLabel(self.groupBox_2)
        self.label_140.setObjectName("label_140")
        self.horizontalLayout_10.addWidget(self.label_140)
        self.lne_domicilio_laboral_buscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_domicilio_laboral_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_domicilio_laboral_buscar.setText("")
        self.lne_domicilio_laboral_buscar.setObjectName("lne_domicilio_laboral_buscar")
        self.horizontalLayout_10.addWidget(self.lne_domicilio_laboral_buscar)
        self.ckbx_posee_sueldo_buscar = QtWidgets.QCheckBox(self.groupBox_2)
        self.ckbx_posee_sueldo_buscar.setChecked(False)
        self.ckbx_posee_sueldo_buscar.setObjectName("ckbx_posee_sueldo_buscar")
        self.horizontalLayout_10.addWidget(self.ckbx_posee_sueldo_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/hombre-en-el-escritorio-de-la-oficina-con-un-ordenador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_17, icon1, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_18)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_18)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tw_garantes_lista = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_garantes_lista.sizePolicy().hasHeightForWidth())
        self.tw_garantes_lista.setSizePolicy(sizePolicy)
        self.tw_garantes_lista.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"")
        self.tw_garantes_lista.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(7)
        self.tw_garantes_lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_garantes_lista.setHorizontalHeaderItem(6, item)
        self.tw_garantes_lista.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout_3.addWidget(self.tw_garantes_lista, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_18, icon2, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_19)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_19)
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_11.addWidget(self.label_36)
        self.lne_tipo_iva_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_tipo_iva_buscar.setText("")
        self.lne_tipo_iva_buscar.setObjectName("lne_tipo_iva_buscar")
        self.horizontalLayout_11.addWidget(self.lne_tipo_iva_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_12.addWidget(self.label_33)
        self.lne_cuit_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cuit_buscar.setText("")
        self.lne_cuit_buscar.setObjectName("lne_cuit_buscar")
        self.horizontalLayout_12.addWidget(self.lne_cuit_buscar)
        self.ckbx_facturas_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_facturas_buscar.setChecked(False)
        self.ckbx_facturas_buscar.setObjectName("ckbx_facturas_buscar")
        self.horizontalLayout_12.addWidget(self.ckbx_facturas_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_13.addWidget(self.label_34)
        self.lne_cbu_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_cbu_buscar.setText("")
        self.lne_cbu_buscar.setObjectName("lne_cbu_buscar")
        self.horizontalLayout_13.addWidget(self.lne_cbu_buscar)
        self.ckbx_veraz_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_veraz_buscar.setChecked(False)
        self.ckbx_veraz_buscar.setObjectName("ckbx_veraz_buscar")
        self.horizontalLayout_13.addWidget(self.ckbx_veraz_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_14.addWidget(self.label_35)
        self.lne_nro_beneficio_buscar = QtWidgets.QLineEdit(self.groupBox_4)
        self.lne_nro_beneficio_buscar.setText("")
        self.lne_nro_beneficio_buscar.setObjectName("lne_nro_beneficio_buscar")
        self.horizontalLayout_14.addWidget(self.lne_nro_beneficio_buscar)
        self.ckbx_jub_pens_buscar = QtWidgets.QCheckBox(self.groupBox_4)
        self.ckbx_jub_pens_buscar.setObjectName("ckbx_jub_pens_buscar")
        self.horizontalLayout_14.addWidget(self.ckbx_jub_pens_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Íconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_19, icon3, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.boton_limpiar = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.gridLayout_6.addWidget(self.boton_limpiar, 2, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Íconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form_clientes_buscar)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_apellido_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_tipo_doc_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nombre_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_cliente_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_estado.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_doc_cliente.clear)
        self.boton_limpiar.clicked.connect(self.lne_fecha_nac.clear)
        self.boton_limpiar.clicked.connect(self.lne_estado_civil.clear)
        self.boton_limpiar.clicked.connect(self.lne_barrio_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_domicilio_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_telefono_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_ciudad_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_email_buscar.clear)
        self.boton_limpiar.clicked.connect(self.txte_observaciones_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_limite_credito_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_ocupacion_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_sueldo_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_antiguedad_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_organismo_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_categoria_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_domicilio_laboral_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_telefono_laboral_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_cuit_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_tipo_iva_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_cbu_buscar.clear)
        self.boton_limpiar.clicked.connect(self.lne_nro_beneficio_buscar.clear)
        QtCore.QMetaObject.connectSlotsByName(Form_clientes_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_dni_filtro_buscar, self.boton_buscar_buscar)
        Form_clientes_buscar.setTabOrder(self.boton_buscar_buscar, self.lne_apellido_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_apellido_buscar, self.lne_nombre_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_nombre_buscar, self.lne_nro_cliente_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_nro_cliente_buscar, self.lne_tipo_doc_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_tipo_doc_buscar, self.lne_nro_doc_cliente)
        Form_clientes_buscar.setTabOrder(self.lne_nro_doc_cliente, self.lne_estado)
        Form_clientes_buscar.setTabOrder(self.lne_estado, self.lne_fecha_nac)
        Form_clientes_buscar.setTabOrder(self.lne_fecha_nac, self.lne_estado_civil)
        Form_clientes_buscar.setTabOrder(self.lne_estado_civil, self.lne_domicilio_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_domicilio_buscar, self.lne_barrio_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_barrio_buscar, self.lne_telefono_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_telefono_buscar, self.lne_ciudad_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_ciudad_buscar, self.lne_limite_credito_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_limite_credito_buscar, self.lne_email_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_email_buscar, self.txte_observaciones_buscar)
        Form_clientes_buscar.setTabOrder(self.txte_observaciones_buscar, self.lne_sueldo_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_sueldo_buscar, self.lne_organismo_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_organismo_buscar, self.lne_antiguedad_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_antiguedad_buscar, self.lne_telefono_laboral_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_telefono_laboral_buscar, self.lne_categoria_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_categoria_buscar, self.lne_domicilio_laboral_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_domicilio_laboral_buscar, self.ckbx_posee_sueldo_buscar)
        Form_clientes_buscar.setTabOrder(self.ckbx_posee_sueldo_buscar, self.lne_tipo_iva_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_tipo_iva_buscar, self.lne_cuit_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_cuit_buscar, self.ckbx_facturas_buscar)
        Form_clientes_buscar.setTabOrder(self.ckbx_facturas_buscar, self.lne_cbu_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_cbu_buscar, self.ckbx_veraz_buscar)
        Form_clientes_buscar.setTabOrder(self.ckbx_veraz_buscar, self.lne_nro_beneficio_buscar)
        Form_clientes_buscar.setTabOrder(self.lne_nro_beneficio_buscar, self.ckbx_jub_pens_buscar)
        Form_clientes_buscar.setTabOrder(self.ckbx_jub_pens_buscar, self.tabWidget_2)
        Form_clientes_buscar.setTabOrder(self.tabWidget_2, self.tabWidget)
        Form_clientes_buscar.setTabOrder(self.tabWidget, self.boton_limpiar)
        Form_clientes_buscar.setTabOrder(self.boton_limpiar, self.tw_garantes_lista)
        Form_clientes_buscar.setTabOrder(self.tw_garantes_lista, self.lne_ocupacion_buscar)

    def retranslateUi(self, Form_clientes_buscar):
        _translate = QtCore.QCoreApplication.translate
        Form_clientes_buscar.setWindowTitle(_translate("Form_clientes_buscar", "Buscar Cliente"))
        self.label_145.setText(_translate("Form_clientes_buscar", "DNI:"))
        self.boton_buscar_buscar.setText(_translate("Form_clientes_buscar", "Buscar"))
        self.label_133.setText(_translate("Form_clientes_buscar", "Apellido:"))
        self.label_124.setText(_translate("Form_clientes_buscar", "Nombre :"))
        self.label_128.setText(_translate("Form_clientes_buscar", "N°  Cliente :"))
        self.label_127.setText(_translate("Form_clientes_buscar", "Tipo Documento:"))
        self.label_130.setText(_translate("Form_clientes_buscar", "Número:"))
        self.label_37.setText(_translate("Form_clientes_buscar", "Estado Persona"))
        self.label_122.setText(_translate("Form_clientes_buscar", "Fecha de Nacimiento:"))
        self.label_125.setText(_translate("Form_clientes_buscar", "Estado Civil:"))
        self.label_135.setText(_translate("Form_clientes_buscar", "Domicilio :"))
        self.label_123.setText(_translate("Form_clientes_buscar", "Barrio:"))
        self.label_126.setText(_translate("Form_clientes_buscar", "Teléfono:"))
        self.label_134.setText(_translate("Form_clientes_buscar", "Ciudad:"))
        self.label_132.setText(_translate("Form_clientes_buscar", "Límite por Créditos:"))
        self.label_129.setText(_translate("Form_clientes_buscar", "Email:"))
        self.label_131.setText(_translate("Form_clientes_buscar", "Observaciones: "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), _translate("Form_clientes_buscar", "Datos Personales"))
        self.label_138.setText(_translate("Form_clientes_buscar", "Organismo: "))
        self.label_141.setText(_translate("Form_clientes_buscar", "Antigüedad Laboral:"))
        self.label_142.setText(_translate("Form_clientes_buscar", "años"))
        self.label_139.setText(_translate("Form_clientes_buscar", "Ocupación:"))
        self.label_136.setText(_translate("Form_clientes_buscar", "Sueldo $:"))
        self.label_137.setText(_translate("Form_clientes_buscar", "Teléfono Laboral:"))
        self.label_143.setText(_translate("Form_clientes_buscar", "Categoría: "))
        self.label_140.setText(_translate("Form_clientes_buscar", "Domicilio Laboral:"))
        self.ckbx_posee_sueldo_buscar.setText(_translate("Form_clientes_buscar", "Posee Recibo de Sueldo"))
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
        self.label_36.setText(_translate("Form_clientes_buscar", "Tipo IVA:"))
        self.label_33.setText(_translate("Form_clientes_buscar", "N° CUIT:"))
        self.ckbx_facturas_buscar.setText(_translate("Form_clientes_buscar", "Presentó Facturas de Luz, Gas"))
        self.label_34.setText(_translate("Form_clientes_buscar", "N° CBU:"))
        self.ckbx_veraz_buscar.setText(_translate("Form_clientes_buscar", "Figura en el Veraz"))
        self.label_35.setText(_translate("Form_clientes_buscar", "N° Beneficio:"))
        self.ckbx_jub_pens_buscar.setText(_translate("Form_clientes_buscar", "Es Jubilado / Pensionado"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("Form_clientes_buscar", "Otros Datos"))
        self.boton_limpiar.setText(_translate("Form_clientes_buscar", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_clientes_buscar", "Buscar Cliente"))

