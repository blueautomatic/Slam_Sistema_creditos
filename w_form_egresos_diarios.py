import sys, datetime
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

class egresos_diarios(QDialog):
    obj_form = Ui_form_egresos_diarios()
    lst_ord = list()
    
    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_egresos_diarios()
        self.obj_form.setupUi(self)
        self.obj_form.boton_egresos_imprimir.clicked.connect(self.imprimir)
        self.obj_form.boton_egresos_buscar.clicked.connect(self.egresos_diarios)
        

    def egresos_diarios(self):

        while (self.obj_form.tw_ingresos_registros.rowCount() > 0):
            self.obj_form.tw_ingresos_registros.removeRow(0)
            
        obj_N_egresos = N_egresos(1)
        lista_egresos = obj_N_egresos.buscar_egresos(self.obj_form.dte_fecha_egresos_mov.text())

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
        styleSheet=getSampleStyleSheet()
        img=Image("credi1.png",504,145)
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

        h = Paragraph(texto_principal, estilo_texto)
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

        P=Paragraph("<b>Registro de egresos diarios " + str(datetime.datetime.now()) +" </b> ",style_barra)
        story.append(P)
        story.append(Spacer(0,25))
        #nombre apellido dni Nro prestamo nro cuota monto
        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['N° Orden', 'Nombre y Apellido', 'Cuota', 'Número','Nro Importe']]

        for item in  self.lst_ord:           
            integrantes.append([str(item.id),str(item.nombre_cliente + ", " + item.apellido),str(item.nro_credito),str(item.cantidad_cuotas),str(item.importe_primer_venc),str(item.costo)])
            t=Table(integrantes, (150,55, 100, 135, 55,55))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))
        story.append(t)
        story.append(Spacer(0,15))
        doc=SimpleDocTemplate("Registro de Egresos diarios" + str(datetime.datetime.now()) +".pdf")
        doc.build(story)
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Correcto")
        msgBox.setText( 'Se genero el informe correctamente.')
        msgBox.exec_()
        

#app = QApplication(sys.argv)
#dialogo= egresos_diarios()
#dialogo.show()
#app.exec_()

