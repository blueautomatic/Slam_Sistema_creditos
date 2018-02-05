import sys, datetime, os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from form_creditos_agregar_nuevos import Ui_form_agregar_nuevos_creditos
from N_cliente import N_datos_personales_cliente, N_party_address,  N_party_garante,N_party_cliente
from N_creditos import N_creditos
from N_cuotas import N_cuotas
from N_cliente import N_garante_credito
from N_egresos import N_egresos
from E_party_party import E_party_party
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from PyQt5.QtWidgets import QFileDialog
import subprocess
from E_configuracion import configuracion
from E_historial_cuota import E_historial_cuota
from PyQt5.QtCore import pyqtRemoveInputHook


class credito_nuevo(QDialog):
    obj_form = Ui_form_agregar_nuevos_creditos()
    id_party = ""
    nro_cliente = ""
    num_doc = ""
    obj_N_creditos = N_creditos(1)
    lista_cuotas = list()
    lista_garantes_credito= list()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_agregar_nuevos_creditos()
        self.obj_form.setupUi(self)
        self.limpiar()
        self.obj_form.boton_buscar_cliente_creditonuevo.clicked.connect(self.buscar_cliente_por_dni)
        self.obj_form.boton_generar_creditonuevo.clicked.connect(self.cuota_de_credito)
        self.obj_form.boton_grabar_creditonuevo.clicked.connect(self.guardar_credito)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar_garante)
        self.obj_form.boton_agregar.clicked.connect(self.agregar)
        self.obj_form.boton_limpiar_creditonuevo.clicked.connect(self.limpiar)
        self.obj_form.boton_imprimir.clicked.connect(self.imprimir)

    def imprimir(self):
        #monto_total_credito_letras = to_word(int(self.obj_form.lne_importe_prestamo_creditonuevo.text()),'EUR')
        #cant_cta_letras = to_word(int(self.obj_form.spbx_cantidad_cuotas_creditonuevo.text()),'EUR')
        obj_E_party = E_party_party()
        obj_asoc = obj_E_party.get_party_party(self.obj_form.lne_nro_doc_creditonuevo.text())
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

       # P=Paragraph("<|b>DNI:  </b>" + obj_asoc.num_doc + " " , otro_estilo)
       # story.append(P)
       # story.append(Spacer(0,5))

        P=Paragraph("<b>Domicilio: </b>" + obj_party_address.domicilio + " ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))

        P=Paragraph("<b>Localidad: </b>" + obj_party_address.ciudad + " ",otro_estilo)
        story.append(P)
        story.append(Spacer(0,5))




        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''',styleSheet["BodyText"])],
                [Paragraph('''<font size=10> <b> N° Cuota</b></font>''',estilo_texto),
                Paragraph('''<font size=10> <b> 1er Venc </b></font>''',estilo_texto),
                Paragraph('''<font size=10> <b> Importe 1er Venc </b></font>''',estilo_texto)]]

        for row in xrange(self.obj_form.tw_lista_cuotas_creditonuevo.rowCount ()):
            nro_cuota = self.obj_form.tw_lista_cuotas_creditonuevo.item(row,0).text()
            capital= self.obj_form.tw_lista_cuotas_creditonuevo.item(row,1).text()
            interes= self.obj_form.tw_lista_cuotas_creditonuevo.item(row,2).text()
            _1er_Venc= self.obj_form.tw_lista_cuotas_creditonuevo.item(row,4).text()
            fec_venc = datetime.datetime.strptime(_1er_Venc, "%Y-%m-%d %H:%M:%S")

            importe_1er_Venc= self.obj_form.tw_lista_cuotas_creditonuevo.item(row,5).text()
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            mes = self.convert_Mes(fec_venc.month)

            estilonom_plan= " <font size=9>" + nro_cuota + "</font>"
            estilodescuento= " <font size=9>" + str(fec_venc.day) + "/ " + mes + " </font>"
            estilointeres= " <font size=9>" + importe_1er_Venc + "</font>"

            integrantes.append([ Paragraph(estilonom_plan,estilo_texto),
                                     Paragraph(estilodescuento,estilo_texto),
                                     Paragraph(estilointeres,estilo_texto)])

            t=Table(integrantes, (175, 175, 175))
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

        file_path = cadena + "/pdf/credito/credito"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc=SimpleDocTemplate(file_path+ "/credito_" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre + ".pdf")
        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Credito")
        msgBox.setText("El Credito se ha generado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/credito_" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre +".pdf"])
        else:
            os.startfile( file_path +"/credito_" +  obj_asoc.apellido+ "_"+ obj_asoc.nombre +".pdf")

        return True



    def limpiar_garante(self):

        while (self.obj_form.tw_garantes_lista_creditonuevo.rowCount() > 0):
            self.obj_form.tw_garantes_lista_creditonuevo.removeRow(0)

        for item in self.lista_garantes_credito:
            self.lista_garantes_credito.remove(item)



    def guardar_credito(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Agrego el Garante al credito?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            obj_creditos = N_creditos("a")
            result = obj_creditos.guardar_credito(self.obj_N_creditos)
            nro_credito =  obj_creditos.buscar_nro_credito_por_party(self.obj_form.lne_nro_creditonuevo_2.text())

            obj_garante_credito = N_garante_credito(1)
            obj_garante_credito.guardar(self.lista_garantes_credito,nro_credito)


            obj_N_cuotas = N_cuotas(1)
            obj_N_cuotas.guardar(self.lista_cuotas, nro_credito)

            obj_histo_cta = E_historial_cuota()
            obj_histo_cta.guardar_historial(nro_credito)

            obj_N_egresos = N_egresos(1)
            obj_N_egresos.guardar_egresos_creditos(self.obj_N_creditos,nro_credito)


            if result :
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msg = 'El credito se grabo correctamente. Nro : ' + str(nro_credito)
                msgBox.setText(msg)
                msgBox.exec_()
                self.obj_form.lne_nro_creditonuevo.setText(str(nro_credito))
                self.limpiar()

    def redondear(self,obj_capital):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        pos = obj_capital.find('.')

        unidad = obj_capital[(pos-1)]
        lista = list(obj_capital)
        result = ""
        if (int(unidad) <= 3):
            lista[(pos-1)] = '0'
        elif (int(unidad) >= 4) :
            lista[(pos-1)] = '5'


        for item in lista:
            if item != '.' :
                result = result + str(item)
            elif item == '.':
                break

        return int(result)
    def cuota_de_credito(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        #self.limpiar()
        result2 = QMessageBox.Yes
        if self.obj_form.spbx_cantidad_cuotas_creditonuevo.text() =='3' or self.obj_form.spbx_cantidad_cuotas_creditonuevo.text() =='4' or self.obj_form.spbx_cantidad_cuotas_creditonuevo.text() =='5':
                if self.obj_form.spbx_tasa_creditonuevo.text() !='11':
                    w = QWidget()
                    result2 = QMessageBox.question(w, 'Alerta', " Se cambio la tasa al 11%?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                else:
                    result2 =QMessageBox.Yes

        if result2 == QMessageBox.Yes :
            self.obj_form.boton_agregar.setEnabled(True)
            numero_capital= self.obj_form.lne_importe_prestamo_creditonuevo.text()
            obj_N_datos_cliente= N_creditos("a")
            if numero_capital == "" :
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText( 'Ingresar nuevamente el capital a prestar')
                msgBox.exec_()
                return False

            if numero_capital != "":
                try:
                   capital = float(numero_capital)
                except:
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Atencion")
                    msgBox.setText( 'Ingresar nuevamente el importe prestamo')
                    msgBox.exec_()
                    return False

                num_doc_cliente = self.obj_form.lne_nro_doc_creditonuevo.text()
                num_credito_nuevo = self.obj_form.lne_nro_creditonuevo.text()
                cantidad_cuotas = self.obj_form.spbx_cantidad_cuotas_creditonuevo.text()
                tasa = self.obj_form.spbx_tasa_creditonuevo.text()

                interes=self.redondear(str((float(capital) * float(tasa))/100))
                obj_capital = str(float(capital) / float(cantidad_cuotas))
                obj_capital=self.redondear(obj_capital)

                obj_n_party_cliente= N_party_cliente(1)
                self.obj_N_creditos.nro_cliente = self.nro_cliente
                self.obj_N_creditos.id_party = self.obj_form.lne_nro_creditonuevo_2.text()
                self.obj_N_creditos.fecha_credito = self.obj_form.dte_fec_creditonuevo.text()
                self.obj_N_creditos.tasa =  self.obj_form.spbx_tasa_creditonuevo.text()
                self.obj_N_creditos.formula = self.obj_form.cbx_formula_creditonuevo.currentText()
                self.obj_N_creditos.importe_prestamo = capital
                self.obj_N_creditos.cantidad_cuotas = cantidad_cuotas
                self.obj_N_creditos.vto_primer_cuota = self.obj_form.dte_vto_primer_cuota_creditonuevo.text()
                self.obj_N_creditos.interes = interes
                self.obj_N_creditos.observaciones = self.obj_form.lne_observaciones_creditonuevo.text()

                obj_credito_total=0
                interes_total=0
                obj_N_cuotas= N_cuotas(1)
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                vencimiento_primer_cuota= self.obj_form.dte_vto_primer_cuota_creditonuevo.text()
                obj_date_venc_1er_cuota = datetime.datetime.strptime(vencimiento_primer_cuota, '%d/%m/%Y')
                gastos = self.calcular_Gastos(int(cantidad_cuotas))
                resultado_gatos= gastos * int(cantidad_cuotas)

                self.obj_N_creditos.gastos = resultado_gatos

                self.obj_form.lne_gastos_creditonuevo.setText(str(resultado_gatos))

                hoy = obj_date_venc_1er_cuota
                contador = 0
                for item in  range(0,int(cantidad_cuotas)):
                    obj_cuotas= N_cuotas(1)
                    #agrego registros en la grillaform_creditos_cuotas_buscar.ui
                    rowPosition = self.obj_form.tw_lista_cuotas_creditonuevo.rowCount()
                    self.obj_form.tw_lista_cuotas_creditonuevo.insertRow(rowPosition)
                    valor_cuota = float(interes) + float(obj_capital) + float(gastos)
                    obj_credito_total= obj_credito_total +  float(interes) + float(obj_capital) + float(gastos)
                    interes_total= interes_total + interes
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    obj_cuotas.nro_cuota = str(item + 1)
                    obj_cuotas.capital = obj_capital
                    obj_cuotas.interes = self.redondear(str(interes))
                    obj_cuotas.gastos = gastos
                    self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 0, QTableWidgetItem(str(obj_cuotas.nro_cuota)))
                    self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 2, QTableWidgetItem(str(self.redondear(str(interes)))))
                    self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 1, QTableWidgetItem(str(obj_capital)))
                    self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 3, QTableWidgetItem(str(gastos)))

                    if contador == 0 :
                        self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem(str(obj_date_venc_1er_cuota)))

                        obj_cuotas.primer_Vencimiento = vencimiento_primer_cuota
                    else:
                        #pyqtRemoveInputHook()
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


                        obj_fecha_cuota= datetime.datetime(nuevo_year, nuevo_mes, nuevo_dia)
                        self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem(str(obj_fecha_cuota)   ))
                        obj_cuotas.primer_Vencimiento = obj_fecha_cuota

                    self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 5, QTableWidgetItem(str(self.redondear(str(valor_cuota)))))          #self.obj_form.tw_lista_cuotas_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem((str(float(capital) / float(tasa)))))
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    obj_cuotas.id_usuario = 1
                    obj_cuotas.estado_cuota ="A pagar"
                    obj_cuotas.importe_cobrado = 0
                    obj_cuotas.importe_primer_vencimiento= self.redondear(str(valor_cuota))
                    contador = contador + 1
                    self.lista_cuotas.append(obj_cuotas)

                self.obj_form.lne_interes_creditonuevo.setText(str(interes_total))
                self.obj_form.lne_credito_total_creditonuevo.setText(str(obj_credito_total))
                self.obj_N_creditos.cred_total = obj_credito_total

    def buscar_cliente_por_dni(self):
        self.limpiar()

        numero_dni= self.obj_form.lne_nro_doc_creditonuevo.text()
        obj_N_datos_cliente= N_creditos("a")
        if numero_dni != "":
            try:
                numero_documento_cliente= int(numero_dni)
            except:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
                msgBox.exec_()
                return False
        elif numero_dni == "" :
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Ingresar nuevamente el numero de documento sin espacios y sin puntos')
            msgBox.exec_()
            return False

        obj_N_datos_personales_cliente = N_datos_personales_cliente()

        obj_party_party=obj_N_datos_personales_cliente.buscar_party_party_por_nro_doc(numero_documento_cliente)

        if obj_party_party != False:
            #self.obj_form.lne_party_party.setText()
            self.id_party = obj_party_party.id_party
            obj_party_cliente= N_party_cliente(1)
            self.nro_cliente = obj_party_cliente.get_nro_cliente(self.id_party)
            obj_N_garante =N_party_garante(1)
            lista_garantes = obj_N_garante.get_list_party_garante(self.nro_cliente)
            for item in lista_garantes:
                obj_party_garante = obj_N_datos_personales_cliente.buscar_party_party_por_id(item.id_party_garante)
                valor = str(item.id_party_garante) + ", " + obj_party_garante.nombre + ", " + obj_party_garante.apellido + ", " + obj_party_garante.nro_doc
                self.obj_form.cbx_garante_creditonuevo.addItem(valor)
                #.append(item)

            self.obj_form.lne_nom_ape.setText(obj_party_party.nombre+ ", " + obj_party_party.apellido)
            self.obj_form.dte_fec_creditonuevo.setDate(datetime.datetime.now())
            self.obj_form.dte_vto_primer_cuota_creditonuevo.setDate(datetime.datetime.now())

            self.id_party= obj_party_party.id_party
            self.obj_form.lne_nro_creditonuevo_2.setText(str(self.id_party))
            obj_party_cliente= N_party_cliente(1)
            self.nro_cliente = obj_party_cliente.get_nro_cliente(self.id_party)
            self.obj_form.lne_nro_creditonuevo.text()
            self.obj_form.dte_fec_creditonuevo.setEnabled(True)
            self.obj_form.cbx_formula_creditonuevo.setEnabled(True)
            self.obj_form.spbx_tasa_creditonuevo.setEnabled(True)
            self.obj_form.lne_nro_creditonuevo.setEnabled(True)
            self.obj_form.lne_importe_prestamo_creditonuevo.setEnabled(True)
            self.obj_form.spbx_cantidad_cuotas_creditonuevo.setEnabled(True)
            self.obj_form.dte_vto_primer_cuota_creditonuevo.setEnabled(True)
            self.obj_form.boton_generar_creditonuevo.setEnabled(True)
            self.obj_form.tw_lista_cuotas_creditonuevo.setEnabled(True)
            self.obj_form.lne_observaciones_creditonuevo.setEnabled(True)
            self.obj_form.lne_interes_creditonuevo.setEnabled(True)
            self.obj_form.lne_gastos_creditonuevo.setEnabled(True)
            self.obj_form.lne_credito_total_creditonuevo.setEnabled(True)
            self.obj_form.boton_grabar_creditonuevo.setEnabled(True)
            self.obj_form.boton_limpiar_creditonuevo.setEnabled(True)
        else:
            self.obj_form.dte_fec_creditonuevo.setEnabled(False)
            self.obj_form.lne_nro_creditonuevo.setEnabled(False)
            self.obj_form.cbx_formula_creditonuevo.setEnabled(False)
            self.obj_form.spbx_tasa_creditonuevo.setEnabled(False)
            self.obj_form.lne_importe_prestamo_creditonuevo.setEnabled(False)
            self.obj_form.spbx_cantidad_cuotas_creditonuevo.setEnabled(False)
            self.obj_form.dte_vto_primer_cuota_creditonuevo.setEnabled(False)
            self.obj_form.boton_generar_creditonuevo.setEnabled(False)
            self.obj_form.tw_lista_cuotas_creditonuevo.setEnabled(False)
            self.obj_form.lne_observaciones_creditonuevo.setEnabled(False)
            self.obj_form.lne_interes_creditonuevo.setEnabled(False)
            self.obj_form.lne_gastos_creditonuevo.setEnabled(False)
            self.obj_form.lne_credito_total_creditonuevo.setEnabled(False)
            self.obj_form.boton_grabar_creditonuevo.setEnabled(False)
            self.obj_form.boton_limpiar_creditonuevo.setEnabled(False)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Error numero de DNI inexistente')
            msgBox.exec_()

    def calcular_Gastos(self, cant_cuotas):
        if (cant_cuotas >= 3) and (cant_cuotas <= 5):
            gastos =80
        elif (cant_cuotas == 6):
            gastos =62
        elif (cant_cuotas == 7):
            gastos = 42
        elif (cant_cuotas >= 8) and (cant_cuotas <= 12):
            gastos = 25
        elif (cant_cuotas >= 13) and (cant_cuotas <= 15):
            gastos = 15
        elif (cant_cuotas >= 16) and (cant_cuotas <= 18):
            gastos = 5
        elif (cant_cuotas >= 19):
            gastos = 0

        return gastos

    def agregar(self):
        obj_garante_credito = N_garante_credito(1)
        garante_creditonuevo = self.obj_form.cbx_garante_creditonuevo.currentText()
        pos = garante_creditonuevo.find(',')

        datos_garante = garante_creditonuevo.split(",")
        id_party_garante = garante_creditonuevo[:pos]
        obj_garante_credito.id_party_garante = id_party_garante
        obj_garante_credito.tipo_garante = self.obj_form.cbx_tipo_garante_creditonuevo.currentText()

        self.lista_garantes_credito.append(obj_garante_credito)

        rowPosition = self.obj_form.tw_garantes_lista_creditonuevo.rowCount()
        self.obj_form.tw_garantes_lista_creditonuevo.insertRow(rowPosition)
        self.obj_form.tw_garantes_lista_creditonuevo.setItem(rowPosition , 0, QTableWidgetItem(id_party_garante))
        self.obj_form.tw_garantes_lista_creditonuevo.setItem(rowPosition , 1, QTableWidgetItem(datos_garante[1]))
        self.obj_form.tw_garantes_lista_creditonuevo.setItem(rowPosition , 2, QTableWidgetItem(datos_garante[2]))
        self.obj_form.tw_garantes_lista_creditonuevo.setItem(rowPosition , 3, QTableWidgetItem(datos_garante[3]))
        self.obj_form.tw_garantes_lista_creditonuevo.setItem(rowPosition , 4, QTableWidgetItem(self.obj_form.cbx_tipo_garante_creditonuevo.currentText()))

    def convert_Mes(self, nro_mes):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        mes=""
        if (nro_mes == 1):
            mes = "enero"
        elif (nro_mes == 2):
            mes = "febrero"
        elif (nro_mes == 3):
            mes="marzo"
        elif (nro_mes == 4):
            mes="abril"
        elif (nro_mes ==5) :
            mes = "abril"
        elif (nro_mes == 6):
            mes = "mayo"
        elif (nro_mes == 7):
            mes = "junio"
        elif (nro_mes == 8):
            mes = "julio"
        elif (nro_mes == 9):
            mes = "agosto"
        elif (nro_mes == 10):
            mes = "octubre"
        elif (nro_mes ==11):
            mes = "noviembre"
        elif (nro_mes ==12):
            mes = "diciembre"

        return mes

    def limpiar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()


        while (self.obj_form.tw_lista_cuotas_creditonuevo.rowCount() > 0):
            self.obj_form.tw_lista_cuotas_creditonuevo.removeRow(0)

            for item in self.lista_cuotas:
                self.lista_cuotas.remove(item)
        self.obj_form.lne_party_party.setText("")
        self.limpiar_garante()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in range(self.obj_form.cbx_garante_creditonuevo.count()) :
            self.obj_form.cbx_garante_creditonuevo.removeItem(item)



#app = QApplication(sys.argv)
#dialogo= credito_nuevo()
#dialogo.show()
#app.exec_()
