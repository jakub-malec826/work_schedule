from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.database.actions.EmployeeActions import EmployeeActions

from src.database.database import get_db
from src.request_type.EmployeeRequest import EmployeeRequest


employee_router = APIRouter(prefix="/employee", tags=["Employee"])

db = get_db()


@employee_router.get("/get_all")
async def get_all():
    print(EmployeeActions.fetch_all(db))
    return JSONResponse(jsonable_encoder(EmployeeActions.fetch_all(db)))


@employee_router.post("/create")
async def create_new(request: EmployeeRequest):
    return JSONResponse(EmployeeActions.create(db, request=request))


@employee_router.delete("/remove/{pin}")
async def remove(pin: int):
    return JSONResponse(EmployeeActions.remove(db, pin))


@employee_router.get("/start-end-work/{pin}")
async def login(pin: int):
    return JSONResponse(EmployeeActions.start_end_work(db, pin))
