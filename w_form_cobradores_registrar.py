import sys, re
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from form_cobradores_registrar import Ui_form_registrar_cobradores
from N_cobradores import  N_datos_cobrador

class cobradores(QDialog):
    obj_form= Ui_form_registrar_cobradores()
    id_party=""
    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_registrar_cobradores()
        self.obj_form.setupUi(self)
        self.obj_form.btn_agregar.clicked.connect(self.agregar)
        self.obj_form.btn_limpiar.clicked.connect(self.limpiar)

    def limpiar(self):
    	self.obj_form.cbx_cobra_predeterminado.setChecked(False)
    	self.obj_form.cbx_cobra_activo.setChecked(False)

    def agregar(self):

    	obj_N_cobrador= N_datos_cobrador(1)
    	obj_N_cobrador.nombre = self.obj_form.lne_nombre.text() 
        obj_N_cobrador.apellido = self.obj_form.lne_apellido.text()
        obj_N_cobrador.domicilio = self.obj_form.lne_domicilio.text()
        obj_N_cobrador.documento = self.obj_form.lne_documento.text()
        obj_N_cobrador.telefono = self.obj_form.lne_telefono.text()
        obj_N_cobrador.aplicar_importe_peso = self.obj_form.lne_importe_peso.text()
        obj_N_cobrador.aplicar_importe_porcentaje = self.obj_form.lne_importeporcentaje.text()
      
        if self.obj_form.cbx_cobra_predeterminado.isChecked():
            obj_N_cobrador.cbdor_predeterminado = True
        else:
            obj_N_cobrador.cbdor_predeterminado = False



        if self.obj_form.cbx_cobra_activo.isChecked():
            obj_N_cobrador.cbdor_activo = True
        else:
            obj_N_cobrador.cbdor_activo = False

        obj_datos_cobrador = N_datos_cobrador(1)
        obj_datos_cobrador.guardar(obj_N_cobrador)

        if obj_datos_cobrador :
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msg = 'Datos cargados correctamente.' 
            msgBox.setText(msg)
            msgBox.exec_()
        else: 
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msg = 'Error al cargar los datos, intentelo nuevamente.' 
            msgBox.setText(msg)
            msgBox.exec_()
        


#app = QApplication(sys.argv)
#dialogo= Dialogo()
#dialogo.show()
#app.exec_()