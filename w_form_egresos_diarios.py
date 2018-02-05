import sys, datetime,os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_egresos_diarios import Ui_form_egresos_diarios
#from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente, N_party_contacto
#from N_creditos import N_creditos
from N_egresos import N_egresos
from PyQt5.QtCore import pyqtRemoveInputHook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog
from E_configuracion import configuracion
import subprocess

class egresos_diarios(QDialog):
    obj_form = Ui_form_egresos_diarios()
    lst_ord = list()
    bandera = False

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_egresos_diarios()
        self.obj_form.setupUi(self)
        self.obj_form.boton_egresos_imprimir.clicked.connect(self.imprimir)
        self.obj_form.boton_egresos_buscar.clicked.connect(self.egresos_diarios)
        self.obj_form.dte_fecha_egresos_mov.setDate(datetime.datetime.now())
        self.bandera= False


    def egresos_diarios(self):

        while (self.obj_form.tw_ingresos_registros.rowCount() > 0):
            self.obj_form.tw_ingresos_registros.removeRow(0)

        obj_N_egresos = N_egresos(1)
        lista_egresos = obj_N_egresos.buscar_egresos(self.obj_form.dte_fecha_egresos_mov.text())

        if len(lista_egresos) !=0:
            self.bandera = True
            self.lst_ord = [ (i.id, i) for i in lista_egresos ]
            self.lst_ord.sort()
            self.lst_ord = [ i[1] for i in self.lst_ord ]

            importe = 0
            for item in self.lst_ord :
                importe = importe + float(item.costo)
                rowPosition = self.obj_form.tw_ingresos_registros.rowCount()
                self.obj_form.tw_ingresos_registros.insertRow(rowPosition)
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 0, QTableWidgetItem(str(item.id)))
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 1, QTableWidgetItem(str(item.nombre_cliente + ", " + item.apellido)))
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 3, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 4, QTableWidgetItem(str(item.importe_primer_venc)))
                self.obj_form.tw_ingresos_registros.setItem(rowPosition , 5, QTableWidgetItem(str(item.costo)))

            self.obj_form.lne_egresos_total.setText(str(importe))

    def imprimir(self):
        if self.bandera ==True:
            fec_hoy= datetime.date.today()
            hoy = fec_hoy.strftime("%d/%m/%Y")


            styleSheet=getSampleStyleSheet()
            img=Image("cabezalcaida.png",225,50)
            otro_estilo= ParagraphStyle('',fontSize = 20,textColor = '#000',leftIndent = 200,rightIndent = 50)
            style_barra= ParagraphStyle('',fontSize = 13,textColor = '#000',leftIndent = 300, rightIndent = 0)
            estilo_cabezal= ParagraphStyle('',fontSize = 15,textColor = '#000',leftIndent = 100,rightIndent = 0)

            texto_principal = ""
            estilo_texto = ParagraphStyle('',
                    fontSize = 12,
                            alignment = 0,
                            spaceBefore = 0,
                            spaceAfter = 0,
                #backColor = '#fff',
                textColor = '#999',
                leftIndent = 10 )

            h = Paragraph(texto_principal, estilo_texto)
            banner = [ [ img,h ] ]
            options = QFileDialog.Options()
            story=[]
            ban = Table( banner, colWidths=0, rowHeights=10)

            story.append(ban)
            story.append(Spacer(0,15))


            P=Paragraph("<u>Registro de egresos diarios </u> ",estilo_cabezal)
            story.append(P)
            story.append(Spacer(0,25))

            P=Paragraph("<b>Fecha:  " + str (hoy)+ " </b> ",style_barra)
            story.append(P)
            story.append(Spacer(0,5))

            #nombre apellido dni Nro prestamo nro cuota monto
            integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                    ['N° Orden', 'Cliente','Nro. Credito','Cant. Cta', 'Monto Cta.',' Total Crédito']]

            for item in  self.lst_ord:
                integrantes.append([str(item.id),str(item.apellido + ", " + item.nombre_cliente),str(item.nro_credito),str(item.cantidad_cuotas),str(item.importe_primer_venc),str(item.costo)])
                t=Table(integrantes, (50,150, 75, 75, 75,75))
                t.setStyle(TableStyle([
                                   ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                   ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                   ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                   ]))
            story.append(t)
            story.append(Spacer(0,15))


            obj_config = configuracion()
            cadena = obj_config.ruta()

            file_path = cadena  + "pdf/ingresos/Reg_Egresos_"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
            #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
            if not os.path.exists(file_path):
                   os.makedirs(file_path)

            doc=SimpleDocTemplate(file_path +"/Reg_Egresos_"+  str(datetime.date.today())   +".pdf")
            doc.build(story )

            msgBox = QMessageBox()
            msgBox.setWindowTitle("Estado de Egresos")
            msgBox.setText("El Egreso se ha generado correctamente : Reg_Egresos_" +  str(datetime.date.today()))
            msgBox.exec_()

            if sys.platform == 'linux':
                subprocess.call(["xdg-open", file_path +"/Reg_Egresos_"+   str(datetime.date.today())  +".pdf"])
            else:
                os.startfile( file_path +"/Reg_Egresos_"+  str(datetime.date.today())  +".pdf")





            #doc=SimpleDocTemplate("Reg_Egresos_" + str(datetime.date.today()) +".pdf")
            #doc.build(story)

            #msgBox = QMessageBox()
            #msgBox.setWindowTitle("Correcto")
            #msgBox.setText( 'Se genero el informe correctamente.')
            #msgBox.exec_()


    #app = QApplication(sys.argv)
    #dialogo= egresos_diarios()
    #dialogo.show()
    #app.exec_()

