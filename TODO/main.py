import models

from models         import Todos
from pydantic       import BaseModel, Field
from fastapi        import FastAPI, Depends, HTTPException, Path
from database       import engine, SessionLocal
from sqlalchemy.orm import Session
from typing         import Annotated
from starlette      import status


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()

  try:
    yield db
  finally:
    db.close()

db_depencency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
  title: str = Field(min_length=3)
  description: str = Field(min_length=3, max_length=100)
  priority: int = Field(ge=1, le=5)
  complete: bool


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_depencency):
  return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_depencency, todo_id: int = Path(gt=0)):
  todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

  if todo_model is not None:
    return todo_model
  
  raise HTTPException(status_code=404, detail="Todo Not Found!")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_depencency, todo_request: TodoRequest):
  todo_model = Todos(**todo_request.dict())

  db.add(todo_model)
  db.commit()