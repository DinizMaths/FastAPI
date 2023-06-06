from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

YOUR_POSTGRESQL_PASSWORD = ""
YOUR_POSTGRESQL_SERVER   = ""

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{YOUR_POSTGRESQL_PASSWORD}@localhost/{YOUR_POSTGRESQL_SERVER}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()