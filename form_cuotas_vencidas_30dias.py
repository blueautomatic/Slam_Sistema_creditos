# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuotas_vencidas_30dias.ui'
#
# Created: Thu Oct 20 17:28:07 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuotas_vencidas_30dias(object):
    def setupUi(self, form_cuotas_vencidas_30dias):
        form_cuotas_vencidas_30dias.setObjectName("form_cuotas_vencidas_30dias")
        form_cuotas_vencidas_30dias.resize(480, 282)
        form_cuotas_vencidas_30dias.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font:  75 10Pt \"Century Schoolbook L\";\n"
"background-color:rgb(139, 44, 21);\n"
"\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(form_cuotas_vencidas_30dias)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 461, 261))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 153, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 164, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 153, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 164, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 164, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 164, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setStyleSheet("background-color: rgb(239, 235, 231);\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.boton_generar = QtWidgets.QPushButton(self.tab)
        self.boton_generar.setGeometry(QtCore.QRect(379, 53, 61, 23))
        self.boton_generar.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar.setObjectName("boton_generar")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 23, 421, 23))
        self.lineEdit.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"border-style: soid;\n"
"border-widht: 2px;\n"
"border-radius: 2px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 93, 421, 21))
        self.label_2.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"border-style: soid;\n"
"border-widht: 2px;\n"
"border-radius: 2px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.boton_generar_60_dias = QtWidgets.QPushButton(self.tab)
        self.boton_generar_60_dias.setGeometry(QtCore.QRect(379, 121, 61, 23))
        self.boton_generar_60_dias.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar_60_dias.setObjectName("boton_generar_60_dias")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 164, 421, 21))
        self.label_3.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"border-style: soid;\n"
"border-widht: 2px;\n"
"border-radius: 2px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.boton_generar_90_dias = QtWidgets.QPushButton(self.tab)
        self.boton_generar_90_dias.setGeometry(QtCore.QRect(379, 192, 61, 23))
        self.boton_generar_90_dias.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar_90_dias.setObjectName("boton_generar_90_dias")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")

        self.retranslateUi(form_cuotas_vencidas_30dias)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_cuotas_vencidas_30dias)

    def retranslateUi(self, form_cuotas_vencidas_30dias):
        _translate = QtCore.QCoreApplication.translate
        form_cuotas_vencidas_30dias.setWindowTitle(_translate("form_cuotas_vencidas_30dias", "Reportes Morosos"))
        self.boton_generar.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.lineEdit.setText(_translate("form_cuotas_vencidas_30dias", "LISTADO DE MOROSOS CON CUOTAS VENCIDAS A 30 DÍAS"))
        self.label_2.setText(_translate("form_cuotas_vencidas_30dias", " LISTADO DE MOROSOS CON CUOTAS VENCIDAS A 60 DÍAS"))
        self.boton_generar_60_dias.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.label_3.setText(_translate("form_cuotas_vencidas_30dias", "  LISTADO DE MOROSOS CON CUOTAS VENCIDAS  A 90 DÍAS"))
        self.boton_generar_90_dias.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_cuotas_vencidas_30dias", "Generador por Vencimientos"))

