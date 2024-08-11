import random

from sqlalchemy.orm import sessionmaker
from models import User, engine, Order

Session = sessionmaker(bind=engine)
with Session() as session:
    users = session.query(User).all()
    for user in users:
        print(f"{user.name} have these orders: {user.orders}")
    session.commit()
