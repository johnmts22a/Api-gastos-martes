from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.tablasSQL import Base
from app.api.routes.endpoints import rutas

from starlette.responses import RedirectResponse

#Crear las tablas SQL desde python
Base.metadata.create_all(bind = engine)


#Variable para administrar la aplicación
app = FastAPI()

#Activar el API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)