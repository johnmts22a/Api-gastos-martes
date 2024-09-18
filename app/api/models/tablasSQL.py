from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base 

#Llamado a la base para crear tablas

Base = declarative_base ()

#Definición de las tablas de mi modelo

#usuario
class Usuario(Base):
    __tablename__= 'usuarios'
    id = Column(Integer,primary_key = True, autoincrement = True)
    nombres = Column(String(50))
    fechaNacimiento = Column(Date)
    ubicacion = Column(String(100))
    metaAhorro = Column(Float)
    
class Gasto(Base):
    __tablename__ = 'gastos'
    descripcion = Column(String(50))
    categoria = Column(String(30))
    valor = Column(Float)
    fecha = Column (Date)
    
class Categoria(Base):
    __Tablename__ = 'categoria'
    id = Column(Integer,primary_key = True, autoincrement = True)
    nombre = Column(Integer(50))
    descripcion = Column(String(70))
    fotoCategoria = Column(String(270))
    
class Ingreso(Base):
    __Tablename__ = 'ingreso'
    id = Column(Integer,primary_key = True, autoincrement = True)
    valor = Column(Float)
    descripcion = Column(String(30))
    fecha = Column(Date)