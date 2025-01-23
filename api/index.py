from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"], 
)

with open("q-vercel-python.json") as f:
    student_data = json.load(f)

def get_marks_by_name(name):
    for student in student_data:
        if student["name"].lower() == name.lower():
            return student["marks"]
    return None

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [get_marks_by_name(student_name) for student_name in name]
    return JSONResponse(content={"marks": marks})
