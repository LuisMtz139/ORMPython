from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255))

class UserRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(session_factory)

    def get_all_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    def get_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        if user:
            return {'id': user.id, 'name': user.name, 'email': user.email}
        else:
            return None

    def create_user(self, user_data):
        session = self.Session()
        new_user = User(name=user_data['name'], email=user_data['email'])
        session.add(new_user)
        session.commit()
        user_dict = {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}
        session.close()
        return user_dict
    
    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
