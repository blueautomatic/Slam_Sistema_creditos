# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_historial_garante.ui'
#
# Created: Thu Oct 20 17:29:53 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(990, 590)
        Form.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 971, 571))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 55, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(8, 36, 951, 461))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"font: 75 10pt \"KacstOne\";")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 911, 410))
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
        self.tw_garantes_lista.setGeometry(QtCore.QRect(20, 210, 871, 151))
        self.tw_garantes_lista.setStyleSheet("background-color: rgb(251, 204, 193);\n"
"color: rgb(0, 0, 0);")
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(7)
        self.tw_garantes_lista.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(222, 22, 4))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tw_garantes_lista.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setItem(1, 6, item)
        self.tw_garantes_lista.horizontalHeader().setDefaultSectionSize(160)
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(19, 71, 111, 20))
        self.label_51.setObjectName("label_51")
        self.lne_garante_nro_doc = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_doc.setGeometry(QtCore.QRect(149, 70, 191, 23))
        self.lne_garante_nro_doc.setText("")
        self.lne_garante_nro_doc.setObjectName("lne_garante_nro_doc")
        self.lne_garante_apellido = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_apellido.setGeometry(QtCore.QRect(149, 40, 191, 23))
        self.lne_garante_apellido.setText("")
        self.lne_garante_apellido.setObjectName("lne_garante_apellido")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(357, 43, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(42, 43, 61, 16))
        self.label_29.setObjectName("label_29")
        self.lne_garante_nombre = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nombre.setGeometry(QtCore.QRect(430, 40, 191, 23))
        self.lne_garante_nombre.setText("")
        self.lne_garante_nombre.setObjectName("lne_garante_nombre")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(60, 100, 61, 16))
        self.label_23.setObjectName("label_23")
        self.lne_garante_estado = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_estado.setGeometry(QtCore.QRect(149, 100, 191, 23))
        self.lne_garante_estado.setText("")
        self.lne_garante_estado.setObjectName("lne_garante_estado")
        self.cbx_tipo_garante = QtWidgets.QComboBox(self.groupBox_3)
        self.cbx_tipo_garante.setGeometry(QtCore.QRect(653, 70, 181, 23))
        self.cbx_tipo_garante.setObjectName("cbx_tipo_garante")
        self.cbx_tipo_garante.addItem("")
        self.cbx_tipo_garante.setItemText(0, "")
        self.cbx_tipo_garante.addItem("")
        self.cbx_tipo_garante.addItem("")
        self.cbx_tipo_garante.addItem("")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(546, 74, 101, 16))
        self.label_24.setObjectName("label_24")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(356, 76, 81, 16))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lne_garante_nro_cliente_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_cliente_2.setGeometry(QtCore.QRect(450, 73, 81, 20))
        self.lne_garante_nro_cliente_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente_2.setText("")
        self.lne_garante_nro_cliente_2.setObjectName("lne_garante_nro_cliente_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 180, 151, 16))
        self.label.setObjectName("label")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_6, icon, "")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar.setGeometry(QtCore.QRect(833, 504, 61, 23))
        self.boton_limpiar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_guardar = QtWidgets.QPushButton(self.tab)
        self.boton_guardar.setGeometry(QtCore.QRect(900, 504, 61, 23))
        self.boton_guardar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_guardar.setObjectName("boton_guardar")
        self.lne_garante_nro_cliente = QtWidgets.QLineEdit(self.tab)
        self.lne_garante_nro_cliente.setGeometry(QtCore.QRect(710, 10, 81, 20))
        self.lne_garante_nro_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente.setText("")
        self.lne_garante_nro_cliente.setObjectName("lne_garante_nro_cliente")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(616, 13, 81, 16))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.boton_buscar_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar_buscar.setGeometry(QtCore.QRect(810, 10, 61, 20))
        self.boton_buscar_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar_buscar.setObjectName("boton_buscar_buscar")
        self.lne_dni_filtro_buscar = QtWidgets.QLineEdit(self.tab)
        self.lne_dni_filtro_buscar.setGeometry(QtCore.QRect(510, 9, 91, 20))
        self.lne_dni_filtro_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_dni_filtro_buscar.setObjectName("lne_dni_filtro_buscar")
        self.label_121 = QtWidgets.QLabel(self.tab)
        self.label_121.setGeometry(QtCore.QRect(470, 11, 31, 16))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 11pt \"KacstOne\";")
        self.label_121.setObjectName("label_121")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/silueta-masculina-de-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon1, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tw_garantes_lista.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tw_garantes_lista.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tw_garantes_lista.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tw_garantes_lista.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tw_garantes_lista.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tw_garantes_lista.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tipo Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Estado "))
        item = self.tw_garantes_lista.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Monto del Préstamo"))
        item = self.tw_garantes_lista.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nro. Cliente Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Número Documento Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Apellido Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Nombre Asociado"))
        __sortingEnabled = self.tw_garantes_lista.isSortingEnabled()
        self.tw_garantes_lista.setSortingEnabled(False)
        item = self.tw_garantes_lista.item(0, 0)
        item.setText(_translate("Form", "Principal"))
        item = self.tw_garantes_lista.item(0, 1)
        item.setText(_translate("Form", "ACTIVO"))
        item = self.tw_garantes_lista.item(0, 3)
        item.setText(_translate("Form", "1"))
        item = self.tw_garantes_lista.item(0, 4)
        item.setText(_translate("Form", "23132123"))
        item = self.tw_garantes_lista.item(0, 5)
        item.setText(_translate("Form", "Riccombene"))
        item = self.tw_garantes_lista.item(0, 6)
        item.setText(_translate("Form", "Lucas"))
        item = self.tw_garantes_lista.item(1, 0)
        item.setText(_translate("Form", "Principal"))
        item = self.tw_garantes_lista.item(1, 1)
        item.setText(_translate("Form", "MOROSO "))
        item = self.tw_garantes_lista.item(1, 3)
        item.setText(_translate("Form", "49"))
        item = self.tw_garantes_lista.item(1, 4)
        item.setText(_translate("Form", "2222"))
        item = self.tw_garantes_lista.item(1, 5)
        item.setText(_translate("Form", "Rulli"))
        item = self.tw_garantes_lista.item(1, 6)
        item.setText(_translate("Form", "Tatiana"))
        self.tw_garantes_lista.setSortingEnabled(__sortingEnabled)
        self.label_51.setText(_translate("Form", "Nro Documento:"))
        self.label_4.setText(_translate("Form", "Nombre :"))
        self.label_29.setText(_translate("Form", "Apellido:"))
        self.label_23.setText(_translate("Form", "Estado :"))
        self.cbx_tipo_garante.setItemText(1, _translate("Form", "Garante Principal"))
        self.cbx_tipo_garante.setItemText(2, _translate("Form", "Garante Secundario"))
        self.cbx_tipo_garante.setItemText(3, _translate("Form", "Otro Garante"))
        self.label_24.setText(_translate("Form", "Tipo Garante :"))
        self.label_32.setText(_translate("Form", "N°  Cliente :"))
        self.label.setText(_translate("Form", "Historial de Garantías "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "Garantías Existentes"))
        self.boton_limpiar.setText(_translate("Form", "Limpiar"))
        self.boton_guardar.setText(_translate("Form", "Guardar"))
        self.label_31.setText(_translate("Form", "N°  Cliente :"))
        self.boton_buscar_buscar.setText(_translate("Form", "Buscar"))
        self.lne_dni_filtro_buscar.setText(_translate("Form", "32033505"))
        self.label_121.setText(_translate("Form", "DNI:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Historial Garante"))

