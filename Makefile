run:
	@uvicorn workout_api.main:app --reload


create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

