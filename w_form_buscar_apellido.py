import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from N_cliente import N_datos_personales_cliente
from form_buscar_apellido import Ui_Form_buscar_apellido
from PyQt5.QtCore import pyqtRemoveInputHook
#pyqtRemoveInputHook()
#import pdb; pdb.set_trace()

class buscar_apellido(QDialog):
    obj_form= Ui_Form_buscar_apellido()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form= Ui_Form_buscar_apellido()
        self.obj_form.setupUi(self)
        self.obj_form.boton_apellido_buscar.clicked.connect(self.buscar)

    def buscar(self):
        self.limpiar()
        apellido = self.obj_form.lne_apellido.text()
        obj_N_cliente = N_datos_personales_cliente()
        list_clientes= list()  
        list_clientes = obj_N_cliente.buscar(apellido.upper())

        for item in list_clientes:
            rowPosition = self.obj_form.tw_resultado.rowCount()
            self.obj_form.tw_resultado.insertRow(rowPosition)
            self.obj_form.tw_resultado.setItem(rowPosition, 0, QTableWidgetItem(str(item.apellido)))
            self.obj_form.tw_resultado.setItem(rowPosition, 1, QTableWidgetItem(str(item.nombre)))
            self.obj_form.tw_resultado.setItem(rowPosition, 2 , QTableWidgetItem(str(item.num_doc)))

        
    def limpiar(self):

        while (self.obj_form.tw_resultado.rowCount() > 0):
            self.obj_form.tw_resultado.removeRow(0)



#app = QApplication(sys.argv)
#dialogo= buscar_apellido()
#dialogo.show()
#app.exec_()  
