# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuota_reparar.ui'
#
# Created: Mon Dec  5 11:53:24 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_reparar_cuota(object):
    def setupUi(self, Form_reparar_cuota):
        Form_reparar_cuota.setObjectName("Form_reparar_cuota")
        Form_reparar_cuota.resize(640, 480)
        Form_reparar_cuota.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(Form_reparar_cuota)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 431))
        self.tabWidget.setStyleSheet("selection-background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"KacstOne\";\n"
"background-color: rgb(172, 55, 26);\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 51))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: rgb(211, 211, 186);\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(172, 55, 26);\n"
"border-radius: 8px;\n"
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
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(71, 18, 81, 16))
        self.label.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(258, 16, 71, 16))
        self.label_2.setStyleSheet("background-color: rgb(211, 211, 186);\n"
"")
        self.label_2.setObjectName("label_2")
        self.lne_num_credito = QtWidgets.QLineEdit(self.groupBox)
        self.lne_num_credito.setGeometry(QtCore.QRect(152, 16, 101, 21))
        self.lne_num_credito.setObjectName("lne_num_credito")
        self.lne_num_cuota = QtWidgets.QLineEdit(self.groupBox)
        self.lne_num_cuota.setGeometry(QtCore.QRect(331, 16, 91, 21))
        self.lne_num_cuota.setObjectName("lne_num_cuota")
        self.boton_buscar = QtWidgets.QPushButton(self.groupBox)
        self.boton_buscar.setGeometry(QtCore.QRect(431, 16, 81, 21))
        self.boton_buscar.setObjectName("boton_buscar")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 70, 601, 321))
        self.tabWidget_2.setStyleSheet("\n"
"background-color: rgb(211, 211, 186);\n"
"\n"
"\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 30, 144, 252))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lne_id_cuota_reparar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_id_cuota_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_id_cuota_reparar.setObjectName("lne_id_cuota_reparar")
        self.verticalLayout_2.addWidget(self.lne_id_cuota_reparar)
        self.lne_nro_cuota_reparar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_nro_cuota_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_cuota_reparar.setObjectName("lne_nro_cuota_reparar")
        self.verticalLayout_2.addWidget(self.lne_nro_cuota_reparar)
        self.cbx_estado = QtWidgets.QComboBox(self.layoutWidget)
        self.cbx_estado.setEnabled(True)
        self.cbx_estado.setStyleSheet("background-color: rgb(252, 188, 188);")
        self.cbx_estado.setObjectName("cbx_estado")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.cbx_estado.addItem("")
        self.verticalLayout_2.addWidget(self.cbx_estado)
        self.lne_venc_reparar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_venc_reparar.setEnabled(False)
        self.lne_venc_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_venc_reparar.setObjectName("lne_venc_reparar")
        self.verticalLayout_2.addWidget(self.lne_venc_reparar)
        self.lne_importe_cuota_reparar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_importe_cuota_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_importe_cuota_reparar.setObjectName("lne_importe_cuota_reparar")
        self.verticalLayout_2.addWidget(self.lne_importe_cuota_reparar)
        self.dte_fecha_cobro = QtWidgets.QDateEdit(self.layoutWidget)
        self.dte_fecha_cobro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fecha_cobro.setDate(QtCore.QDate(2017, 1, 1))
        self.dte_fecha_cobro.setObjectName("dte_fecha_cobro")
        self.verticalLayout_2.addWidget(self.dte_fecha_cobro)
        self.lne_descripcion_reparar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_descripcion_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descripcion_reparar.setObjectName("lne_descripcion_reparar")
        self.verticalLayout_2.addWidget(self.lne_descripcion_reparar)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(300, 30, 120, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 30, 121, 251))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(430, 30, 144, 220))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lne_cobrado_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_cobrado_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cobrado_reparar.setObjectName("lne_cobrado_reparar")
        self.verticalLayout_4.addWidget(self.lne_cobrado_reparar)
        self.lne_interes_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_interes_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_interes_reparar.setObjectName("lne_interes_reparar")
        self.verticalLayout_4.addWidget(self.lne_interes_reparar)
        self.lne_gastos_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_gastos_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_gastos_reparar.setObjectName("lne_gastos_reparar")
        self.verticalLayout_4.addWidget(self.lne_gastos_reparar)
        self.lne_capital_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_capital_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_capital_reparar.setObjectName("lne_capital_reparar")
        self.verticalLayout_4.addWidget(self.lne_capital_reparar)
        self.lne_punitorio_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_punitorio_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_punitorio_reparar.setObjectName("lne_punitorio_reparar")
        self.verticalLayout_4.addWidget(self.lne_punitorio_reparar)
        self.lne_descuento_reparar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lne_descuento_reparar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_descuento_reparar.setObjectName("lne_descuento_reparar")
        self.verticalLayout_4.addWidget(self.lne_descuento_reparar)
        self.tabWidget_2.addTab(self.tab_2, "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Íconos/icono-de-una-tuerca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.boton_actualizar = QtWidgets.QPushButton(Form_reparar_cuota)
        self.boton_actualizar.setGeometry(QtCore.QRect(550, 450, 81, 21))
        self.boton_actualizar.setStyleSheet("background-color: rgb(172, 55, 26);")
        self.boton_actualizar.setObjectName("boton_actualizar")

        self.retranslateUi(Form_reparar_cuota)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_reparar_cuota)
        Form_reparar_cuota.setTabOrder(self.lne_num_credito, self.lne_num_cuota)
        Form_reparar_cuota.setTabOrder(self.lne_num_cuota, self.boton_buscar)
        Form_reparar_cuota.setTabOrder(self.boton_buscar, self.boton_actualizar)
        Form_reparar_cuota.setTabOrder(self.boton_actualizar, self.tabWidget)

    def retranslateUi(self, Form_reparar_cuota):
        _translate = QtCore.QCoreApplication.translate
        Form_reparar_cuota.setWindowTitle(_translate("Form_reparar_cuota", "Reparar Cuota"))
        self.label.setText(_translate("Form_reparar_cuota", "N° Crédito : "))
        self.label_2.setText(_translate("Form_reparar_cuota", "N° Cuota : "))
        self.boton_buscar.setText(_translate("Form_reparar_cuota", "Buscar"))
        self.cbx_estado.setItemText(0, _translate("Form_reparar_cuota", "Pagada"))
        self.cbx_estado.setItemText(1, _translate("Form_reparar_cuota", "Pago Parcial"))
        self.cbx_estado.setItemText(2, _translate("Form_reparar_cuota", "A pagar"))
        self.cbx_estado.setItemText(3, _translate("Form_reparar_cuota", "Vencida 30 días"))
        self.cbx_estado.setItemText(4, _translate("Form_reparar_cuota", "Vencida 60 días"))
        self.cbx_estado.setItemText(5, _translate("Form_reparar_cuota", "Vencida 90 días"))
        self.cbx_estado.setItemText(6, _translate("Form_reparar_cuota", "Vencida 120 días"))
        self.cbx_estado.setItemText(7, _translate("Form_reparar_cuota", "Vencida 150 días"))
        self.cbx_estado.setItemText(8, _translate("Form_reparar_cuota", "Vencida 180 días"))
        self.cbx_estado.setItemText(9, _translate("Form_reparar_cuota", "En Judiciales"))
        self.dte_fecha_cobro.setDisplayFormat(_translate("Form_reparar_cuota", "dd/MM/yyyy"))
        self.label_15.setText(_translate("Form_reparar_cuota", "Importe Cobrado: "))
        self.label_5.setText(_translate("Form_reparar_cuota", "Interés:"))
        self.label_6.setText(_translate("Form_reparar_cuota", "Gastos:"))
        self.label_4.setText(_translate("Form_reparar_cuota", "Capital:"))
        self.label_16.setText(_translate("Form_reparar_cuota", "Punitorio: "))
        self.label_18.setText(_translate("Form_reparar_cuota", "Descuento :"))
        self.label_9.setText(_translate("Form_reparar_cuota", "id:"))
        self.label_3.setText(_translate("Form_reparar_cuota", "N° Cuota: "))
        self.label_13.setText(_translate("Form_reparar_cuota", "Estado: "))
        self.label_12.setText(_translate("Form_reparar_cuota", "Vencimiento: "))
        self.label_11.setText(_translate("Form_reparar_cuota", "Importe 1er Venc: "))
        self.label_17.setText(_translate("Form_reparar_cuota", "Fecha de Cobro: "))
        self.label_8.setText(_translate("Form_reparar_cuota", "Descripción:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form_reparar_cuota", "Detalle de Cuota"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_reparar_cuota", "Reparar Cuota"))
        self.boton_actualizar.setText(_translate("Form_reparar_cuota", "Actualizar"))

