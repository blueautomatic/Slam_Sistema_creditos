import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from N_usuario import N_usuario
from form_usuario import Ui_form_usuario


class usuario(QDialog):
    obj_form= Ui_form_usuario()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_usuario()
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar.clicked.connect(self.guardar)


    def guardar(self):
        obj_usu = N_usuario()
        obj_usu.nombre =self.obj_form.lne_nombre.text() 
        obj_usu.tipo_usuario = self.obj_form.cbx_tipo_usu.currentText()
        obj_usu.password = self.obj_form.lne_pass.text()
        obj_usu.password2 = self.obj_form.lne_pass2.text()
        obj_usu.guardar(obj_usu)
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se creo correctamente el usuario: ' + self.obj_form.lne_nombre.text())
        msgBox.exec_()
        return False  


#app = QApplication(sys.argv)
#dialogo= usuario()
#dialogo.show()
#app.exec_()