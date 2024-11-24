from typing import List, Set, Union
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from datetime import date


app = FastAPI()

class Contents(BaseModel):
    name: str
    description: str
    
class subjects(BaseModel):
    
    name: str
    levelToCourse: str
    creditUnits: float
    price: float
    description: str
    content: List[Contents]

class Student(BaseModel):
    
    id: int
    name: str
    lastname: str
    birthDate: date
    phone: str
    address: str
    academicRecord: List[subjects]
    
@app.post("/students/")
async def create_student(student: Student):
    info = {"Students": student}
    return info
    
    