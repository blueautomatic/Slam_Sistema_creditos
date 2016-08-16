import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_clientes_nuevo import Ui_Form_clientes_nuevo
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente, N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook


class Dialogo(QDialog):
    obj_form= Ui_Form_clientes_nuevo()
    id_usu=1
    id_party =""
    list_garante = list()
    nro_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_Form_clientes_nuevo()
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar.clicked.connect(self.guardar)
        self.obj_form.boton_agregar.clicked.connect(self.agregar)
        self.obj_form.boton_buscar_garante.clicked.connect(self.buscar_garante)


    def buscar_garante(self):
        number= self.obj_form.lne_garante_nro_doc.text()
        try:
            numero_documento_garante= int(number)
        except exception:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el número de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False
        
        obj_N_datos_garante= N_datos_personales_cliente("a")
        if numero_documento_garante != "":
            obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar(str(numero_documento_garante))
            self.obj_form.lne_garante_apellido.setText(obj_datos_garante.apellido)
            self.obj_form.lne_garante_nombre.setText(obj_datos_garante.nombre)
            self.obj_form.lne_garante_estado.setText(obj_datos_garante.estado)
            
            obj_N_party_cliente = N_party_cliente(obj_datos_garante.id_party)
            nro_cliente_garante = obj_N_party_cliente.get_nro_cliente(obj_datos_garante.id_party)
            self.obj_form.lne_garante_nro_cliente.setText(str(nro_cliente_garante))

        else :
            obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar_nrocliente(str(nro_cliente))
            self.obj_form.lne_garante_apellido.setText(obj_datos_garante.apellido)
            self.obj_form.lne_garante_nombre.setText(obj_datos_garante.nombre)
            self.obj_form.lne_garante_estado.setText(obj_datos_garante.estado)
            self.obj_form.lne_garante_nro_doc.setText(obj_datos_garante.nro_doc)

            

    def guardar(self):

        numero_documento_cliente= self.obj_form.lne_nro_doc.text()
        try:
            numero_documento= int(numero_documento_cliente)
        except exception:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el número de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False

        apellido = self.obj_form.lne_apellido.text()
        obj_N_datos_personales_cliente = N_datos_personales_cliente(apellido) 

        obj_N_datos_personales_cliente.nombre = self.obj_form.lne_nombre.text()  
        obj_N_datos_personales_cliente.apellido = self.obj_form.lne_apellido.text()
        obj_N_datos_personales_cliente.fec_nac = self.obj_form.dte_nacimiento.text()
        obj_N_datos_personales_cliente.tipo_doc = self.obj_form.cbx_tipo_doc.currentText()
        obj_N_datos_personales_cliente.nro_doc = numero_documento
        obj_N_datos_personales_cliente.estado_civil = self.obj_form.cbx_estado_civil.currentText()
        obj_N_datos_personales_cliente.limite_credito = self.obj_form.lne_limite_credito.text()
        obj_N_datos_personales_cliente.estado = self.obj_form.cbx_estado.currentText()
        #boton guardar
        obj_datos_personales_cliente = N_datos_personales_cliente(apellido)

        self.id_party=obj_datos_personales_cliente.guardar(obj_N_datos_personales_cliente, self.id_usu)



        if self.id_party != "False" :
            obj_party_cliente = N_party_cliente(self.id_party)


            obj_party_cliente.guardar_N_party_cliente(self.obj_form.txte_observaciones.toPlainText(), self.id_party)
            self.nro_cliente = obj_party_cliente.get_nro_cliente(self.id_party)
            self.obj_form.lne_nro_cliente.setText(str(self.nro_cliente))

            obj_party_contacto3= N_party_contacto(1)

            obj_party_contacto3.type_contacto= "Telefono"
            obj_party_contacto3.value =self.obj_form.lne_telefono.text()

            obj_party_contacto_email=N_party_contacto(1)
            obj_party_contacto_email.type_contacto="Email"
            obj_party_contacto_email.value= self.obj_form.lne_email.text()

            
            obj_N_party_contacto=N_party_contacto(1)
            obj_N_party_contacto.guardar(obj_party_contacto3, self.id_party)
            obj_N_party_contacto.guardar(obj_party_contacto_email, self.id_party)
              
            ciudad = self.obj_form.lne_barrio.text()
            obj_N_party_address = N_party_address(ciudad)
            obj_N_party_address.domicilio = self.obj_form.lne_domicilio.text()
            obj_N_party_address.barrio = self.obj_form.lne_barrio.text()
            obj_N_party_address.ciudad = self.obj_form.cbx_ciudad.currentText()
                #boton guardar

            obj_party_address= N_party_address(ciudad)
            obj_party_address.guardar(obj_N_party_address, self.id_party)



            organismo = self.obj_form.lne_organismo.text()
            obj_N_datos_laborales = N_datos_laborales(organismo)
            obj_N_datos_laborales.sueldo = self.obj_form.lne_sueldo.text()
            obj_N_datos_laborales.anti_laboral = self.obj_form.lne_antiguedad.text()
            obj_N_datos_laborales.tel_laboral = self.obj_form.lne_telefono_laboral.text()
            obj_N_datos_laborales.dom_laboral = self.obj_form.lne_domicilio_laboral.text()
            obj_N_datos_laborales.organismo = self.obj_form.lne_organismo.text()
            obj_N_datos_laborales.ocupacion = self.obj_form.lne_ocupacion.text()
            obj_N_datos_laborales.categoria = self.obj_form.lne_categoria.text()
            if self.obj_form.ckbx_recibo_sueldo.isChecked():
                obj_N_datos_laborales.posee_recibo_sueldo = True
            else:
                obj_N_datos_laborales.posee_recibo_sueldo = False
            #boton guardar

            obj_datos_laborales= N_datos_laborales(organismo)
            obj_datos_laborales.guardar(obj_N_datos_laborales,self.id_party)


            cuit = self.obj_form.lne_cuit.text()
            obj_N_party_otros = N_party_otros(cuit)
            obj_N_party_otros.tipo_iva = self.obj_form.cbx_tipo_iva.currentText()
            obj_N_party_otros.cuit = self.obj_form.lne_cuit.text()
            obj_N_party_otros.cbu = self.obj_form.lne_cbu.text()
            obj_N_party_otros.num_beneficio = self.obj_form.lne_nro_beneficio.text()
            #boton guardar
            obj_party_otros= N_party_otros(cuit)
            obj_party_garante2 = N_party_garante("A")
            obj_party_garante2.guardar(self.list_garante,self.nro_cliente)

        else: 
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("No se pudo grabar: Número de documento duplicado, actualice los datos")
            msgBox.exec_()


    def agregar (self):
        number= self.obj_form.lne_garante_nro_doc.text()
        id_party_party_garante=""
        try:
            nro_doc_garante= int(number)
        except exception:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el número de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False

        obj_Cliente_garante = N_party_garante("a")
        existe_garante=False

        existe_garante = obj_Cliente_garante.es_garante_de_otro_cliente(nro_doc_garante)
        
        obj_party_party_garante = N_datos_personales_cliente(1)
        id_party_party_garante = obj_party_party_garante.get_id_party_party_garante(nro_doc_garante)


        obj_N_creditos = N_creditos(1)
        tiene_prestamo =  obj_N_creditos.get_tiene_prestamos_activo(self.obj_form.lne_garante_nro_doc.text())
        
        if (existe_garante == True ) or (tiene_prestamo == True) :
            msgBox = QMessageBox.question(self, 'Validar Clientes y Garantes ', 'Desea agregarlo igualmente?',QMessageBox.Yes | QMessageBox.No)
            if msgBox == QMessageBox.Yes :
                garante_nro_doc = self.obj_form.lne_garante_nro_doc.text()

                cliente_nro_del_garante = int(self.obj_form.lne_garante_nro_cliente.text())
                garante_apellido = self.obj_form.lne_garante_apellido.text()
                garante_nombre = self.obj_form.lne_garante_nombre.text()
                garante_estado = self.obj_form.lne_garante_estado.text()
                tipo_garante = self.obj_form.cbx_tipo_garante.currentText()
                
                obj_N_party_garante = N_party_garante("A")
                obj_party_garante = N_party_garante("A")
                obj_party_garante.comment = self.obj_form.txte_garante_observaciones.toPlainText()
                obj_party_garante.tipo_garante = self.obj_form.cbx_tipo_garante.currentText()
                obj_party_garante.id_party_garante = id_party_party_garante
                self.list_garante.append(obj_party_garante)


                #AGREGAR REGISTROS EN LA GRILLA
                rowPosition = self.obj_form.tw_garantes_lista.rowCount()
                self.obj_form.tw_garantes_lista.insertRow(rowPosition)
                 #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(garante_estado))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(tipo_garante))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(cliente_nro_del_garante))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(garante_apellido))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(garante_nombre))
                self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(garante_nro_doc))
        else: 
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            garante_nro_doc = self.obj_form.lne_garante_nro_doc.text()
            cliente_nro_del_garante = self.obj_form.lne_garante_nro_cliente.text()
            garante_apellido = self.obj_form.lne_garante_apellido.text()
            garante_nombre = self.obj_form.lne_garante_nombre.text()
            garante_estado = self.obj_form.lne_garante_estado.text()

            
            obj_N_party_garante = N_party_garante("A")
            obj_party_garante = N_party_garante("A")
            obj_party_garante.comment = self.obj_form.txte_garante_observaciones.toPlainText()
            obj_party_garante.tipo_garante = self.obj_form.cbx_tipo_garante.currentText()
            obj_party_garante.id_party_garante = id_party_party_garante
            self.list_garante.append(obj_party_garante)

            #AGREGAR REGISTROS EN LA GRILLA
            rowPosition = self.obj_form.tw_garantes_lista.rowCount()
            self.obj_form.tw_garantes_lista.insertRow(rowPosition)
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(garante_nro_doc))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(garante_nombre))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(garante_apellido))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(cliente_nro_del_garante))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(garante_nro_doc))
            self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(garante_estado))



app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()