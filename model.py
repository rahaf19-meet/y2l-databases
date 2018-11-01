from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    id = Column(Integer, primary_key= True)
    __tablename__ = 'products'
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    color = Column(String)
    over= Column(Boolean)

