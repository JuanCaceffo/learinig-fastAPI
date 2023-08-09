from fastapi import FastAPI
from routers import user,users,products

app = FastAPI()

#for router_ in [user,users,products]:
#    app.include_router(router_.router, prefix=f"/{router_.__name__}", tags=[str(router_.__name__)])
app.include_router(users.router)
app.include_router(user.router)

@app.get("/")
async def saludo():
    return {"message" : "bienvenido a mi API!"}