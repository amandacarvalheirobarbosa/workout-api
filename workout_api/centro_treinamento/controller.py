from fastapi import APIRouter

router = APIRouter()

@router.post('/', summary='Criar novo centro de treinamento')
async def post():
    pass