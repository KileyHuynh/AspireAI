import datetime
import streamlit as st 
import os
st.set_page_config(
    page_title="Start Today",
    page_icon="🌱",
)

from openai import OpenAI
client = os.environ["OPENAI_API_KEY"]

def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ]
    )
   return completion.choices[0].message.content

st.header(":green[Get Started Today] 🌱", divider="rainbow")
st.markdown("With :violet[**AspireAI**], you can develop SMART goals, explore extracurriculars, and find courses that align with your career aspirations—all supported by tailored resources and expert guidance.")

col1, col2 = st.columns([3,2])
with col1:
    st.subheader("🎯 Develop SMART Goals")
    options = ["Resume Building", "Job or Internship Search", "Networking", "Skill Development", "Other (please specify)"]
    o = st.radio("**Type of Goal:**", options)
    if o == "Other (please specify)":
        free_text = st.text_input("Please specify your goal type:")
with col2:
    st.image("BUS118i/pages/images/SG.webp")

s = st.text_input("""
:blue-background[:blue[**Specific:**]] What career goal do you want to accomplish? Please provide as much detail as you can.   
:gray[(Example: “Secure a summer internship in my desired field by applying to at least 10 positions a week.")] """)

M,A,RT = st.columns([2,3,3])
   
with M:
    options = ["Resume critiques", "Jobs applied", "Events attended", "Other"]
    m = st.radio(":green-background[:green[**Measurable:**]] How will you track your progress?", options)
    if m == "Other":
        free_text = st.text_input("Please specify your metrics:")

with A:
    a = st.text_area(":orange-background[:orange[**Achievable:**]] List any skills/resources you have that are relevant to this goal:",height=100)
with RT:
    r = st.multiselect(
    ":red-background[:red[**Relevant:**]] What are the career benefits?",
    ["Career Advancement", "Skill Development", "Job Security", "Enhanced Work Experience", "Professional Network Growth", "Higher Job Satisfaction", "Increased Confidence"],
)
    t = st.date_input(":violet-background[:violet[**Time-bound:**]] What's your target deadline?", value=None, format="MM/DD/YYYY")

system_role = """You are AspireAI, a professional business career advisor.
    Use the student's input to develop a detailed one to two sentence SMART goal. Make it easy for college students to understand.
    Then, provide specific action steps with due dates using the suggested deadline starting with today's date. Include the time it would take to complete each task by minutes/hours
    Format it as bolded SMART Goal:
    Then bold Action Steps:
    1. new line 2. etc."""

if st.button("Generate Your SMART Goal & Action Plan"):
    r_string = ', '.join(r)
    if t is not None:
        t_string = t.strftime("%m/%d/%Y")
    else:
        t_string = "No deadline set"
    prompt = "My goal type is:" + o + ". My S is " + s + ". My M is " + m + ". My skills/resources are " + a + ". My long-term career aspirations are " + r_string + ". My T is " + t_string
    st.write(get_completion(system_role, prompt))

st.subheader("📚 :blue[College Courses (MIS Prototype)]")
system_role2 = """You are AspireAI, a professional business career advisor.
    Use the student's input to generate a list of useful college course titles."""

hobby = st.text_input("What are your career interests, hobbies and/or skillsets?")


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