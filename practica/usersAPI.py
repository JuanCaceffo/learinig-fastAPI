from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

##--------------------------------------- mensjaes error ---------------------------------------
ERROR_USERNOTFOUND = "user not found"
ERROR_USEREXIST = "User exist"
ERROR_USERDONOTEXIST = "User doesn't exist"
##--------------------------------------- mensjaes error ---------------------------------------

##--------------------------------------- Validcaiones ---------------------------------------
def errorUserNotFund(users:list):
    if (len(users) == 0): raise HTTPException(status_code=404,detail=ERROR_USERNOTFOUND)
def errorUserExist(id:int):
    users = list(filter(lambda user: user.id == id,users_list))
    if (len(users) != 0): raise HTTPException(status_code=409,detail=ERROR_USEREXIST)
##--------------------------------------- Validcaiones ---------------------------------------

##-------------------------------------------------- GET -------------------------------------------------- 

@app.get("/users")
async def getUsers():
    return users_list

#para parametrizar un pedido a la api en el path ponemos el parametro que vamos a recibir entre corchetes
#dentro del get
@app.get("/user/{id}",status_code=200)
async def getUserByID(id: int):
    users = list(filter(lambda user: user.id == id, users_list))
    errorUserNotFund(users)
    return list(users)[0]


##busqueda por id utilizando query en vez de path
##la llamada a este get se hace de la siguiente forma
##http://127.0.0.1:8000/userquery/?parametro=dato
@app.get("/userquery/",status_code=200)
async def userQueryId(id: int):
    users = list(filter(lambda user: user.id == id, users_list))
    errorUserNotFund(users)
    return list(users)[0]


@app.get("/userQueryNameLastname/",status_code=200)
async def userQueryNameLastname(name: str,lastName: str):
    """Busqueda por nombre y apellido"""
    name = name.lower( )
    lastName = lastName.lower()
    users = [user for user in users_list if (user.name == name and user.lastname == lastName)]
    errorUserNotFund(users)
    return users

##IMPORTANTE EL PATH SE UTILIZA PAR APARAMETROS QUE VAN FIJOS Y LA QUERY PARA LOS OPCIONALES, (POR CONVENCION)  
##-------------------------------------------------- GET -------------------------------------------------- 

##-------------------------------------------------- POST -------------------------------------------------- 

@app.post("/user/",status_code=201)
async def user(user: Users):
    errorUserExist(user.id)
    users_list.append(user)
        
##-------------------------------------------------- POST -------------------------------------------------- 

##-------------------------------------------------- PUT -------------------------------------------------- 


@app.put("/user/",status_code=201)
async def user(user: Users):
    try:   
        index = [user_.id for user_ in users_list].index(user.id)
        users_list[index] = user
    except ValueError:    
        raise HTTPException(status_code=404,detail=ERROR_USERDONOTEXIST)
##-------------------------------------------------- PUT -------------------------------------------------- 

##-------------------------------------------------- DELETE -------------------------------------------------- 
@app.delete("/user/{id}")
async def user(id:int):
    try:
        index = [user.id for user in users_list].index(id)
        users_list.pop(index)
    except ValueError:
        raise HTTPException(status_code=404,detail=ERROR_USERDONOTEXIST)

@app.delete("/user/{name}/{lastName}")
async def user(name:str,lastName:str):
    name = name.lower()
    lastName = lastName.lower()
    global users_list
    USERS = list(filter(lambda user: (user.name != name and user.lastname != lastName), users_list))
    if (len(USERS) == len(users_list)): raise HTTPException(status_code=409,detail=ERROR_USERDONOTEXIST)
    users_list = USERS 

##-------------------------------------------------- DELETE -------------------------------------------------- 
