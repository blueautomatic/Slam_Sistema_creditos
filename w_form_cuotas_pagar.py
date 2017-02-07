import sys,datetime
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
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog
from E_party_party import E_party_party


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

    def __init__(self,singleton):
        QDialog.__init__(self)
        obj_form= Ui_form_cuotas_pagar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        self.obj_form.tw_listado_cuotas.cellClicked.connect(self.seleccion_item_tabla)
        self.obj_form.boton_pagar.clicked.connect(self.pagar_cuota)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)
        self.singleton= singleton
        self.obj_form.boton_ticket.clicked.connect(self.ticket)


    #def seleccion_item_tabla_listado_cuotas(self,clickedIndex):
     #   twi0 = self.obj_form.tw_listado_cuotas.item(clickedIndex,0)
      #  twi1 = self.obj_form.tw_listado_cuotas.item(clickedIndex,1)
      #  nro_credito = twi0.text()
      #  nro_cuota = twi1.text()
      #  obj_cuotas = N_cuotas(1)
      #  lista_cuotas = list()

        #lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

    def ticket(self):
        obj_E_party = E_party_party()
        obj_asoc = obj_E_party.get_party_party(self.obj_form.lne_dni.text())
        fec_hoy= datetime.date.today()


        styleSheet=getSampleStyleSheet()
        img=Image("credi1.png",250,75)
        img.hAlign = "LEFT"
        otro_estilo= ParagraphStyle('',fontSize =12,textColor = '#000',leftIndent = 0,rightIndent = 50)

        style_barra= ParagraphStyle('',fontSize = 12,textColor = '#000',leftIndent = 0,rightIndent = 50)
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
        ban = Table( banner, colWidths=0, rowHeights=10)
        story.append(ban)
        story.append(Spacer(0,25))

        P=Paragraph("<b>Ticket</b>",style_barra)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>CrediProm </b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Razón social: Grupo Prom S.R.L.</b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>CUIT: 30-71446302-7</b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Dirección: </b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Teléfono: 02920-429-675</b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,20))

        P=Paragraph("<b>Datos del cliente </b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Apellido y nombre: " + obj_asoc.apellido+ " "+ obj_asoc.nombre  + " </b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>DNI: " + obj_asoc.num_doc + " </b>",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))



        integrantes = [[Paragraph('''<font size=12> <b> </b></font>''',styleSheet["BodyText"])],
                [Paragraph('''<font size=12> <b> </b>Estado</font>''',estilo_texto),
                Paragraph('''<font size=12> <b> </b>N° cuota</font>''',estilo_texto),
                Paragraph('''<font size=12> <b> </b>Importe</font>''',estilo_texto),
                Paragraph('''<font size=12> <b> </b>Descuento</font>''',estilo_texto),
                Paragraph('''<font size=12> <b> </b>Interes</font>''',estilo_texto)]]

        for item in self.lista_ticket:

            estilonom_plan= " <font size=10>" + item.estado_cuota + "</font>"
            estilonro_cta= " <font size=10>" + item.nro_cuota + "</font>"
            estiloimporte= " <font size=10>" + str(item.importe_cobrado) + "</font>"
            estilodescuento= " <font size=10>" + str(item.descuento) + "</font>"
            estilointeres= " <font size=10>" + str(item.punitorios) + "</font>"

            integrantes.append([ Paragraph(estilonom_plan,estilo_texto),
                                 Paragraph(estilonro_cta,estilo_texto),
                                 Paragraph(estiloimporte,estilo_texto),
                                 Paragraph(estilodescuento,estilo_texto),
                                 Paragraph(estilointeres,estilo_texto)])

            t=Table(integrantes, (100, 80, 100,70,70))
            t.setStyle(TableStyle([
                                       ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                       ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                       ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                       ]))

        story.append(t)
        story.append(Spacer(0,5))


        #P=Paragraph("<b>Total: " + importe + " </b>",style_barra)
        #story.append(P)
        #story.append(Spacer(0,5))

        doc=SimpleDocTemplate("ticket.pdf")
        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Ticket")
        msgBox.setText("El ticket se ha generado correctamente")
        msgBox.exec_()

    def limpiar(self):
        self.id_party = ""
        self.id_cuota = 0
        self.nro_cuota = 0
        self.importe_apagar = 0
        self.importe_cobrado = 0

        while (self.obj_form.tw_lista_creditos.rowCount() > 0):
            self.obj_form.tw_lista_creditos.removeRow(0)

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

    def seleccion_item_tabla(self, clickedIndex):

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
        nro_cuota = self.nro_cuota.text()
        estado_cuota =self.estado_cuota.text()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        self.id_cuota = self.obj_form.tw_listado_cuotas.item(clickedIndex,14)
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
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
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
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
            if item.fecha_cobro != None :
                self.obj_form.tw_listado_cuotas.setItem(rowPosition ,9 , QTableWidgetItem(str(item.fecha_cobro)))
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
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
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
        self.lista_ticket.append(obj_cuotas)

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        obj_cuota_nro_credito = obj_N_cuotas.buscar_cuota_por_id_cuota(obj_cuotas.id)
        nro_credito = obj_cuota_nro_credito.nro_credito
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
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
            if item.fecha_cobro != None :
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(str(item.fecha_cobro)))
            else:
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))

            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(cuota_pagar)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(round(item.importe_cobrado))))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(saldo)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(str(item.fecha_cobro)))
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
                obj_creditos = N_creditos(1)
                obj_creditos.cancelar_credito(nro_credito)
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText( 'El credito fue cancelado')
                msgBox.exec_()


            control_de_cta=control_de_cta+1


    def buscar_cliente(self):
        self.limpiar()
        numero_dni= self.obj_form.lne_dni.text()
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
            self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido)
            self.obj_form.tw_lista_creditos.setEnabled(True)
            self.obj_form.tw_listado_cuotas.setEnabled(True)

            obj_N_credito = N_creditos(1)
            list_credito_party = obj_N_credito.get_list_credito(obj_party_party.id_party)


            for item in list_credito_party:
                nro_cliente = item.nro_cliente
                fecha_credito = item.fecha_credito
                nro_credito = item.nro_credito
                cantidad_cuotas = item.cantidad_cuotas
                cred_total = item.cred_total
                observaciones = item.observaciones
                estado = item.estado

                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 0, QTableWidgetItem(str(nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 1, QTableWidgetItem(str(nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 2, QTableWidgetItem(str(fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 3, QTableWidgetItem(str(cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 4, QTableWidgetItem(str(cred_total)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 5, QTableWidgetItem(str(estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition , 6, QTableWidgetItem(str(observaciones)))


#app = QApplication(sys.argv)
#dialogo= Cuotas_pagar()
#dialogo.show()
#app.exec_()
