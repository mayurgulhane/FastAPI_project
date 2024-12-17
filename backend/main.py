from  fastapi import FastAPI
from core.config import settings
from apis.base import api_router
from db.session import engine
# from db.base import Base

# def create_tables():
#     Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title= settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    # create_tables()
    return app

app = start_application()

@app.get("/")
def hello():
    return {"msg":"Hello FastApi"}