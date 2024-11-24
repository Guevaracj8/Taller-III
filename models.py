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
    
studentsList = []

@app.get("/students/")
def listOfStudents():
    return studentsList
    
@app.post("/students/")
async def create_student(student: Student):
    info = {"Students": student}
    studentsList.append(student)
    return info

@app.put("/students/{id}")
async def update_student(id: int, student: Student):
    for stu in studentsList:
        if stu.id == id:
            index = studentsList.index(stu)
            studentsList[index] = student
    return student

@app.delete("/students/{id}")
async def delete_student(id: int):
    for stu in studentsList:
        if stu.id == id:
            index = studentsList.index(stu)
            del studentsList[index]
    return {"mensaje": "Student Deleted Correctly."}
    
    
