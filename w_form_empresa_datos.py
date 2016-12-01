import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from form_empresa_datos import Ui_Form_empresa_datos
from N_empresa import  N_datos_empresa

class empresanuevo(QDialog):
    obj_form= Ui_Form_empresa_datos()
    id_empresa=""
    email=""
    id_party=""
    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_Form_empresa_datos()
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar.clicked.connect(self.guardar)
        #self.obj_form.boton_actualizar.clicked.connect(self.actualizar)

    def guardar(self):
        empresa= self.obj_form.lne_nombre.text()
        if empresa != "": 
            obj_empresa = N_datos_empresa(1)
            existe_empresa =  obj_empresa.get_empresa_actualizar("credired")
            if existe_empresa == None: 
                obj_N_datos_empresa = N_datos_empresa(1) 
                obj_N_datos_empresa.nombre = self.obj_form.lne_nombre.text() 
                obj_N_datos_empresa.ciudad = self.obj_form.lne_ciudad.text()
                obj_N_datos_empresa.direccion = self.obj_form.lne_direccion.text()
                obj_N_datos_empresa.telefono = self.obj_form.lne_telefono.text()
                obj_N_datos_empresa.email = self.obj_form.lne_email.text()
                obj_N_datos_empresa.website = self.obj_form.lne_website.text()
                obj_N_datos_empresa.tipo_iva = self.obj_form.cbx_tipo_iva.currentText()
                obj_N_datos_empresa.ingresos_brutos = self.obj_form.lne_ingresos_brutos.text()
                obj_N_datos_empresa.cuit = self.obj_form.lne_cuit.text()
                obj_N_datos_empresa.nombre_fantasia = self.obj_form.lne_nombre_fantasia.text()

                #boton guardar
                obj_datos_empresa = N_datos_empresa(1)
                result=obj_datos_empresa.guardar(obj_N_datos_empresa)
                if result :
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
            else: 
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msg = 'Error al cargar los datos, ya existe una empresa (ir a actualizar). Gracias.' 
                msgBox.setText(msg)
                msgBox.exec_()
        else: 
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msg = 'Error al cargar los datos, campo empresa vacio. Gracias.' 
                msgBox.setText(msg)
                msgBox.exec_()

#app = QApplication(sys.argv)
#dialogo= empresanuevo()
#dialogo.show()
#app.exec_()
