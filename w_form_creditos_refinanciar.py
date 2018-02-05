import sys,datetime,os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem, QFileDialog
from PyQt5 import uic
from form_creditos_refinanciar import Ui_form_creditos_refinanciar
from N_creditos import N_creditos
from N_cliente import N_datos_personales_cliente,N_party_address
from N_cuotas import N_cuotas
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cuotas import E_cuotas
from E_party_party import E_party_party
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from E_configuracion import configuracion
from E_historial_cuota import E_historial_cuota


class creditos_refinanciar(QDialog):
    obj_form= Ui_form_creditos_refinanciar()
    nro_credito_historial=0
    lst_ord_cta=list()
    lista_cta_modificadas=list()
    lista_cta_nuevas=list()
    obj_cta_modificadas= E_cuotas(1)
    id_party=""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_creditos_refinanciar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_agregar.clicked.connect(self.agregar)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        self.obj_form.boton_imprimir.clicked.connect(self.imprimir)
        #self.obj_form.boton_actualizar.clicked.connect(self.actualizar)

    def limpiar(self):
        a=1


    def agregar(self):
        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        cant_cta=int(self.obj_form.cant_cuotas.text())

        estado_cuota= "A pagar"
        obj_e_cta = E_cuotas(1)
        obj_cta_max = obj_e_cta.get_max_cta(self.nro_credito_historial)
        nro_cuota =obj_cta_max

        primerVencimiento = self.obj_form.dte_primer_venc.text()
        obj_date_venc_1er_cuota = datetime.datetime.strptime(primerVencimiento, '%d/%m/%y')

        contador = 0
        valor_cta =self.obj_form.lne_monto.text()
        hoy=obj_date_venc_1er_cuota
        nro_credito=0
        for item in self.lst_ord_cta:
            nro_credito = item.nro_credito
            if item.estado_cuota == "Pagada":
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
            else:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
                self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str("A pagar")))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(item.capital)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 11, QTableWidgetItem(str(0)))
                if contador == 0 :
                    fec_1= obj_date_venc_1er_cuota
                    nuevo_mes = fec_1.month
                    nuevo_year = fec_1.year
                    nuevo_dia = 5
                    fec= str(nuevo_year)+"-"+ str(nuevo_mes)+"-" +str(nuevo_dia)
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(fec))


                    vencimiento2 =str(nuevo_year) +"/"+ str(nuevo_mes) +"/"+str(nuevo_dia)
                    self.obj_cta_modificadas.primerVencimiento = vencimiento2
                else:

                    nuevo_mes = hoy.month + contador
                    nuevo_year = hoy.year
                    nuevo_dia = 5
                    if nuevo_mes > 12 and nuevo_mes < 25:
                        nuevo_mes = nuevo_mes % 12
                        if nuevo_mes == 0:
                            nuevo_mes=12
                        nuevo_year += 1
                    elif nuevo_mes > 24 and nuevo_mes < 37:
                        nuevo_mes = nuevo_mes % 12
                        if nuevo_mes == 0:
                            nuevo_mes=12
                        nuevo_year += 2

                    fec= str(nuevo_year)+"-"+ str(nuevo_mes)+"-" +str(nuevo_dia)
                    vencimiento1 =str(nuevo_year) +"/"+ str(nuevo_mes) +"/"+str(nuevo_dia)
                    self.obj_cta_modificadas.primerVencimiento=vencimiento1
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(fec)))


                    #self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_Vencimiento)[:10]))

                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(valor_cta)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(0)))
                if item.fecha_cobro != None :
                    self.obj_form.tw_listado_cuotas.setItem(rowPosition ,9 , QTableWidgetItem(str("")))
                else:

                    self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))
                #obj_cta_modificadas.fecha_cobro = None
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(0)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(valor_cta)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(0)))
                #obj_cta_modificadas.importe_cobrado = valor_cta
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(valor_cta)))

                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(0)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 12, QTableWidgetItem(str(0)))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 13, QTableWidgetItem(str("refinanciado")))
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 14, QTableWidgetItem(str(item.id)))
                contador = contador + 1
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.obj_cta_modificadas.id = item.id
                self.obj_cta_modificadas.estado_cuota="A pagar"
                self.obj_cta_modificadas.nro_cuota = item.nro_cuota
                self.obj_cta_modificadas.capital= valor_cta
                self.obj_cta_modificadas.interes = 0
                self.obj_cta_modificadas.importe_cuota = valor_cta
                self.obj_cta_modificadas.punitorios = 0
                self.obj_cta_modificadas.descuento = 0
                self.obj_cta_modificadas.importe_cobrado = 0
                self.obj_cta_modificadas.gastos = 0
                self.obj_cta_modificadas.descripcion = "refinanciado"
                self.obj_cta_modificadas.importe_primer_venc = valor_cta
                obj_e_ctas= E_cuotas(1)
                obj_e_ctas.actualizar_refinanciacion(self.obj_cta_modificadas)
                #self.lista_cta_modificadas.append(self.obj_cta_modificadas)

                obj_hist = E_historial_cuota()
                obj_hist.nro_credito = nro_credito
                obj_hist.nro_cuota = item.nro_cuota
                obj_hist.estado_cuota = "A pagar"
                obj_hist.descripcion = " Se refinancio"
                obj_hist.id_cuota = item.id
                obj_hist.guardar(obj_hist)


        obj_cta_nuevas = E_cuotas(1)
        for item in range(0,cant_cta) :
            nro_cuota = nro_cuota + 1

            #saldo= round(float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios)  - float(item.importe_cobrado),2)  - round(float(item.descuento),2)
            #cuota_pagar = float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios) - float(item.descuento)
            rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
            self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(estado_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(nro_cuota)))
            obj_cta_nuevas.nro_cuota = nro_cuota

            if contador == 0 :
                fec= str(nuevo_year)+"/"+ str(nuevo_mes)+"/" +str(nuevo_dia)
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(fec))
                obj_cta_nuevas.primerVencimiento = fec
            else:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                nuevo_mes = hoy.month + contador
                nuevo_year = hoy.year
                nuevo_dia = 5
                if nuevo_mes > 12 and nuevo_mes < 25:
                    nuevo_mes = nuevo_mes % 12
                    if nuevo_mes == 0:
                        nuevo_mes=12
                    nuevo_year += 1
                elif nuevo_mes > 24 and nuevo_mes < 37:
                    nuevo_mes = nuevo_mes % 12
                    if nuevo_mes == 0:
                        nuevo_mes=12
                    nuevo_year += 2

                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                #obj_fecha_cuota= datetime.datetime(nuevo_year, nuevo_mes, nuevo_dia)
                fec= str(nuevo_year)+"/"+ str(nuevo_mes)+"/" +str(nuevo_dia)
                self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(fec)))
                obj_cta_nuevas.primerVencimiento = fec

            contador = contador + 1

            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 3, QTableWidgetItem(str(valor_cta)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 4, QTableWidgetItem(str(round(0))))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 5, QTableWidgetItem(str(0)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 6, QTableWidgetItem(str(valor_cta)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 7, QTableWidgetItem(str(0)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 8, QTableWidgetItem(str(valor_cta)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 9, QTableWidgetItem(""))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 10, QTableWidgetItem(str(0)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 11, QTableWidgetItem(str(valor_cta)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 12, QTableWidgetItem(str(0)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 13, QTableWidgetItem("refinanciada"))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 14, QTableWidgetItem(str(0)))

            #obj_cta_nuevas.nro_credito = self.nro_credito_historial
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_cta_nuevas.estado_cuota="A pagar"
            obj_cta_nuevas.capital= valor_cta
            obj_cta_nuevas.interes = 0
            obj_cta_nuevas.importe_cuota = valor_cta
            obj_cta_nuevas.punitorios = 0
            obj_cta_nuevas.descuento = 0
            obj_cta_nuevas.importe_cobrado = 0
            obj_cta_nuevas.gastos = 0
            obj_cta_nuevas.descripcion = "refinanciado"
            obj_cta_nuevas.importe_primer_venc = valor_cta
            obj_e_cta_nuevas = E_cuotas(1)
            obj_e_ctas.guardar_refinanciacion(obj_cta_nuevas,self.nro_credito_historial)


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
            self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido + "   DNI:" +  obj_party_party.num_doc)
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

    def seleccion_item_tabla_creditos(self,clickedIndex):

        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        twi0 = self.obj_form.tw_lista_creditos.item(clickedIndex,0)
        nro_credito = twi0.text()
        self.nro_credito_historial= int(twi0.text())
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

        self.lst_ord_cta = [ (i.nro_cuota, i) for i in lista_cuotas ]
        self.lst_ord_cta.sort()
        self.lst_ord_cta = [ i[1] for i in self.lst_ord_cta ]
        for item in self.lst_ord_cta:
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

    def imprimir(self):

        obj_E_party = E_party_party()
        obj_asoc = obj_E_party.get_party_party(self.obj_form.lne_dni.text())
        obj_N_party_address =N_party_address("a")
        obj_party_address =obj_N_party_address.get_party_address(obj_asoc.id_party)

        fec_hoy= datetime.date.today()
        hoy = fec_hoy.strftime("%d/%m/%Y")

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



        P=Paragraph("<b>Sr/a: </b>"  + obj_asoc.apellido+ " "+ obj_asoc.nombre  + " ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>DNI:  </b>" + obj_asoc.num_doc + "",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Domicilio: </b>" + obj_party_address.domicilio + " ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Localidad: </b>" + obj_party_address.ciudad + " ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))


        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''',styleSheet["BodyText"])],
                [Paragraph('''<font size=10> <b> N° Cuota</b></font>''',estilo_texto),
                Paragraph('''<font size=10> <b> 1er Venc </b></font>''',estilo_texto),
                Paragraph('''<font size=10> <b> Pesos </b></font>''',estilo_texto),
                Paragraph('''<font size=10> <b> Estado </b></font>''',estilo_texto)]]



        for row in xrange(self.obj_form.tw_listado_cuotas.rowCount ()):

            estado = self.obj_form.tw_listado_cuotas.item(row,0).text()
            nro_cuota = self.obj_form.tw_listado_cuotas.item(row,1).text()
            fec_venc= self.obj_form.tw_listado_cuotas.item(row,2).text()
            importe_cta = self.obj_form.tw_listado_cuotas.item(row,3).text()
            #descripcion = self.obj_form.tw_listado_cuotas.item(row,13).text()

            estilonom_plan= " <font size=9>" + nro_cuota + "</font>"
            #estilodescuento= " <font size=9>" + str(fec_venc.strftime("%d/%m/%Y"))+ " </font>"
            estilodescuento= " <font size=9>" + str(fec_venc)+ " </font>"
            estilointeres= " <font size=9>" + str(importe_cta) + "</font>"
            estilodescripcion= " <font size=9>" + estado + "</font>"

            integrantes.append([ Paragraph(estilonom_plan,estilo_texto),
                                     Paragraph(estilodescuento,estilo_texto),
                                     Paragraph(estilointeres,estilo_texto),
                                     Paragraph(estilodescripcion,estilo_texto)])

            t=Table(integrantes, (80, 80, 80,80))
            t.setStyle(TableStyle([
                                        ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                           ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                           ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                           ]))


        story.append(t)
        story.append(Spacer(0,25))
        P=Paragraph("*** Informamos que ante el pago fuera de término, la empresa aplicará interés por mora***",style_barra)
        story.append(P)

        #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/credito/refinanciacion"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc=SimpleDocTemplate(file_path+ "/refinanciacion" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre + ".pdf")
        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Credito")
        msgBox.setText("El Credito refinanciado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/credito_" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre +".pdf"])
        else:
            os.startfile( file_path +"/credito_" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre +".pdf")

        return True
