# 📌 Mini Python REST API Project
# 1. REST API (Definition)
# REST (Representational State Transfer) is an architectural style for designing APIs.
# REST APIs use HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources,
# typically represented in JSON format.
###############################################################################
# 2. Endpoint (Definition)
# Endpoint is a specific URL where an API resource can be accessed.
# For example, /students is an endpoint to fetch or create students.
# Code:
#------------------------------------------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to Student API"}
#---------------------------------------------------------------------------
# Explanation:
# FastAPI() creates the API app.
# @app.get("/") defines the root endpoint that responds to a GET request.
# Visiting http://127.0.0.1:8000/ returns {"message": "Welcome to Student API"}.
##############################################################################
# 3. GET Method (Definition)
# GET is used to retrieve information from the server without modifying it.
# Code:
#------------------------------------------------------------------------------
students = {"1": "Alice", "2": "Bob"}
@app.get("/students")
def get_students():
    return students
#------------------------------------------------------------------------------
# Explanation:
# /students endpoint fetches all students.
# GET request returns data without changing anything.
#################################################################################
# 4. POST Method (Definition)
# POST is used to create a new resource on the server.
# Code:
#------------------------------------------------------------------------------
class Student(BaseModel):
    name: str
@app.post("/students")
def add_student(student: Student):
    new_id = str(len(students) + 1)
    students[new_id] = student.name
    return {"id": new_id, "name": student.name}
#------------------------------------------------------------------------------
# Explanation:
# BaseModel ensures input validation (expects a JSON body with name).
# A new student is added to the dictionary.
# Returns the new student’s ID and name.
#################################################################################
# 5. PUT Method (Definition)
# PUT is used to update an existing resource.
# Code:
#------------------------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):
    if student_id in students:
        students[student_id] = student.name
        return {"id": student_id, "updated_name": student.name}
    return {"error": "Student not found"}
#------------------------------------------------------------------------------
# Explanation:
# {student_id} is a path parameter.
# Updates student’s name if ID exists.
# Returns an error if student not found.
##########################################################################################
# 6. DELETE Method (Definition)
# DELETE removes a resource from the server.
# Code:
#------------------------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    if student_id in students:
        deleted = students.pop(student_id)
        return {"deleted_id": student_id, "deleted_name": deleted}
    return {"error": "Student not found"}
#------------------------------------------------------------------------------
# Explanation:
# Removes student if ID exists.
# Returns deleted student details, else error message.
#########################################################################################
# 7. Query Parameters (Definition)
# Query parameters are used to filter or
# customize data in a request (e.g., /students?name=Alice).
# Code:
#------------------------------------------------------------------------------
@app.get("/search")
def search_student(name: str):
    results = {id: n for id, n in students.items() if n == name}
    return results or {"message": "No match found"}
#------------------------------------------------------------------------------
# Explanation:
# Accepts name as a query parameter.
# Filters students by name.
# Returns matching students.
#####################################################################################
# 8. Status Codes (Definition)
# Status codes indicate the result of an API request (e.g., 200 OK, 404 Not Found, 201 Created).
# Code:
#------------------------------------------------------------------------------
from fastapi import status
from fastapi.responses import JSONResponse

@app.get("/check/{student_id}")
def check_student(student_id: str):
    if student_id in students:
        return JSONResponse(content={"id": student_id, "name": students[student_id]}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"error": "Not found"}, status_code=status.HTTP_404_NOT_FOUND)
#------------------------------------------------------------------------------
# Explanation:
# 200 OK returned if student exists.
# 404 Not Found returned if student not found.
#####################################################################################
# 9. Request Body (Definition)
# Request Body contains the data sent by the client (mainly in POST/PUT requests).
# Already demonstrated in POST and PUT methods using Student(BaseModel).
####################################################################################
# 10. JSON (Definition)
# JSON (JavaScript Object Notation) is the standard format used in REST APIs for request and response data.
# Example Response:
# {
#   "id": "1",
#   "name": "Alice"
# }
##########################################################################################
# ✅ This project covers all core REST API concepts:
# Endpoints
# GET, POST, PUT, DELETE
# Path & Query Parameters
# Status Codes
# Request Body
# JSON
######################################################################
#Code to begin the server
#code:
#---------------------------------------------------------
# ✅ Add server start point
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
#------------------------------------------------------------------------
