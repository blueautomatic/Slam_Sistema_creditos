import sys, datetime, os
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtWidgets import QFileDialog
from form_reporte_deuda_cliente import Ui_form_deuda_cliente
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cuotas import E_cuotas
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
import subprocess
from E_configuracion import configuracion

class Reporte_deuda_cliente(QDialog):

    obj_form_reporte= Ui_form_deuda_cliente()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form_reporte = Ui_form_deuda_cliente()
        self.obj_form_reporte.setupUi(self)
        self.obj_form_reporte.boton_reporte.clicked.connect(self.reporte)

    def reporte(self):
        fec_hoy= datetime.date.today()
        hoy = fec_hoy.strftime("%d/%m/%Y")

        obj_e_cuotas = E_cuotas(1)


        styleSheet=getSampleStyleSheet()
        img=Image("cabezalcaida.png",100,25)
        img.hAlign = "RIGHT"
        otro_estilo= ParagraphStyle('',fontSize =9,textColor = '#000',leftIndent = -44,rightIndent = 150)
        fec_estilo= ParagraphStyle('',fontSize =9,textColor = '#000',leftIndent = 360,rightIndent = 0)
        style_barra= ParagraphStyle('',fontSize = 10,textColor = '#000',leftIndent = 0,rightIndent = 10)
        texto_principal = ""
        estilo_texto = ParagraphStyle('',
                fontSize = 5,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#000',
            leftIndent = 5 )


        h = Paragraph( texto_principal, estilo_texto)
        banner = [ [ img,h ] ]
        options = QFileDialog.Options()
        story=[]
        ban = Table( banner, colWidths=270, rowHeights=-25)
        story.append(ban)
        story.append(Spacer(0,25))

        P=Paragraph("<b> Fecha:  </b>" + str(hoy)+"",fec_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        #grilla cabezal
        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''', styleSheet["BodyText"])],
                       [Paragraph('''<font size=10> <b> Cliente</b></font>''', estilo_texto),
                        Paragraph('''<font size=10> <b> Monto</b></font>''', estilo_texto)]]

        t=""
        list_cuotas=list()
        list_cuotas = obj_e_cuotas.reporte_deuda_por_cliente()
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        for item in list_cuotas:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            apellido = item[1]
            nombre = item[2]
            monto = item[0]
            estiloape_nom= " <font size=9>" + apellido +', '+nombre  + "</font>"
            estilodescuento= " <font size=9>" + str(monto) + " </font>"

            integrantes.append([Paragraph(estiloape_nom, estilo_texto),
                                  Paragraph(estilodescuento, estilo_texto)])

            t=Table(integrantes, (175, 175))
            t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                            ]))
        story.append(t)


        # ---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        # pyqtRemoveInputHook()
        # import pdb; pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/credito/credito" + str(datetime.date.today().year) + "_" + str(
            datetime.date.today().month)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc = SimpleDocTemplate(file_path + "/reporte_cliente_deuda.pdf")
        doc.build(story)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Reporte Cliente Deuda")
        msgBox.setText("El Reporte fue generado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path + "/reporte_cliente_deuda.pdf"])
        else:
            os.startfile(file_path + "/reporte_cliente_deuda.pdf")

        return True



