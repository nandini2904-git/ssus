import streamlit as st
from database.mongodb import students_collection

st.title("Student Registration")

first_name = st.text_input(
    "first_name"
)

last_name = st.text_input(
    "last name"
)

email = st.text_input(
    "email"
    
)
course = set.text_input(
    "course"
)

if st.button("registration student"):
    students_collection.insert_one({
        "first_name": first_name,
        "last_name": last_name,""
        "email": email,
        "course": course

    })

    st.success(
        "Student Registered Successfully"
    )