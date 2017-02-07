import sys, datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_clientes_actualizar import Ui_Form_clientes_actualizar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook

class clientes_actualizar(QDialog):

    obj_form= Ui_Form_clientes_actualizar()
    id_usu=1
    id_party =""
    list_garante = list()
    nro_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_Form_clientes_actualizar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_actualizar.clicked.connect(self.buscar_cliente)
        self.obj_form.boton_actualizar.clicked.connect(self.actualizar_cliente)
        self.obj_form.boton_buscar_garante_actualizar.clicked.connect(self.buscar_garante)
        self.obj_form.boton_agregar_actualizar.clicked.connect(self.agregar_garante)
        self.obj_form.boton_limpiar_actualizar_cliente.clicked.connect(self.limpiar)

        

        self.obj_form.tw_garantes_lista.cellClicked.connect(self.seleccion_item_tabla)

    def limpiar(self):
        self.obj_form.ckbx_facturas_actualizar.setChecked(False)
        self.obj_form.ckbx_veraz_actualizar.setChecked(False)
        self.obj_form.ckbx_jub_pens_actualizar.setChecked(False)
        self.obj_form.ckbx_recibo_sueldo_actualizar.setChecked(False)
        while (self.obj_form.tw_garantes_lista.rowCount() > 0):
            self.obj_form.tw_garantes_lista.removeRow(0)

        for item in self.list_garante:
            self.list_garante.remove(item)


    def agregar_garante(self):
        number= self.obj_form.lne_garante_nro_doc_actualizar.text()
        id_party_party_garante=""
        try:
            nro_doc_garante= int(number)
        except exception:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
            msgBox.exec_()

        obj_Cliente_garante = N_party_garante("a")
        existe_garante=False

        existe_garante = obj_Cliente_garante.es_garante_de_otro_cliente(nro_doc_garante)
        
        obj_party_party_garante = N_datos_personales_cliente()
        id_party_party_garante = obj_party_party_garante.get_id_party_party_garante(nro_doc_garante)

        obj_N_creditos = N_creditos(1)
        tiene_prestamo =  obj_N_creditos.get_tiene_prestamos_activo(self.obj_form.lne_garante_nro_doc_actualizar.text())
        
        if (existe_garante == True ) or (tiene_prestamo == True) :
            msgBox = QMessageBox.question(self, 'Validar Clientes y Garantes ', 'Desea agregarlo igualmente?',QMessageBox.Yes | QMessageBox.No)
            if msgBox == QMessageBox.Yes :
                garante_nro_doc = self.obj_form.lne_garante_nro_doc_actualizar.text()

                cliente_nro_del_garante = int(self.obj_form.lne_garante_nro_cliente_actualizar.text())
                garante_apellido = self.obj_form.lne_garante_apellido_actualizar.text()
                garante_nombre = self.obj_form.lne_garante_nombre_actualizar.text()
                garante_estado = self.obj_form.lne_garante_estado_actualizar.text()
                tipo_garante = self.obj_form.cbx_tipo_garante_actualizar.currentText()
                
                obj_N_party_garante = N_party_garante("A")
                obj_party_garante = N_party_garante("A")
                obj_party_garante.comment = self.obj_form.txte_garante_observaciones_actualizar.toPlainText()
                obj_party_garante.tipo_garante = self.obj_form.cbx_tipo_garante_actualizar.currentText()
                obj_party_garante.nro_cliente = int(self.obj_form.lne_garante_nro_cliente_actualizar.text())

                obj_party_garante.id_party_garante = id_party_party_garante
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.list_garante.append(obj_party_garante)


                #AGREGAR REGISTROS EN LA GRILLA
                rowPosition = self.obj_form.tw_garantes_lista.rowCount()
                self.obj_form.tw_garantes_lista.insertRow(rowPosition)
                 #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(garante_estado))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(tipo_garante))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_garante_nro_cliente_actualizar.text()))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(garante_apellido))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(garante_nombre))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(garante_nro_doc))
        else: 
            garante_nro_doc = self.obj_form.lne_garante_nro_doc_actualizar.text()

            cliente_nro_del_garante = int(self.obj_form.lne_garante_nro_cliente_actualizar.text())
            garante_apellido = self.obj_form.lne_garante_apellido_actualizar.text()
            garante_nombre = self.obj_form.lne_garante_nombre_actualizar.text()
            garante_estado = self.obj_form.lne_garante_estado_actualizar.text()
            tipo_garante = self.obj_form.cbx_tipo_garante_actualizar.currentText()
            
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_N_party_garante = N_party_garante("A")
            obj_party_garante = N_party_garante("A")
            obj_party_garante.comment = self.obj_form.txte_garante_observaciones_actualizar.toPlainText()
            obj_party_garante.tipo_garante = self.obj_form.cbx_tipo_garante_actualizar.currentText()
            obj_party_garante.nro_cliente = int(self.obj_form.lne_garante_nro_cliente_actualizar.text())

            obj_party_garante.id_party_garante = id_party_party_garante

            self.list_garante.append(obj_party_garante)


            #AGREGAR REGISTROS EN LA GRILLA
            rowPosition = self.obj_form.tw_garantes_lista.rowCount()
            self.obj_form.tw_garantes_lista.insertRow(rowPosition)
             #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(garante_estado))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(tipo_garante))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_garante_nro_cliente_actualizar.text()))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(garante_apellido))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(garante_nombre))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(garante_nro_doc))
    
    def buscar_garante(self):
      
        number= self.obj_form.lne_garante_nro_doc_actualizar.text()
        

       
        obj_N_datos_garante= N_datos_personales_cliente()
        if number != "":
            try:
                numero_documento_garante= int(number)
            except:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()
            obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar(str(numero_documento_garante))
            if obj_datos_garante != None:
                self.obj_form.lne_garante_apellido_actualizar.setText(obj_datos_garante.apellido)
                self.obj_form.lne_garante_nombre_actualizar.setText(obj_datos_garante.nombre)
                self.obj_form.lne_garante_estado_actualizar.setText(obj_datos_garante.estado)
                
                obj_N_party_cliente = N_party_cliente(obj_datos_garante.id_party)
                nro_cliente_garante = obj_N_party_cliente.get_nro_cliente(obj_datos_garante.id_party)
                self.obj_form.lne_garante_nro_cliente_actualizar.setText(str(nro_cliente_garante))

                
            else:

                msgBox = QMessageBox()
                msgBox.setText('Numero de documento inexistente')
                msgBox.exec_()
                



        else :
            if self.obj_form.lne_garante_nro_cliente_actualizar.text() != "":
                try:
                    garante_nro_cliente_nuevo = int(self.obj_form.lne_garante_nro_cliente_actualizar.text())
                    
                    obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar_nrocliente(garante_nro_cliente_nuevo)
                    self.obj_form.lne_garante_apellido_actualizar.setText(obj_datos_garante.apellido)
                    self.obj_form.lne_garante_nombre_actualizar.setText(obj_datos_garante.nombre)
                    self.obj_form.lne_garante_estado_actualizar.setText(obj_datos_garante.estado)
                    self.obj_form.lne_garante_nro_doc_actualizar.setText(obj_datos_garante.num_doc)
                    

                except:
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Atencion")
                    msgBox.setText('Verificar Numero de cliente garante sin espacios y sin puntos ')
                    msgBox.exec_()


                    return False
    def seleccion_item_tabla(self, clickedIndex):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        twi0 = self.obj_form.tw_garantes_lista.item(clickedIndex,0)
        twi1 = self.obj_form.tw_garantes_lista.item(clickedIndex,1)
        twi2 = self.obj_form.tw_garantes_lista.item(clickedIndex,2)
        twi3 = self.obj_form.tw_garantes_lista.item(clickedIndex,3)
        twi4 = self.obj_form.tw_garantes_lista.item(clickedIndex,4)
        twi5 = self.obj_form.tw_garantes_lista.item(clickedIndex,5)
            
        self.obj_form.lne_garante_estado_actualizar.setText(twi0.text())
        self.obj_form.lne_garante_nro_cliente_actualizar.setText(twi2.text())
        self.obj_form.lne_garante_apellido_actualizar.setText(twi3.text())
        self.obj_form.lne_garante_nombre_actualizar.setText(twi4.text())
        self.obj_form.lne_garante_nro_doc_actualizar.setText(twi5.text())            
        self.obj_form.tw_garantes_lista.removeRow(clickedIndex)

        obj_N_datos_personales_cliente= N_datos_personales_cliente()
        obj_dpc=N_datos_personales_cliente()
        obj_dpc=obj_N_datos_personales_cliente.buscar_partyparty_por_nrodoc(self.obj_form.lne_garante_nro_doc_actualizar.text())
        contador=0
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in self.list_garante:
            if obj_dpc.id_party == item.id_party_garante:
                self.list_garante.remove(item)
                #contador = contador+1

    def buscar_cliente(self,id_party):
        self.limpiar()
        numero_documento_cliente= self.obj_form.lne_dni_filtro_actualizar.text()
        try:
            numero_documento=int(numero_documento_cliente)
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
            msgBox.exec_()


        obj_N_datos_personales_cliente = N_datos_personales_cliente()
        obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(self.obj_form.lne_dni_filtro_actualizar.text())


        if obj_party_party != False:
            self.obj_form.tab_widget_actualizar_cliente.setEnabled(True)
            self.obj_form.lne_id_party_actualizar.setText(str(obj_party_party.id_party))
            self.id_party = obj_party_party.id_party
            self.obj_form.lne_apellido_actualizar.setText(obj_party_party.apellido)  
            self.obj_form.lne_nombre_actualizar.setText(obj_party_party.nombre)
            index_tipo_doc=self.obj_form.cbx_tipo_doc_actualizar.findText(str(obj_party_party.tipo_doc))
            self.obj_form.cbx_tipo_doc_actualizar.setCurrentIndex(index_tipo_doc)
            self.obj_form.lne_dni_filtro_actualizar.setText(obj_party_party.num_doc)
            self.obj_form.lne_nro_doc_actualizar.setText(obj_party_party.num_doc)
            index_estado= self.obj_form.cbx_estado_actualizar.findText(str(obj_party_party.estado))
            self.obj_form.cbx_estado_actualizar.setCurrentIndex(index_estado)   
            self.obj_form.dte_nacimiento_actualizar.setDate(obj_party_party.fec_nac)
            index_estado_civil= self.obj_form.cbx_estado_civil_actualizar.findText(obj_party_party.estado_civil)
            self.obj_form.cbx_estado_civil_actualizar.setCurrentIndex(index_estado_civil)
            self.obj_form.lne_limite_credito_actualizar.setText(str(obj_party_party.limite_credito))
            #tabla party adddreeeeeesssss actualizar
            obj_N_party_address= N_party_address(1)
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_party_address = obj_N_party_address.get_party_address(self.id_party)
            self.obj_form.lne_domicilio_actualizar.setText(obj_party_address.domicilio)
            index_ciudad=self.obj_form.cbx_ciudad_actualizar.findText(str(obj_party_address.ciudad))
            self.obj_form.cbx_ciudad_actualizar.setCurrentIndex(index_ciudad)
            self.obj_form.lne_barrio_actualizar.setText(obj_party_address.barrio)
            #tabla contacto 
            
            #VER EL OBSERVACIONES
            
            obj_n_cliente = N_party_cliente(1)
            obj_comentario = obj_n_cliente.get_party_cliente(self.id_party)
            self.obj_form.txte_observaciones_actualizar.setText(obj_comentario.comment)           
            
            obj_N_party_contacto= N_party_contacto(1)
            list_party_contacto= obj_N_party_contacto.get_list_party_contacto(self.id_party)
            for item in list_party_contacto:
                if item.type_contacto == "Telefono":
                    self.obj_form.lne_telefono_actualizar.setText(item.value)
                if item.type_contacto=="Email":
                    self.obj_form.lne_email_actualizar.setText(item.value)

            #party cliente         
            obj_N_party_cliente= N_party_cliente(1)
            obj_party_cliente=obj_N_party_cliente.get_party_cliente(self.id_party)
            self.obj_form.lne_nro_cliente.setText(str(obj_party_cliente.nro_cliente))
            #datos laborales  
            obj_N_datos_laborales=N_datos_laborales()
            obj_datos_laborales= obj_N_datos_laborales.get_datos_laborales(self.id_party)
            self.obj_form.lne_ocupacion_actualizar.setText(obj_datos_laborales.ocupacion)
            self.obj_form.lne_organismo_actualizar.setText(obj_datos_laborales.organismo)
            self.obj_form.lne_telefono_laboral_actualizar.setText(obj_datos_laborales.tel_laboral)
            self.obj_form.lne_domicilio_laboral_actualizar.setText(obj_datos_laborales.dom_laboral)
            self.obj_form.lne_sueldo_actualizar.setText(str(obj_datos_laborales.sueldo))
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            self.obj_form.lne_antiguedad_actualizar.setText(obj_datos_laborales.anti_laboral)
            self.obj_form.lne_categoria_actualizar.setText(obj_datos_laborales.categoria)
            self.obj_form.ckbx_recibo_sueldo_actualizar.setChecked(obj_datos_laborales.posee_recibo_sueldo)
            #party otros  
            obj_N_otros_datos_actualizar= N_party_otros(1)
            obj_party_otros=obj_N_otros_datos_actualizar.get_party_otros(self.id_party)
            index_tipo_iva=self.obj_form.cbx_tipo_iva_actualizar.findText(str(obj_party_otros.tipo_iva))
            self.obj_form.cbx_tipo_iva_actualizar.setCurrentIndex(index_tipo_iva)
            self.obj_form.lne_cuit_actualizar.setText(obj_party_otros.cuit)
            self.obj_form.lne_cbu_actualizar.setText(obj_party_otros.cbu)
            self.obj_form.lne_nro_beneficio_actualizar.setText(obj_party_otros.num_beneficio)
            self.obj_form.ckbx_facturas_actualizar.setChecked(obj_party_otros.presento_factura)
            self.obj_form.ckbx_veraz_actualizar.setChecked(obj_party_otros.figura_veraz)
            #self.obj_form.ckbx_monotributista_actualizar.setChecked(obj_party_otros.monotributista)
            #self.obj_form.ckbx_cliente_bloqueado_actualizar.setChecked(obj_party_otros.cliente_bloqueado)
            self.obj_form.ckbx_jub_pens_actualizar.setChecked(obj_party_otros.es_jubilado_pensionado)
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
        else:
            msgBox = QMessageBox()
            msgBox.setText('Error numero de DNI inexistente')
            msgBox.exec_()

            #actualizo al cliente
    def actualizar_cliente(self,id_party):

        #  party party
        if (self.obj_form.lne_apellido_actualizar.text() !="") and (self.obj_form.lne_nombre_actualizar.text() !="") and (self.obj_form.lne_nro_doc_actualizar.text() !="") and (self.obj_form.lne_nro_cliente.text() !=""):
            obj_N_datos_personales_cliente = N_datos_personales_cliente()

            obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_id(self.obj_form.lne_id_party_actualizar.text())

            self.id_party = obj_party_party.id_party
            obj_party_party = N_datos_personales_cliente()

            obj_party_party.apellido = self.obj_form.lne_apellido_actualizar.text().upper()
            obj_party_party.nombre = self.obj_form.lne_nombre_actualizar.text().upper()
            
           
            obj_party_party.tipo_doc = self.obj_form.cbx_tipo_doc_actualizar.currentText()
            obj_party_party.nro_doc = self.obj_form.lne_nro_doc_actualizar.text()
            obj_party_party.estado_civil = self.obj_form.cbx_estado_civil_actualizar.currentText()
            obj_party_party.fec_nac = self.obj_form.dte_nacimiento_actualizar.text()
            obj_party_party.limite_credito = self.obj_form.lne_limite_credito_actualizar.text()
            obj_party_party.estado = self.obj_form.cbx_estado_actualizar.currentText()

            obj_N_datos_personales_cliente.actualizar_party_party(obj_party_party, self.id_party)
            obj_party_cliente = N_party_cliente(self.id_party)

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_comentario = obj_party_cliente.actualizar_comentario(self.id_party, self.obj_form.txte_observaciones_actualizar.toPlainText())
      

            self.nro_cliente = obj_party_cliente.get_nro_cliente(self.id_party)
            self.obj_form.lne_nro_cliente.setText(str(self.nro_cliente))
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()

            # tabla address
            ciudad = self.obj_form.lne_barrio_actualizar.text()
            obj_N_party_address = N_party_address(ciudad)
            obj_N_party_address.domicilio = self.obj_form.lne_domicilio_actualizar.text()
            obj_N_party_address.barrio = self.obj_form.lne_barrio_actualizar.text()
            obj_N_party_address.ciudad = self.obj_form.cbx_ciudad_actualizar.currentText()
            #boton guardar
            obj_party_address= N_party_address(ciudad)
            obj_party_address.actualizar_party_address(obj_N_party_address, self.id_party) 

            # actualizo tabla contact

            obj_party_contacto3= N_party_contacto(1)

            obj_party_contacto3.type_contacto= "Telefono"
            obj_party_contacto3.value =self.obj_form.lne_telefono_actualizar.text()

            obj_party_contacto_email=N_party_contacto(1)
            obj_party_contacto_email.type_contacto="Email"
            obj_party_contacto_email.value= self.obj_form.lne_email_actualizar.text()

            
            obj_N_party_contacto=N_party_contacto(1)
            #obj_N_party_contacto.domicilio = self.obj_form.txte_observaciones_actualizar.text()
            obj_N_party_contacto.actualizar_party_contact(obj_party_contacto3, self.id_party)
            obj_N_party_contacto.actualizar_party_contact(obj_party_contacto_email, self.id_party)



            #actualizo party datos laborales

            

            organismo = self.obj_form.lne_organismo_actualizar.text()
            obj_N_datos_laborales = N_datos_laborales()
            obj_N_datos_laborales.sueldo = self.obj_form.lne_sueldo_actualizar.text()
            obj_N_datos_laborales.anti_laboral = self.obj_form.lne_antiguedad_actualizar.text()
            obj_N_datos_laborales.tel_laboral = self.obj_form.lne_telefono_laboral_actualizar.text()
            obj_N_datos_laborales.dom_laboral = self.obj_form.lne_domicilio_laboral_actualizar.text()
            obj_N_datos_laborales.organismo = self.obj_form.lne_organismo_actualizar.text()
            obj_N_datos_laborales.ocupacion = self.obj_form.lne_ocupacion_actualizar.text()
            obj_N_datos_laborales.categoria = self.obj_form.lne_categoria_actualizar.text()

            if self.obj_form.ckbx_recibo_sueldo_actualizar.isChecked():
                obj_N_datos_laborales.posee_recibo_sueldo = True
            else:
                obj_N_datos_laborales.posee_recibo_sueldo = False
            

            #boton guardar
            obj_datos_laborales= N_datos_laborales()
            obj_datos_laborales.actualizar_datos_laborales(obj_N_datos_laborales,self.id_party)


            # tabla party otros------------
            cuit = self.obj_form.lne_cuit_actualizar.text()
            obj_N_party_otros = N_party_otros(cuit)
            obj_N_party_otros.tipo_iva = self.obj_form.cbx_tipo_iva_actualizar.currentText()
            obj_N_party_otros.cuit = self.obj_form.lne_cuit_actualizar.text()
            obj_N_party_otros.cbu = self.obj_form.lne_cbu_actualizar.text()
            obj_N_party_otros.num_beneficio = self.obj_form.lne_nro_beneficio_actualizar.text()


            if self.obj_form.ckbx_facturas_actualizar.isChecked():
                obj_N_party_otros.presento_factura = True

            if self.obj_form.ckbx_veraz_actualizar.isChecked():
                obj_N_party_otros.figura_veraz = True

            if self.obj_form.ckbx_jub_pens_actualizar.isChecked():
                obj_N_party_otros.es_jubilado_pensionado = True

            #if self.obj_form.ckbx_monotributista_actualizar.isChecked():
             #   obj_N_party_otros.monotributista = True

            #if self.obj_form.ckbx_cliente_bloqueado_actualizar.isChecked():
             #   obj_N_party_otros.cliente_bloqueado = True
        

            #boton guardar
            obj_party_otros= N_party_otros(cuit)
            obj_party_otros.actualizar_party_otros(obj_N_party_otros,self.id_party)

            #grilla actualizar           
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_N_garante = N_party_garante(1)
            obj_N_garante.actualizar_lista_garante(self.list_garante, self.nro_cliente)

            msgBox = QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setText("Cliente actualizado.")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Advertencia")
            msgBox.setText("Revisar campos obligatorios: Nombre, Apellido y Dni.")
            msgBox.exec_()



#   app = QApplication(sys.argv)
#    dialogo= clientes_actualizar()
#    dialogo.show()
#    app.exec_()