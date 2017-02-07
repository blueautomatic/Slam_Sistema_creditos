import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_garante_historial import Ui_form_garante_historial
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente, N_party_contacto, N_garante_credito
from N_creditos import N_creditos,N_historial_garante
from PyQt5.QtCore import pyqtRemoveInputHook

class Garante_historial(QDialog):
    obj_form = Ui_form_garante_historial()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_garante_historial()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar.clicked.connect(self.buscar_garante)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)

    def buscar_garante(self):
        self.limpiar()
        number= self.obj_form.lne_garante_nro_doc_nuevo.text()
        obj_N_datos_garante= N_datos_personales_cliente()
        if number != "":
            try:
                numero_documento_garante= int(number)
            except:
                msgBox = QMessageBox()
                msgBox.about(self, 'Error , Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()
                return False
            obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar(str(numero_documento_garante))
            if obj_datos_garante != None:
                self.obj_form.lne_garante_apellido.setText(obj_datos_garante.apellido)
                self.obj_form.lne_garante_nombre.setText(obj_datos_garante.nombre)
                self.obj_form.lne_garante_estado.setText(obj_datos_garante.estado)
                self.obj_form.lne_garante_nro_doc.setText(obj_datos_garante.num_doc)
                obj_N_party_cliente = N_party_cliente(obj_datos_garante.id_party)
                nro_cliente_garante = obj_N_party_cliente.get_nro_cliente(obj_datos_garante.id_party)
                self.obj_form.lne_garante_nro_cliente_2.setText(str(nro_cliente_garante))
                
                lista_garante_historial = list()
                obj_N_historial_garante = N_historial_garante(1)

                lista_garante_historial = obj_N_historial_garante.buscar_historial_garante(obj_datos_garante.id_party)
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                for item in lista_garante_historial:
                    rowPosition = self.obj_form.tw_garantes_lista.rowCount()
                    self.obj_form.tw_garantes_lista.insertRow(rowPosition)
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(item.tipo_garante))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(item.estado_credito))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_credito)))        
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_prestamo)))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(str(item.nro_cliente)))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(item.num_doc))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 6, QTableWidgetItem(item.apellido))
                    self.obj_form.tw_garantes_lista.setItem(rowPosition , 7, QTableWidgetItem(item.nombre))
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msg = 'Advertencia , Numero de documento inexistente'
                msgBox.setText(msg)
                msgBox.exec_()
                return False

        else :
            
            if self.obj_form.lne_garante_nro_cliente.text() != "":
                try:
                    garante_nro_cliente = int(self.obj_form.lne_garante_nro_cliente.text())
                    obj_N_party_cliente = N_party_cliente(1)
                    obj_party_cliente = obj_N_party_cliente.buscar_E_party_cliente_por_nro_cliente(garante_nro_cliente)
                    obj_N_datos_personales_cliente = N_datos_personales_cliente()
                    obj_party= obj_N_datos_personales_cliente.buscar_party_party_por_id(obj_party_cliente.id_party)
                    obj_datos_garante = obj_N_datos_garante.get_garante_habilitado_buscar(str(obj_party.nro_doc))
                    if obj_datos_garante != None:
                        self.obj_form.lne_garante_apellido.setText(obj_datos_garante.apellido)
                        self.obj_form.lne_garante_nombre.setText(obj_datos_garante.nombre)
                        self.obj_form.lne_garante_estado.setText(obj_datos_garante.estado)
                        self.obj_form.lne_garante_nro_doc.setText(obj_datos_garante.num_doc)
                        obj_N_party_cliente = N_party_cliente(obj_datos_garante.id_party)
                        nro_cliente_garante = obj_N_party_cliente.get_nro_cliente(obj_datos_garante.id_party)
                        self.obj_form.lne_garante_nro_cliente_2.setText(str(nro_cliente_garante))
                        
                        lista_garante_historial = list()
                        obj_N_historial_garante = N_historial_garante(1)

                        lista_garante_historial = obj_N_historial_garante.buscar_historial_garante(obj_datos_garante.id_party)
                        for item in lista_garante_historial:
                            rowPosition = self.obj_form.tw_garantes_lista.rowCount()
                            self.obj_form.tw_garantes_lista.insertRow(rowPosition)
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 0, QTableWidgetItem(item.tipo_garante))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 1, QTableWidgetItem(item.estado_credito))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_credito)))        
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_prestamo)))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 4, QTableWidgetItem(str(item.nro_cliente)))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 5, QTableWidgetItem(item.num_doc))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 6, QTableWidgetItem(item.apellido))
                            self.obj_form.tw_garantes_lista.setItem(rowPosition , 7, QTableWidgetItem(item.nombre))
                except:
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Atencion")
                    msgBox.setText('Error, Verificar Numero de cliente garante sin espacios y sin puntos ')
                    msgBox.exec_()
                    return False

    def limpiar(self):
        while (self.obj_form.tw_garantes_lista.rowCount() > 0):
            self.obj_form.tw_garantes_lista.removeRow(0)

#app = QApplication(sys.argv)
#dialogo= Garante_historial()
#dialogo.show()
#app.exec_()