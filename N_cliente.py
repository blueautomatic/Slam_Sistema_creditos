import sys
import datetime
from E_party_garante import E_party_garante
from E_party_contacto import E_party_contacto
from E_party_party import E_party_party
from E_datos_laborales import E_datos_laborales
from E_party_address import E_party_address
from E_party_otros import E_party_otros
from E_usuario import E_usuario
from E_party_cliente import E_party_cliente
from E_party_address import E_party_address
from E_garante_credito import E_garante_credito

from PyQt5.QtCore import pyqtRemoveInputHook


class N_datos_personales_cliente(object):
    apellido = ""
    nombre = ""
    tipo_doc = ""
    nro_doc = ""
    estado_civil = ""
    fec_nac = ""
    limite_credito = 0
    id_party = 0
    estado = ""


    @classmethod
    def guardar(self, obj_N_datos_laborales): 
        return E_party_party().guardar(obj_N_datos_laborales)

    def actualizar_party_party(self,N_datos_personales_cliente,id_party):
        obj_E_party = E_party_party()
       # pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_E_party.actualizar(N_datos_personales_cliente, id_party)

    def get_garante_habilitado_buscar(self, numero_documento_garante):
        obj_E_party_cliente = E_party_party()
        obj_party_cliente = obj_E_party_cliente.get_party_party(numero_documento_garante)
        return obj_party_cliente

    def buscar_partyparty_por_nrodoc(self, numero_documento):
        obj_E_party_cliente = E_party_party()
        obj_party_cliente = obj_E_party_cliente.get_party_party(numero_documento)
        return obj_party_cliente

    def get_garante_habilitado_buscar_nrocliente(self,nro_cliente):
        obj_E_party_cliente = E_party_party()
        obj_party_cliente = obj_E_party_cliente.get_party_party(nro_cliente)
        return obj_party_cliente

    def get_id_party_party_garante(self,nro_doc_garante):
        obj_E_party_cliente = E_party_party()
        id_party_party_garante = obj_E_party_cliente.get_id_party(nro_doc_garante)
        return id_party_party_garante

    def buscar_party_party_por_id(self, id_party):
       
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_E_party_id = E_party_party()
        party_party_por_nro_doc = obj_E_party_id.buscar_party_party_id(id_party)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if party_party_por_nro_doc != None:
            self.apellido = party_party_por_nro_doc.apellido
            self.nombre = party_party_por_nro_doc.nombre
            self.tipo_doc = party_party_por_nro_doc.tipo_doc
            self.nro_doc = party_party_por_nro_doc.num_doc
            self.estado_civil = party_party_por_nro_doc.estado_civil
            self.fec_nac = party_party_por_nro_doc.fec_nac
            self.limite_credito = party_party_por_nro_doc.limite_credito
            self.id_party = party_party_por_nro_doc.id_party
            self.estado = party_party_por_nro_doc.estado
            return self      
        else:
            return False
    
    def buscar_party_party_por_nro_doc(self, dni_cliente):

        obj_E_party_party_nro_cliente = E_party_party()
        party_party_por_nro_doc = obj_E_party_party_nro_cliente.get_party_party(dni_cliente)
        if party_party_por_nro_doc != None:
            return party_party_por_nro_doc
        else:    
            return False
   
    def buscar (self, apellido):
        obj_party_party = E_party_party()
        return obj_party_party.buscar(apellido)




class N_party_cliente(object):
    nro_cliente = ""
    comment=""
    id_party=""

    def __init__(self,id_party):
        a= id_party

    def actualizar_comentario(self,id_party,observaciones):
        obj_E_party_cliente = E_party_cliente()
        obj_E_party_cliente.actualizar_comentario(id_party,observaciones)
        return True


    def get_party_cliente(self, id_party):
        obj_E_party_cliente = E_party_cliente()
        party_cliente = obj_E_party_cliente.get_party_cliente(id_party)
        if party_cliente != None:
            return party_cliente
        else:
            return False

    def get_nro_cliente(self,id_party):

        obj_E_party_cliente=E_party_cliente()
        nro_cliente=obj_E_party_cliente.get_nro_cliente(id_party)
        return nro_cliente

    def guardar_N_party_cliente(self, comment, id_party):
        obj_E_party_cliente= E_party_cliente()
        obj_E_party_cliente.guardar(comment, id_party)

    def buscar_id_party_por_nro_cliente(self, nro_cliente):
        obj_E_party_cliente= E_party_cliente()
        return obj_E_party_cliente.buscar_id_party_por_nro_cliente(nro_cliente)        

    def buscar_E_party_cliente_por_nro_cliente(self,nro_cliente):
        obj_E_party_cliente= E_party_cliente()
        return obj_E_party_cliente.buscar_E_party_cliente_por_nro_cliente(nro_cliente)      

