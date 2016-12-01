import sys, datetime
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


    def buscar_ingresos(self):
        self.limpiar()
        fecha= self.obj_form.dte_fecha_ingresos_mov.text()
        obj_ingresos = N_ingresos(1)
        self.lista_ingresos=obj_ingresos.ingresos_buscar(fecha)
        ingreso_total = 0

        for item in self.lista_ingresos :
            ingreso_total = ingreso_total + item.importe_cobrado             
            rowPosition = self.obj_form.tw_ingresos_registros.rowCount()
            self.obj_form.tw_ingresos_registros.insertRow(rowPosition)
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 0, QTableWidgetItem(str(item.nombre + ", " + item.apellido)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 1, QTableWidgetItem(str("Cuota Credito")))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cobrado)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 4, QTableWidgetItem(str(item.punitorios)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
            self.obj_form.tw_ingresos_registros.setItem(rowPosition , 6, QTableWidgetItem(str(item.estado_cuota)))

            self.lst_ord.append(item)

        self.obj_form.lne_ingresos_total.setText(str(ingreso_total))

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

        P=Paragraph("<b>Registro de ingresos diarios "+ str(datetime.datetime.now()) +"</b> ",style_barra)
        story.append(P)
        story.append(Spacer(0,25))
        #nombre apellido dni Nro prestamo nro cuota monto
        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                ['Nombre y Apellido', 'Cuota', 'Número','Nro Importe', 'Punitorios','Descuento', 'Estado']]
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        
        for item in self.lst_ord:           
            integrantes.append([str(item.nombre + ", " + item.apellido),str("cuota credito"),str(item.nro_cuota),str(item.importe_cobrado),str(item.punitorios), str(item.descuento), str(item.estado_cuota)])
            t=Table(integrantes, (120,80, 60, 60,53,50,40))
            t.setStyle(TableStyle([
                               ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                               ]))
        
        story.append(t)
        story.append(Spacer(0,15))
        nombre_archivo = "Reg_ing_diarios" + str(datetime.datetime.now()) + ".pdf"
        doc=SimpleDocTemplate(nombre_archivo)
        doc.build(story)
        if doc:            
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Correcto")
            msgBox.setText( 'Se genero el informe correctamente : ' + nombre_archivo)
            msgBox.exec_()
            return False 

    def limpiar(self):
        while (self.obj_form.tw_ingresos_registros.rowCount() > 0):
            self.obj_form.tw_ingresos_registros.removeRow(0)

#app = QApplication(sys.argv)
#dialogo= ingresos_diarios()
#dialogo.show()
#app.exec_()