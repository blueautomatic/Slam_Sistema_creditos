import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog

from w_form_clientes_actualizar import clientes_actualizar
from w_form_credito_calcular import Calcular_credito
from w_form_clientes_nuevo import Cliente_nuevo
from w_form_creditos_agregar_nuevos import credito_nuevo
from w_form_creditos_cuotas_buscar import creditos_cuotas_buscar
from w_form_cuotas_pagar import Cuotas_pagar
from w_form_cuotas_vencidas_30dias import Cuotas_vencidas_30dias
from w_form_garante_historial import Garante_historial
from w_form_empresa_datos import empresanuevo
from w_form_empresa_datos_actualizar import Empresa_actualizar
from w_form_egresos_diarios import egresos_diarios
from w_form_ingresos_diarios import ingresos_diarios
from w_form_usuario_actualizar import usuario_actualizar
from w_form_usuario import usuario
from w_form_clientes_buscar import buscar_clientes
from w_form_punitorios import punitorios
from w_form_buscar_apellido import buscar_apellido
from w_form_cuota_reparar import cuotas_reparar


class Mainwindow(QMainWindow):
    singleton =""
    singleton_idusu=""
    def __init__(self,singleton,singleton_idusu):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.obj_form_main = Ui_MainWindow()
        self.obj_form_main.setupUi(self)
        self.obj_form_main.actionEmpresa.triggered.connect(self.empresanuevo12)
        self.obj_form_main.actionEmpresaActualizar.triggered.connect(self.empresa_actualizar12)
        self.obj_form_main.action_alta_cliente_nuevo.triggered.connect(self.Agregar_cliente)
        self.obj_form_main.action_cliente_actualizar.triggered.connect(self.Actualizar_cliente)
        self.obj_form_main.action_buscar_cliente.triggered.connect(self.buscar_clientes)
        self.obj_form_main.action_credito_agregar_nuevo.triggered.connect(self.credito_nuevo)
        self.obj_form_main.actionCobradores.triggered.connect(self.cobradores)
        self.obj_form_main.actionREPORTE_DE_CUOTAS.triggered.connect(self.REPORTE_DE_CUOTAS)
        self.obj_form_main.actionCOBRAR_CUOTAS.triggered.connect(self.Cuotas)
        self.obj_form_main.actionEgresos.triggered.connect(self.egresos)
        self.obj_form_main.actionIngresos.triggered.connect(self.ingresos_diarios)
        self.obj_form_main.actionCALCULADOR.triggered.connect(self.CALCULADOR)
        self.obj_form_main.actionHISTORIAL_GARANTE.triggered.connect(self.garante_historial12)
        self.obj_form_main.actionUsu.triggered.connect(self.usuario)
        self.obj_form_main.actionUsu_Act.triggered.connect(self.usuario_actualizar)
        self.obj_form_main.actionGenerador_punitorios.triggered.connect(self.Punitorios)
        #self.obj_form_main.actionGenerador_punitorios.triggered.connect(self.Buscar_apellido)

        self.obj_form_main.actionBuscar_apellido.triggered.connect(self.Buscar_apellido)
        self.obj_form_main.actionReparar_Cuotas.triggered.connect(self.reparar_cta)
        self.obj_form_main.actionHist_cred_y_ctas.triggered.connect(self.credito_buscar_estado)
        self.singleton =singleton
        self.singleton_idusu =singleton_idusu


    def credito_buscar_estado(self):
        self.form_profesionales = creditos_cuotas_buscar()
        self.form_profesionales.show()


    def reparar_cta(self):
        self.form_profesionales = cuotas_reparar(singleton_idusu)
        self.form_profesionales.show()

    def Buscar_apellido(self):
        self.form_profesionales = buscar_apellido()
        self.form_profesionales.show()

    def usuario_actualizar(self):
        self.form_profesionales = usuario_actualizar()
        self.form_profesionales.show()

    def usuario(self):
        self.form_profesionales = usuario()
        self.form_profesionales.show()

    def garante_historial12(self):
        self.form_profesionales = Garante_historial()
        self.form_profesionales.show()

    def CALCULADOR(self):
        self.form_profesionales=Calcular_credito()
        self.form_profesionales.show()

    def ingresos_diarios(self):
        self.form_profesionales=ingresos_diarios()
        self.form_profesionales.show()

    def egresos(self):
        self.form_profesionales=egresos_diarios()
        self.form_profesionales.show()

    def Agregar_cliente(self):

        self.form_profesionales=Cliente_nuevo()
        self.form_profesionales.show()
    def Actualizar_cliente(self):
        self.form_clientes_actualizar=clientes_actualizar()
        self.form_clientes_actualizar.show()
    def buscar_clientes(self):
        self.form_clientes_buscar=buscar_clientes()
        self.form_clientes_buscar.show()
    def credito_nuevo(self):
        self.form_creditos_agregar_nuevos=credito_nuevo()
        self.form_creditos_agregar_nuevos.show()
    def empresanuevo12(self):
        self.form_empresa_datos=empresanuevo()
        self.form_empresa_datos.show()
    def empresa_actualizar12(self):
        self.form_empresa_datos_actualizar=Empresa_actualizar()
        self.form_empresa_datos_actualizar.show()
    def cobradores(self):
        self.form_cobradores_registrar=cobradores()
        self.form_cobradores_registrar.show()
    def REPORTE_DE_CUOTAS(self):
        self.form_cobradores_registrar=Cuotas_vencidas_30dias()
        self.form_cobradores_registrar.show()

    def Cuotas(self):
        self.form_cobradores_registrar=Cuotas_pagar(self.singleton)
        self.form_cobradores_registrar.show()

    def Punitorios(self):
        self.form_cobradores_registrar=punitorios(self.singleton)
        self.form_cobradores_registrar.show()


#app = QApplication(sys.argv)
#_ventana = Mainwindow()
#_ventana.show()
#app.exec_()


