import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_credito_calcular import Ui_form_credito_calcular
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook
import math


class Calcular_credito(QDialog):
    obj_form= Ui_form_credito_calcular()
    id_usu=1
    id_party =""
    list_garante = list()
    nro_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_credito_calcular()
        self.obj_form.setupUi(self)
        self.obj_form.boton_generar_creditonuevo.clicked.connect(self.calcular_credito)
        self.obj_form.boton_limpiar_creditonuevo.clicked.connect(self.limpiar_nuevo)


    def limpiar_nuevo(self):
        while (self.obj_form.tw_lista_cuotas_creditonuevo.rowCount() > 0):
            self.obj_form.tw_lista_cuotas_creditonuevo.removeRow(0)

    def calcular_credito(self):
        self.limpiar_nuevo()
        
        obj_credito_total=0
        interes_total=0
        vencimiento_primer_cuota= self.obj_form.dte_fec_creditonuevo.text()
        capital = self.obj_form.lne_importe_prestamo_creditonuevo.text()
        tasa = self.obj_form.lne_interes_creditonuevo.text()
        cantidad_cuotas = self.obj_form.spbx_cantidad_cuotas_creditonuevo.text()

        obj_date_venc_1er_cuota = datetime.datetime.strptime(vencimiento_primer_cuota, '%d/%m/%Y')
        interes=self.redondear(str(float(capital) / float(tasa)))
        obj_capital = self.redondear(str(float(capital) / float(cantidad_cuotas)))

        hoy = obj_date_venc_1er_cuota
        contador = 0
        gastos = self.calcular_Gastos(int(cantidad_cuotas))
        resultado_gatos= gastos * int(cantidad_cuotas)

        for item in  range(0,int(cantidad_cuotas)):
            #obj_cuotas= N_cuotas(1)
            #agrego registros en la grilla
            rowPosition = self.obj_form.tw_lista_cuotas_creditonuevo.rowCount()
            self.obj_form.tw_lista_cuotas_creditonuevo.insertRow(rowPosition)
            valor_cuota =float(interes) + float(obj_capital) + float(gastos)
            obj_credito_total= obj_credito_total +  float(interes) + float(obj_capital) + float(gastos)
            interes_total= interes_total + interes
            nro_cuota = str(item + 1)
            
            self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 0, QTableWidgetItem(str(nro_cuota)))
            self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 1, QTableWidgetItem(str(obj_capital)))
            self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 2, QTableWidgetItem(str(interes)))
            self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 3, QTableWidgetItem(str(gastos)))

            if contador == 0 :
                self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem(str(obj_date_venc_1er_cuota)))
                #obj_cuotas.primer_Vencimiento = vencimiento_primer_cuota
            else:
                 nuevo_mes = hoy.month + contador
                 nuevo_year = hoy.year
                 nuevo_dia = 5
                 if nuevo_mes > 12:
                    nuevo_mes = nuevo_mes % 12
                    nuevo_year += 1
                
                 obj_fecha_cuota= datetime.datetime(nuevo_year, nuevo_mes, nuevo_dia)
                 self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem(str(obj_fecha_cuota)   ))
                 #obj_cuotas.primer_Vencimiento = obj_fecha_cuota
           
            self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 5, QTableWidgetItem(str(valor_cuota)))
            #self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem((str(float(capital) / float(tasa)))))
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            contador = contador + 1

        self.obj_form.lne_credito_total.setText(str(obj_credito_total))
        self.obj_form.lne_interes_total.setText(str(interes_total))
        self.obj_form.lne_otros_total.setText(str(resultado_gatos))

    def redondear(self,obj_capital):
        pos = obj_capital.find('.') 
        unidad = obj_capital[(pos-1)]
        lista = list(obj_capital)
        result = ""
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        capital = int(round(float(obj_capital),2))
        if (int(unidad) <= 3):
            lista[(pos-1)] = '0'
        elif (int(unidad) > 3) and (int(unidad) < 8):
            lista[(pos-1)] = '5'
        elif (int(unidad) > 8):
            result2 = capital/10 
            result3 = math.ceil(result2)
            result = result3 * 10
            return int(result)
            
        for item in lista:
            if item != '.' :
                result = result + str(item)
            elif item == '.':
                break
        return int(result)
    
    def calcular_Gastos(self, cant_cuotas):
        if (cant_cuotas >= 3) and (cant_cuotas <= 5):
            gastos =80
        elif (cant_cuotas == 6):
            gastos =62
        elif (cant_cuotas == 7):
            gastos = 42
        elif (cant_cuotas >= 8) and (cant_cuotas <= 12):
            gastos = 25
        elif (cant_cuotas >= 13) and (cant_cuotas <= 15):
            gastos = 15
        elif (cant_cuotas >= 16) and (cant_cuotas <= 18):
            gastos = 5
        elif (cant_cuotas >= 19):
            gastos = 0

        return gastos
     

#app = QApplication(sys.argv)
#dialogo= Calcular_credito()
#dialogo.show()
#app.exec_()


