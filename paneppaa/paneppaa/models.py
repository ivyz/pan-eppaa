from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    born_year = Column(Integer)
    description = Column(Text)
    size = Column(Text)
    kind = Column(Text)
    image = Column(Text)

    def __init__(self, name, born_year, description, size, kind, image):
        self.name = name
        self.born_year = born_year
        self.description = description
        self.size = size
        self.kind = kind
        self.image = image

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    date = Column(Date)
    description = Column(Text)
    image = Column(Text)

    def __init__(self, title, date, description, image=None):
        self.title = title
        self.description = description
        self.date = date
        self.image = image

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    date = Column(Date)
    text = Column(Text)
    image = Column(Text)
    video = Column(Text)

    def __init__(self, title, date, text, image=None, video=None):
        self.title = title
        self.text = text
        self.date = date
        self.image = image
        self.video = video