class N_party_address(object):
    ciudad = ""
    barrio = ""
    domicilio = ""
    id_party = ""

    def __init__(self, ciudad):
        a = ciudad
    def get_party_address(self,id_party):
        obj_E_party_address3= E_party_address()
        obj_E_party_address2 =obj_E_party_address3.get_party_address(id_party)
       # pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        obj_N_party_address= N_party_address(1)
        if obj_N_party_address != None:
            obj_N_party_address.ciudad = obj_E_party_address2.ciudad
            obj_N_party_address.domicilio = obj_E_party_address2.domicilio
            obj_N_party_address.barrio= obj_E_party_address2.barrio  
            return obj_N_party_address
        else:
            return False


        

    def guardar(self, N_party_address, id_party):
        obj_E_party_address = E_party_address()
        result = obj_E_party_address.guardar(N_party_address, id_party)
        return result
    

    def actualizar_party_address(self ,N_datos_address ,id_party):
        obj_E_party_address = E_party_address()
        obj_E_party_address.actualizar(N_datos_address ,id_party)

class N_datos_laborales(object):
    id_party = ""
    sueldo = 0
    anti_laboral = ""
    tel_laboral = ""
    dom_laboral = ""
    organismo = ""
    ocupacion = ""
    categoria = ""
    posee_recibo_sueldo = ""



    def get_datos_laborales(self, id_party):
        obj_E_datos_laborales=E_datos_laborales()
        obj_datos_laborales=obj_E_datos_laborales.get_datos_laborales(id_party)
        self.sueldo = obj_datos_laborales.sueldo
        self.anti_laboral = obj_datos_laborales.anti_laboral
        self.tel_laboral = obj_datos_laborales.tel_laboral
        self.dom_laboral = obj_datos_laborales.dom_laboral
        self.organismo = obj_datos_laborales.organismo
        self.ocupacion = obj_datos_laborales.ocupacion
        self.categoria = obj_datos_laborales.categoria
        self.posee_recibo_sueldo = obj_datos_laborales.posee_recibo_sueldo
        return self



    def guardar(self, obj_N_datos_laborales, id_party):
        obj_E_datos_laborales = E_datos_laborales()
        result = obj_E_datos_laborales.guardar(obj_N_datos_laborales, id_party)
        return result
    def actualizar_datos_laborales(self ,N_datos_laborales ,id_party):
        obj_E_datos_laborales = E_datos_laborales()
        obj_E_datos_laborales.actualizar(N_datos_laborales ,id_party)

class N_party_otros(object):

    id=""
    id_party = ""
    tipo_iva = ""
    cuit = ""
    cbu = ""
    num_beneficio =""
    presento_factura= False
    figura_veraz= False
    es_jubilado_pensionado= False
    cliente_bloqueado= False
    monotributista=False


    def __init__(self, id):
        a = id

    def get_party_otros(self, id_party):
        obj_E_party_otros=E_party_otros(1)
        obj_party_otros=obj_E_party_otros.get_party_otros(id_party)
        if obj_party_otros != None:
            obj_N_party_otros=N_party_otros(1)
            obj_N_party_otros.cuit=obj_party_otros.cuit
            obj_N_party_otros.tipo_iva=obj_party_otros.tipo_iva
            obj_N_party_otros.cbu=obj_party_otros.cbu
            obj_N_party_otros.num_beneficio=obj_party_otros.num_beneficio
            obj_N_party_otros.presento_factura=obj_party_otros.presento_factura
            obj_N_party_otros.figura_veraz=obj_party_otros.figura_veraz
            obj_N_party_otros.es_jubilado_pensionado=obj_party_otros.es_jubilado_pensionado

            return obj_N_party_otros
        else:
            return False



    def guardar(self, obj_N_party_otros, id_party):

        obj_E_party_otros = E_party_otros(1)
        result = obj_E_party_otros.guardar(obj_N_party_otros, id_party)
        return result
    def actualizar_party_otros(self ,N_party_otros ,id_party):
        obj_E_party_otros = E_party_otros(id_party)
        obj_E_party_otros.actualizar(N_party_otros ,id_party)   

