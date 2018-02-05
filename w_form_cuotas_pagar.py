import sys,datetime, os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem, QScrollArea
from PyQt5 import uic
from form_creditos_cuotas_buscar import Ui_form_creditos_cuotas_buscar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from N_cuotas import N_cuotas
from form_cuotas_pagar import Ui_form_cuotas_pagar
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image,Flowable
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.shapes import String, Line
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog
from E_party_party import E_party_party
from E_party_address import E_party_address
from E_ticket import E_ticket
from E_historial_cuota import E_historial_cuota
from w_form_cuota_historial import Cuota_historial
import subprocess
from E_configuracion import configuracion


class Cuotas_pagar(QDialog):
    obj_form = Ui_form_cuotas_pagar()
    id_party = ""
    id_cuota = 0
    nro_cuota = 0
    importe_apagar = 0
    importe_cobrado = 0
    list_importe_cuota = list()
    total_cuotas=0
    singleton =""
    lista_ticket = list()
    nro_credito_ticket=0
    singleton_idusu=""
    clickedIndex_pagar=0
    id_cuota_historial=0
    nro_credito_historial=0
    vencimiento_historial=""
    credito_cancelado = False

    def __init__(self,singleton,singleton_idusu):
        QDialog.__init__(self)
        obj_form= Ui_form_cuotas_pagar()
        self.obj_form.setupUi(self)
        self.limpiar()
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        self.obj_form.tw_listado_cuotas.cellClicked.connect(self.seleccion_item_tabla)
        self.obj_form.boton_pagar.clicked.connect(self.pagar_cuota)
        self.obj_form.boton_re_ticket.clicked.connect(self.re_ticket)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)
        self.singleton= singleton
        self.singleton_idusu = singleton_idusu
        self.obj_form.boton_ticket.clicked.connect(self.ticket)
        self.obj_form.boton_historial_cuota.clicked.connect(self.historial_cuota)


    #def seleccion_item_tabla_listado_cuotas(self,clickedIndex):
     #   twi0 = self.obj_form.tw_listado_cuotas.item(clickedIndex,0)
      #  twi1 = self.obj_form.tw_listado_cuotas.item(clickedIndex,1)
      #  nro_credito = twi0.text()
      #  nro_cuota = twi1.text()
      #  obj_cuotas = N_cuotas(1)
      #  lista_cuotas = list()

        #lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

    def re_ticket(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        obj_N_cuotas = N_cuotas(1)
        obj_cuotas = N_cuotas(1)
        try:
            obj_cuotas.id = int(self.id_cuota.text())
            obj_cuotas.nro_cuota = self.nro_cuota.text()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText( 'Seleccione la cuota nuevamente')
            msgBox.exec_()
            return False
        obj_cuota_nro_credito = obj_N_cuotas.buscar_cuota_por_id_cuota(obj_cuotas.id)
        nro_credito = obj_cuota_nro_credito.nro_credito
        self.nro_credito_ticket = nro_credito

        obj_cuotas.estado_cuota = self.obj_form.cbx_estado.currentText()
        obj_cuotas.fecha_cobro = self.obj_form.dte_fecha_cobro.text()
        obj_cuotas.importe_cobrado =  float (self.obj_form.lne_importe_cobrar.text()) +  self.importe_cobrado
        obj_cuotas.interes = float (self.obj_form.lne_interes.text())
        obj_cuotas.punitorios = float (self.obj_form.lne_punitorios.text())
        obj_cuotas.gastos = float (self.obj_form.lne_gastos.text())
        obj_cuotas.descripcion = self.obj_form.lne_descripcion.text()
        obj_cuotas.descuento = self.obj_form.lne_descuento.text()
        self.lista_ticket.append(obj_cuotas)
        self.ticket()

    def historial_cuota(self):
        self.obj_form_cta_hist = Cuota_historial(self.id_cuota_historial)
        #obj_form_cta_hist.show()
        self.obj_form_cta_hist.show()


    def ticket(self):

        monto_ticket=0
        for item in self.lista_ticket:
            monto_ticket = monto_ticket + item.importe_cobrado

        obj_E_ticket = E_ticket()
        obj_E_ticket.monto = monto_ticket
        obj_E_ticket.fecha = datetime.date.today()
        obj_E_ticket.nro_credito = self.nro_credito_ticket
        obj_E_ticket.write_uid = self.singleton_idusu.idusu
        obj_E_ticket.guardar_ticket(obj_E_ticket)

        nro_ticket = obj_E_ticket.buscar_ticket(self.nro_credito_ticket)

        obj_E_party = E_party_party()
        obj_asoc = obj_E_party.get_party_party(self.obj_form.lne_dni.text())
        obj_E_address = E_party_address()
        obj_address = obj_E_address.get_party_address(obj_asoc.id_party)
        fec_hoy= datetime.date.today()
        hoy = fec_hoy.strftime("%d/%m/%Y")

        styleSheet=getSampleStyleSheet()
        img=Image("cabezal3.png",150,35)
        img.hAlign = "RIGHT"
        otro_estilo= ParagraphStyle('',fontSize =6,textColor = '#000',leftIndent = 0,rightIndent = 100)

        style_barra= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 0)
        texto_banner2 = ParagraphStyle('',fontSize =6,textColor = '#000',leftIndent =-150,rightIndent = 0)

        estilo_texto = ParagraphStyle('',
                fontSize = 5,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#000',
            leftIndent = 5 )


        h = ""#Paragraph("<br/><br/><br/>aa<br/><b>Buenos Aires 53 -Local 2 y 3 -Tel.:02920-432424/ Cel.:02920-15695353</b>  ",texto_banner2)

        banner = [ [ img,h] ]

        banner2 = [[Paragraph('''<font size=3> <b> </b></font>''',styleSheet["BodyText"])],
                    [Paragraph("<b>Buenos Aires 53 -Local 2 y 3 -Tel.:02920-432424/ Cel.:02920-15695353</b><br/><b> Viedma - Río Negro - E-mail: crediprom@outlook.com.ar</b> ",texto_banner2)]]

        banner3 = [[Paragraph('''<font size=8> <b> </b></font>''',styleSheet["BodyText"])],
                    [Paragraph("<b>RECIBO N° " + str(nro_ticket) + "<br/>Fecha:   " + str (hoy)+ "<br/> CUIT: 30-71446302-7 <br/> ING. BRUTOS: 45969604 <br/> INIC. ACTIVIDADES: 20/05/2014</b>  ",texto_secundario)]]

        options = QFileDialog.Options()
        story=[]

        ban = Table( banner, colWidths=300, rowHeights=70,hAlign = "RIGHT")
        ban2 = Table( banner2, colWidths=300, rowHeights=10)
        ban3 = Table(banner3, colWidths=318, rowHeights=75, hAlign='RIGHT')


        tban3=ban3
        tban3.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.white),
                                    ('BOX', (0,1), (0,-1), 0.25, colors.white),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        #story.append(Spacer(100,10))
        ##superior
        d = Drawing(100, 1)
        d.add(Line(-5, -15, 585, -15))
        story.append(d)
        #izquierda
        d = Drawing(100, 1)
        d.add(Line(-5, -15, -5, -94))
        story.append(d)

        story.append(ban)
        story.append(Spacer(0,1))
        story.append(ban2)
        story.append(Spacer(0,-150))
        story.append(tban3)

        #centro
        d = Drawing(100, 1)
        d.add(Line(250, -2, 250, 79))
        story.append(d)
        #derecha
        d = Drawing(100, 1)
        d.add(Line(585, -1, 585, 79))
        story.append(d)
        #inferior
        d = Drawing(100, 1)
        d.add(Line(-5, 0, 585, 0))
        story.append(d)
        story.append(Spacer(150,-10))

        cabezal =[[Paragraph('''<font size=8> <b> </b></font>''',styleSheet["BodyText"])],
                    [Paragraph('<font size=8> <b> Señor(es): '+ obj_asoc.apellido +", "+obj_asoc.nombre +'</b> <br/> <b> Domicilio: ' +obj_address.domicilio +'</b><br/></font>',estilo_texto)]]

        tcabezal=Table(cabezal, (590))
        tcabezal.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        story.append(tcabezal)
        story.append(Spacer(0,-15))

        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''',styleSheet["BodyText"])],
                       [Paragraph('''<font size=10> <b> </b>Credito N°</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Cuota N°</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Monto</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Vencimiento</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Estado</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Descuento</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Interes</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Importe</font>''',estilo_texto)]]



        for item in self.lista_ticket:
            #obj_cuotas.nro_credito = self.nro_credito_historial
            #obj_cuotas.importe_primer_venc = self.vencimiento_historial.text()
            #obj_cuotas.primer_Vencimiento = self.vencimiento_historial.text()

            estilonro_credi= " <font size=8>" + str(item.nro_credito) + "</font>"
            estilonro_cta= " <font size=8>" + str(item.nro_cuota) + "</font>"
            estilomonto = " <font size=8>" + str(item.importe_primer_venc) + "</font>"
            estiloprimer_venc = " <font size=8>" + str(item.primer_Vencimiento) + "</font>"
            estiloestado_cta = " <font size=8>" + item.estado_cuota + "</font>"
            estilodescuento = " <font size=8>" + str(item.descuento) + "</font>"
            estilointeres = " <font size=8>" + str(item.punitorios) + "</font>"
            estiloimporte = " <font size=8>" + str(item.importe_cobrado) + "</font>"


            integrantes.append([Paragraph(estilonro_credi,estilo_texto),
                                Paragraph(estilonro_cta,estilo_texto),
                                Paragraph(estilomonto,estilo_texto),
                                Paragraph(estiloprimer_venc,estilo_texto),
                                Paragraph(estiloestado_cta,estilo_texto),
                                Paragraph(estilodescuento,estilo_texto),
                                Paragraph(estilointeres,estilo_texto),
                                Paragraph(estiloimporte,estilo_texto)])

            tintegrantes=Table(integrantes,(60,60,60,70,70,70,70,70))
            tintegrantes.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                    ]))
        story.append(tintegrantes)
        cant_list = len(self.lista_ticket)
        if(cant_list <10):
            result = 11-cant_list
            for item in range(1,result):
                story.append(Spacer(0,8))

        story.append(Spacer(0,1))

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        a = ("%.2f" % monto_ticket)
        totales =[[Paragraph('''<font size=8> <b> </b></font>''',styleSheet["BodyText"])],
                    [Paragraph("<b>Importe: $"+str(a) +"  </b>",style_barra)]]


        tota = Table(totales, colWidths=200, rowHeights=20, hAlign='RIGHT')
        #t=Table(totales, (590))
        tota.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        story.append(tota)

        if cant_list >= 1 and cant_list < 6:
            story.append(Spacer(0,50))
        elif cant_list > 6 and cant_list < 10:
            story.append(Spacer(0,25))




        #dejo un mesaje tengo que agregar un while que compara si la cantidad de cuotas pagas es igual
        # a cantidad el credito esta cancelado
        #pyqtRemoveInputHook()
        #import pdb;
        #pdb.set_trace()
        if self.credito_cancelado:

            totales = [[Paragraph('''<font size=5> <b> </b></font>''', styleSheet["BodyText"])],
                       [Paragraph("<b>CREDITO CANCELADO</b>", style_barra)]]

            tota = Table(totales, colWidths=200, rowHeights=20, hAlign='LEFT')
            # t=Table(totales, (590))
            tota.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
            story.append(tota)

        #-------------Duplicado------------------#

        ##superior
        d = Drawing(100, 1)
        d.add(Line(-5, -15, 585, -15))
        story.append(d)
        #izquierda
        d = Drawing(100, 1)
        d.add(Line(-5, -15, -5, -94))
        story.append(d)

        story.append(ban)
        story.append(Spacer(0,1))
        story.append(ban2)
        story.append(Spacer(0,-150))
        story.append(tban3)
        #centro
        d = Drawing(100, 1)
        d.add(Line(250, -2, 250, 79))
        story.append(d)
        #derecha
        d = Drawing(100, 1)
        d.add(Line(585, -1, 585, 79))
        story.append(d)
        #inferior
        d = Drawing(100, 1)
        d.add(Line(-5, 0, 585, 0))
        story.append(d)
        story.append(Spacer(150,-10))

        story.append(Spacer(0,10))
        story.append(tcabezal)
        story.append(Spacer(0,10))
        story.append(tintegrantes)
        cant_list = len(self.lista_ticket)
        if(cant_list <10):
            result = 11-cant_list
            for item in range(1,result):
                story.append(Spacer(0,8))

        story.append(Spacer(0,1))
        story.append(tota)

        if cant_list >= 1 and cant_list < 6:
            story.append(Spacer(0,50))
        elif cant_list > 6 and cant_list < 10:
            story.append(Spacer(0,25))


        #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#

        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena  + "/pdf/ticket/ticket"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
        #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
               os.makedirs(file_path)
        doc = SimpleDocTemplate(file_path +"/ticket"+  obj_asoc.apellido +"_"+obj_asoc.nombre +".pdf", pagesize=A4, rightMargin=0.5,leftMargin=0.5, topMargin=5,bottomMargin=18)

        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Ticket")
        msgBox.setText("El ticket se ha generado correctamente : ticket" + obj_asoc.apellido +"_"+obj_asoc.nombre )
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/ticket"+  obj_asoc.apellido +"_"+obj_asoc.nombre +".pdf"])
        else:
            os.startfile( file_path +"/ticket"+ obj_asoc.apellido +"_"+obj_asoc.nombre  +".pdf")


    def limpiar(self):
        self.id_party = ""
        self.id_cuota = 0
        self.nro_cuota = 0
        self.importe_apagar = 0
        self.importe_cobrado = 0
        self.nro_credito_ticket = 0

        while (self.obj_form.tw_lista_creditos.rowCount() > 0):
            self.obj_form.tw_lista_creditos.removeRow(0)

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        for item in self.lista_ticket:
            self.lista_ticket.remove(item)

        for x in self.lista_ticket:
            self.lista_ticket.remove(x)


    def seleccion_item_tabla(self, clickedIndex):

        self.clickedIndex_pagar=clickedIndex
        #print (clickedIndex)
        #*-------------ACA SE VALIDA USUARIO PARA EDITAR PAGOS PARCIALEES INICIO-------------##
        #singleton = Singleton()                                                            #
        if self.singleton.tipo_usuario == "Administrador":
            self.obj_form.lne_importe_cuota.setEnabled(True)
            self.obj_form.lne_punitorios.setEnabled(True)
            self.obj_form.lne_descuento.setEnabled(True)                                      #
            self.obj_form.lne_importe_cobrar.setEnabled(True)                                    #
        #                                                                                     #
        #-+----------------------------DESCOMENTAR FIN para el mainwindow----------------#
        self.obj_form.cbx_estado.setEnabled(True)
        self.obj_form.dte_fecha_cobro.setEnabled(True)
        self.obj_form.dte_fecha_cobro.setDate(datetime.datetime.now())
        self.estado_cuota = self.obj_form.tw_listado_cuotas.item(clickedIndex,0)
        self.nro_cuota = self.obj_form.tw_listado_cuotas.item(clickedIndex,1)
        self.vencimiento_historial = self.obj_form.tw_listado_cuotas.item(clickedIndex,2)
        nro_cuota = self.nro_cuota.text()
        estado_cuota =self.estado_cuota.text()

        self.id_cuota = self.obj_form.tw_listado_cuotas.item(clickedIndex,14)
        self.id_cuota_historial= int(self.obj_form.tw_listado_cuotas.item(clickedIndex,14).text())
        self.nro_cuota = self.obj_form.tw_listado_cuotas.item(clickedIndex,1)

        twi2 = self.obj_form.tw_listado_cuotas.item(clickedIndex, 10)
        twi3 = self.obj_form.tw_listado_cuotas.item(clickedIndex, 11)
        twi4 = self.obj_form.tw_listado_cuotas.item(clickedIndex, 12)
        #twi7 = self.obj_form.tw_listado_cuotas.item(clickedIndex,)
        twi9 = self.obj_form.tw_listado_cuotas.item(clickedIndex,7)
        twi11 = self.obj_form.tw_listado_cuotas.item(clickedIndex,4)
        twi12 = self.obj_form.tw_listado_cuotas.item(clickedIndex,1)
        twi13 = self.obj_form.tw_listado_cuotas.item(clickedIndex,3)
        twi14 = self.obj_form.tw_listado_cuotas.item(clickedIndex,5)
        twi15 = self.obj_form.tw_listado_cuotas.item(clickedIndex,8)

        self.obj_form.lne_nro_cuota.setText(twi12.text())
        self.obj_form.lne_importe_cuota.setText(twi13.text())
        self.obj_form.lne_descuento.setText(twi14.text())
        self.obj_form.lne_saldo.setText(twi15.text())
        self.obj_form.lne_capital.setText(twi2.text())
        self.obj_form.lne_interes.setText(twi3.text())

        self.obj_form.lne_gastos.setText(twi4.text())
        self.obj_form.lne_punitorios.setText(twi11.text())
        self.importe_apagar = self.obj_form.lne_saldo.text()
        self.obj_form.lne_importe_cobrar.setText(str(self.importe_apagar))
        self.importe_cobrado =float(twi9.text())
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        twi16 =  self.obj_form.tw_listado_cuotas.item(clickedIndex, 14)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        twi17 = self.obj_form.tw_listado_cuotas.item(clickedIndex, 13)
        a = twi17.text()

        self.obj_form.lne_descripcion.setText(str(a))
        id = twi16.text()
        importe_cuota = twi13.text()
        obj_N_cuotas = N_cuotas(1)
        obj_N_cuotas.importe_cuota = importe_cuota
        obj_N_cuotas.id= id
        obj_N_cuotas.punitorios = self.obj_form.lne_punitorios.text()
        obj_N_cuotas.descuento = self.obj_form.lne_descuento.text()
        obj_N_cuotas.importe_cobrado = self.importe_cobrado
        noagregar_obj_N_cuotas= True
        for item in self.list_importe_cuota:
            if item.id == obj_N_cuotas.id:
                self.list_importe_cuota.remove(item)
                noagregar_obj_N_cuotas = False
        if noagregar_obj_N_cuotas == True :
            self.list_importe_cuota.append(obj_N_cuotas)
        total_cuotas =0
        for item in self.list_importe_cuota:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            total_cuotas = float(total_cuotas) + float (item.importe_cuota) - float(item.importe_cobrado)+ float(item.punitorios)  - float(item.descuento)
            self.obj_form.lne_total_cuotas.setText(str (round(total_cuotas,2)))

        self.obj_form.lne_cant_cuotas.setText(str(len(self.list_importe_cuota)))
        if self.obj_form.lne_cant_cuotas.text() == "0" :
            self.obj_form.lne_total_cuotas.setText("0")
            self.obj_form.lne_descripcion.setText("")


    def seleccion_item_tabla_creditos(self,clickedIndex):

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        twi0 = self.obj_form.tw_lista_creditos.item(clickedIndex,0)
        nro_credito = twi0.text()
        self.nro_credito_historial= int(twi0.text())
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

        lst_ord = [ (i.nro_cuota, i) for i in lista_cuotas ]
        lst_ord.sort()
        lst_ord = [ i[1] for i in lst_ord ]
        for item in lst_ord:
            saldo= round(float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios)  - float(item.importe_cobrado),2)  - round(float(item.descuento),2)
            cuota_pagar = float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios) - float(item.descuento)
            rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
            self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_vencimiento)[:10]))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
            if item.fecha_cobro != None :
                self.obj_form.tw_listado_cuotas.setItem(rowPosition ,9 , QTableWidgetItem(str(item.fecha_cobro)[:10]))
            else:
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))

            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(round(cuota_pagar,2))))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(item.importe_cobrado)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(round(saldo,2))))

            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(item.capital)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 11, QTableWidgetItem(str(item.interes)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 12, QTableWidgetItem(str(item.gastos)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 13, QTableWidgetItem(str(item.descripcion)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 14, QTableWidgetItem(str(item.id)))

    def pagar_cuota(self):
            estado = self.obj_form.tw_listado_cuotas.item(self.clickedIndex_pagar,0).text()
            if estado != "Pagada":
                obj_N_cuotas = N_cuotas(1)
                obj_cuotas = N_cuotas(1)

                try:
                    obj_cuotas.id = int(self.id_cuota.text())
                    obj_cuotas.nro_cuota = self.nro_cuota.text()
                except:
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Error")
                    msgBox.setText( 'Seleccione la cuota nuevamente')
                    msgBox.exec_()
                    return False

                obj_cuotas.estado_cuota = self.obj_form.cbx_estado.currentText()
                obj_cuotas.fecha_cobro = self.obj_form.dte_fecha_cobro.text()
                obj_cuotas.importe_cobrado =  float (self.obj_form.lne_importe_cobrar.text()) +  self.importe_cobrado
                obj_cuotas.interes = float (self.obj_form.lne_interes.text())
                obj_cuotas.punitorios = float (self.obj_form.lne_punitorios.text())
                obj_cuotas.gastos = float (self.obj_form.lne_gastos.text())
                obj_cuotas.descripcion = self.obj_form.lne_descripcion.text()
                obj_cuotas.descuento = self.obj_form.lne_descuento.text()

                if self.obj_form.cbx_estado.currentText() == "Pagada":
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    if obj_cuotas.nro_cuota == 1 :
                        resultado = float(float (self.importe_apagar) - float(self.obj_form.lne_importe_cobrar.text()) - float(self.obj_form.lne_descuento.text()))
                        if resultado >= 0:
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Error")
                            msgBox.setText( 'Actualizar el estado de la cuota a Pago Parcial. No se modifico el saldo')
                            msgBox.exec_()
                            return False
                    else :
                        resultado = float(float (self.importe_apagar) - float(self.obj_form.lne_importe_cobrar.text()) - float(self.obj_form.lne_descuento.text()))
                        if resultado >= 0:
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Error")
                            msgBox.setText( 'Actualizar el estado de la cuota a Pago Parcial. No se modifico el saldo')
                            msgBox.exec_()
                            return False

                if self.obj_form.cbx_estado.currentText() == "Pago Parcial":
                    resultado = float(float (self.importe_apagar) - float(self.obj_form.lne_importe_cobrar.text()))
                    if resultado == 0:
                        msgBox = QMessageBox()
                        msgBox.setWindowTitle("Aviso Cambiar estado cuota")
                        msgBox.setText( 'Actualizar el estado de la cuota a Pagada. No se modifico el saldo')
                        msgBox.exec_()
                        return False
                a=0

                while (self.obj_form.tw_listado_cuotas.rowCount() != a):

                    estado = self.obj_form.tw_listado_cuotas.item(a,0).text()
                    if estado == "A pagar":
                        if int(self.obj_form.lne_nro_cuota.text()) > int(self.obj_form.tw_listado_cuotas.item(a,1).text()):
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Informacion")
                            msgBox.setText('Tiene cuotas pendientes')
                            msgBox.exec_()
                            return False
                    elif estado == "Pago Parcial":
                        if int(self.obj_form.lne_nro_cuota.text()) > int(self.obj_form.tw_listado_cuotas.item(a,1).text()):
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Informacion")
                            msgBox.setText( 'Tiene cuotas pendientes')
                            msgBox.exec_()
                            return False
                    a = a + 1

                obj_N_cuotas.pagar_cuota(obj_cuotas)
                obj_N_cuotas.guardar_ingresos(obj_cuotas)
                obj_hist_cuota= E_historial_cuota()
                obj_hist_cuota.nro_credito =self.nro_credito_historial
                obj_hist_cuota.nro_cuota = int(self.obj_form.lne_nro_cuota.text())
                obj_hist_cuota.estado_cuota = self.obj_form.cbx_estado.currentText()
                obj_hist_cuota.fecha_cobro = self.obj_form.dte_fecha_cobro.text()
                obj_hist_cuota.importe_cobrado= float (self.obj_form.lne_importe_cobrar.text())
                obj_hist_cuota.descripcion= self.obj_form.lne_descripcion.text()
                obj_hist_cuota.importe_cuota= self.obj_form.lne_importe_cuota.text()
                obj_hist_cuota.write_uid= self.singleton_idusu.idusu
                obj_hist_cuota.primer_vencimiento= self.vencimiento_historial.text()
                obj_hist_cuota.id_cuota = self.id_cuota_historial

                obj_E_hist_cuota= E_historial_cuota()
                obj_E_hist_cuota.guardar(obj_hist_cuota)

                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                obj_cuotas.nro_credito = self.nro_credito_historial
                obj_cuotas.importe_primer_venc = self.obj_form.lne_importe_cuota.text()
                obj_cuotas.primer_Vencimiento = self.vencimiento_historial.text()
                self.lista_ticket.append(obj_cuotas)

                while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
                    self.obj_form.tw_listado_cuotas.removeRow(0)

                obj_cuota_nro_credito = obj_N_cuotas.buscar_cuota_por_id_cuota(obj_cuotas.id)
                nro_credito = obj_cuota_nro_credito.nro_credito
                self.nro_credito_ticket=nro_credito
                obj_cuotas = N_cuotas(1)
                lista_cuotas = list()
                lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))
                #ordena lista
                lst_ord = [ (i.nro_cuota, i) for i in lista_cuotas ]
                lst_ord.sort()
                lst_ord = [ i[1] for i in lst_ord ]


                for item in lst_ord:
                    saldo= round(float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios)  - float(item.importe_cobrado),2)  - round(float(item.descuento),2)
                    cuota_pagar = float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios) - float(item.descuento)
                    rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
                    self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_vencimiento)[:10]))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
                    if item.fecha_cobro != None :
                        self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(str(item.fecha_cobro)[:10]))
                    else:
                        self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))

                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(cuota_pagar)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(round(item.importe_cobrado))))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(saldo)))
                    #self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(str(item.fecha_cobro)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(item.capital)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 11, QTableWidgetItem(str(item.interes)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 12, QTableWidgetItem(str(item.gastos)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 13, QTableWidgetItem(str(item.descripcion)))
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 14, QTableWidgetItem(str(item.id)))

                self.obj_form.lne_total_cuotas.setText("0")
                self.obj_form.lne_descripcion.setText("")
                self.obj_form.lne_cant_cuotas.setText("0")
                for item in self.list_importe_cuota :
                    self.list_importe_cuota.remove(item)

                msgBox = QMessageBox()
                msgBox.setWindowTitle("Informacion")
                msgBox.setText( 'Pago Realizado')
                msgBox.exec_()

                control_de_cta=0
                prestamo_cancelado=0

                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                while (self.obj_form.tw_listado_cuotas.rowCount() != control_de_cta):
                    estado = self.obj_form.tw_listado_cuotas.item(control_de_cta,0).text()
                    if estado == "Pagada":
                        prestamo_cancelado=prestamo_cancelado+1
                    if prestamo_cancelado ==int(self.obj_form.tw_listado_cuotas.rowCount()):
                        #aca hay que terminar y actualizar el prestamo cancelado
                        self.credito_cancelado = True
                        obj_creditos = N_creditos(1)
                        obj_creditos.cancelar_credito(nro_credito)
                        msgBox = QMessageBox()
                        msgBox.setWindowTitle("Atencion")
                        msgBox.setText( 'El credito fue cancelado')
                        msgBox.exec_()


                    control_de_cta=control_de_cta+1
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atención")
                msgBox.setText( 'La cuota ya esta pagada.')
                msgBox.exec_()
                return True


    def buscar_cliente(self):
        self.limpiar()
        numero_dni = self.obj_form.lne_dni.text()
        obj_N_datos_cliente= N_creditos("a")
        if numero_dni != "":
            try:
                numero_documento_cliente= int(numero_dni)
            except:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText( 'Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()

        obj_N_datos_personales_cliente = N_datos_personales_cliente()
        obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(numero_documento_cliente)
        if obj_party_party != False:
            self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido + "   DNI:" +  obj_party_party.num_doc)
            self.obj_form.tw_lista_creditos.setEnabled(True)
            self.obj_form.tw_listado_cuotas.setEnabled(True)

            obj_N_credito = N_creditos(1)
            list_credito_party = obj_N_credito.get_list_credito(obj_party_party.id_party)

            lst_cred_party_activos=list()
            lst_cred_party_morosos = list()
            lst_cred_party_cancelado = list()

            for item in list_credito_party:
                if item.estado == "Activo":
                    lst_cred_party_activos.append(item)
                elif item.estado == "Cancelado":
                    lst_cred_party_cancelado.append(item)
                else:
                    lst_cred_party_morosos.append(item)

            for item in lst_cred_party_activos:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))

            for item in lst_cred_party_morosos:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))

            for item in lst_cred_party_cancelado:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))





#app = QApplication(sys.argv)
#dialogo= Cuotas_pagar()
#dialogo.show()
#app.exec_()
