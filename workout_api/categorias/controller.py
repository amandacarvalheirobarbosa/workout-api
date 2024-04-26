from fastapi import APIRouter

router = APIRouter()

@router.post('/', summary='Criar nova categoria')
async def post():
    pass