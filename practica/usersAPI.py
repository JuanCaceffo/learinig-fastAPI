from fastapi import FastAPI
from pydantic import BaseModel
import itertools as it

app = FastAPI()

##BaseModle nos da la capacidad de crear una entidad
class Users(BaseModel):
    id: int
    name: str
    lastname: str
    age: int

##--------------------------------------- base de datos imaginara ---------------------------------------
users_list = [Users(id= 1,name="juanchi",lastname="caceffo", age=20),
             Users(id= 2,name="facundo",lastname="barneche",age=30),
             Users(id= 3,name="alejo",  lastname="menini",  age=22)]
##--------------------------------------- base de datos imaginara ---------------------------------------
RAISE_ERROR_USERNOTFOUND = {"error": "user not found"}
RAISE_ERROR_USEREXIST = {"error": "User exist"}
RAISE_ERROR_USERDONOTEXIST = {"error": "User doesn't exist"}
##-------------------------------------------------- GET -------------------------------------------------- 
@app.get("/users")
async def getUsers():
    return users_list

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return RAISE_ERROR_USERNOTFOUND


#para parametrizar un pedido a la api en el path ponemos el parametro que vamos a recibir entre corchetes
#dentro del get
@app.get("/user/{id}")
async def getUserByID(id: int):
    return search_user(id)


##busqueda por id utilizando query en vez de path
##la llamada a este get se hace de la siguiente forma
##http://127.0.0.1:8000/userquery/?parametro=dato
@app.get("/userquery/")
async def userQueryId(id: int):
    return search_user(id)

@app.get("/userQueryNameLastname/")
async def userQueryNameLastname(name: str,lastName: str):
    """Busqueda por nombre y apellido"""
    name = name.lower( )
    lastName = lastName.lower()
    users = [user for user in users_list if (user.name == name and user.lastname == lastName)]
    try:
        return users[0]
    except:
        return RAISE_ERROR_USERNOTFOUND

##IMPORTANTE EL PATH SE UTILIZA PAR APARAMETROS QUE VAN FIJOS Y LA QUERY PARA LOS OPCIONALES, (POR CONVENCION)  
##-------------------------------------------------- GET -------------------------------------------------- 

##-------------------------------------------------- POST -------------------------------------------------- 

@app.post("/user/")
async def user(user: Users):
    try:   
        errorUserExist(user)
        users_list.append(user)
        return user
    except ValueError as e:
        return e.__str__()


def errorUserExist(user: Users):
    if (type(search_user(user.id)) == Users):
        raise ValueError(RAISE_ERROR_USEREXIST)
        
##-------------------------------------------------- POST -------------------------------------------------- 

##-------------------------------------------------- PUT -------------------------------------------------- 
@app.put("/user/")
async def user(user: Users):
    try:
        errorUserDosentExist(user)
        for index, value in enumerate(users_list):
            if user.id == value.id:
                users_list[index] = user
                return user
    except Exception as e:
        return e.__str__()
    
def errorUserDosentExist(user:Users):
    if (search_user(user.id) == RAISE_ERROR_USERNOTFOUND):
        raise Exception(RAISE_ERROR_USERNOTFOUND)
##-------------------------------------------------- PUT -------------------------------------------------- 

##-------------------------------------------------- DELETE -------------------------------------------------- 
@app.delete("/user/{id}")
async def user(id:int):
    try:
        if (search_user(id) == RAISE_ERROR_USERNOTFOUND):
            raise Exception(RAISE_ERROR_USERNOTFOUND)
        for i, user in enumerate(users_list):
            if user.id == id:
                return users_list.pop(i)
    except Exception as e:
        return str(e)
##-------------------------------------------------- DELETE -------------------------------------------------- 
