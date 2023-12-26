from sqlalchemy import Column, Integer, String, DateTime

from src.database.database import Base


class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pin = Column(Integer, unique=True)
    entry_datetime = Column(DateTime)
    leave_datetime = Column(DateTime)
