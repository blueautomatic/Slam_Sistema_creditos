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
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Frame
from reportlab.platypus import Paragraph, Image
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
from reportlab.lib.units import mm
from E_party_cliente import E_party_cliente
from convert_nro_letra import hundreds_word, __convert_group, to_word


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
    cant_cta=0
    vencimiento_cta=""
    nro_credito_historial2 = 0

    def __init__(self,singleton,singleton_idusu):
        QDialog.__init__(self)
        obj_form= Ui_form_cuotas_pagar()
        self.obj_form.setupUi(self)
        self.limpiar()
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        self.obj_form.tw_listado_cuotas.cellClicked.connect(self.seleccion_item_tabla)
        self.obj_form.boton_pagar.clicked.connect(self.pagar_cuota)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)
        self.singleton= singleton
        self.singleton_idusu = singleton_idusu
        self.obj_form.boton_ticket.clicked.connect(self.ticket)
        self.obj_form.boton_historial_cuota.clicked.connect(self.historial_cuota)

    def historial_cuota(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        self.obj_form_cta_hist = Cuota_historial(self.id_cuota_historial)
        #obj_form_cta_hist.show()
        self.obj_form_cta_hist.show()

    def ticket(self):

        monto_ticket = 0
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
        fec_hoy = datetime.date.today()
        hoy = fec_hoy.strftime("%d/%m/%Y")
        obj_e_party_cliente = E_party_cliente()
        obj_party_cliente = obj_e_party_cliente.get_party_cliente(obj_asoc.id_party)

        styleSheet = getSampleStyleSheet()
        otro_estilo = ParagraphStyle('', fontSize=6, textColor='#000', leftIndent=0, rightIndent=100)

        style_barra = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=200, rightIndent=1)
        estilo_texto = ParagraphStyle('',
                                      fontSize=5,
                                      alignment=0,
                                      spaceBefore=0,
                                      spaceAfter=0,
                                      # backColor = '#fff',
                                      textColor='#000',
                                      leftIndent=5)
        estilo_detalle_cuota = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=0)

        options = QFileDialog.Options()
        story = []

        nro_credito = self.nro_credito_historial
        nro_credito2 = self.nro_credito_historial2
        encabezado = [[Paragraph('''<font size=10> <b> </b></font>''', styleSheet["BodyText"])],
                      [Paragraph('<font size=10> <b> </b>Crédito N°: <b>' + str(nro_credito2) + '</b> </font>',
                                 estilo_texto),
                       Paragraph('<font size=10> <b> </b>RECIBO N°: ' + str(nro_ticket) + '</font>', estilo_texto),
                       Paragraph('<font size=10> Fecha: ' + str(hoy) + '</font>', estilo_texto)]]

        t = Table(encabezado, (185, 185, 185))
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
            ('BACKGROUND', (0, 1), (-1, 1), colors.white)
        ]))

        story.append(t)
        story.append(Spacer(0, -15))

        cabezal = [[Paragraph('<font size=10> <b> </b></font>', styleSheet["BodyText"])],
                   [Paragraph('<font size=10> <b> Cliente N°: </b> ' + str(obj_party_cliente.nro_cliente) + '</font>',
                              estilo_texto),
                    Paragraph('<font size=10>' + obj_asoc.apellido + ", " + obj_asoc.nombre + ' </font>',
                              estilo_texto)]]

        # cabezal =[[Paragraph('font size=8> <b> </b></font>',styleSheet["BodyText"])],
        #           [Paragraph('<font size=8> <b> Cliente N°: 61 </font>',estilo_texto),
        #           Paragraph('<font size=10> <b>  CHAZARRETA, GUSTAVO ANDRÉS </b> </font>',estilo_texto)]]

        t = Table(cabezal, (277, 278))
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
            ('BACKGROUND', (0, 1), (-1, 1), colors.white)
        ]))
        story.append(t)
        story.append(Spacer(-10, -15))

        # a = ("%.2f" % monto_ticket)

        importe = float(self.obj_form.lne_importe_cuota.text()) + float(self.obj_form.lne_punitorios.text()) - float(self.obj_form.lne_descuento.text())
        self.obj_form.lne_importe_cobrar.setText(str(importe))

        cuadro_detalle_cta = [[Paragraph('<font size=8> <b> </b></font>', styleSheet["BodyText"])],
                              [Paragraph('<font size=8> </font>', estilo_texto),
                               Paragraph(
                                   '<font size=10>  Importe Cuota:<br/>Interés por Mora:<br/> Otros: <br/>Descuento:</font>',
                                   estilo_texto),
                               Paragraph(
                                   '<font size=10> $' + self.obj_form.lne_importe_cuota.text() + ' <br/> $' + self.obj_form.lne_punitorios.text() + ' <br/> $' + "" + '<br/> $' + self.obj_form.lne_descuento.text() + '</font>',
                                   estilo_texto)]]

        estilonom_plan = " <font size=8> </font>"
        # colocar donde dice 64545 el importe total
        estilonro_cta = '<font size=8>$' + self.obj_form.lne_importe_cobrar.text() + '</font>'
        estilointeres = " <font size=8>TOTAL: </font>"

        cuadro_detalle_cta.append([Paragraph(estilonom_plan, estilo_texto),
                                   Paragraph(estilointeres, estilo_texto),
                                   Paragraph(estilonro_cta, estilo_texto)])

        t = Table(cuadro_detalle_cta, (305, 125, 125))
        # El SPAN unifica celdas (los pares ordenados son: [(0,0),(1,0),(2,0)
        #                                                 (0,1,),(1,1),(2,1)
        #                                                 (0,2),(1,2),(2,2)]
        # En este caso se unificó:(0,1),(0,2)
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
            ('BACKGROUND', (0, 1), (-1, 1), colors.white),
            ('SPAN', (0, 1), (0, 2)),
        ]))
        story.append(t)
        story.append(Spacer(-10, -5))
        monto_total_cta_letras = to_word(float(self.obj_form.lne_importe_cobrar.text()), 'EUR')
        # pyqtRemoveInputHook()
        # import pdb; pdb.set_trace()
        prox_fec_venc = datetime.datetime.strptime(self.vencimiento_cta, '%Y-%m-%d').date()

        if prox_fec_venc.month == 12:
            cadena = '  <br/> <u>   Su próxima cuota vence el:  <b>' + str(prox_fec_venc.day) + "/" + str(1) + "/" + str(prox_fec_venc.year + 1) + ' </b></u><br/>'
        else:
            cadena = '  <br/> <u>   Su próxima cuota vence el:  <b>' + str(prox_fec_venc.day) + "/" + str(prox_fec_venc.month + 1) + "/" + str(prox_fec_venc.year) + ' </b></u><br/>'

        if str(self.cant_cta) != self.obj_form.lne_nro_cuota.text():
            leyenda = [[Paragraph('''<font size=10> <b> </b></font>''', styleSheet["BodyText"])],
                       [Paragraph(
                           '<font size=10> <br/> Recibimos conformes la suma de: $' + self.obj_form.lne_importe_cobrar.text() + ' <br/> Son: ' + monto_total_cta_letras + ' Pesos <br/>' +
                           '<br/> En concepto de cuota N°: ' + self.obj_form.lne_nro_cuota.text() + ' de ' + str(
                               self.cant_cta) + ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Venc.: ' + str(prox_fec_venc.day) + "/" + str(
                               prox_fec_venc.month) + "/" + str(prox_fec_venc.year) + cadena +
                           '<u>  Duplicado </u>     <br/>  Firma Responsable</font>', estilo_texto)]]
            t = Table(leyenda, (555))
            t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
            story.append(t)
            story.append(Spacer(0, -15))
        # pyqtRemoveInputHook()
        # import pdb; pdb.set_trace()

        if str(self.cant_cta) == self.obj_form.lne_nro_cuota.text():
            leyenda = [[Paragraph('''<font size=10> <b> </b></font>''', styleSheet["BodyText"])],
                       [Paragraph(
                           '<font size=10> <br/> Recibimos conformes la suma de : $' + self.obj_form.lne_importe_cobrar.text() + ' <br/> Son: ' + monto_total_cta_letras + ' Pesos <br/>' +
                           '<br/> En concepto de cuota N°: ' + self.obj_form.lne_nro_cuota.text() + ' de ' + str(
                               self.cant_cta) + ' Venc.: ' + str(self.vencimiento_cta) +
                           '  <br/> <u>   Su próxima cuota vence el:  <b>  CANCELADO </b></u><br/>' +
                           '<u>  Duplicado </u>     <br/>  Firma Responsable</font>', estilo_texto)]]
            t = Table(leyenda, (555))
            t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
            story.append(t)
            story.append(Spacer(0, -15))

        # ---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#

        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/ticket/ticket" + str(datetime.date.today().year) + "_" + str(
            datetime.date.today().month)
        # ---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc = SimpleDocTemplate(file_path + "/ticket" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf", pagesize=A4,
                                rightMargin=14, leftMargin=14, topMargin=5, bottomMargin=18)
        doc.build(story)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Ticket")
        msgBox.setText("El ticket se ha generado correctamente : ticket" + obj_asoc.apellido + "_" + obj_asoc.nombre)
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path + "/ticket" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf"])
        else:
            os.startfile(file_path + "/ticket" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf")

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
        self.vencimiento_cta = self.vencimiento_historial.text()


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
        #//ACLARACIÓN: twi0 y twi10 estan cruzados porque se agregó nueva columna crédito2
        twi0 = self.obj_form.tw_lista_creditos.item(clickedIndex,10)
        twi10 = self.obj_form.tw_lista_creditos.item(clickedIndex,0)
        nro_credito = twi0.text()


        self.nro_credito_historial= int(twi0.text())
        self.nro_credito_historial2 = int(twi10.text())
        cant_ctas= self.obj_form.tw_lista_creditos.item(clickedIndex,3)
        self.cant_cta = int(cant_ctas.text())
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

        lst_ord = [ (i.nro_cuota, i) for i in lista_cuotas ]
        lst_ord.sort()
        lst_ord = [ i[1] for i in lst_ord ]
        for item in lst_ord:
            #saldo = item.importe_cuota
            saldo = float(item.importe_cuota) + float(item.punitorios) - float(item.descuento) - float(item.importe_cobrado)
            cuota_pagar = float(item.importe_cuota) + float(item.punitorios) - float(item.descuento) - float(item.importe_cobrado)
            #cuota_pagar = item.importe_cuota
            rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
            self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            #☻self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)[:10]))
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
            self.obj_form.tw_listado_cuotas.setItem(rowPosition, 15, QTableWidgetItem(str(item.nro_credito)))

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
            obj_cuotas.importe_cobrado = float(self.obj_form.lne_importe_cobrar.text()) + self.importe_cobrado
            obj_cuotas.interes = float(self.obj_form.lne_interes.text())
            obj_cuotas.punitorios = float(self.obj_form.lne_punitorios.text())
            obj_cuotas.gastos = float(self.obj_form.lne_gastos.text())
            obj_cuotas.descripcion = self.obj_form.lne_descripcion.text()
            obj_cuotas.descuento = self.obj_form.lne_descuento.text()
            obj_cuotas.nro_credito = int(self.obj_form.tw_listado_cuotas.item(self.clickedIndex_pagar,15).text())

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            if self.obj_form.cbx_estado.currentText() == "Pagada":
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                if obj_cuotas.nro_cuota == '1' :
                    resultado = float(float (self.importe_apagar) - float(self.obj_form.lne_importe_cobrar.text()) - float(self.obj_form.lne_descuento.text()))
                    if resultado > 0.0:
                        msgBox = QMessageBox()
                        msgBox.setWindowTitle("Error")
                        msgBox.setText( 'Actualizar el estado de la cuota a Pago Parcial. No se modifico el saldo')
                        msgBox.exec_()
                        return False
                else :
                    resultado = float(float (self.importe_apagar) - float(self.obj_form.lne_importe_cobrar.text()) - float(self.obj_form.lne_descuento.text()))
                    if resultado > 0.0:
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
            obj_hist_cuota.importe_cobrado= float(self.obj_form.lne_importe_cobrar.text())
            obj_hist_cuota.descripcion= self.obj_form.lne_descripcion.text()
            obj_hist_cuota.importe_cuota= self.obj_form.lne_importe_cuota.text()
            obj_hist_cuota.write_uid= self.singleton_idusu.idusu
            obj_hist_cuota.primer_Vencimiento= self.vencimiento_historial.text()
            obj_hist_cuota.id_cuota = self.id_cuota_historial

            obj_E_hist_cuota= E_historial_cuota()
            obj_E_hist_cuota.guardar(obj_hist_cuota)

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_cuotas.nro_credito = self.nro_credito_historial
            obj_cuotas.importe_primer_venc = self.obj_form.lne_importe_cuota.text()
            obj_cuotas.primer_Vencimiento = self.vencimiento_historial.text()
            obj_cuotas.importe_cobrado =  float(self.obj_form.lne_importe_cobrar.text())
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
                saldo = float(item.importe_cuota) + float(item.punitorios) - float(item.descuento) - float(item.importe_cobrado)
                cuota_pagar = float(item.importe_cuota) + float(item.punitorios) - float(item.descuento) - float(item.importe_cobrado)
                rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
                self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)[:10]))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(item.importe_cuota)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(item.punitorios,2))))
                if item.fecha_cobro != None :
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(str(item.fecha_cobro)[:10]))
                else:
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))

                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(item.descuento)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(cuota_pagar)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(item.importe_cobrado)))
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
        try:
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
                self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido + "   DNI:" +  obj_party_party.num_doc)
                self.obj_form.tw_lista_creditos.setEnabled(True)
                self.obj_form.tw_listado_cuotas.setEnabled(True)

                obj_N_credito = N_creditos(1)
                list_credito_party = obj_N_credito.get_list_credito(obj_party_party.id_party)


                for item in list_credito_party:
                    nro_cliente = item.nro_cliente
                    fecha_credito = item.fecha_credito
                    nro_credito = item.nro_credito2
                    cantidad_cuotas = item.cantidad_cuotas
                    importe_prestamo = item.importe_prestamo
                    observaciones = item.observaciones
                    estado = item.estado
                    formula = item.formula

                    rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                    self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 0, QTableWidgetItem(str(nro_credito)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 1, QTableWidgetItem(str(nro_cliente)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 2, QTableWidgetItem(str(fecha_credito)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 3, QTableWidgetItem(str(cantidad_cuotas)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 4, QTableWidgetItem(str(importe_prestamo)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 5, QTableWidgetItem(str(estado)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 6, QTableWidgetItem(str(formula)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 7, QTableWidgetItem(str(observaciones)))
                    self.obj_form.tw_lista_creditos.setItem(rowPosition , 10, QTableWidgetItem(str(item.nro_credito)))
            else:
                QMessageBox.information(self, "Atención", "Número de DNI incorrecto.")
        except:
            QMessageBox.information(self, "Atención", "Debe ingresar un número de DNI para realizar la búsqueda.")


#app = QApplication(sys.argv)
#dialogo= Cuotas_pagar()
#dialogo.show()
#app.exec_()
