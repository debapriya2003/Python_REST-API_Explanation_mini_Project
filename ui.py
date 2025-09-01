import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # FastAPI backend

st.set_page_config(page_title="Student API UI", layout="centered")
st.title("🎓 Student Management API")

# Navigation
menu = ["View All Students", "Add Student", "Update Student", "Delete Student", "Search Student"]
choice = st.sidebar.radio("Navigation", menu)

# 1. View All Students
if choice == "View All Students":
    st.subheader("📋 All Students")
    response = requests.get(f"{API_URL}/students")
    if response.status_code == 200:
        students = response.json()
        if students:
            st.json(students)
        else:
            st.warning("No students found.")
    else:
        st.error("Error fetching students")

# 2. Add Student
elif choice == "Add Student":
    st.subheader("➕ Add New Student")
    name = st.text_input("Enter Student Name")
    if st.button("Add"):
        if name:
            response = requests.post(f"{API_URL}/students", json={"name": name})
            if response.status_code == 200:
                st.success(f"Student Added ✅ ID: {response.json()['id']}")
            else:
                st.error("Failed to add student")
        else:
            st.warning("Please enter a name")

# 3. Update Student
elif choice == "Update Student":
    st.subheader("✏️ Update Student")
    student_id = st.text_input("Enter Student ID to Update")
    new_name = st.text_input("Enter New Name")
    if st.button("Update"):
        if student_id and new_name:
            response = requests.put(f"{API_URL}/students/{student_id}", json={"name": new_name})
            if response.status_code == 200 and "error" not in response.json():
                st.success(f"Updated: {response.json()}")
            else:
                st.error("Student not found ❌")
        else:
            st.warning("Please provide both ID and new name")

# 4. Delete Student
elif choice == "Delete Student":
    st.subheader("🗑️ Delete Student")
    student_id = st.text_input("Enter Student ID to Delete")
    if st.button("Delete"):
        if student_id:
            response = requests.delete(f"{API_URL}/students/{student_id}")
            if response.status_code == 200 and "error" not in response.json():
                st.success(f"Deleted: {response.json()}")
            else:
                st.error("Student not found ❌")
        else:
            st.warning("Please provide a student ID")

# 5. Search Student
elif choice == "Search Student":
    st.subheader("🔍 Search Student by Name")
    search_name = st.text_input("Enter Name to Search")
    if st.button("Search"):
        if search_name:
            response = requests.get(f"{API_URL}/search", params={"name": search_name})
            if response.status_code == 200:
                data = response.json()
                if "message" in data:
                    st.warning("No match found")
                else:
                    st.json(data)
            else:
                st.error("Error searching student")
        else:
            st.warning("Please enter a name")
