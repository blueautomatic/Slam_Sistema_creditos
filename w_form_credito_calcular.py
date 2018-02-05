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
        self.obj_form.boton_calcular.clicked.connect(self.calcular_cuotas)
        #self.obj_form.boton_limpiar_creditonuevo.clicked.connect(self.limpiar_nuevo)


    def limpiar_nuevo(self):
        pass

    def calcular_cuotas(self):
        capital = self.obj_form.lne_capital.text()
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()

        if capital != "":

            self.obj_form.lne_cta_3.setText(str(self.valor_cuota(3)))
            self.obj_form.lne_cta_4.setText(str(self.valor_cuota(4)))
            self.obj_form.lne_cta_5.setText(str(self.valor_cuota(5)))
            self.obj_form.lne_cta_6.setText(str(self.valor_cuota(6)))
            self.obj_form.lne_cta_7.setText(str(self.valor_cuota(7)))
            self.obj_form.lne_cta_8.setText(str(self.valor_cuota(8)))
            self.obj_form.lne_cta_9.setText(str(self.valor_cuota(9)))
            self.obj_form.lne_cta_10.setText(str(self.valor_cuota(10)))
            self.obj_form.lne_cta_11.setText(str(self.valor_cuota(11)))
            self.obj_form.lne_cta_12.setText(str(self.valor_cuota(12)))
            self.obj_form.lne_cta_13.setText(str(self.valor_cuota(13)))
            self.obj_form.lne_cta_14.setText(str(self.valor_cuota(14)))
            self.obj_form.lne_cta_15.setText(str(self.valor_cuota(15)))
            self.obj_form.lne_cta_16.setText(str(self.valor_cuota(16)))
            self.obj_form.lne_cta_17.setText(str(self.valor_cuota(17)))
            self.obj_form.lne_cta_18.setText(str(self.valor_cuota(18)))
            self.obj_form.lne_cta_19.setText(str(self.valor_cuota(19)))
            self.obj_form.lne_cta_20.setText(str(self.valor_cuota(20)))
            self.obj_form.lne_cta_21.setText(str(self.valor_cuota(21)))
            self.obj_form.lne_cta_22.setText(str(self.valor_cuota(22)))
            self.obj_form.lne_cta_23.setText(str(self.valor_cuota(23)))
            self.obj_form.lne_cta_24.setText(str(self.valor_cuota(24)))


        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Verificar que el campo Capital y Nro de cuota vacios')
            msgBox.exec_()

    def valor_cuota(self, cant_cuotas):


        tasa=8
        capital = self.obj_form.lne_capital.text()
        if  cant_cuotas >1 and cant_cuotas < 6:
            tasa=11

        interes=(float(capital) * tasa)/100
        obj_capital = str(float(capital) / float(cant_cuotas))
        obj_capital=self.redondear(obj_capital)
        gastos = self.calcular_Gastos(int(cant_cuotas))
        valor_cuota = float(interes) + float(obj_capital) + float(gastos)

        return valor_cuota


    def redondear1(self,obj_capital):
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


    def redondear(self,obj_capital):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        pos = obj_capital.find('.')

        unidad = obj_capital[(pos-1)]
        lista = list(obj_capital)
        result = ""
        if (int(unidad) <= 3):
            lista[(pos-1)] = '0'
        elif (int(unidad) >= 4) :
            lista[(pos-1)] = '5'


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


