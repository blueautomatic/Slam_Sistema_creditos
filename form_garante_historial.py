# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_garante_historial.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_garante_historial(object):
    def setupUi(self, form_garante_historial):
        form_garante_historial.setObjectName("form_garante_historial")
        form_garante_historial.resize(1099, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_garante_historial.sizePolicy().hasHeightForWidth())
        form_garante_historial.setSizePolicy(sizePolicy)
        form_garante_historial.setMinimumSize(QtCore.QSize(800, 450))
        form_garante_historial.setMaximumSize(QtCore.QSize(1600, 800))
        form_garante_historial.setStyleSheet("font: 75 10pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(81, 1, 1);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout_4 = QtWidgets.QGridLayout(form_garante_historial)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(form_garante_historial)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgba(136, 3, 3);\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab)
        self.boton_limpiar.setStyleSheet("background-color: rgb(234, 179, 167);")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.horizontalLayout_4.addWidget(self.boton_limpiar)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setMinimumSize(QtCore.QSize(75, 25))
        self.label_31.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_6.addWidget(self.label_31, 0, QtCore.Qt.AlignRight)
        self.lne_garante_nro_cliente = QtWidgets.QLineEdit(self.tab)
        self.lne_garante_nro_cliente.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_cliente.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente.setText("")
        self.lne_garante_nro_cliente.setObjectName("lne_garante_nro_cliente")
        self.horizontalLayout_6.addWidget(self.lne_garante_nro_cliente, 0, QtCore.Qt.AlignRight)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout.addWidget(self.label_29)
        self.lne_garante_apellido = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_apellido.setMinimumSize(QtCore.QSize(150, 0))
        self.lne_garante_apellido.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lne_garante_apellido.setText("")
        self.lne_garante_apellido.setObjectName("lne_garante_apellido")
        self.horizontalLayout.addWidget(self.lne_garante_apellido)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lne_garante_nombre = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nombre.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lne_garante_nombre.setText("")
        self.lne_garante_nombre.setObjectName("lne_garante_nombre")
        self.horizontalLayout.addWidget(self.lne_garante_nombre)
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setMinimumSize(QtCore.QSize(110, 0))
        self.label_51.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_51.setObjectName("label_51")
        self.horizontalLayout.addWidget(self.label_51)
        self.lne_garante_nro_doc = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_doc.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_doc.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_doc.setText("")
        self.lne_garante_nro_doc.setObjectName("lne_garante_nro_doc")
        self.horizontalLayout.addWidget(self.lne_garante_nro_doc)
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setMinimumSize(QtCore.QSize(78, 0))
        self.label_32.setMaximumSize(QtCore.QSize(78, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout.addWidget(self.label_32)
        self.lne_garante_nro_cliente_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_nro_cliente_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lne_garante_nro_cliente_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lne_garante_nro_cliente_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_cliente_2.setText("")
        self.lne_garante_nro_cliente_2.setObjectName("lne_garante_nro_cliente_2")
        self.horizontalLayout.addWidget(self.lne_garante_nro_cliente_2)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout.addWidget(self.label_23)
        self.lne_garante_estado = QtWidgets.QLineEdit(self.groupBox_3)
        self.lne_garante_estado.setMinimumSize(QtCore.QSize(100, 0))
        self.lne_garante_estado.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_garante_estado.setText("")
        self.lne_garante_estado.setObjectName("lne_garante_estado")
        self.horizontalLayout.addWidget(self.lne_garante_estado)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tw_garantes_lista = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_garantes_lista.setStyleSheet("background-color: rgb(235, 160, 143);\n"
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
        self.verticalLayout.addWidget(self.tw_garantes_lista)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_6, icon, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 1, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_121 = QtWidgets.QLabel(self.tab)
        self.label_121.setMinimumSize(QtCore.QSize(50, 25))
        self.label_121.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("")
        self.label_121.setObjectName("label_121")
        self.horizontalLayout_5.addWidget(self.label_121, 0, QtCore.Qt.AlignRight)
        self.lne_garante_nro_doc_nuevo = QtWidgets.QLineEdit(self.tab)
        self.lne_garante_nro_doc_nuevo.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_doc_nuevo.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_garante_nro_doc_nuevo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_garante_nro_doc_nuevo.setText("")
        self.lne_garante_nro_doc_nuevo.setObjectName("lne_garante_nro_doc_nuevo")
        self.horizontalLayout_5.addWidget(self.lne_garante_nro_doc_nuevo, 0, QtCore.Qt.AlignRight)
        self.boton_buscar = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_buscar.sizePolicy().hasHeightForWidth())
        self.boton_buscar.setSizePolicy(sizePolicy)
        self.boton_buscar.setMinimumSize(QtCore.QSize(75, 25))
        self.boton_buscar.setMaximumSize(QtCore.QSize(75, 25))
        self.boton_buscar.setStyleSheet("background-color: rgb(235, 160, 143);\n"
"")
        self.boton_buscar.setObjectName("boton_buscar")
        self.horizontalLayout_5.addWidget(self.boton_buscar, 0, QtCore.Qt.AlignRight)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 1, 1, 2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Íconos/silueta-masculina-de-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_garante_historial)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_cliente.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_doc_nuevo.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_cliente_2.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_estado.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_apellido.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nro_doc.clear)
        self.boton_limpiar.clicked.connect(self.lne_garante_nombre.clear)
        QtCore.QMetaObject.connectSlotsByName(form_garante_historial)
        form_garante_historial.setTabOrder(self.lne_garante_nro_cliente, self.lne_garante_nro_doc_nuevo)
        form_garante_historial.setTabOrder(self.lne_garante_nro_doc_nuevo, self.boton_buscar)
        form_garante_historial.setTabOrder(self.boton_buscar, self.tabWidget_2)
        form_garante_historial.setTabOrder(self.tabWidget_2, self.lne_garante_apellido)
        form_garante_historial.setTabOrder(self.lne_garante_apellido, self.lne_garante_nombre)
        form_garante_historial.setTabOrder(self.lne_garante_nombre, self.tw_garantes_lista)
        form_garante_historial.setTabOrder(self.tw_garantes_lista, self.boton_limpiar)
        form_garante_historial.setTabOrder(self.boton_limpiar, self.tabWidget)

    def retranslateUi(self, form_garante_historial):
        _translate = QtCore.QCoreApplication.translate
        form_garante_historial.setWindowTitle(_translate("form_garante_historial", "Historial Garante"))
        self.boton_limpiar.setText(_translate("form_garante_historial", "Limpiar"))
        self.label_31.setText(_translate("form_garante_historial", "N°  Cliente :"))
        self.label_29.setText(_translate("form_garante_historial", "Apellido:"))
        self.label_4.setText(_translate("form_garante_historial", "Nombre :"))
        self.label_51.setText(_translate("form_garante_historial", "Nro Documento:"))
        self.label_32.setText(_translate("form_garante_historial", "N°  Cliente :"))
        self.label_23.setText(_translate("form_garante_historial", "Estado :"))
        self.label.setText(_translate("form_garante_historial", "Historial de Garantías "))
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("form_garante_historial", "Garantías Existentes"))
        self.label_121.setText(_translate("form_garante_historial", "DNI:"))
        self.boton_buscar.setText(_translate("form_garante_historial", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_garante_historial", "Historial Garante"))

