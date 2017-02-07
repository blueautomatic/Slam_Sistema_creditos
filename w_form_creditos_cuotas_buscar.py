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
    id_party = ""
    id_cuota = 0
    nro_cuota = 0
    importe_apagar = 0
    importe_cobrado = 0
    list_importe_cuota = list()
    total_cuotas=0
    singleton =""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_creditos_cuotas_buscar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        #self.obj_form.tw_listado_cuotas.cellClicked.connect(self.seleccion_item_tabla)
        #self.obj_form.boton_pagar.clicked.connect(self.pagar_cuota)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)



    def limpiar(self):
        self.id_party = ""
        self.id_cuota = 0
        self.nro_cuota = 0
        self.importe_apagar = 0
        self.importe_cobrado = 0

        while (self.obj_form.tw_lista_creditos.rowCount() > 0):
            self.obj_form.tw_lista_creditos.removeRow(0)

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

  

    def seleccion_item_tabla_creditos(self,clickedIndex):
        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        twi0 = self.obj_form.tw_lista_creditos.item(clickedIndex,1)
        nro_credito = twi0.text()
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

        lst_ord = [ (i.nro_cuota, i) for i in lista_cuotas ]
        lst_ord.sort()
        lst_ord = [ i[1] for i in lst_ord ]
        for item in lst_ord:
            saldo= round(float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios)  - float(item.importe_cobrado),2)  - round(float(item.descuento),2)
            cuota_pagar = float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios) - float(item.descuento)
            rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
            self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
            if item.fecha_cobro != None :
                self.obj_form.tw_listado_cuotas.setItem(rowPosition ,9 , QTableWidgetItem(str(item.fecha_cobro)))
            else:
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))
            
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(round(cuota_pagar,2))))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(item.importe_cobrado)))        
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(round(saldo,2))))

            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(item.capital)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 11, QTableWidgetItem(str(item.interes)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 12, QTableWidgetItem(str(item.gastos)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 13, QTableWidgetItem(str(item.descripcion)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 14, QTableWidgetItem(str(item.id)))

    def buscar_cliente(self):
        numero_dni= self.obj_form.lne_dni.text()
        obj_N_datos_cliente= N_creditos("a")
        if numero_dni != "":
            try:
                numero_documento_cliente= int(numero_dni)
            except:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText( 'Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()

        obj_N_datos_personales_cliente = N_datos_personales_cliente()
        obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(numero_documento_cliente)
        if obj_party_party != False:
           # self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido)
            self.obj_form.tw_lista_creditos.setEnabled(True)
            self.obj_form.tw_listado_cuotas.setEnabled(True)

            obj_N_credito = N_creditos(1)   
            list_credito_party = obj_N_credito.get_list_credito(obj_party_party.id_party)

            for item in list_credito_party:
                nro_cliente = item.nro_cliente
                fecha_credito = item.fecha_credito
                nro_credito = item.nro_credito
                cantidad_cuotas = item.cantidad_cuotas
                cred_total = item.cred_total
                observaciones = item.observaciones
                estado = item.estado

                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 0, QTableWidgetItem(str(estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 1, QTableWidgetItem(str(nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 2, QTableWidgetItem(str(nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 3, QTableWidgetItem(str(fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 4, QTableWidgetItem(str(cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 5, QTableWidgetItem(str(cred_total)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 6, QTableWidgetItem(str(observaciones)))

