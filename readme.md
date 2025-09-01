# 📘 Student Management REST API with UI

## 📌 Project Overview

This project demonstrates the core concepts of **REST API** using **FastAPI** as the backend framework and **Streamlit** as the frontend UI.

The backend provides a **Student Management API** with CRUD operations, while the frontend allows users to interact with the API through a simple interface.

It is designed as a **mini learning project** to cover all major REST API concepts:

* Endpoints
* HTTP Methods (GET, POST, PUT, DELETE)
* Path Parameters
* Query Parameters
* Request Body
* JSON Responses
* Status Codes
* API Documentation

---

## ⚙️ Tech Stack

* **Backend**: FastAPI (Python)
* **Frontend**: Streamlit (Python)
* **Server**: Uvicorn (ASGI server)
* **Data Storage**: In-memory Python dictionary (for learning purposes)

---

## 🗂️ Project Structure

```
python_rest_api_project/
│
├── app.py       # FastAPI backend (REST API)
├── ui.py        # Streamlit frontend (UI for CRUD operations)
└── README.md    # Project documentation
```

---

## 🚀 Features

### 🔹 Backend (FastAPI)

* `GET /students` → Retrieve all students
* `POST /students` → Add a new student
* `PUT /students/{id}` → Update a student by ID
* `DELETE /students/{id}` → Delete a student by ID
* `GET /search?name=Alice` → Search student by name
* Built-in **Swagger UI** documentation at `http://127.0.0.1:8000/docs`

### 🔹 Frontend (Streamlit)

* View all students
* Add a new student
* Update an existing student
* Delete a student
* Search for students by name

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the project

```bash
git clone https://github.com/yourusername/python_rest_api_project.git
cd python_rest_api_project
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn streamlit requests
```

### 4️⃣ Start the backend (FastAPI)

```bash
python app.py
```

or

```bash
uvicorn app:app --reload --port 8000
```

### 5️⃣ Start the frontend (Streamlit UI)

```bash
streamlit run ui.py
```

---

## 📡 API Endpoints

| Method | Endpoint             | Description               | Example Request Body    |
| ------ | -------------------- | ------------------------- | ----------------------- |
| GET    | `/students`          | Fetch all students        | –                       |
| POST   | `/students`          | Add a new student         | `{ "name": "Charlie" }` |
| PUT    | `/students/{id}`     | Update student name by ID | `{ "name": "David" }`   |
| DELETE | `/students/{id}`     | Delete a student by ID    | –                       |
| GET    | `/search?name=Alice` | Search student by name    | –                       |

---

## 🖼️ Frontend (UI) Preview

* Sidebar navigation to switch between CRUD operations
* JSON results displayed in structured format
* Error messages for invalid inputs
* Simple and interactive interface

---

## 📖 Learning Outcomes

By completing this project, you will understand:

* What a REST API is and how it works
* How to implement REST API endpoints in FastAPI
* The difference between HTTP methods (GET, POST, PUT, DELETE)
* Using Path Parameters and Query Parameters
* Handling JSON request bodies with Pydantic models
* Returning structured responses and status codes
* How to build a simple UI to interact with an API

---

## 🌟 Future Improvements

* Replace in-memory dictionary with **SQLite / MySQL database**
* Add authentication (JWT tokens)
* Improve UI with tables and forms instead of JSON dumps
* Dockerize the project for easy deployment

---

## 📜 License

This project is open-source and free to use for learning purposes.

---