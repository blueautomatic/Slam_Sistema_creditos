import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
    class E_party_contacto(Base):
    	    __tablename__="party_contact"
    	    id_contact = Column(Integer, primary_key=True, autoincrement=True)	
    	    id_party = Column(Integer, ForeignKey('party_party.id_party'))
    	    create_date = Column(DateTime, default=func.now())
    	    write_date = Column(DateTime, default=func.now())
    	    comment = Column(String(200))
    	    value = Column(String(50))
            type_contacto = Column(String(50))
    	

         def __init__(self,id_party,id_contact,comment,value,type_contacto,create_date,write_date):
            self.id_party = id_party
            self.comment = comment
            self.create_uid = create_uid
            self.create_date = create_date
            self.value = value
            self.write_date = write_date
            self.activo = activo
            self.type_contacto = type_contacto

        def guardar(self):

            engine=create_engine('postgresql://postgres:121212@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_party_contacto		
            new_record.comment = comment
            new_record.value = value
            new_record.type_contacto = type_contacto
            session.add(new_record)
            session.commit()

