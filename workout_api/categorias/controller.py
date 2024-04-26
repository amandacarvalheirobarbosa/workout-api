from uuid import uuid4
from fastapi import APIRouter, Body, status
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.categorias.models import CategoriaModel

from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/',
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def post(
    db_session: DatabaseDependency,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.dict())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    # breakpoint()
    pass