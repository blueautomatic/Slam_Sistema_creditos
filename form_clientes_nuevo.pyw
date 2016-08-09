import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from form_clientes_nuevo import Ui_Form_clientes_nuevo
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente
from PyQt5.QtCore import pyqtRemoveInputHook


class Dialogo(QDialog):
    obj_form= Ui_Form_clientes_nuevo()
    id_usu=1
    id_party =""
    list_N_garantes = list()

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
            obj_datos_garante = obj_N_datos_garante.get_garante_habilitado(str(numero_documento_garante))
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
        #boton guardar
        obj_datos_personales_cliente = N_datos_personales_cliente(apellido)

        self.id_party=obj_datos_personales_cliente.guardar(obj_N_datos_personales_cliente, self.id_usu)

        if self.id_party != "False" :                
            self.obj_form.lne_nro_cliente.setText(str(self.id_party))
              
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
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_datos_laborales= N_datos_laborales(organismo)
            obj_datos_laborales.guardar(obj_N_datos_laborales,self.id_party)


            cuit = self.obj_form.lne_cuit.text()
            obj_N_party_otros = N_party_otros(cuit)
            obj_N_party_otros.tipo_iva = self.obj_form.lne_iva.text()
            obj_N_party_otros.cuit = self.obj_form.lne_cuit.text()
            obj_N_party_otros.cbu = self.obj_form.lne_cbu.text()
            obj_N_party_otros.num_beneficio = self.obj_form.lne_nro_beneficio.text()
            #boton guardar
            obj_party_otros= N_party_otros(cuit)
            obj_party_garante.guardar(obj_N_party_garante, self.id_party)

        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("No se pudo grabar: Número de documento duplicado, actualice los datos")
            msgBox.exec_()


    def agregar (self):
        number= self.obj_form.lne_garante_nro_doc.text()
        try:
            numero_documento_garante= int(number)
        except exception:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el número de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False

        obj_N_Cliente_garante = N_datos_personales_cliente("a")
        existe_garante = obj_N_Cliente_garante.get_existe_nro_doc_garante(numero_documento_garante)
        existe_cliente = obj_N_Cliente_garante.get_existe_nro_doc_cliente(numero_documento_garante)
        
        if (existe_garante == True ) or (existe_cliente == True) :
            msgBox = QMessageBox.question(self, 'El Garante existe en el sistema. Validar Clientes y Garantes ', 'Desea agregarlo igualmente?',QMessageBox.Yes | QMessageBox.No)
            if msgBox == QMessageBox.Yes :
                garante_nro_doc = self.form.lne_garante_nro_doc.text()
                garante_nro_cliente = self.form.lne_garante_nro_cliente.text()
                garante_apellido = self.form.lne_garante_apellido.text()
                garante_nombre = self.form.lne_garante_nombre.text()
                garante_estado = self.form.lne_garante_estado.text()
                
                obj_N_party_garante = N_party_garante("A")
                obj_party_garante = N_party_garante("A")
                obj_party_garante.nro_doc = self.form.lne_garante_nro_doc.text()
                obj_party_garante.comment = self.obj_form.txte_garante_observaciones.text()
                obj_N_party_garante.guardar_garante(obj_party_garante)
        

        #AGREGAR REGISTROS EN LA GRILLA
        rowPosition = self.obj_form.tw_registrotitulos.rowCount()
        self.obj_form.tw_registrotitulos.insertRow(rowPosition)
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 0, QTableWidgetItem(titulo_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 1, QTableWidgetItem(universidad_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 2, QTableWidgetItem(str(dte_fecha_titulo_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 3, QTableWidgetItem(str(dte_fecha_aut_min_educ_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 4, QTableWidgetItem(str(dte_fecha_aut_min_int_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 5, QTableWidgetItem(str(especialidad)))


app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()