from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

URL_DATABASE = "sqlite:///db/game.db"

engine = create_engine(URL_DATABASE,connect_args = {"check_same_thread":False})
session = sessionmaker(autoflush = False,autocommit = False,bind = engine)
base = declarative_base()
