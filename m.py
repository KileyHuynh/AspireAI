courses = {
    "CS101": "Introduction to Programming: Learn the basics of programming using Python.",
    "CS102": "Data Structures: Explore various data structures and their applications.",
    "WD201": "Web Development: Build dynamic websites using HTML, CSS, and JavaScript.",
    "ML202": "Machine Learning: Understand the fundamentals of machine learning and its techniques."
}

def get_course_description(course_number):
    """Return the course description based on the course number."""
    return courses.get(course_number, "Course not found.")

# Example usage
while True:
    user_input = input("Enter a course number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    description = get_course_description(user_input)
    print(description)

prompt = "Provide career opportunities based on courses that the students have taken or are currently taking with consideration of the following course descriptions:"
+ description

#Provide career opportunities based on courses that the students have taken or are currently taking with consideration of the following course descriptions with reference to which courses correspond to the suggested job title. Group the results by job title