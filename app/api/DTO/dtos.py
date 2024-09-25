from pydantic import BaseModel,Field  #Paquete del api que permite crear un modelo base del DTO
from datetime import date  #Paquete para fechas y horas.

#Los DTO son clases que establecen el modelo de transferencia de datos.

class UsuarioDTOPeticion(BaseModel): #Petición para guardar los datos en la BD
    nombres: str
    fechaNacimiento:date
    ubicacion: str
    metaAhorro: float
    class config:
        orm_mode = True

class UsuarioDTORespuesta(BaseModel): #Petición para traer los datos de la BD
    id: int
    nombres: str
    metaAhorro: float
    class config:
        orm_mode = True
        
class GastoDTOPeticion(BaseModel):
    descripcion: str
    categoria: str
    valor: float
    fecha: date
    class config:
        orm_mode = True
    
class GastoDTORespuesta(BaseModel):
    id: int
    descripcion: str
    categoria: str
    valor: float
    fecha: date
    class config:
        orm_mode = True
        
class CategoriaDTOPeticion(BaseModel):
    nombre: str
    descripcion: str
    fotoCategoria: str
    class config:
        orm_mode = True
        
class CategoriaDTORespuesta(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fotoCategoria: str
    class config:
        orm_mode = True
        
class IngresoDTOPeticion(BaseModel):
    valor: float
    descripcion: str
    fecha: date
    
class IngresoDTORespuesta(BaseModel):
    id: int
    valor: float
    descripcion: str
    fecha: date



