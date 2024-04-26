from fastapi import APIRouter, status

router = APIRouter()

@router.post(
    '/',
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED
)
async def post():
    pass