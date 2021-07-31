from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///personal_helper.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

 

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(25))
    birthday = Column(String(25), nullable=True)


class Phone(Base):
    __tablename__ = 'phone'
    
    id = Column(Integer, primary_key=True)
    phone = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


Base.metadata.create_all(engine)
Base.metadata.bind = engine


for person in session.query(User).filter(User.name.like('%or%')):
    print(person.name, person.email)






