import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from form_creditos_estados import Ui_form_creditos_estados
from N_cliente import N_datos_personales_cliente

class creditos_estados(QDialog):
    obj_form= Ui_form_creditos_estados()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_creditos_estados()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        #self.obj_form.boton_limpiar.clicked.connect(self.limpiar)

    def buscar_cliente(self):
        obj_party = N_datos_personales_cliente()
        obj_cliente = obj_party.buscar_partyparty_por_nrodoc(self.obj_form.lne_nro_dni_cuotas.text())
        self.obj_form.lne_apellido.setText(obj_cliente.apellido)
        self.obj_form.lne_nro_doc.setText(obj_cliente.lne_nro_doc)
        lista_prestamos









