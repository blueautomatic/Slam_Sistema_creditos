import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_clientes_buscar import Ui_Form_clientes_buscar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto,N_garante_credito
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook


class buscar_clientes(QDialog):
    obj_form= Ui_Form_clientes_buscar()
    id_usu=1
    id_party =""
    list_garante = list()
    nro_cliente = ""


    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_Form_clientes_buscar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_buscar.clicked.connect(self.buscar_cliente)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)


    def limpiar(self):
        self.obj_form.ckbx_facturas_buscar.setChecked(False)
        self.obj_form.ckbx_veraz_buscar.setChecked(False)
        self.obj_form.ckbx_jub_pens_buscar.setChecked(False)
        self.obj_form.ckbx_posee_sueldo_buscar.setChecked(False)

        while (self.obj_form.tw_garantes_lista.rowCount() > 0):
            self.obj_form.tw_garantes_lista.removeRow(0)



    def buscar_cliente(self):

        numero_documento_cliente= self.obj_form.lne_dni_filtro_buscar.text()
        if numero_documento_cliente != "":
            try:
                numero_documento=int(numero_documento_cliente)
            except:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()
                return False


            obj_N_datos_personales_cliente = N_datos_personales_cliente()
            obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(numero_documento)

            if obj_party_party != False:
                #tabla party party
                self.id_party = obj_party_party.id_party
                self.obj_form.lne_apellido_buscar.setText(obj_party_party.apellido)  
                self.obj_form.lne_nombre_buscar.setText(obj_party_party.nombre)
                self.obj_form.lne_tipo_doc_buscar.setText(obj_party_party.tipo_doc)
                self.obj_form.lne_nro_doc_cliente.setText(obj_party_party.num_doc)
                self.obj_form.lne_estado.setText(obj_party_party.estado)        
                self.obj_form.lne_fecha_nac.setText(str(obj_party_party.fec_nac))
                self.obj_form.lne_estado_civil.setText(obj_party_party.estado_civil) 
                self.obj_form.lne_limite_credito_buscar.setText(str(obj_party_party.limite_credito))      

                #talba address
                obj_N_party_address= N_party_address(1)
                obj_party_address = obj_N_party_address.get_party_address(self.id_party)
                self.obj_form.lne_domicilio_buscar.setText(obj_party_address.domicilio)
                self.obj_form.lne_ciudad_buscar.setText(obj_party_address.ciudad)
                self.obj_form.lne_barrio_buscar.setText(obj_party_address.barrio)


                #table contacto

                obj_N_party_contacto= N_party_contacto(1)
                list_party_contacto= obj_N_party_contacto.get_list_party_contacto(self.id_party)
                for item in list_party_contacto:
                    if item.type_contacto == "Telefono":
                        self.obj_form.lne_telefono_buscar.setText(item.value)
                    if item.type_contacto=="Email":
                        self.obj_form.lne_email_buscar.setText(item.value)



            
                #party cliente        
                obj_N_party_cliente= N_party_cliente(1)
                obj_party_cliente=obj_N_party_cliente.get_party_cliente(self.id_party)
                self.obj_form.lne_nro_cliente_buscar.setText(str(obj_party_cliente.nro_cliente))
                self.obj_form.txte_observaciones_buscar.setText(obj_party_cliente.comment) 
                


                #terminar buscar propiedad para seteart cliente
                #self.obj_form.txte_observaciones_buscar.setText(obj_party_cliente.comment)
                #toPlainText
                obj_N_datos_laborales=N_datos_laborales()
                obj_datos_laborales= obj_N_datos_laborales.get_datos_laborales(self.id_party)
                self.obj_form.lne_ocupacion_buscar.setText(obj_datos_laborales.ocupacion)

                self.obj_form.lne_organismo_buscar.setText(obj_datos_laborales.organismo)
                self.obj_form.lne_telefono_laboral_buscar.setText(obj_datos_laborales.tel_laboral)
                self.obj_form.lne_domicilio_laboral_buscar.setText(obj_datos_laborales.dom_laboral)
                self.obj_form.lne_sueldo_buscar.setText(str(obj_datos_laborales.sueldo))
                self.obj_form.lne_antiguedad_buscar.setText(obj_datos_laborales.anti_laboral)
                self.obj_form.lne_categoria_buscar.setText(obj_datos_laborales.categoria)
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.obj_form.ckbx_posee_sueldo_buscar.setChecked(obj_datos_laborales.posee_recibo_sueldo)


                obj_N_garante= N_party_garante(1)   
                self.list_garante = obj_N_garante.get_list_party_garante(obj_party_cliente.nro_cliente)
                for item in self.list_garante :
                    nro_cliente = item.nro_cliente
                    tipo_garante = item.tipo_garante
                    comment = item.comment
                    obj_N_datos_personales_cliente=N_datos_personales_cliente()
                    obj_datos_personales_cliente = obj_N_datos_personales_cliente.buscar_party_party_por_id(item.id_party_garante)

                    #AGREGAR REGISTROS EN LA GRILLA
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    rowPosition = self.obj_form.tw_garantes_lista.rowCount()
                    self.obj_form.tw_garantes_lista.insertRow(rowPosition)
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(obj_datos_personales_cliente.estado))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(item.tipo_garante))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(str(obj_party_cliente.nro_cliente)))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(obj_datos_personales_cliente.apellido))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(obj_datos_personales_cliente.nombre))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(obj_datos_personales_cliente.nro_doc))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 6, QTableWidgetItem(comment))  


                #tabla party otros buscar/gonzalo
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                obj_N_otros_datos= N_party_otros(1)
                obj_party_otros=obj_N_otros_datos.get_party_otros(self.id_party)

                self.obj_form.lne_tipo_iva_buscar.setText(obj_party_otros.tipo_iva)
                self.obj_form.lne_cuit_buscar.setText(obj_party_otros.cuit)
                self.obj_form.lne_cbu_buscar.setText(obj_party_otros.cbu)
                self.obj_form.lne_nro_beneficio_buscar.setText(obj_party_otros.num_beneficio)
                
                self.obj_form.ckbx_facturas_buscar.setChecked(obj_party_otros.presento_factura)
                self.obj_form.ckbx_veraz_buscar.setChecked(obj_party_otros.figura_veraz)
                self.obj_form.ckbx_jub_pens_buscar.setChecked(obj_party_otros.es_jubilado_pensionado)

            else:

                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText("Error, el asociado no existe o el campo esta vacio.")
                msgBox.exec_()
                return False


#app = QApplication(sys.argv)
#dialogo= buscar_clientes()
#dialogo.show()
#app.exec_()