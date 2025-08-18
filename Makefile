run:
	@uvicorn paleodex_api.main:app --reload

create-migrations:
	@PYTHONPATCH=$PYTHONPAH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATCH=$PYTHONPAH:$(pwd) alembic upgrade head
