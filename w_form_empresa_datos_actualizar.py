import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from form_empresa_datos_actualizar import Ui_form_empresa_datos_actualizar
from N_empresa import  N_datos_empresa

class Empresa_actualizar(QDialog):
    obj_form= Ui_form_empresa_datos_actualizar()
    id_empresa=""
    email=""
    id_party=""
    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_empresa_datos_actualizar()
        self.obj_form.setupUi(self)
        #self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_actualizarr.clicked.connect(self.actualizar)
        obj_N_datos_empresa=N_datos_empresa(1)
        obj_datos_empresa = obj_N_datos_empresa.get_empresa_actualizar("credired")
        if obj_datos_empresa != None:
                
            self.obj_form.lne_nombre.setText(obj_datos_empresa.nombre)
            self.obj_form.lne_ciudad.setText(obj_datos_empresa.ciudad)
            self.obj_form.lne_direccion.setText(obj_datos_empresa.direccion)
            self.obj_form.lne_telefono.setText(obj_datos_empresa.telefono)
            self.obj_form.lne_email.setText(obj_datos_empresa.email)
            self.obj_form.lne_website.setText(obj_datos_empresa.website)
        
            index_tipo_iva=self.obj_form.cbx_tipo_iva.findText(str(obj_datos_empresa.tipo_iva))
            self.obj_form.cbx_tipo_iva.setCurrentIndex(index_tipo_iva)


            self.obj_form.lne_ingresos_brutos.setText(str(obj_datos_empresa.ingresos_brutos))
            self.obj_form.lne_cuit.setText(obj_datos_empresa.cuit)
            self.obj_form.lne_nombre_fantasia.setText(obj_datos_empresa.nombre_fantasia)



    def actualizar(self):
        obj_N_datos_empresa = N_datos_empresa(1)
        obj_N_datos_empresa.nombre = self.obj_form.lne_nombre.text()
        obj_N_datos_empresa.ciudad = self.obj_form.lne_ciudad.text()
        obj_N_datos_empresa.direccion = self.obj_form.lne_direccion.text()
        obj_N_datos_empresa.telefono = self.obj_form.lne_telefono.text()
        obj_N_datos_empresa.email = self.obj_form.lne_email.text()
        obj_N_datos_empresa.website = self.obj_form.lne_website.text()
        obj_N_datos_empresa.tipo_iva=self.obj_form.cbx_tipo_iva.currentText()
        obj_N_datos_empresa.ingresos_brutos = self.obj_form.lne_ingresos_brutos.text()
        obj_N_datos_empresa.cuit = self.obj_form.lne_cuit.text()
        obj_N_datos_empresa.nombre_fantasia = self.obj_form.lne_nombre_fantasia.text()

        #boton guardar
        obj_datos_empresa= N_datos_empresa(1)
        obj_datos_empresa.actualizar(obj_N_datos_empresa)

        if obj_datos_empresa:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msg = 'Datos de empresa cargados correctamente.' 
            msgBox.setText(msg)
            msgBox.exec_()
        else: 
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msg = 'Error al cargar los datos, intentelo nuevamente o pongase en contacto con el soporte tecnico. Gracias.' 
            msgBox.setText(msg)
            msgBox.exec_()

       


#app = QApplication(sys.argv)
#dialogo= Empresa_actualizar()
#dialogo.show()
#app.exec_()
