import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer,func,update, text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion


base = declarative_base()

class E_creditos(base):
    __tablename__= "credito"
    nro_credito = Column(Integer, primary_key=True, autoincrement=True)
    nro_credito2 = Column(Integer)
    nro_cliente = Column(Integer)
    id_party = Column(Integer)
    fecha_credito = Column(DateTime, default=func.now())
    tasa = Column(String)
    formula = Column(String)
    importe_prestamo = Column(String)
    cantidad_cuotas = Column(String)
    vto_primer_cuota = Column(DateTime, default=func.now())
    interes = Column(Integer)
    gastos = Column(Integer)
    cred_total = Column(Integer)
    observaciones = Column(String)
    estado = Column(String)
    write_uid = Column(Integer)
    session =""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_creditos(self,id_party):

        obj_creditos = self.session.query(E_creditos).filter_by(id_party=id_party).all()
        try:
            self.session.close()
            return obj_creditos
        except :
            self.session.close()
            return False

    @classmethod
    def guardar(cls, obj_N_credito):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = cls()
        new_record.id_party = obj_N_credito.id_party
        new_record.nro_cliente = obj_N_credito.nro_cliente
        new_record.fecha_credito = obj_N_credito.fecha_credito
        new_record.tasa = obj_N_credito.tasa
        new_record.formula = obj_N_credito.formula
        new_record.importe_prestamo = obj_N_credito.importe_prestamo
        new_record.cantidad_cuotas = obj_N_credito.cantidad_cuotas
        new_record.vto_primer_cuota = obj_N_credito.vto_primer_cuota
        new_record.interes = obj_N_credito.interes
        new_record.gastos = obj_N_credito.gastos
        new_record.seguros = obj_N_credito.seguros
        new_record.impuestos = obj_N_credito.impuestos
        new_record.cred_total = obj_N_credito.cred_total
        new_record.observaciones = obj_N_credito.observaciones
        new_record.estado = obj_N_credito.estado
        new_record.nro_credito2 = obj_N_credito.nro_credito2
        new_record.write_uid=0

        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except:
            new_record.session.rollback()
            new_record.session.close()
            return False

    def get_tiene_prestamos_activo(self, nro_cliente):

        obj_E_creditos = self.session.query(E_creditos).filter_by(nro_cliente= nro_cliente).first()

        if obj_E_creditos != None :
            return obj_E_creditos.nro_credito
        self.session.close()
        return 0

    def buscar_creditos_por_cliente(self,nro_cliente):

        obj_creditos_cliente = self.session.query(E_creditos).filter_by(nro_cliente=str(nro_cliente)).all()
        self.session.close()
        return obj_creditos_cliente

    def buscar_nro_credito_por_party(self,id_party):
        nro_credito = self.session.query(func.max(E_creditos.nro_credito)).filter_by(id_party= id_party).scalar()
        if nro_credito != None :
            self.session.close()
            return nro_credito
        return False

    def buscar_credito_por_nro_credito(self, nro_credito):

        obj_credito = self.session.query(E_creditos).filter_by(nro_credito=nro_credito).first()
        self.session.close()
        return obj_credito

    def cancelar_credito(self,nro_credito):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        u = update(E_creditos).where(E_creditos.nro_credito == nro_credito).values(estado="Cancelado")
        self.session.execute(u)
        self.session.commit()
        self.session.close()

    def buscar_historial_garante(self,id_party):
        #engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        #Session= sessionmaker(bind=engine)
        #session=Session()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        sql = text("select  gc.tipo_garante, gc.nro_credito, c.importe_prestamo, pc.nro_cliente, pp.num_doc, pp.apellido, pp.nombre, c.estado from garante_credito as gc INNER JOIN credito as c ON gc.nro_credito  = c.nro_credito INNER JOIN party_party as pp ON c.id_party = pp.id_party INNER JOIN party_cliente as pc ON c.id_party = pc.id_party INNER JOIN party_garante as pg ON gc.id_party_garante = pg.id_party_garante where pg.id_party_garante =" + str(id_party) + "group by gc.tipo_garante, gc.nro_credito, c.importe_prestamo, pc.nro_cliente, pp.num_doc, pp.apellido, pp.nombre, c.estado")
        result = self.session.execute(sql)
        lista_historial_garante = list()
        for row in result:
            obj_E_historial_garante = E_historial_garante(1)
            obj_E_historial_garante.tipo_garante = row[0]
            obj_E_historial_garante.nro_credito = row[1]
            obj_E_historial_garante.importe_prestamo = row[2]
            obj_E_historial_garante.nro_cliente = row[3]
            obj_E_historial_garante.num_doc = row[4]
            obj_E_historial_garante.apellido = row[5]
            obj_E_historial_garante.nombre = row[6]
            obj_E_historial_garante.estado_credito = row[7]
            lista_historial_garante.append(obj_E_historial_garante)
        self.session.close()
        return lista_historial_garante

    def buscar_ultimo_credito(self):
        nro_credito = self.session.query(func.max(E_creditos.nro_credito)).scalar()
        if nro_credito != None :
            self.session.close()
            return nro_credito
        return False

    def buscar_ultimo_credito2(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        nro_credito = self.session.query(func.max(E_creditos.nro_credito2)).scalar()
        if nro_credito != None :
            self.session.close()
            return nro_credito
        return False

    def actualizar_estado_credito(self, nro_credito, estado):
        query = update(E_creditos).where(E_creditos.nro_credito == nro_credito).values(estado=estado)
        try:
            self.session.execute(query)
            self.session.commit()
            self.session.close()
            return True
        except:
            self.session.close()
            return False
