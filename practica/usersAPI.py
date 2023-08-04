from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

##BaseModle nos da la capacidad de crear una entidad
class Users(BaseModel):
    id: int
    name: str
    lastname: str
    age: int

@app.get("/users")
def getUsers():
    return users_list

#para parametrizar un pedido a la api en el path ponemos el parametro que vamos a recibir entre corchetes
#dentro del get
@app.get("/user/{id}")
def getUserByID(id: int):
    #metodo que se me ocurrio a mi
    users = [user for user in users_list if user.id == id]
    try:
        return users[0]
    except:
        return "not Found"

    #metodo usando la funcion filter de python
    #return filter(lambda user: user.id == id, users_list) 

##--------------------------------------- base de datos imaginara ---------------------------------------
users_list = [Users(id= 1,name="juanchi",lastname="caceffo", age=20),
             Users(id= 2,name="facundo",lastname="barneche",age=30),
             Users(id= 3,name="alejo",  lastname="menini",  age=22)]
##--------------------------------------- base de datos imaginara ---------------------------------------
