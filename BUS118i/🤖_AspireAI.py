import streamlit as st 
from openai import OpenAI
import OS

#🤖_AspireAI.py
st.set_page_config(
    page_title="AspireAI",
    page_icon="🤖",
)
#st.sidebar.success("Select a page above.")

client = OS.environ("OPENAI_API_KEY")

def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
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

st.write("Discover what steps you can take right now to enhance your career readiness. Plus, get essential networking tips to connect with industry professionals and build meaningful relationships.")
#—such as pursuing internships, setting SMART goals, and engaging in extracurricular activities—
st.subheader(":blue[Ready to explore?]", divider="rainbow")
st.markdown("Navigate through each page to start your career journey today:")

col1, col2, col3 = st.columns(3)
with col1:
   st.image("pages/images/CP.png")
   st.page_link("pages/1_🚀_Career_Pathways.py", label="Learn About Careers", icon="🚀")
   st.image("pages/images/GST.webp")
   st.page_link("pages/4_🌱_Get_Started_Today.py", label="Get Started Today", icon="🌱")
with col2:
   st.image("pages/images/JAI.webp")
   st.page_link("pages/2_🤝_Land_a_Job_or_Internship.py", label="Land a Job or Internship", icon="🤝")
   st.image("pages/images/AMA.webp")
   st.page_link("pages/5_🔎_Ask_Me_Any_Question!.py", label="Ask Me Any Question", icon="🔎")
with col3:
   st.image("pages/images/RH.webp")
   st.page_link("pages/3_💼_Resume_Help.py", label="Tailor Your Resume", icon="💼")
   st.image("pages/images/AbASP2.png")
   st.page_link("pages/6_💡_About_AspireAI.py", label="About AspireAI", icon="💡")