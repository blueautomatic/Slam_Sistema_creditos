# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_garante_historial.ui'
#
# Created: Thu Oct 20 17:29:30 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_garante_historial(object):
    def setupUi(self, form_garante_historial):
        form_garante_historial.setObjectName("form_garante_historial")
        form_garante_historial.resize(1043, 582)
        form_garante_historial.setStyleSheet("selection-background-color: rgb(222, 222, 222);\n"
"selection-color: rgb(0, 0, 0);")
        self.tabWidget = QtWidgets.QTabWidget(form_garante_historial)
        self.tabWidget.setGeometry(QtCore.QRect(10, 11, 1020, 561))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
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
"font:  75 11pt \"Century Schoolbook L\";\n"
"selection-background-color: rgb(255, 170, 127);")
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
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 940, 410))
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
        self.tw_garantes_lista.setGeometry(QtCore.QRect(20, 160, 901, 151))
        self.tw_garantes_lista.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tw_garantes_lista.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_garantes_lista.setObjectName("tw_garantes_lista")
        self.tw_garantes_lista.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_garantes_lista.setHorizontalHeaderItem(7, item)
        self.tw_garantes_lista.horizontalHeader().setDefaultSectionSize(175)
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(19, 51, 111, 20))
        self.label_51.setObjectName("label_51")
        self.lne_garante_nro_doc = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_doc.setGeometry(QtCore.QRect(149, 50, 191, 23))
        self.lne_garante_nro_doc.setText("")
        self.lne_garante_nro_doc.setObjectName("lne_garante_nro_doc")
        self.lne_garante_apellido = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_apellido.setGeometry(QtCore.QRect(150, 20, 191, 23))
        self.lne_garante_apellido.setText("")
        self.lne_garante_apellido.setObjectName("lne_garante_apellido")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(357, 23, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(42, 23, 61, 16))
        self.label_29.setObjectName("label_29")
        self.lne_garante_nombre = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nombre.setGeometry(QtCore.QRect(430, 20, 191, 23))
        self.lne_garante_nombre.setText("")
        self.lne_garante_nombre.setObjectName("lne_garante_nombre")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(60, 80, 61, 16))
        self.label_23.setObjectName("label_23")
        self.lne_garante_estado = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_estado.setGeometry(QtCore.QRect(150, 80, 191, 23))
        self.lne_garante_estado.setText("")
        self.lne_garante_estado.setObjectName("lne_garante_estado")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(356, 56, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lne_garante_nro_cliente_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_cliente_2.setGeometry(QtCore.QRect(450, 53, 81, 20))
        self.lne_garante_nro_cliente_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente_2.setText("")
        self.lne_garante_nro_cliente_2.setObjectName("lne_garante_nro_cliente_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 130, 151, 16))
        self.label.setObjectName("label")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_6, icon, "")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar.setGeometry(QtCore.QRect(821, 490, 80, 23))
        self.boton_limpiar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_guardar = QtWidgets.QPushButton(self.tab)
        self.boton_guardar.setGeometry(QtCore.QRect(910, 490, 80, 23))
        self.boton_guardar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";\n"
"")
        self.boton_guardar.setObjectName("boton_guardar")
        self.lne_garante_nro_cliente = QtWidgets.QLineEdit(self.tab)
        self.lne_garante_nro_cliente.setGeometry(QtCore.QRect(620, 17, 81, 20))
        self.lne_garante_nro_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente.setText("")
        self.lne_garante_nro_cliente.setObjectName("lne_garante_nro_cliente")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(526, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/silueta-masculina-de-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.boton_buscar = QtWidgets.QPushButton(form_garante_historial)
        self.boton_buscar.setGeometry(QtCore.QRect(918, 60, 80, 20))
        self.boton_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"font: 75 10pt \"KacstOne\";")
        self.boton_buscar.setObjectName("boton_buscar")
        self.label_121 = QtWidgets.QLabel(form_garante_historial)
        self.label_121.setGeometry(QtCore.QRect(727, 63, 31, 16))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("background-color: rgb(172, 55, 26);\n"
"font: 75 10pt \"KacstOne\";")
        self.label_121.setObjectName("label_121")
        self.lne_garante_nro_doc_nuevo = QtWidgets.QLineEdit(form_garante_historial)
        self.lne_garante_nro_doc_nuevo.setGeometry(QtCore.QRect(758, 61, 151, 20))
        self.lne_garante_nro_doc_nuevo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_doc_nuevo.setText("")
        self.lne_garante_nro_doc_nuevo.setObjectName("lne_garante_nro_doc_nuevo")

        self.retranslateUi(form_garante_historial)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_garante_estado.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_cliente_2.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_doc.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_apellido.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nombre.clear)
        QtCore.QMetaObject.connectSlotsByName(form_garante_historial)

    def retranslateUi(self, form_garante_historial):
        _translate = QtCore.QCoreApplication.translate
        form_garante_historial.setWindowTitle(_translate("form_garante_historial", "Historial Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(0)
        item.setText(_translate("form_garante_historial", "Tipo Garante"))
        item = self.tw_garantes_lista.horizontalHeaderItem(1)
        item.setText(_translate("form_garante_historial", "Estado credito "))
        item = self.tw_garantes_lista.horizontalHeaderItem(2)
        item.setText(_translate("form_garante_historial", "Nro_credito"))
        item = self.tw_garantes_lista.horizontalHeaderItem(3)
        item.setText(_translate("form_garante_historial", "Monto del Préstamo"))
        item = self.tw_garantes_lista.horizontalHeaderItem(4)
        item.setText(_translate("form_garante_historial", "Nro. Cliente Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(5)
        item.setText(_translate("form_garante_historial", "DNI Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(6)
        item.setText(_translate("form_garante_historial", "Apellido Asociado"))
        item = self.tw_garantes_lista.horizontalHeaderItem(7)
        item.setText(_translate("form_garante_historial", "Nombre Asociado"))
        self.label_51.setText(_translate("form_garante_historial", "Nro Documento:"))
        self.label_4.setText(_translate("form_garante_historial", "Nombre :"))
        self.label_29.setText(_translate("form_garante_historial", "Apellido:"))
        self.label_23.setText(_translate("form_garante_historial", "Estado :"))
        self.label_32.setText(_translate("form_garante_historial", "N°  Cliente :"))
        self.label.setText(_translate("form_garante_historial", "Historial de Garantías "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("form_garante_historial", "Garantías Existentes"))
        self.boton_limpiar.setText(_translate("form_garante_historial", "Limpiar"))
        self.boton_guardar.setText(_translate("form_garante_historial", "Guardar"))
        self.label_31.setText(_translate("form_garante_historial", "N°  Cliente :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_garante_historial", "Historial Garante"))
        self.boton_buscar.setText(_translate("form_garante_historial", "Buscar"))
        self.label_121.setText(_translate("form_garante_historial", "DNI:"))

