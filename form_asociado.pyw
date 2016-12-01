import sys, datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic

from PyQt5.QtCore import pyqtRemoveInputHook

class asociado(QDialog):

    obj_form= Ui_form_asociado()
    id_usu=1
    id_party =""
    list_garante = list()
    nro_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_asociado()
        self.obj_form.setupUi(self)
        self.obj_form.boton.clicked.connect(self.asoc)

app = QApplication(sys.argv)
dialogo= asociado()
dialogo.show()
app.exec_()