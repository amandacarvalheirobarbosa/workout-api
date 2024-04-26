from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Av. Francisco Junqueira', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', example='João', max_length=30)]
