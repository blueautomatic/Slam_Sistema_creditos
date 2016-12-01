import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_creditos_cuotas_buscar import Ui_form_creditos_cuotas_buscar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from N_cuotas import N_cuotas

class creditos_cuotas_buscar(QDialog):
    obj_form= Ui_form_creditos_cuotas_buscar()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_creditos_cuotas_buscar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos_cuotas_buscar.cellClicked.connect(self.seleccion_item_tabla_creditos)
        #self.obj_form.boton_limpiar.clicked.connect(self.limpiar)

    def seleccion_item_tabla_creditos(self,clickedIndex):
        #allRows = self.obj_form.tw_registrotitulos.rowCount()
        while (self.obj_form.tw_listado_cuotas_cuotas_buscar.rowCount() > 0):
            self.obj_form.tw_listado_cuotas_cuotas_buscar.removeRow(0)
        twi0 = self.obj_form.tw_lista_creditos_cuotas_buscar.item(clickedIndex,0)
        nro_credito = twi0.text()
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))
        for item in lista_cuotas:
            rowPosition = self.obj_form.tw_listado_cuotas_cuotas_buscar.rowCount()
            self.obj_form.tw_listado_cuotas_cuotas_buscar.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_credito)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 2, QTableWidgetItem(str(item.capital)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 2, QTableWidgetItem(str(item.interes)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 5, QTableWidgetItem(str(item.primer_Vencimiento)))        
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 6, QTableWidgetItem(str(item.importe_primer_venc)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 8, QTableWidgetItem(str(item.fecha_cobro)))
            self.obj_form.tw_listado_cuotas_cuotas_buscar.setItem(rowPosition , 9, QTableWidgetItem(str(item.importe_cobrado)))
    def buscar_cliente(self):
        self.limpiar()
        numero_documento_cliente= self.obj_form.lne_nro_dni_cuotas.text()
        try:
            numero_documento=int(numero_documento_cliente)
        except:
            msgBox=QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el numero de documento sin espacios y sin puntos')
            msgBox.exec_()
        obj_N_datos_personales_cliente = N_datos_personales_cliente("a")
        obj_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(numero_documento_cliente)
        if obj_party != False:
            obj_N_credito = N_creditos(1)   
            list_credito_party = obj_N_credito.get_list_credito(obj_party.id_party)
            for item in list_credito_party:
                nro_cliente = item.nro_cliente
                fecha_credito = item.fecha_credito
                nro_credito = item.nro_credito
                cantidad_cuotas = item.cantidad_cuotas
                cred_total = item.cred_total
                observaciones = item.observaciones
                rowPosition = self.obj_form.tw_lista_creditos_cuotas_buscar.rowCount()
                self.obj_form.tw_lista_creditos_cuotas_buscar.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 0, QTableWidgetItem(str(nro_credito)))
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 1, QTableWidgetItem(str(nro_cliente)))
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 2, QTableWidgetItem(str(fecha_credito)))
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 3, QTableWidgetItem(str(cantidad_cuotas)))
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 4, QTableWidgetItem(str(cred_total)))
                self.obj_form.tw_lista_creditos_cuotas_buscar.setItem(rowPosition , 6, QTableWidgetItem(str(observaciones)))
        else:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Error numero de DNI inexistente')
            msgBox.exec_()

    def limpiar(self):
        while (self.obj_form.tw_lista_creditos_cuotas_buscar.rowCount() > 0):
            self.obj_form.tw_lista_creditos_cuotas_buscar.removeRow(0)
        while (self.obj_form.tw_listado_cuotas_cuotas_buscar.rowCount() > 0):
            self.obj_form.tw_listado_cuotas_cuotas_buscar.removeRow(0)

#app = QApplication(sys.argv)
#dialogo= creditos_cuotas_buscar()
#dialogo.show()
#app.exec_()