import models

from models         import Todos
from pydantic       import BaseModel, Field
from fastapi        import FastAPI, Depends, HTTPException, Path
from database       import engine, SessionLocal
from sqlalchemy.orm import Session
from typing         import Annotated
from starlette      import status

from routers import auth, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)