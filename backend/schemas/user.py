from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    first_name: str = Field(..., )
    last_name: str
    username: str
    email: EmailStr
    password: str = Field(..., min=4)
    course_of_interest: str


class ShowUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    course_of_interest: str
    is_active: bool

    class Config:
        orm_mode = True


class UpdateUser(UserCreate):
        pass
