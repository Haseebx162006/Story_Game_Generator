from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

engine = create_engine(settings.DATABASE_URL)

session=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base

def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()
        
        
def create_tables():
    Base.metadata.create_all(bind=engine)
