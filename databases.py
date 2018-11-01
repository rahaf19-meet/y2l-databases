from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,stock,color,over):
	if price>300:
		print("PRICE TOO HIGH")
	else:
		pro=Product(
			name=name,
			price=price,
			stock=stock,
			color=color,
			over=over,
			)
		session.add(pro)
		session.commit()

def update_product(name,stock):
	pro=session.query(Product).filter_by(name=name).first()
	pro.stock=stock
	session.commit()


def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()

def get_product(id):
  pass

create_product("glasses",50,750,"white",False)
create_product("shoes",60,600,"red",True)
create_product("braclets",400,800,"pink",False)
delete_product("glasses")
update_product("braclets",600)