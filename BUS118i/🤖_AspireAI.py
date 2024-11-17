import streamlit as st 
import openai
import os

#test

#🤖_AspireAI.py
st.set_page_config(
    page_title="AspireAI",
    page_icon="🤖",
)
#st.sidebar.success("Select a page above.")

openai.api_key = os.environ["OPENAI_API_KEY"]
def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
   completion = openai.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ]
    )
   return completion.choices[0].message.content
system_role = """You are Aspire, a professional business career advisor.
Provide detailed advice and practical tips for college students
in Business majors."""

#Home page
st.title("Welcome to :violet[AspireAI] 🤖")
st.markdown("""Introducing your ultimate Business Career Advisor! Designed specifically for SJSU students,   
:violet[**AspireAI**] equips you with valuable industry insights, skills and tips to help you succeed.
""")

st.write("Discover what steps you can take right now to enhance your career readiness. Plus, learn how to set SMART career goals and tailor your resume to align with specific job applications.")

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(":green[*Get started by exploring MIS courses and the career opporunities they offer: ➜*]")
with col2:
    st.page_link("pages/1_📚_Explore_MIS_Courses.py", label=":blue[**Explore MIS Courses**]", icon="📚")

st.subheader(":blue[Ready to explore?]", divider="rainbow")
st.markdown("Navigate through each page to begin your career journey today.")

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.image("BUS118i/pages/images/MIS.webp")
   st.page_link("pages/1_📚_Explore_MIS_Courses.py", label="Explore MIS Courses")
with col2:
   st.image("BUS118i/pages/images/CP.png")
   st.page_link("pages/2_🚀_Career_Pathways.py", label="Learn About Careers")
with col3:
   st.image("BUS118i/pages/images/RH.webp")
   st.page_link("pages/3_💼_Resume_Help.py", label="Tailor Your Resume")
with col4:
   st.image("BUS118i/pages/images/GST.webp")
   st.page_link("pages/4_🌱_Get_Started_Today.py", label="Get Started Today")

st.write("")

st.subheader(":gray[Ask me Anything] 👨🏻‍💻 :violet[-AspireAI]", divider="rainbow")

system_role = """You are AspireAI, a professional business career advisor.
Provide advice and practical tips for business college students."""

with st.form(key = "chat"):
    prompt = st.text_input("🔎 Ask me any career-related question!")    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(get_completion(system_role, prompt))