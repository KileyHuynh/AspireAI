import streamlit as st 
import os
st.set_page_config(
    page_title="For MIS Majors",
    page_icon="💻",
)

st.header(":blue[MIS Course Search] 💻", divider="rainbow")
st.markdown("Select a course number(s) to get the description.")

courses = {
    "CS101": "Introduction to Programming: Learn the basics of programming using Python.",
    "CS102": "Data Structures: Explore various data structures and their applications.",
    "WD201": "Web Development: Build dynamic websites using HTML, CSS, and JavaScript.",
    "ML202": "Machine Learning: Understand the fundamentals of machine learning and its techniques."
}

def get_course_description(course_number):
    """Return the course description based on the course number."""
    return courses.get(course_number, "Course not found.")

# Streamlit UI components
st.title("Course Finder App")
st.write("Enter a course number to get the description.")

# User input for the course number
user_input = st.text_input("Course Number (e.g., CS101, CS102, etc.):")

if user_input:
    # Get the course description
    description = get_course_description(user_input)
    
    # Display the course description
    st.write(f"Course Description for {user_input}:")
    st.write(description)

    # Prompt for career opportunities
    prompt = f"Provide career opportunities based on courses that the students have taken or are currently taking with consideration of the following course descriptions: {description}"
    st.write("Prompt for career opportunities:")
    st.write(prompt)