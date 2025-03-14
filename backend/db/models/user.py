from db.base_class import Base         # from db.base_class import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    course_of_interest = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
#    blogs = relationship("Blog", back_populates="author")


