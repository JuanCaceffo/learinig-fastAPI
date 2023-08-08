from fastapi import APIRouter

router = APIRouter()

produtct_list = ["product 1", "product 2","product 3","product 4"]

@router.get("/")
async def products():
    return produtct_list