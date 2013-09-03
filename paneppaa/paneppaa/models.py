from sqlalchemy import (
    Column,
    Integer,
    Text,
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
