from datetime import datetime
from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    name: str
    pin: int
    entry_datetime: datetime
    leave_datetime: datetime
