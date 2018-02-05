import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from N_cliente import N_datos_personales_cliente
from form_cuota_reparar import Ui_Form_reparar_cuota
from PyQt5.QtCore import pyqtRemoveInputHook
from N_creditos import N_creditos
from N_cuotas import N_cuotas
from E_cuotas import E_cuotas
from E_historial_cuota import E_historial_cuota

class cuotas_reparar(QDialog):
    obj_form= Ui_Form_reparar_cuota()
    singleton_idusu=""

    def __init__(self,singleton_idusu):
        QDialog.__init__(self)
        self.obj_form= Ui_Form_reparar_cuota()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar.clicked.connect(self.buscar)
        self.obj_form.boton_actualizar.clicked.connect(self.actualizar)
        self.singleton_idusu= singleton_idusu


    def actualizar(self):
        obj_cuota = E_cuotas(1)
        obj_cuota.nro_credito = self.obj_form.lne_num_credito.text()
        obj_cuota.nro_cta = self.obj_form.lne_num_cuota.text()
        obj_cuota.id = self.obj_form.lne_id_cuota_reparar.text()
        obj_cuota.nro_cuota = self.obj_form.lne_nro_cuota_reparar.text()

        obj_cuota.estado_cuota = self.obj_form.cbx_estado.currentText()
        obj_cuota.importe_primer_venc = self.obj_form.lne_importe_cuota_reparar.text()
        obj_cuota.importe_cuota = self.obj_form.lne_importe_cuota_reparar.text()

        obj_cuota.fecha_cobro =self.obj_form.dte_fecha_cobro.text()

        obj_cuota.importe_cobrado = self.obj_form.lne_cobrado_reparar.text()
        obj_cuota.capital = self.obj_form.lne_capital_reparar.text()
        obj_cuota.interes = self.obj_form.lne_interes_reparar.text()
        obj_cuota.gastos = self.obj_form.lne_gastos_reparar.text()
        obj_cuota.punitorios = self.obj_form.lne_punitorio_reparar.text()
        #obj_cuota.importe_cuota = self.obj_form.lne_importe_cuota_reparar.text()

        obj_cuota.descripcion = self.obj_form.lne_descripcion_reparar.text()
        obj_cuota.descuento = self.obj_form.lne_descuento_reparar.text()

        obj_e_cuota = E_cuotas(1)
        obj_e_cuota.actualizar_reparar(obj_cuota)

        obj_hist = E_historial_cuota()
        obj_hist.nro_credito =  self.obj_form.lne_num_credito.text()
        obj_hist.nro_cuota = self.obj_form.lne_num_cuota.text()
        obj_hist.estado_cuota = self.obj_form.cbx_estado.currentText()
        obj_hist.fecha_cobro = self.obj_form.dte_fecha_cobro.text()
        obj_hist.importe_cobrado = self.obj_form.lne_cobrado_reparar.text()
        obj_hist.descripcion = self.obj_form.lne_descripcion_reparar.text() + ". Se reparo la cuota"
        obj_hist.id_cuota = self.obj_form.lne_id_cuota_reparar.text()
        obj_hist.guardar(obj_hist)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Datos actualizados correctamente')
        msgBox.exec_()


    def buscar(self):
        nro_credito = self.obj_form.lne_num_credito.text()
        nro_cta = self.obj_form.lne_num_cuota.text()
        obj_cta = N_cuotas(1)
        obj_result = obj_cta.buscar_cta_por_nro_cred_y_nro_cta(nro_credito, nro_cta)
        self.obj_form.lne_id_cuota_reparar.setText(str(obj_result.id))
        self.obj_form.lne_nro_cuota_reparar.setText(str(obj_result.nro_cuota))
        self.obj_form.lne_venc_reparar.setText(str(obj_result.primer_vencimiento))
        #self.obj_form. .setText(str(obj_result.importe_primer_venc))
        index_estado=self.obj_form.cbx_estado.findText(str(obj_result.estado_cuota))
        self.obj_form.cbx_estado.setCurrentIndex(index_estado)

        if str(obj_result.fecha_cobro) != "None":

            self.obj_form.dte_fecha_cobro.setDate(obj_result.fecha_cobro)

        self.obj_form.lne_cobrado_reparar.setText(str(obj_result.importe_cobrado))
        self.obj_form.lne_capital_reparar.setText(str(obj_result.capital))
        self.obj_form.lne_interes_reparar.setText(str(obj_result.interes))
        self.obj_form.lne_gastos_reparar.setText(str(obj_result.gastos))
        self.obj_form.lne_punitorio_reparar.setText(str(round(obj_result.punitorios,2)))
        self.obj_form.lne_importe_cuota_reparar.setText(str(obj_result.importe_cuota))
        self.obj_form.lne_descripcion_reparar.setText(str(obj_result.descripcion))
        self.obj_form.lne_descuento_reparar.setText(str(obj_result.descuento))
#app = QApplication(sys.argv)
#dialogo= cuotas_reparar()
#dialogo.show()
#app.exec_()
