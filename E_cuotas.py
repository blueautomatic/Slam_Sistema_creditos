import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion



base = declarative_base()

class E_cuotas(base):
        __tablename__= "cuotas"
        id = Column(Integer, primary_key=True, autoincrement=True)
        nro_credito= Column(Integer)
        nro_cuota= Column(Integer)
        primer_vencimiento=Column(DateTime)
        importe_primer_venc=Column(Numeric)
        estado_cuota=Column(String)
        fecha_cobro=Column(DateTime)
        importe_cobrado=Column(Numeric)
        capital = Column(Numeric)
        interes = Column(Numeric)
        gastos = Column(Numeric)
        punitorios = Column(Numeric)
        descripcion = Column(String)
        descuento = Column(Numeric)
        importe_cuota = Column(Numeric)
        write_uid = Column(Integer)
        session=""


        def __init__(self,id_usuario):
            a = id_usuario
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

        @classmethod
        def guardar(cls, obj_N_cuotas, nro_credito):
            new_record = cls(1)
            new_record.nro_credito = nro_credito
            new_record.nro_cuota = obj_N_cuotas.nro_cuota
            new_record.primer_vencimiento = str(obj_N_cuotas.primer_Vencimiento)
            new_record.importe_cuota = obj_N_cuotas.importe_primer_vencimiento
            new_record.importe_primer_venc = obj_N_cuotas.importe_primer_vencimiento
            new_record.estado_cuota = obj_N_cuotas.estado_cuota
            new_record.capital = obj_N_cuotas.capital
            new_record.interes = obj_N_cuotas.interes
            new_record.gastos = obj_N_cuotas.gastos
            new_record.importe_cobrado = 0
            new_record.punitorios = obj_N_cuotas.punitorios
            new_record.descripcion = ""
            new_record.write_uid = 0
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            calc_interes = (obj_N_cuotas.capital + obj_N_cuotas.interes + obj_N_cuotas.gastos) * 6/ 100
            obj_redondear = E_cuotas(1)
            new_record.descuento =obj_redondear.redondear(str(calc_interes))

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

        def get_cuotas_por_nro_credito(self, nro_creditos):

            lista_cuotas = self.session.query(E_cuotas).filter_by(nro_credito = nro_creditos).all()
            try:
                self.session.close()
                return lista_cuotas
            except :
                self.session.close()
                return False

        def get_E_actuacion_laboral(self, id_party):
            list_actuacion_laboral = self.session.query(E_actuacion_laboral).filter_by(id_party=id_party).all()
            self.session.close()
            return list_actuacion_laboral

        def pagar_cuota(self, obj_cuotas):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            query = update(E_cuotas).where(E_cuotas.id == obj_cuotas.id ).values(estado_cuota=obj_cuotas.estado_cuota, importe_cobrado = obj_cuotas.importe_cobrado, fecha_cobro = obj_cuotas.fecha_cobro,interes = obj_cuotas.interes,gastos = obj_cuotas.gastos, punitorios = obj_cuotas.punitorios, descripcion= obj_cuotas.descripcion, descuento = obj_cuotas.descuento  )
            self.session.execute(query)
            self.session.commit()
            self.session.close()

        def lista_cuotas_venc_30_dias(self):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            lista_cuotas = self.session.query(E_cuotas).filter_by(estado_cuota = "Vencida 30 días").all()
            try:
                self.session.close()
                return lista_cuotas
            except :
                self.session.close()
                return False

        def lista_cuotas_venc_60_dias(self,slam):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            lista_cuotas = self.session.query(E_cuotas).filter_by(estado_cuota = "Vencida 60 días").all()
            try:
                self.session.close()
                return lista_cuotas
            except :
                self.session.close()
                return False

        def lista_cuotas_venc_90_dias(self,slam):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            lista_cuotas = self.session.query(E_cuotas).filter_by(estado_cuota = "Vencida 90 días").all()
            try:
                self.session.close()
                return lista_cuotas
            except :
                self.session.close()
                return False

        def buscar_cuota_por_id_cuota(self, id_cuota):
            #import pdb; pdb.set_trace()
            lista_cuotas = self.session.query(E_cuotas).filter_by(id = id_cuota).first()
            try:
                self.session.close()
                return lista_cuotas
            except :
                self.session.close()
                return False

        def generar_punitorios(self,id):
            slam = id
            sql = text('SELECT miprimerfuncion()')
            result = self.session.execute(sql)

            try:
                self.session.commit()
                self.session.close()
                return 1
            except :
                self.session.close()
                return False

        def buscar_cta_por_nro_cred_y_nro_cta(self, nro_credito, nro_cuota):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_cuotas = self.session.query(E_cuotas).filter_by(nro_credito = nro_credito,nro_cuota = nro_cuota).first()
            try:
                self.session.close()
                return obj_cuotas
            except :
                self.session.close()
                return False

        def actualizar(self, obj_cuotas):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            query = update(E_cuotas).where(E_cuotas.id == obj_cuotas.id ).values(estado_cuota=obj_cuotas.estado_cuota, importe_cobrado = obj_cuotas.importe_cobrado, fecha_cobro = obj_cuotas.fecha_cobro,interes = obj_cuotas.interes,gastos = obj_cuotas.gastos, punitorios = obj_cuotas.punitorios, descripcion= obj_cuotas.descripcion, descuento = obj_cuotas.descuento)
            try:
                self.session.execute(query)
                self.session.commit()
                self.session.close()
                return True
            except:
                self.session.rollback()
                self.session.close()
                return False

        def actualizar_reparar(self, obj_cuotas):

                query = update(E_cuotas).where(E_cuotas.id == obj_cuotas.id ).values(estado_cuota=obj_cuotas.estado_cuota, importe_cobrado = obj_cuotas.importe_cobrado, fecha_cobro = obj_cuotas.fecha_cobro,interes = obj_cuotas.interes,gastos = obj_cuotas.gastos, punitorios = obj_cuotas.punitorios, descripcion= obj_cuotas.descripcion, descuento = obj_cuotas.descuento, importe_cuota= obj_cuotas.importe_cuota, importe_primer_venc =obj_cuotas.importe_primer_venc)
                try:
                    self.session.execute(query)
                    self.session.commit()
                    self.session.close()
                    return True
                except:
                    self.session.rollback()
                    self.session.close()
                    return False

        def actualizar_refinanciacion(self, obj_cuotas):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            query = update(E_cuotas).where(E_cuotas.id == obj_cuotas.id ).values( importe_cuota = obj_cuotas.importe_cuota, importe_primer_venc= obj_cuotas.importe_primer_venc, primer_vencimiento = obj_cuotas.primer_vencimiento , estado_cuota=obj_cuotas.estado_cuota,capital = obj_cuotas.capital,importe_cobrado = obj_cuotas.importe_cobrado,interes = obj_cuotas.interes,gastos = obj_cuotas.gastos,punitorios = obj_cuotas.punitorios,descripcion= obj_cuotas.descripcion,descuento = obj_cuotas.descuento)
            try:
                self.session.execute(query)
                self.session.commit()
                self.session.close()
                return True
            except:
                self.session.rollback()
                self.session.close()
                return False




        def get_max_cta(self, nro_credito):
            sql = text('SELECT max(nro_cuota) as nro_cta from cuotas where nro_credito = ' + str(nro_credito))
            result = self.session.execute(sql)
            try:
                self.session.close()
                for item in result :
                    return item.nro_cta
            except :
                self.session.close()
                return False


        @classmethod
        def guardar_refinanciacion(cls, obj_e_cuotas, nro_credito):

            new_record = cls(1)
            new_record.nro_credito = nro_credito
            new_record.nro_cuota = obj_e_cuotas.nro_cuota
            new_record.primer_vencimiento = obj_e_cuotas.primer_vencimiento
            new_record.importe_cuota = obj_e_cuotas.importe_primer_venc
            new_record.importe_primer_venc = obj_e_cuotas.importe_primer_venc
            new_record.estado_cuota = obj_e_cuotas.estado_cuota
            new_record.capital = obj_e_cuotas.capital
            new_record.interes = obj_e_cuotas.interes
            new_record.gastos = obj_e_cuotas.gastos
            new_record.importe_cobrado = 0
            new_record.punitorios = obj_e_cuotas.punitorios
            new_record.descripcion = obj_e_cuotas.descripcion
            new_record.descuento = 0
            new_record.write_uid = 0
            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

        def redondear(self, obj_capital):
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

        def reporte_deuda_por_cliente(self):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            sql = text("select round(SUM(c.capital) + SUM(c.interes) + SUM(c.gastos) + SUM(c.punitorios)) "
                       "as total, pp.apellido, pp.nombre from cuotas c inner join credito ct on "
                       "c.nro_credito=ct.nro_credito inner join party_party pp on ct.id_party= pp.id_party "
                       "where c.estado_cuota!='Pagada' group by c.nro_credito,pp.id_party  order by c.nro_credito")
            result = self.session.execute(sql)
            try:
                self.session.close()
                return result
            except :
                self.session.close()
                return False

        def reporte_cuotas_pagas_por_mes(self):

            sql = text("select (sum(capital) + sum(interes)+ sum(gastos) + sum(punitorios) ) as total, "
                       "date_trunc('month', primer_vencimiento) AS txn_month, from cuotas "
                       "where estado_cuota='Pagada' group by txn_month order by txn_month")

            result = self.session.execute(sql)
            try:
                self.session.close()
                return result
            except :
                self.session.close()
                return False



            def reporte_total_cta_pagar_por_mes(self):
                sql = text("select (sum(capital) + sum(interes)+ sum(gastos) + sum(punitorios) ) as total ,"
                           "date_trunc('month', primer_vencimiento) AS txn_month from cuotas "
                           "where estado_cuota='Pagada' group by txn_month order by txn_month")

                result = self.session.execute(sql)
                try:
                    self.session.close()
                    return result
                except:
                    self.session.close()
                    return False
