from sqlalchemy import Column,String,Integer
from database import base


class Users(base):

    __tablename__ = "users"

    id = Column(Integer,primary_key = True,index = True )
    username = Column(String,unique = True)
    email = Column(String,unique = True)
    password = Column(String)
    free_game = Column(Integer,default = 5)
