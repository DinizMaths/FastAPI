import models

from models import Todos

from fastapi  import FastAPI, Depends
from database import engine, SessionLocal

from sqlalchemy.orm import Session

from typing import Annotated


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()

  try:
    yield db
  finally:
    db.close()

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
  return db.query(Todos).all()