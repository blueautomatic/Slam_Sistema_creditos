import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_cuotas_vencidas_30dias import Ui_form_cuotas_vencidas_30dias
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente, N_party_contacto
from N_creditos import N_creditos
from N_cuotas import N_cuotas
from PyQt5.QtCore import pyqtRemoveInputHook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog

class Cuotas_vencidas_30dias(QDialog):
    obj_form = Ui_form_cuotas_vencidas_30dias()
    listado_cuotas_30_dias = list()
    listado_cuotas_60_dias = list()
    listado_cuotas_90_dias = list()

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_cuotas_vencidas_30dias()
        self.obj_form.setupUi(self)
        self.obj_form.boton_generar.clicked.connect(self.generar_30dias)
        self.obj_form.boton_generar_60_dias.clicked.connect(self.generar_60dias)
        self.obj_form.boton_generar_90_dias.clicked.connect(self.generar_90dias)

    def generar_30dias(self):
        obj_N_nuotas = N_cuotas(1)
        self.listado_cuotas_30_dias = obj_N_nuotas.lista_cuotas_venc_30_dias("slam")

        styleSheet=getSampleStyleSheet()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        
        img=Image("credi1.png",504,145)
        #img.hAlign = "LEFT"
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
       

        otro_estilo= ParagraphStyle('',fontSize = 20,textColor = '#000',leftIndent = 200,rightIndent = 50)

        style_barra= ParagraphStyle('',fontSize = 13,textColor = '#000',backColor='#f5f5f5',borderColor ='#a3a3a3',borderWidth = 1,borderPadding = (1, 2, 5))
        texto_principal = ""
        estilo_texto = ParagraphStyle('',
                fontSize = 22,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#999',
            leftIndent = 10 )

        h = Paragraph( texto_principal, estilo_texto)
        banner = [ [ img,h ] ]
        options = QFileDialog.Options()
        story=[]
        ban = Table( banner, colWidths=300 )
        ban.setStyle([ ('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(0,0),(1,0),'LEFT'), ('VALIGN',(0,0),(1,0),'TOP'),
                    ('TEXTCOLOR',(0,1),(0,-1), colors.blue) ])
        story.append(ban)
        story.append(Spacer(0,10))


        P= Paragraph("<b>Reportes</b> ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,25))

        P=Paragraph("<b>Cuotas vencidas hasta 30 dias</b> " + str(datetime.datetime.now()),style_barra)
        story.append(P)
        story.append(Spacer(0,25))
        #nombre apellido dni Nro prestamo nro cuota monto
        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['Apellido', 'Nombre', 'D.N.I:', 'Nro Crédito:','Nro Cuota','Monto']]

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in  self.listado_cuotas_30_dias:
            monto_adeudado = float(item.importe_primer_venc) + float(item.punitorios)
            obj_N_credito = N_creditos(1)
            obj_credito = obj_N_credito.buscar_credito_por_nro_credito(item.nro_credito)
            obj_N_datos_personales_cliente = N_datos_personales_cliente()
            obj_party = obj_N_datos_personales_cliente.buscar_party_party_por_id(obj_credito.id_party) 
            integrantes.append([str(obj_party.apellido), str(obj_party.nombre), str(obj_party.nro_doc) ,str(item.nro_credito),str(item.nro_cuota), str(monto_adeudado)])
            t=Table(integrantes, (150,55, 100, 135, 55,55))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))
            story.append(t)
            story.append(Spacer(0,15))

        nombre_archivo = "listado_de_morosos_30dias" + str(datetime.datetime.now()) + ".pdf"
        doc=SimpleDocTemplate(nombre_archivo)
        doc.build(story )
    
    def generar_60dias(self):
        obj_N_cuotas = N_cuotas(1)
        self.listado_cuotas_60_dias = obj_N_cuotas.lista_cuotas_venc_60_dias("slam")

        styleSheet=getSampleStyleSheet()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        
        img=Image("credi1.png",504,145)
        #img.hAlign = "LEFT"
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
       

        otro_estilo= ParagraphStyle('',fontSize = 20,textColor = '#000',leftIndent = 200,rightIndent = 50)

        style_barra= ParagraphStyle('',fontSize = 13,textColor = '#000',backColor='#f5f5f5',borderColor ='#a3a3a3',borderWidth = 1,borderPadding = (1, 2, 5))
        texto_principal = ""
        estilo_texto = ParagraphStyle('',
                fontSize = 22,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#999',
            leftIndent = 10 )

        h = Paragraph( texto_principal, estilo_texto)
        banner = [ [ img,h ] ]
        options = QFileDialog.Options()
        story=[]
        ban = Table( banner, colWidths=300 )
        ban.setStyle([ ('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(0,0),(1,0),'LEFT'), ('VALIGN',(0,0),(1,0),'TOP'),
                    ('TEXTCOLOR',(0,1),(0,-1), colors.blue) ])
        story.append(ban)
        story.append(Spacer(0,10))


        P= Paragraph("<b>Reportes</b> ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,25))

        P=Paragraph("<b>Cuotas vencidas hasta 60 dias</b> "+ str(datetime.datetime.now()),style_barra)
        story.append(P)
        story.append(Spacer(0,25))
        #nombre apellido dni Nro prestamo nro cuota monto
        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['Apellido', 'Nombre', 'D.N.I:', 'Nro Crédito:','Nro Cuota','Monto']]

        for item in  self.listado_cuotas_60_dias:
            monto_adeudado = float(item.importe_primer_venc) + float(item.punitorios)
            obj_N_credito = N_creditos(1)
            obj_credito = obj_N_credito.buscar_credito_por_nro_credito(item.nro_credito)
            obj_N_datos_personales_cliente = N_datos_personales_cliente()
            obj_party = obj_N_datos_personales_cliente.buscar_party_party_por_id(obj_credito.id_party) 
            integrantes.append([str(obj_party.apellido), str(obj_party.nombre), str(obj_party.nro_doc) ,str(item.nro_credito),str(item.nro_cuota), str(round(monto_adeudado,2))])
            t=Table(integrantes, (150,55, 100, 135, 55,55))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))

            story.append(t)
            story.append(Spacer(0,15))
        nombre_archivo = "listado_de_morosos_60dias" + str(datetime.datetime.now()) + ".pdf"
       
        doc=SimpleDocTemplate(nombre_archivo)
        doc.build(story )

    def generar_90dias(self):
        obj_N_cuotas = N_cuotas(1)
        self.listado_cuotas_90_dias = obj_N_cuotas.lista_cuotas_venc_90_dias("slam")

        styleSheet=getSampleStyleSheet()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        
        img=Image("credi1.png",504,145)
        #img.hAlign = "LEFT"
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
       

        otro_estilo= ParagraphStyle('',fontSize = 20,textColor = '#000',leftIndent = 200,rightIndent = 50)

        style_barra= ParagraphStyle('',fontSize = 13,textColor = '#000',backColor='#f5f5f5',borderColor ='#a3a3a3',borderWidth = 1,borderPadding = (1, 2, 5))
        texto_principal = ""
        estilo_texto = ParagraphStyle('',
                fontSize = 22,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#999',
            leftIndent = 10 )

        h = Paragraph( texto_principal, estilo_texto)
        banner = [ [ img,h ] ]
        options = QFileDialog.Options()
        story=[]
        ban = Table( banner, colWidths=300 )
        ban.setStyle([ ('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(0,0),(1,0),'LEFT'), ('VALIGN',(0,0),(1,0),'TOP'),
                    ('TEXTCOLOR',(0,1),(0,-1), colors.blue) ])
        story.append(ban)
        story.append(Spacer(0,10))


        P= Paragraph("<b>Reportes</b> ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,25))

        P=Paragraph("<b>Cuotas vencidas hasta 90 dias</b> " + str(datetime.datetime.now()),style_barra)
        story.append(P)
        story.append(Spacer(0,25))
        #nombre apellido dni Nro prestamo nro cuota monto
        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['Apellido', 'Nombre', 'D.N.I:', 'Nro Crédito:','Nro Cuota','Monto']]

        for item in  self.listado_cuotas_90_dias:
            monto_adeudado = float(item.importe_primer_venc) + float(item.punitorios)
            obj_N_credito = N_creditos(1)
            obj_credito = obj_N_credito.buscar_credito_por_nro_credito(item.nro_credito)
            obj_N_datos_personales_cliente = N_datos_personales_cliente()
            obj_party = obj_N_datos_personales_cliente.buscar_party_party_por_id(obj_credito.id_party) 
            integrantes.append([str(obj_party.apellido), str(obj_party.nombre), str(obj_party.nro_doc) ,str(item.nro_credito),str(item.nro_cuota), str(round(monto_adeudado,2))])
            t=Table(integrantes, (150,55, 100, 135, 55,55))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))

            story.append(t)
            story.append(Spacer(0,15))

        nombre_archivo = "listado_de_morosos_90dias" + str(datetime.datetime.now()) + ".pdf"
        doc=SimpleDocTemplate(nombre_archivo)
        doc.build(story )




#app = QApplication(sys.argv)
#dialogo= Cuotas_vencidas_30dias()
#dialogo.show()
#app.exec_()