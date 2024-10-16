from fastapi import APIRouter, HTTPException #Librería para los servicios que necesito en la base de datos (Actualizar, Guardar, etc)
from sqlalchemy.orm import Session #Comunicación con la base de datos.
from typing import List
from fastapi.params import Depends #Utilizar dependencias del api para comunicación interna.
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.DTO.dtos import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.tablasSQL import Gasto
from app.api.models.tablasSQL import Categoria
from app.api.DTO.dtos import CategoriaDTOPeticion,CategoriaDTORespuesta
from app.api.models.tablasSQL import Ingreso
from app.api.DTO.dtos import IngresoDTOPeticion,IngresoDTORespuesta
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

#Inicio para la tabla usuario (Petición y respuesta)

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
    
#Inicio para la tabla gasto(Petición y respuesta)
    
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
    
@rutas.get("/gasto",response_model = List[GastoDTORespuesta],summary="Buscar todos los gastos en la base de datos")
    
def buscarGasto(database:Session=Depends(conectarConBD)):
    try:
        gastos = database.query(Gasto).all
        return gastos
     
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"No se puede buscar los usuario {error}")
    
#Inicio para la tabla categoria(Petición y respuesta)
    
@rutas.post("/categoria",response_model= CategoriaDTORespuesta, summary= "Registrar una categoría en la base de datos")
        
def guardarCategoria(datosCategoria:CategoriaDTOPeticion, database:Session=Depends(conectarConBD)):
    try:
       categoria = Categoria(
           nombre = datosCategoria.nombre,
           descripcion = datosCategoria.descripcion,
           fotoCategoria = datosCategoria.fotoCategoria
       )
       
       database.add(categoria) #Agregar el usuario a la base de datos.
       database.commit() 
       database.refresh(categoria) #Refrescar la base de datos.
       return categoria
       
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"Tenemos un problema {error}")
    
@rutas.get("/categoria",response_model = List[CategoriaDTORespuesta],summary="Buscar todas las categorías en la base de datos")
    
def buscarCategoria(database:Session=Depends(conectarConBD)):
    try:
        categorias = database.query(Categoria).all
        return categorias
     
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"No se puede buscar las categorías {error}")
    
#Inicio para la tabla ingreso(Petición y respuesta)

@rutas.post("/ingreso",response_model= IngresoDTORespuesta, summary= "Registrar un ingreso en la base de datos")
        
def guardarIngreso(datosIngreso:IngresoDTOPeticion, database:Session=Depends(conectarConBD)):
    try:
       ingreso = Ingreso(
           valor = datosIngreso.valor,
           descripcion = datosIngreso.descripcion,
           fecha = datosIngreso.fecha
       )
       
       database.add(ingreso) #Agregar el usuario a la base de datos.
       database.commit() 
       database.refresh(ingreso) #Refrescar la base de datos.
       return ingreso
       
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"Tenemos un problema {error}")
    
@rutas.get("/ingreso",response_model = List[IngresoDTORespuesta],summary="Buscar todos los ingresos en la base de datos")
    
def buscarCategoria(database:Session=Depends(conectarConBD)):
    try:
        ingresos = database.query(Ingreso).all
        return ingresos
     
    except Exception as error:
        database.rollback() #Si la base de datos falló no hacer nada. 
        raise HTTPException(status_code=400,detail= f"No se puede buscar los ingresos {error}")


    
 
    
   