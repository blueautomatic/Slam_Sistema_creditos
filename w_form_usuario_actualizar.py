import sys
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem, QMessageBox
from PyQt5 import uic
from N_usuario import N_usuario
from form_usuario_actualizar import Ui_form_usu_actualizar
from PyQt5.QtCore import pyqtRemoveInputHook

class usuario_actualizar(QDialog):
    obj_form= Ui_form_usu_actualizar()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form.setupUi(self)
        obj_n_usuario = N_usuario()

        lista_usuario = obj_n_usuario.buscar_todos_los_usuarios()
        for item in lista_usuario:
            rowPosition = self.obj_form.tw_usuario.rowCount()
            self.obj_form.tw_usuario.insertRow(rowPosition)
            self.obj_form.tw_usuario.setItem(rowPosition , 0, QTableWidgetItem(str(item.nombre)))
            self.obj_form.tw_usuario.setItem(rowPosition , 1, QTableWidgetItem(str(item.tipo_usuario)))
            self.obj_form.tw_usuario.setItem(rowPosition, 2 , QTableWidgetItem(str(item.id_usuario)))
            self.obj_form.tw_usuario.setItem(rowPosition, 3 , QTableWidgetItem(str(item.descarga)))

        self.obj_form.tw_usuario.cellClicked.connect(self.select_item)
        self.obj_form.boton_actualizar.clicked.connect(self.actualizar)



    def select_item(self,clickedIndex):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        twi0 = self.obj_form.tw_usuario.item(clickedIndex,0)
        twi1 = self.obj_form.tw_usuario.item(clickedIndex,1)
        twi2 = self.obj_form.tw_usuario.item(clickedIndex,2)
        twi3 = self.obj_form.tw_usuario.item(clickedIndex,3)

        self.obj_form.lne_id.setText(twi2.text())
        self.obj_form.lne_nombre.setText(twi0.text())
        self.obj_form.lne_descarga.setText(twi3.text())
        index_tipo = self.obj_form.cbx_tipo_usu.findText(twi1.text())
        self.obj_form.cbx_tipo_usu.setCurrentIndex(index_tipo)

    def actualizar(self):
        obj_n_usuario = N_usuario()
        obj_n_usuario.id_usuario = self.obj_form.lne_id.text()
        obj_n_usuario.nombre = self.obj_form.lne_nombre.text()
        obj_n_usuario.tipo_usuario = self.obj_form.cbx_tipo_usu.currentText()
        obj_n_usuario.password = self.obj_form.lne_pass.text()
        obj_n_usuario.password2 = self.obj_form.lne_pass2.text()
        obj_n_usuario.descarga = self.obj_form.lne_descarga.text()

        result = obj_n_usuario.actualizar(obj_n_usuario)
        if result :
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Correcto")
            msgBox.setText( 'Se actualizo correctamente.')
            msgBox.exec_()


#app = QApplication(sys.argv)
#dialogo= usuario_actualizar()
#dialogo.show()
#app.exec_()
