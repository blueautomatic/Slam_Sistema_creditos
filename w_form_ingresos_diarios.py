import sys, datetime, os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_ingresos_diarios import Ui_form_ingresos_diarios
#from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente, N_party_contacto
#from N_creditos import N_creditos
#from N_cuotas import N_cuotas
from PyQt5.QtCore import pyqtRemoveInputHook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog
from N_ingresos import N_ingresos
import subprocess


class ingresos_diarios(QDialog):
    obj_form = Ui_form_ingresos_diarios()
    lst_ord = list()
    lista_ingresos= list()
    lst_ord = list()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_ingresos_diarios()
        self.obj_form.setupUi(self)
        self.obj_form.boton_ingresos_imprimir.clicked.connect(self.imprimir)
        self.obj_form.boton_ingresos_buscar.clicked.connect(self.buscar_ingresos)
        self.obj_form.dte_fecha_ingresos_mov.setDate(datetime.datetime.now())

    def buscar_ingresos(self):
        self.limpiar()
        fecha= self.obj_form.dte_fecha_ingresos_mov.text()
        obj_ingresos = N_ingresos(1)
        self.lista_ingresos=obj_ingresos.ingresos_buscar(fecha)
        ingreso_total = 0

        for item in self.lista_ingresos :
            ingreso_total = ingreso_total + item.monto_cobrado
            rowPosition = self.obj_form.tw_ingresos_registros.rowCount()
            self.obj_form.tw_ingresos_registros.insertRow(rowPosition)
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 0, QTableWidgetItem(str(item.nombre + ", " + item.apellido)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 1, QTableWidgetItem(str("Cuota Credito")))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 3, QTableWidgetItem(str(round(item.monto_cobrado,2))))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 5, QTableWidgetItem(str(round(item.descuento,2))))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 6, QTableWidgetItem(str(item.estado_cuota)))

            self.lst_ord.append(item)

        self.obj_form.lne_ingresos_total.setText(str(round(ingreso_total,2)))

    def imprimir(self):

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

        P=Paragraph("<u>Registro de ingresos diarios </u> ",estilo_cabezal)
        story.append(P)
        story.append(Spacer(0,25))

        P=Paragraph("<b>Fecha:  " + str (hoy)+ " </b> ",style_barra)
        story.append(P)
        story.append(Spacer(0,5))

        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['Nombre y Apellido', 'Cuota', 'N° Cuota','Importe', 'Punitorios','Descuento', 'Estado']]
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        for item in self.lst_ord:
            integrantes.append([str(item.nombre + ", " + item.apellido),str("cuota credito"),str(item.nro_cuota),str(round(item.monto_cobrado,2)),str(round(item.punitorios,2)), str(round(item.descuento,2)), str(item.estado_cuota)])
            t=Table(integrantes, (120,65, 60, 60,75,75,50))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))

        story.append(t)
        story.append(Spacer(0,15))


        nombre_archivo = "Reg_ing_diarios" + str(datetime.date.today().year)+"_"+str(datetime.date.today().month) + "_" + str(datetime.date.today().day) + ".pdf"

        #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        file_path ="/home/slam2016/Documentos/credired/credired20170306/pdf/ingresos/ingresos"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)


        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc=SimpleDocTemplate(file_path +"/" + nombre_archivo)
        doc.build(story)
        if doc:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Correcto")
            msgBox.setText( 'Se genero el informe correctamente : ' + nombre_archivo)
            msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/" + nombre_archivo])
        else:
            os.startfile( file_path +"/" + nombre_archivo)

    def limpiar(self):
        while (self.obj_form.tw_ingresos_registros.rowCount() > 0):
            self.obj_form.tw_ingresos_registros.removeRow(0)

#app = QApplication(sys.argv)
#dialogo= ingresos_diarios()
#dialogo.show()
#app.exec_()
