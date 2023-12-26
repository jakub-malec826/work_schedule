from datetime import date, datetime
from sqlalchemy.orm import Session

from src.database.models.EmployeeModel import EmployeeModel
from src.request_type.EmployeeRequest import EmployeeRequest


class EmployeeActions:
    def start_end_work(db: Session, pin: int):
        db_employee = db.query(EmployeeModel).filter(EmployeeModel.pin == pin).first()
        if db_employee:
            if db_employee.entry_datetime is None:
                db_employee.entry_datetime = datetime.now()
                db_employee.leave_datetime = None
                db.commit()
                db.refresh(db_employee)
                return {"message": "login successful", "success": True}
            else:
                db_employee.leave_datetime = datetime.now()
                db_employee.entry_datetime = None
                db.commit()
                db.refresh(db_employee)
                return {"message": "logout successful", "success": True}
        else:
            return {"message": "bad pin", "success": False}

    def create(db: Session, request: EmployeeRequest):
        db_employee = (
            db.query(EmployeeModel).filter(EmployeeModel.pin == request.pin).first()
        )

        if db_employee:
            return {"message": "pin already in database", "success": False}
        else:
            employee = EmployeeModel(name=request.name, pin=request.pin)
            db.add(employee)
            db.commit()
            db.refresh(employee)
            return {"message": "user created", "success": True}

    def fetch_all(db: Session):
        return db.query(EmployeeModel).all()

    def remove(db: Session, pin: int):
        db_employee = db.query(EmployeeModel).filter(EmployeeModel.pin == pin).first()
        if db_employee:
            db.delete(db_employee)
            db.commit()
            return {"message": "user removed", "success": True}
        else:
            return {"message": "bad pin", "success": False}
