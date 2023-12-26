from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.database.database import *
from src.routes.employee_router import employee_router


app = FastAPI()


app.include_router(employee_router)

Base.metadata.create_all(engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return JSONResponse(status_code=200, content={"message": "Work"})


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
