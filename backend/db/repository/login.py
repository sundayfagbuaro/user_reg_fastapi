from sqlalchemy.orm import Session
from db.models.user import User
from core.hashing import Hasher


def get_user_by_email(email: str, db: Session):
        user = db.query(User).filter(User.email==email).first()
        return user

# Create a function to authenticate the user. This will take email, password and db session
def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email=email, db=db)
    print(user)                 # This will print the user if it exists in the database
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user
