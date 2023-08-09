from fastapi import APIRouter

router = APIRouter()
##--------------------------------------- base de datos imaginara ---------------------------------------
produtct_list = ["product 1", "product 2","product 3","product 4"]
##--------------------------------------- base de datos imaginara ---------------------------------------

@router.get("/")
async def products():
    return produtct_list