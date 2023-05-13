from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#from datetime import datetime

Base = declarative_base()


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    intro = Column(String(300), nullable=False)
    text = Column(Text, nullable=False)
    #date = Column(DateTime, default=datetime.utcnow)
    archive = Column(Text, nullable=False)

    def __repr__(self):
        return '<Article %r' % self.id


engine = create_engine('sqlite:///articles.db')
Base.metadata.create_all(engine)
