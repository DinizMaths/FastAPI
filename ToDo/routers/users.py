from typing         import Annotated
from pydantic       import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi        import APIRouter, Depends, HTTPException, Path
from starlette      import status
from models         import Todos
from database       import SessionLocal
from .auth          import get_current_user


router = APIRouter(
   prefix="/users",
   tags=["users"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_user():
  pass

@router.post("/")
async def change_password():
  pass