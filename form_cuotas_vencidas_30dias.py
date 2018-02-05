# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuotas_vencidas_30dias.ui'
#
# Created: Fri Feb 24 11:25:32 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuotas_vencidas_30dias(object):
    def setupUi(self, form_cuotas_vencidas_30dias):
        form_cuotas_vencidas_30dias.setObjectName("form_cuotas_vencidas_30dias")
        form_cuotas_vencidas_30dias.resize(488, 282)
        form_cuotas_vencidas_30dias.setStyleSheet("font: 75 11pt \"KacstOne\";\n"
"selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(136, 3, 3, 100);\n"
"\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_cuotas_vencidas_30dias)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(form_cuotas_vencidas_30dias)
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
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
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
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
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
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
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
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.boton_generar = QtWidgets.QPushButton(self.tab)
        self.boton_generar.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar.setObjectName("boton_generar")
        self.verticalLayout.addWidget(self.boton_generar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.boton_generar_60_dias = QtWidgets.QPushButton(self.tab)
        self.boton_generar_60_dias.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar_60_dias.setObjectName("boton_generar_60_dias")
        self.verticalLayout_2.addWidget(self.boton_generar_60_dias)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet("background-color: rgb(222, 175, 153);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.boton_generar_90_dias = QtWidgets.QPushButton(self.tab)
        self.boton_generar_90_dias.setStyleSheet("background-color: rgb(251, 204, 193);")
        self.boton_generar_90_dias.setObjectName("boton_generar_90_dias")
        self.verticalLayout_3.addWidget(self.boton_generar_90_dias)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_cuotas_vencidas_30dias)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_cuotas_vencidas_30dias)

    def retranslateUi(self, form_cuotas_vencidas_30dias):
        _translate = QtCore.QCoreApplication.translate
        form_cuotas_vencidas_30dias.setWindowTitle(_translate("form_cuotas_vencidas_30dias", "Reportes Morosos"))
        self.lineEdit.setText(_translate("form_cuotas_vencidas_30dias", "LISTADO DE MOROSOS CON CUOTAS VENCIDAS A 30 DÍAS"))
        self.boton_generar.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.label_2.setText(_translate("form_cuotas_vencidas_30dias", " LISTADO DE MOROSOS CON CUOTAS VENCIDAS A 60 DÍAS"))
        self.boton_generar_60_dias.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.label_3.setText(_translate("form_cuotas_vencidas_30dias", "  LISTADO DE MOROSOS CON CUOTAS VENCIDAS  A 90 DÍAS"))
        self.boton_generar_90_dias.setText(_translate("form_cuotas_vencidas_30dias", "Generar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_cuotas_vencidas_30dias", "Generador por Vencimientos"))

