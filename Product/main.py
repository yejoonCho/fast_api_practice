from fastapi import FastAPI
from . import schemas
from . import models
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/product')
def add(request: schemas.Product):
    return request