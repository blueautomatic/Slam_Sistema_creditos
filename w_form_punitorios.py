import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from N_cuotas import N_cuotas
from form_punitorios import Ui_Form_punitorios
from E_reg_procesos import E_reg_procesos

class punitorios(QDialog):
    obj_form = Ui_Form_punitorios()
    singleton=""
    
    def __init__(self,singleton):
        QDialog.__init__(self)
        obj_form= Ui_Form_punitorios()
        self.obj_form.setupUi(self)
        self.obj_form.boton_generar.clicked.connect(self.aceptar)
        self.singleton = singleton
        

    def aceptar(self):
        obj_N_cuotas = N_cuotas(1)
        slam = obj_N_cuotas.generar_punitorios(1)

        if slam:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText( 'Cuotas generadas correctamente')
            msgBox.exec_()

            obj_e_reg_procesos = E_reg_procesos()
            fecha = str (datetime.datetime.now())
            obj_e_reg_procesos.descripcion = "Proceso de punitorios "
            obj_e_reg_procesos.tipo = "Punitorios"
            obj_e_reg_procesos.guardar(obj_e_reg_procesos)
            lista_reg_procesos_punitorios = list() 
            lista_reg_procesos_punitorios = obj_e_reg_procesos.buscar_reg_procesos_punitorios()            
            
            for item in lista_reg_procesos_punitorios:
                rowPosition = self.obj_form.tableWidget.rowCount()
                self.obj_form.tableWidget.insertRow(rowPosition)
                self.obj_form.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(str(item.fecha)))
                self.obj_form.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(str(item.descripcion)))


#app = QApplication(sys.argv)
#punitorio= punitorios()
#punitorio.show()
#app.exec_()
    
    