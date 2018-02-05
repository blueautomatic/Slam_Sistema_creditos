import sys,datetime,os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QFileDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import uic
from form_creditos_cuotas_buscar import Ui_form_creditos_cuotas_buscar
from N_cliente import N_datos_personales_cliente, N_party_address, N_party_otros, N_datos_laborales, N_party_garante,N_party_cliente,N_party_contacto
from N_creditos import N_creditos
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from N_cuotas import N_cuotas
from E_party_party import E_party_party
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
import subprocess
from E_configuracion import configuracion

class creditos_cuotas_buscar(QDialog):
    obj_form= Ui_form_creditos_cuotas_buscar()
    id_party = ""
    id_cuota = 0
    nro_cuota = 0
    importe_apagar = 0
    importe_cobrado = 0
    list_importe_cuota = list()
    total_cuotas=0
    singleton =""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_creditos_cuotas_buscar()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar_creditos.clicked.connect(self.buscar_cliente)
        self.obj_form.tw_lista_creditos.cellClicked.connect(self.seleccion_item_tabla_creditos)
        #self.obj_form.tw_listado_cuotas.cellClicked.connect(self.seleccion_item_tabla)
        #self.obj_form.boton_pagar.clicked.connect(self.pagar_cuota)
        self.obj_form.boton_limpiar.clicked.connect(self.limpiar)
        self.obj_form.boton_imprimir.clicked.connect(self.imprimir)
        self.obj_form.lne_dni.setFocus()

    def imprimir(self):
        obj_E_party = E_party_party()
        obj_asoc = obj_E_party.get_party_party(self.obj_form.lne_dni.text())
        obj_N_party_address = N_party_address("a")
        obj_party_address = obj_N_party_address.get_party_address(obj_asoc.id_party)

        fec_hoy = datetime.date.today()
        hoy = fec_hoy.strftime("%d/%m/%Y")

        styleSheet = getSampleStyleSheet()
        img = Image("cabezalcaida.png", 100, 25)
        img.hAlign = "RIGHT"
        otro_estilo = ParagraphStyle('', fontSize=9, textColor='#000', leftIndent=-44, rightIndent=150)
        fec_estilo = ParagraphStyle('', fontSize=9, textColor='#000', leftIndent=360, rightIndent=0)
        style_barra = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=10)
        texto_principal = ""
        estilo_texto = ParagraphStyle('',
                                      fontSize=5,
                                      alignment=0,
                                      spaceBefore=0,
                                      spaceAfter=0,
                                      # backColor = '#fff',
                                      textColor='#000',
                                      leftIndent=5)

        h = Paragraph(texto_principal, estilo_texto)
        banner = [[img, h]]
        options = QFileDialog.Options()
        story = []
        ban = Table(banner, colWidths=270, rowHeights=-25)
        story.append(ban)
        story.append(Spacer(0, 25))

        P = Paragraph("<b> Fecha:  </b>" + str(hoy) + "", fec_estilo)
        story.append(P)
        story.append(Spacer(0, 5))

        P = Paragraph("<b>Sr/a: </b>" + obj_asoc.apellido + " " + obj_asoc.nombre + " ", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 5))

        P = Paragraph("<b>DNI:  </b>" + obj_asoc.num_doc + "", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 5))

        P = Paragraph("<b>Domicilio: </b>" + obj_party_address.domicilio + " ", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 5))

        P = Paragraph("<b>Localidad: </b>" + obj_party_address.ciudad + " ", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 5))

        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''', styleSheet["BodyText"])],
                       [Paragraph('''<font size=10> <b> N° Cuota</b></font>''', estilo_texto),
                        Paragraph('''<font size=10> <b> 1er Venc </b></font>''', estilo_texto),
                        Paragraph('''<font size=10> <b> Importe 1er Venc </b></font>''', estilo_texto)]]

        for row in xrange(self.obj_form.tw_listado_cuotas.rowCount()):
            nro_cuota = self.obj_form.tw_listado_cuotas.item(row, 2).text()
            #capital = self.obj_form.tw_listado_cuotas.item(row, 1).text()
            #interes = self.obj_form.tw_listado_cuotas.item(row, 2).text()
            _1er_Venc = self.obj_form.tw_listado_cuotas.item(row, 5).text()
            #fec_venc = datetime.datetime.strptime(_1er_Venc, "%Y-%m-%d %H:%M:%S")
            estado = self.obj_form.tw_listado_cuotas.item(row, 0).text()
            importe_1er_Venc = self.obj_form.tw_listado_cuotas.item(row, 5).text()
            estilonom_plan = " <font size=9>" + nro_cuota + "</font>"
            #estilodescuento = " <font size=9>" + str(fec_venc.strftime("%d/%m/%Y")) + " </font>"
            estilofecha = " <font size=9>" + str(_1er_Venc) + " </font>"

            estilointeres = " <font size=9>" + importe_1er_Venc + "</font>"
            estiloestado = " <font size=9>" + estado + "</font>"

            integrantes.append([Paragraph(estilonom_plan, estilo_texto),
                                Paragraph(estilofecha, estilo_texto),
                                Paragraph(estilointeres, estilo_texto),
                                Paragraph(estiloestado, estilo_texto)])

            t = Table(integrantes, (150, 150, 150,120))
            t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey)
            ]))

        story.append(t)
        story.append(Spacer(0, 25))
        P = Paragraph("*** Informamos que ante el pago fuera de término, la empresa aplicará interés por mora***",
                      style_barra)
        story.append(P)

        # ---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        # pyqtRemoveInputHook()
        # import pdb; pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/credito/resumen" + str(datetime.date.today().year) + "_" + str(
            datetime.date.today().month)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc = SimpleDocTemplate(file_path + "/resumen_" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf")
        doc.build(story)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Credito")
        msgBox.setText("El Resumen del Credito se ha generado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path + "/resumen_" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf"])
        else:
            os.startfile(file_path + "/resumen_" + obj_asoc.apellido + "_" + obj_asoc.nombre + ".pdf")

        return True

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



    def seleccion_item_tabla_creditos(self,clickedIndex):
        while (self.obj_form.tw_listado_cuotas.rowCount() > 0):
            self.obj_form.tw_listado_cuotas.removeRow(0)

        twi0 = self.obj_form.tw_lista_creditos.item(clickedIndex,1)
        nro_credito = twi0.text()
        obj_cuotas = N_cuotas(1)
        lista_cuotas = list()
        lista_cuotas = obj_cuotas.get_cuotas_por_nro_credito(int(nro_credito))

        lst_ord = [(i.nro_cuota, i) for i in lista_cuotas]
        lst_ord.sort()
        lst_ord = [i[1] for i in lst_ord]
        for item in lst_ord:
            saldo = round(float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios)  - float(item.importe_cobrado),2)  - round(float(item.descuento),2)
            cuota_pagar = float(item.capital) + float(item.interes) + float(item.gastos) + float(item.punitorios) - float(item.descuento)
            rowPosition = self.obj_form.tw_listado_cuotas.rowCount()
            self.obj_form.tw_listado_cuotas.insertRow(rowPosition)
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 0, QTableWidgetItem(str(item.estado_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_cuota)))
            self.obj_form.tw_listado_cuotas.setItem(rowPosition , 2, QTableWidgetItem(str(item.primer_vencimiento)))
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

    def buscar_cliente(self):
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
           # self.obj_form.lne_nom_ape.setText(obj_party_party.nombre + ", " + obj_party_party.apellido)
            self.obj_form.tw_lista_creditos.setEnabled(True)
            self.obj_form.tw_listado_cuotas.setEnabled(True)

            obj_N_credito = N_creditos(1)
            list_credito_party = obj_N_credito.get_list_credito(obj_party_party.id_party)

            lst_cred_party_activos = list()
            lst_cred_party_morosos = list()
            lst_cred_party_cancelado = list()
            for item in list_credito_party:
                estado = item.estado
                if item.estado == "Activo":
                    lst_cred_party_activos.append(item)
                elif item.estado == "Cancelado":
                    lst_cred_party_cancelado.append(item)
                else:
                    lst_cred_party_morosos.append(item)

        for item in lst_cred_party_activos:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))

        for item in lst_cred_party_morosos:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))

        for item in lst_cred_party_cancelado:
                rowPosition = self.obj_form.tw_lista_creditos.rowCount()
                self.obj_form.tw_lista_creditos.insertRow(rowPosition)
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 0, QTableWidgetItem(str(item.estado)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 1, QTableWidgetItem(str(item.nro_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 2, QTableWidgetItem(str(item.nro_cliente)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 3, QTableWidgetItem(str(item.fecha_credito)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 4, QTableWidgetItem(str(item.cantidad_cuotas)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 5, QTableWidgetItem(str(item.importe_prestamo)))
                self.obj_form.tw_lista_creditos.setItem(rowPosition, 6, QTableWidgetItem(str(item.observaciones)))

