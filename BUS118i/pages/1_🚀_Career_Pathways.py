import streamlit as st 
import os
st.set_page_config(
    page_title="Career Pathways",
    page_icon="🚀",
)

import openai
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

st.header(":red[Career Pathways] 🚀", divider="rainbow")
st.markdown(":violet[**AspireAI**] is here to guide you through your career development! This page offers insights into various job roles, industry trends, and leading companies in your field.")

st.subheader("🗺️ :blue[Job Roles Exploration]")
st.markdown("Learn about job positions by entering your major and interests.")

col1, col2 = st.columns(2)
with col1:
    major = st.selectbox(
        "Business concentration",
        ("Accounting", "Accounting Information Systems (AIS)", "Business Analytics", "Corporate Accounting and Finance", "Entrepreneurship", "Finance", "General Business", "Hospitality, Tourism, Event Management", "Human Resource (HR) Management", "International Business", "Management", "Management Information Systems (MIS)", "Marketing", "Operations and Supply Chain Management"),
        index=None,
        placeholder="Select your major...",
    )
with col2:
    hobby = st.text_input("What are your career interests, hobbies and/or skillsets?")

system_role = """You are AspireAI, a professional business career advisor.
Provide a numbered list of at least 5 job positions for business majors based on their interests/hobbies/skills.
Be detailed and format it as [bolded job position]: [detailed job description].
Also, under each job, briefly show relevant skills and college courses in their major that they should take for entry level jobs.
Bold 'Skills:' and 'Relevant [Major] Courses:' and format it as 'Skills: [skills]' and 'Relevant [Major] Courses: [course], [course], [course]'."""

if st.button("Generate Jobs"):
    prompt = "Your major is: " + major + ", your interest is: " + hobby
    st.write(get_completion(system_role, prompt))


st.subheader("📊 :violet[Industry Insights]")
st.markdown("Discover career trends, skills to develop, and emerging pathways.")

job1 = st.text_input("What job are you interested in learning more about?")

system_role2 = """You are AspireAI, a professional business career advisor.
Provide (1) insights on current trends, (2) key skills to develop, and
(3) any emerging pathways or opportunities I should be aware of."""

system_role4 = """You are AspireAI, a professional business career advisor.
Your output is a URL to a recent public video related to the student's job input.
Ensure the video is currently available and provide the URL in quotes."""

if st.button("Generate Insights"):
    prompt2 = "I am interested in pursuing a career in " + job1
    st.write(get_completion(system_role2, prompt2))

st.subheader("🏢 :green[Explore Companies]")

job2 = st.text_input("What type of job are you looking for?")
city = st.text_input("What location would you like to work at?")
environment = st.text_input("What industry and/or work environment do you see yourself working in?")

if st.button("Research Companies"):
    system_role3 = """You are AspireAI, a professional career advisor.
    Give a description about major companies, considering students' job interests.
    Also, provide 5 descriptions of organizations including startups and established firms."""
#    prompt3 = "For " + major + "majors, What are some notable companies in " + city + " with " + environment + " for " + job2 + "? Provide URL links to their about pages to learn more about them?"
    prompt3 = "What are some companies in this location," + city + " with " + environment + " for " + job2 + "? Provide direct URL links to their about pages to learn more about them."
    st.write(get_completion(system_role3, prompt3))
