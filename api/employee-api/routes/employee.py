from datetime import datetime
import os
from uuid import uuid5, NAMESPACE_DNS
import re

from fastapi import APIRouter, HTTPException, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from models.Employee import EmployeeModel, UpdateEmployeeModel
from database.connection import Connection

router = APIRouter(
    prefix="/v1/employee",
    tags=["employee"],
    responses={404: {"description": "Not found"}},
)

database_connection = Connection()
db = database_connection.setCollectionConnection("employee")

@router.post("/", response_description="Add new employee", response_model=EmployeeModel, status_code=201)
async def create_employee(employee: EmployeeModel = Body(...)):
    employee = jsonable_encoder(employee)
    new_employee = await db.insert_one(employee)
    created_employee = await db.find_one({"_id": new_employee.inserted_id})
    return created_employee

@router.get("/", response_description="List all employees", response_model=List[EmployeeModel], status_code=200)
async def list_employees():
    employees = await db.find().to_list(1000)
    return employees

@router.get("/{nome}", response_description="Get a single employee", response_model=EmployeeModel, status_code=200)
async def show_employee(nome: str):
    rgx = re.compile(f'.*{nome}.*', re.IGNORECASE)
    if (employee := await db.find_one({"nome": rgx})) is not None:
        return employee

    raise HTTPException(status_code=404, detail=f"Employee with {nome} on the name has not found")

@router.put("/{matricula}", response_description="Update a employee", response_model=EmployeeModel, status_code=200)
async def update_employee(matricula: str, employee: UpdateEmployeeModel = Body(...)):
    employee = {k: v for k, v in employee.dict().items() if v is not None}

    if len(employee) >= 1:
        update_result = await db.update_one({"matricula": matricula}, {"$set": employee})

        if update_result.modified_count == 1:
            if (updated_employee := await db.find_one({"matricula": matricula})) is not None:
                return updated_employee

    if (existing_employee := await db.find_one({"matricula": matricula})) is not None:
        return existing_employee

    raise HTTPException(status_code=404, detail=f"Employee with matricula {matricula} not found")

@router.delete("/{matricula}", response_description="Delete a employee", status_code=200)
async def delete_employee(matricula: str):
    delete_result = await db.delete_one({"matricula": matricula})

    if delete_result.deleted_count == 1:
        return 'Employee was deleted!'

    raise HTTPException(status_code=404, detail=f"Employee with matricula {matricula} not found")