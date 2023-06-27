import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False,unique=True)
    firtname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False,unique=True)

class Foollower(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("users.ID"),nullable=False)
    user_to_id = Column(Integer, ForeignKey("users.ID"),nullable=False)



class Media(Base):
    __tablename__ = 'medias'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False )
    url = Column(String(250), nullable=False)
    post_id = Column(Integer,ForeignKey("posts.ID"), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.ID"),nullable=False)


class Comment(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    autor_id = Column(Integer, ForeignKey("users.ID"),nullable=False)
    post_id = Column(Integer, ForeignKey("posts.ID"),nullable=False)
    
def to_dict(self):
    return {}



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
