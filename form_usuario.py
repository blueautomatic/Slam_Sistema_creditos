# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_usuario(object):
    def setupUi(self, form_usuario):
        form_usuario.setObjectName("form_usuario")
        form_usuario.resize(735, 261)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 3, 3))
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
        form_usuario.setPalette(palette)
        form_usuario.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(136, 3, 3);\n"
"font: 75 11pt \"KacstOne\";\n"
"")
        self.tabWidget_2 = QtWidgets.QTabWidget(form_usuario)
        self.tabWidget_2.setGeometry(QtCore.QRect(163, 7, 551, 231))
        self.tabWidget_2.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(7, 7, 530, 148))
        self.groupBox_2.setStyleSheet("QGroupBox\n"
"{\n"
"background-color: rgb(239, 235, 231);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
"font: 10pt \"KacstOne\";\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(239, 235, 231);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
"}\n"
"QLabel{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
"}\n"
"QCheckBox\n"
"{\n"
"background-color: rgb(239, 235, 231);\n"
"\n"
"}\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lne_nombre = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_nombre.setMinimumSize(QtCore.QSize(125, 30))
        self.lne_nombre.setMaximumSize(QtCore.QSize(125, 30))
        self.lne_nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nombre.setObjectName("lne_nombre")
        self.horizontalLayout.addWidget(self.lne_nombre)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.cbx_tipo_usu = QtWidgets.QComboBox(self.groupBox_2)
        self.cbx_tipo_usu.setObjectName("cbx_tipo_usu")
        self.cbx_tipo_usu.addItem("")
        self.cbx_tipo_usu.addItem("")
        self.horizontalLayout.addWidget(self.cbx_tipo_usu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lne_pass = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_pass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_pass.setText("")
        self.lne_pass.setObjectName("lne_pass")
        self.horizontalLayout_2.addWidget(self.lne_pass)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lne_pass2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lne_pass2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_pass2.setText("")
        self.lne_pass2.setObjectName("lne_pass2")
        self.horizontalLayout_2.addWidget(self.lne_pass2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.lne_descarga = QtWidgets.QLineEdit(self.tab_2)
        self.lne_descarga.setGeometry(QtCore.QRect(77, 161, 142, 25))
        self.lne_descarga.setObjectName("lne_descarga")
        self.boton_limpiar = QtWidgets.QPushButton(self.tab_2)
        self.boton_limpiar.setGeometry(QtCore.QRect(269, 161, 80, 24))
        self.boton_limpiar.setStyleSheet("background-color: rgb(251, 203, 193);")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_guardar = QtWidgets.QPushButton(self.tab_2)
        self.boton_guardar.setGeometry(QtCore.QRect(354, 161, 80, 24))
        self.boton_guardar.setStyleSheet("background-color: rgb(250, 217, 211);")
        self.boton_guardar.setObjectName("boton_guardar")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(8, 161, 64, 17))
        self.label_5.setObjectName("label_5")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/llave-de-administrador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon, "")
        self.line_4 = QtWidgets.QFrame(form_usuario)
        self.line_4.setGeometry(QtCore.QRect(163, 356, 16, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(form_usuario)
        self.line_3.setGeometry(QtCore.QRect(401, 356, 16, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(form_usuario)
        self.tabWidget_2.setCurrentIndex(0)
        self.boton_limpiar.clicked.connect(self.lne_nombre.clear)
        self.boton_limpiar.clicked.connect(self.lne_pass.clear)
        self.boton_limpiar.clicked.connect(self.lne_pass2.clear)
        QtCore.QMetaObject.connectSlotsByName(form_usuario)
        form_usuario.setTabOrder(self.tabWidget_2, self.lne_nombre)
        form_usuario.setTabOrder(self.lne_nombre, self.cbx_tipo_usu)
        form_usuario.setTabOrder(self.cbx_tipo_usu, self.lne_pass)
        form_usuario.setTabOrder(self.lne_pass, self.lne_pass2)
        form_usuario.setTabOrder(self.lne_pass2, self.boton_limpiar)
        form_usuario.setTabOrder(self.boton_limpiar, self.boton_guardar)

    def retranslateUi(self, form_usuario):
        _translate = QtCore.QCoreApplication.translate
        form_usuario.setWindowTitle(_translate("form_usuario", "Alta Usuarios"))
        self.label.setText(_translate("form_usuario", "Nombre de Usuario:"))
        self.lne_nombre.setText(_translate("form_usuario", "administrador"))
        self.label_4.setText(_translate("form_usuario", "Tipo Usuario:"))
        self.cbx_tipo_usu.setItemText(0, _translate("form_usuario", "Administrador"))
        self.cbx_tipo_usu.setItemText(1, _translate("form_usuario", "Ventas"))
        self.label_2.setText(_translate("form_usuario", "Contraseña:"))
        self.label_3.setText(_translate("form_usuario", "Reingrese Contraseña:"))
        self.boton_limpiar.setText(_translate("form_usuario", "Limpiar"))
        self.boton_guardar.setText(_translate("form_usuario", "Guardar"))
        self.label_5.setText(_translate("form_usuario", "descarga"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_usuario", "Nuevo Usuario"))

