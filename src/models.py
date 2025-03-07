import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userID = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False) 
    firstName  = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

class Follower (Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    followID = Column(Integer, ForeignKey('user.id'))
    followerID= Column(Integer, ForeignKey('person.id'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    postID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('user.id'))
    likes = Column(Integer)
    hashtag = Column(Integer)

class Reels(Base):
    __tablename__ = 'reels'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    reelID= Column(Integer, primary_key=True)
    url = Column(String(250))
    postID = Column(Integer, ForeignKey('post.id'))
    hashtagreel = Column(Integer)

class Commets(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    CommentID = Column(Integer, primary_key=True)
    commentText = Column(String(250))
    authorID = Column(Integer, ForeignKey('user.id'))
    authorcommentID = Column(Integer, ForeignKey('person.id'))
    postID = Column(Integer, ForeignKey('post.id'))
    
class Engagement(Base):
    __tablename__ = 'engagement'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    engagementID = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('post.id'))
    likestomyPOST = Column(Integer)
    commentstomyPOST=  Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