class N_party_contacto(object):
    id_party=""
    type_contacto=""
    comment=""
    value=""
    id_contact=""

    def __init__(self, id_party):
        a=id_party

    def guardar(self, obj_N_party_contact, id_party):
        obj_E_party_contact = E_party_contacto(1)
        obj_E_party_contact.guardar(obj_N_party_contact, id_party)

    def get_list_party_contacto(self, id_party):
        list_E_party_contact = E_party_contacto(1)
        lista = list()
        lista = list_E_party_contact.get_list_party_contacto(id_party)
        if lista != None:
            return lista
        else:
            return False

    def actualizar_party_contact(self ,N_party_contacto ,id_party):
        obj_E_party_contacto = E_party_contacto(id_party)
        obj_E_party_contacto.actualizar(N_party_contacto ,id_party)
       

class N_party_garante(object):
    id_garante = 0
    id_party_garante = 0
    comment = ""
    nro_doc = ""
    tipo_garante = ""
    nro_cliente = 0
    nro_credito = 0

    def __init__(self, apellido):
        a = apellido

    def guardar(self, list_party_cliente, nro_cliente):
        obj_E_party_garante = E_party_garante(1)

        for item in list_party_cliente:
            obj_E_party_garante.guardar(item, nro_cliente)
        

    def validar_garante(self, obj_N_party_garante):
        a=obj_N_party_garante
    
    def guardar_garante(self, obj_party_garante):
        obj_E_party_party = E_party_party()
        id_party_garante = obj_E_party_party.get_id_party(obj_party_garante.nro_doc)
        obj_E_party_garante = E_party_garante(id_party_garante)
        obj_E_party_garante.guardar(obj_party_garante,id_party_garante)

    def es_garante_de_otro_cliente(self,nro_doc_garante):
        obj_E_party_garante= E_party_garante(nro_doc_garante)
        obj_party_cliente=E_party_party()
        id_party_garante=obj_party_cliente.get_id_party(nro_doc_garante)

        result =obj_E_party_garante.es_garante_de_otro_cliente(id_party_garante)
        return result

    def get_tiene_prestamos_activo(self, nro_doc_garante):
        obj_party_cliente=obj_E_party_party()
        id_party_garante=obj_party_cliente.get_id_party(nro_doc_garante)
        obj_E_prestamo=E_prestamo(1)
        obj_E_prestamo.validar_cliente_prestamo_activo(id_party_garante)

    def get_list_party_garante(self,nro_cliente):

        obj_E_party_garante = E_party_garante(1)
        list_party_garante=list()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        list_party_garante =obj_E_party_garante.get_N_party_garante(nro_cliente)

        list_N_party_garante = list()
        if list_party_garante !=None :
            for item in list_party_garante:
                obj_garante= N_party_garante(1)
                obj_garante.id_party_garante = item.id_party_garante
                obj_garante.tipo_garante = item. tipo_garante
                obj_garante.nro_cliente = item.nro_cliente
                obj_garante.comment = item.comment
                obj_garante.id_garante = item.id_garante
                list_N_party_garante.append(obj_garante)

            return list_N_party_garante  
        else: 
            return False

    def buscar_lista_party_garante_por_id_party(self, id_party):
        obj_E_party_garante = E_party_garante(1)
        return obj_E_party_garante.buscar_lista_party_garante_por_id_party(id_party)

    def actualizar_lista_garante(self, list_garante,nro_cliente):
        obj_E_lista_garante = E_party_garante(1)
        obj_E_lista_garante.actualizar_lista_garante(list_garante,nro_cliente)

    def actualizar_credito_garante(self,lista_garantes_credito,nro_credito):
         obj_E_lista_garante = E_party_garante(1)
         obj_E_lista_garante.actualizar_credito_garante(lista_garantes_credito,nro_credito)

class N_garante_credito(object):
    id = 0
    id_party_garante = 0
    nro_credito= 0
    tipo_garante = ""    
    
    def __init__(self, id_party):
        a = id_party
        
    def guardar(self, lista_garantes_credito,nro_credito):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_E_garante_credito = E_garante_credito(1)
        result = obj_E_garante_credito.guardar(lista_garantes_credito,nro_credito)
        return result

    def get_garante_prestamo(self, id_party):
        obj_E_garante_credito = E_garante_credito(1)
        result = obj_E_garante_credito.get_garante_credito(id_party)
        return result

    def buscar_id_party_por_id_party(self, id_party):
        obj_E_party_cliente = E_garante_credito(1)
        obj_party_party = obj_E_party_cliente.buscar_id_party_por_id_party(id_party_garante)
        return obj_party_party

