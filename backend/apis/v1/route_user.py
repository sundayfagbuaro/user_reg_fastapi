from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.user import UserCreate, ShowUser, UpdateUser
from db.session import get_db

from db.repository.user import create_new_user, retrieve_user, list_users, update_user_by_id, delete_user_by_id

from fastapi import status
from typing import List

#Create an instance of APIRouter
router = APIRouter()


@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)   # The / is the endpoint
def create_user(user: UserCreate, db: Session = Depends(get_db)):  # db of type Session. DB generator will give us a database session
    user = create_new_user(user=user, db=db)  # Pass the user we have received from the FE and the DB session
    return user

@router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = retrieve_user(id=id, db=db)
    if not user:
        raise HTTPException(detail=f"User with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    return user

@router.get("/", response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.put("/{id}", response_model=ShowUser)
def update_a_user(id: int, user: UpdateUser, db: Session = Depends(get_db)):
        user = update_user_by_id(id=id, user=user, db=db)
        if not user:
            raise HTTPException(detail=f"The user with the id {id} does not exist")
        return user

@router.delete("/{id}")
def delete_a_user(id: int, db: Session = Depends(get_db)):
    message = delete_user_by_id(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": message.get("msg")}
