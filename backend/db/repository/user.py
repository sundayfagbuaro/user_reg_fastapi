from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User         # This will allow us to create an instance of the User class
from core.hashing import Hasher
from schemas.user import UpdateUser 


def create_new_user(user: UserCreate, db: Session):
    user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        username = user.username,
        email = user.email,                                 # This will be the email supplied by the user
        password = Hasher.get_password_hash(user.password), # The palin password
        course_of_interest = user.course_of_interest,
        is_active = True)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retrieve_user(id: int, db: Session):
    user = db.query(User).filter(User.id==id).first()
    return user

def list_users(db: Session):
    users = db.query(User).filter(User.is_active==True).all()
    return users

def update_user_by_id(id: int, user: UpdateUser, db: Session):
        user_in_db = db.query(User).filter(User.id==id).first()
        if not user_in_db:
            return
        user_in_db.first_name = user.first_name
        user_in_db.last_name = user.last_name
        user_in_db.username = user.username
        user_in_db.email = user.email
        user_in_db.course_of_interest = user.course_of_interest
        db.add(user_in_db)
        db.commit()
        return user_in_db

def delete_user_by_id(id: int, db: Session):
        user_in_db = db.query(User).filter(User.id==id)
        if not user_in_db.first():                      # .first will give us an instance of the blog
            return {"error": f"The user with the id {id} could not be found"}
        user_in_db.delete()
        db.commit()
        return {"msg": "The user with id {id} has been successfully deleted"}
