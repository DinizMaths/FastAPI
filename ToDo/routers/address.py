import sys

sys.path.append("..")

from typing  import Optional, Annotated
from fastapi import Depends, APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception

router = APIRouter(
  prefix="/address",
  tags=["address"],
  responses={404: {"description": "Not found"}}
)

def get_db():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

db_dependency   = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class AddressRequest(BaseModel):
  address1:    str
  address2:    Optional[str]
  city:        str
  state:       str
  country:     str
  postal_code: str
  apt_num:     Optional[int]


@router.post("/")
async def create_address(address: AddressRequest, user: user_dependency, db: db_dependency):
  if user is None:
    raise get_user_exception()

  address_model = models.Address()

  address_model.address1    = address.address1
  address_model.address2    = address.address2
  address_model.city        = address.city
  address_model.state       = address.state
  address_model.country     = address.country
  address_model.postal_code = address.postal_code
  address_model.apt_num     = address.apt_num

  db.add(address_model)
  db.flush()

  user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()

  user_model.address_id = address_model.id

  db.add(user_model)

  db.commit()