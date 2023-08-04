from fastapi import FastAPI

app = FastAPI()

#pedimos al servidor que nos devuelva lo que tiene en la raiz
@app.get("/")
async def root():
    """
        gracias a la funcion asincrona podemos hacer peticiones al servidor y que lo demas siga en funcionamiento
        ya que se ejecuta de forma asincronica xD
    """
    return {"message":"Hola brodeers"}

@app.get("/url")
async def url(): 
    return {"url_root":"http://127.0.0.1:8000/"}

#iniciar server: 
# uvicorn nombreArchivo.py:InstanciaDelMiniFrameworkFASTAPI --reolad(cada vez que guardes el doc se recarga el server)
# Documentacion automatica:
#swagger: http://127.0.0.1:8000/docs
#Readocly: http://127.0.0.1:8000/redoc  