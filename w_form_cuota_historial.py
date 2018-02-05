import sys, datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtRemoveInputHook
from E_party_party import E_party_party
from form_cuota_historial import Ui_form_cuota_historial
from E_historial_cuota import E_historial_cuota

class Cuota_historial(QDialog):
    obj_form = Ui_form_cuota_historial()


    def __init__(self,id_cuota):
        QDialog.__init__(self)
        obj_form= Ui_form_cuota_historial()
        self.obj_form.setupUi(self)
        self.cargar_grilla(id_cuota)


    def cargar_grilla(self,id_cuota):

        obj_E_historial_cuota = E_historial_cuota()
        lista_historial_cuota = obj_E_historial_cuota.get_historial_cuota(id_cuota)

        for item in lista_historial_cuota:
                estado = item.estado_cuota
                nro_cta = item.nro_cuota
                venc = item.primer_vencimiento
                import_cta = item.importe_cuota
                import_cobrado = item.importe_cobrado
                fec_cobro = item.fecha_cobro
                descripcion = item.descripcion
                nro_credito = item.nro_credito
                id = item.id

                rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
                self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(estado)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(nro_cta)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(venc)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(import_cta)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(import_cobrado)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(fec_cobro)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(descripcion)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(nro_credito)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(id)))




