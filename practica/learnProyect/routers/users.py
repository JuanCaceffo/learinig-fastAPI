from fastapi import APIRouter, HTTPException
from routers.user import errorUserNotFund, ERROR_USERDONOTEXIST, users_list

router = APIRouter(prefix="/users",tags=["users"])


##-------------------------------------------------- GET -------------------------------------------------- 

@router.get("/")
async def getUsers():
    return users_list

##IMPORTANTE LOS PARAMTEROS  POR PATH SE UTILIZA CUANDO ESTOS VAN FIJOS Y LA QUERY PARA LOS OPCIONALES,
##ADEMAS SI YA EXISTE UN METODO GET CON EL MISMO PATH EL QUE USE QUERYS VAS A TENER QUE CAMBIARLE EL PATH
@router.get("/search",status_code=200)
async def getUsersBy(name: str,lastName: str):
    """Busqueda por nombre y apellido"""
    name = name.lower( )
    lastName = lastName.lower()
    users = [user for user in users_list if (user.name == name and user.lastname == lastName)]
    errorUserNotFund(users)
    return users

##-------------------------------------------------- GET -------------------------------------------------- 

##-------------------------------------------------- DELETE -------------------------------------------------- 

@router.delete("/{name}/{lastName}")
async def deletUsersBy(name:str,lastName:str):
    name = name.lower()
    lastName = lastName.lower()
    global users_list
    USERS = list(filter(lambda user: (user.name != name and user.lastname != lastName), users_list))
    if (len(USERS) == len(users_list)): raise HTTPException(status_code=409,detail=ERROR_USERDONOTEXIST)
    users_list = USERS 

##-------------------------------------------------- DELETE -------------------------------------------------- 
