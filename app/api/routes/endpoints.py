from fastapi import APIRouter, HTTPException #Librería para los servicios que necesito en la base de datos (Actualizar, Guardar, etc)
from sqlalchemy.orm import Session #Comunicación con la base de datos.
from typing import List
from fastapi.params import Depends #Utilizar dependencias del api para comunicación interna.
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.DTO.dtos import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.tablasSQL import Gasto
from app.database.configuration import SessionLocal,engine

rutas = APIRouter()

def conectarConBD():
    try:
        basedatos = SessionLocal()
        yield basedatos #Activar la base de datos
           
    except Exception as error:
        basedatos.rollback() #Si la base de datos falló no hacer nada.
        raise error
    
    finally:
        basedatos.close()
        
#Construyendo nuestros servicios.

#Cada servicio (operación o transacción en BD) debe programarse como una función.

@rutas.post("/usuario",response_model = UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")

def guardarUsuario(datosUsuario:UsuarioDTOPeticion, database:Session=Depends(conectarConBD)): #datos y conexión con la base de datos respectivamente.
    try:
        usuario = Usuario(
            nombres = datosUsuario.nombres,
            fechaNacimiento = datosUsuario.fechaNacimiento,
            ubicacion = datosUsuario.ubicacion,
            metaAhorro = datosUsuario.metaAhorro
        )
        
        #Dando órdenes a la base de datos:
        
        database.add(usuario) #Agregar el usuario a la base de datos.
        database.commit() 
        database.refresh(usuario) #Refrescar la base de datos.
        return usuario
        
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"Tenemos un problema {error}")
    
@rutas.get("/usuario",response_model = List[UsuarioDTORespuesta],summary="Buscar todos los usuario en la base de datos")
    
def buscarUsuario(database:Session=Depends(conectarConBD)):
    try:
        usuarios = database.query(Usuario).all
        return usuarios
        
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"No se puede buscar los usuario {error}")
    
@rutas.post("/gasto",response_model= GastoDTORespuesta, summary= "Registrar un gasto en la base de datos")
        
def guardarGasto(datosGasto:GastoDTOPeticion, database:Session=Depends(conectarConBD)):
    try:
       gasto = Gasto(
           descripcion = datosGasto.descripcion,
           categoria = datosGasto.categoria,
           valor = datosGasto.valor,
           fecha = datosGasto.fecha
       )
       
       database.add(gasto) #Agregar el usuario a la base de datos.
       database.commit() 
       database.refresh(gasto) #Refrescar la base de datos.
       return gasto
       
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"Tenemos un problema {error}")
    
@rutas.get("/gasto",response_model = List[GastoDTORespuesta],summary="Buscar todos los usuario en la base de datos")
    
def buscarGasto(database:Session=Depends(conectarConBD)):
    try:
        gastos = database.query(Gasto).all
        return gastos
     
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"No se puede buscar los usuario {error}")
    

    
 
    
   