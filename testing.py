from sqlalchemy import create_engine
import sqlalchemy.orm

engine = create_engine('mysql://root:example@localhost:3306/mysql')
session = sqlalchemy.orm.Session(engine)

session.execute("select * from meme")
session.commit()
