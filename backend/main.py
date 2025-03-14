from fastapi import FastAPI
from core.config import settings

from db.session import engine
from db.base_class import Base

from apis.base import api_router


def include_router(app):
	app.include_router(api_router)

#app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


def create_tables():
    Base.metadata.create_all(bind=engine)

        
def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
#    create_tables()  # This should be removed if we are going to use alembic to create the tables
    include_router(app)
    return app


app = start_application()

@app.get("/")
def hello():
    return {"msg": "Hello FastAPI"}  # This will return a json output
