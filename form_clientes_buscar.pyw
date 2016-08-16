import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_clientes_buscar import Ui_Form_clientes_buscar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook


class Dialogo(QDialog):
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



    def buscar_cliente(self):

        numero_documento_cliente= self.obj_form.lne_nro_doc_cliente.text()
        try:
            numero_documento= int(numero_documento_cliente)
        except:
            msgBox = QMessageBox()
            msgBox.about(self, 'Error','Ingresar nuevamente el numero de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False


        obj_N_datos_personales_cliente = N_datos_personales_cliente("a")
        obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(self.obj_form.lne_dni_filtro_buscar.text())

            
        self.id_party = obj_party_party.id_party
        self.obj_form.lne_apellido_buscar.setText(obj_party_party.apellido)  
        self.obj_form.lne_nombre_buscar.setText(obj_party_party.nombre)
        self.obj_form.lne_tipo_doc_buscar.setText(obj_party_party.tipo_doc)
        self.obj_form.lne_nro_doc_cliente.setText(obj_party_party.nro_doc)
        self.obj_form.lne_estado.setText(obj_party_party.estado)        
        self.obj_form.lne_fecha_nac.setText(str(obj_party_party.fec_nac))
        self.obj_form.lne_estado_civil.setText(obj_party_party.estado_civil) 
        self.obj_form.lne_limite_credito_buscar.setText(str(obj_party_party.limite_credito))      

        obj_N_party_address= N_party_address(1)
        obj_party_address = obj_N_party_address.get_party_address(self.id_party)
        self.obj_form.lne_domicilio_buscar.setText(obj_party_address.domicilio)
        self.obj_form.lne_ciudad_buscar.setText(obj_party_address.ciudad)
        self.obj_form.lne_barrio_buscar.setText(obj_party_address.barrio)

        obj_N_party_contacto= N_party_contacto(1)
        list_party_contacto= obj_N_party_contacto.get_list_party_contacto(self.id_party)
        for item in list_party_contacto:
            if item.type_contacto == "Telefono":
                self.obj_form.lne_telefono_buscar.setText(item.value)
            if item.type_contacto=="Email":
                self.obj_form.lne_email_buscar.setText(item.value)


        obj_N_party_cliente= N_party_cliente(1)
        obj_party_cliente=obj_N_party_cliente.get_party_cliente(self.id_party)
        self.obj_form.lne_nro_cliente_buscar.setText(str(obj_party_cliente.nro_cliente))
        
        #terminar buscar propiedad para seteart cliente
        #self.obj_form.txte_observaciones_buscar.setText(obj_party_cliente.comment)
        #toPlainText
        obj_N_datos_laborales=N_datos_laborales(1)
        obj_datos_laborales= obj_N_datos_laborales.get_datos_laborales(self.id_party)
        self.obj_form.lne_ocupacion_buscar.setText(obj_datos_laborales.ocupacion)

        self.obj_form.lne_organismo_buscar.setText(obj_datos_laborales.organismo)
        self.obj_form.lne_telefono_laboral_buscar.setText(obj_datos_laborales.tel_laboral)
        self.obj_form.lne_domicilio_laboral_buscar.setText(obj_datos_laborales.dom_laboral)
        self.obj_form.lne_sueldo_buscar.setText(str(obj_datos_laborales.sueldo))
        self.obj_form.lne_antiguedad_buscar.setText(obj_datos_laborales.anti_laboral)
        self.obj_form.lne_categoria_buscar.setText(obj_datos_laborales.categoria)
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        self.obj_form.ckbx_posee_sueldo_buscar.setChecked(obj_datos_laborales.posee_recibo_sueldo)
        





app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()