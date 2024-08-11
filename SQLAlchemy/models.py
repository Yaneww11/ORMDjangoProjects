from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine


DATABASE_URL = 'postgresql+psycopg2://postgres:password@localhost/sqlAlchemy'
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship('Order')

    def __repr__(self):
        return "<User(id='%i', name='%s', email='%s')>" % (
            self.id,
            self.name,
            self.email,
    )


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return "<Order(id='%i)>" % (
            self.id
        )


