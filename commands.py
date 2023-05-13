from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Article, Base

engine = create_engine('sqlite:///band-list.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)

session = DBsession()

# CREATE
articleOne = Article(title=" ", intro=" ", text=" ")
session.add(articleOne)
session.commit()

# READ
all_articles = session.query(Article).all()
first_article = session.query(Article).first()

# UPDATE
editedArticle = session.quary(Article).filter_by(id=1).one()
editedArticle.title = " "
session.add(editedArticle)
session.commit()

# DELETE
articleToDelete = session.query(Article).filter_by(title=' ').one()
session.delete(articleToDelete)
session.commit()
