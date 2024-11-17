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
st.markdown(":violet[**AspireAI**] offers insights into various job roles, industry trends, and leading companies in your field.")

st.subheader("🗺️ :blue[Job Roles Exploration]")
#st.markdown("Learn about potential career paths by entering your major and interests.")

col1, col2 = st.columns([7,5])
with col1:
    major = st.selectbox(
        "Business concentration",
        ("Accounting", "Accounting Information Systems (AIS)", "Business Analytics", "Corporate Accounting and Finance", "Entrepreneurship", "Finance", "General Business", "Hospitality, Tourism, Event Management", "Human Resource (HR) Management", "International Business", "Management", "Management Information Systems (MIS)", "Marketing", "Operations and Supply Chain Management"),
        index=None,
        placeholder="Select your major...",
    )
    hobby = st.text_input("What are your career interests and/or hobbies?")
with col2:
    st.image("BUS118i/pages/images/CaPa2.webp")

system_role = """You are AspireAI, a professional business career advisor.
Provide a numbered list of at least 5 job positions for business majors based on their interests/hobbies/skills.
Be detailed and format it as [bolded job position]: [detailed job description].
Also, under each job, briefly show relevant skills and college courses in their major that they should take for entry level jobs.
Bold 'Skills:' and 'Relevant Courses:' and format it as 'Skills: [skills]' and 'Relevant Courses: [course], [course], [course]'."""

if st.button("Explore Possible Careers"):
    prompt = "Your major is: " + major + ", your interest is: " + hobby
    st.write(get_completion(system_role, prompt))

st.write("")

st.subheader("📊 :violet[Industry Insights]")
#st.markdown("Discover career trends, skills to develop, and emerging pathways.")

job1 = st.text_input("Which job interests you? You can select one from the results above.")

system_role2 = """You are AspireAI, a professional business career advisor.
Provide (1) insights on current trends, (2) key skills to develop, and
(3) any emerging pathways or opportunities I should be aware of.
Be detailed and format it as [bolded title]: [detailed insights].
Bold 'Current Industry Trends:', 'Key Skills to Develop:', and 'Emerging Opportunities:'.
"""

system_role4 = """You are AspireAI, a professional business career advisor.
Your output is a URL to a recent public video related to the student's job input.
Ensure the video is currently available and provide the URL in quotes."""

if st.button("Discover Industry Trends, Skills to Develop, and Emerging Opportunities"):
    prompt2 = "I am interested in pursuing a career in " + job1
    st.write(get_completion(system_role2, prompt2))

st.write("")

st.subheader("🏢 :green[Major Companies by Location]")

cola, colb = st.columns([7,5])
with cola:
    city = st.text_input("What city would you like to work in?")
    options = ["Open to Any", "Technology", "Financial Services / Banking", "Healthcare / Biotech", "Business Consulting", "Cybersecurity", "E-Commerce and Retail", "Digital Marketing", "Semiconductors and Electronics", "Manufacturing / Supply Chain Management", "Transportation and Logistics", "Real Estate", "Other"]
    environment = st.multiselect("What industry interests you?", options)
    if "Other" in environment:
        other_option = st.text_input("Please specify your option:")
        if other_option:
            environment.remove("Other")
            environment.append(other_option)
#    environment = st.text_input("What industry/work environment do you see yourself in?")
with colb:
    st.image("BUS118i/pages/images/CaPa4.webp")

if st.button("Research Companies"):
    system_role3 = """You are AspireAI, a professional career advisor.
    Give a description about major companies in the user's selected location input and industry input, considering their job interests.
    Also, provide 5 descriptions of organizations including startups and established firms.
    Format it as [bolded company name]: [company description and URL]."""
    e_string = ', '.join(environment)
    prompt3 = "What are some companies in this city, " + city + " in industry " + e_string + " for " + job1 + "? Provide direct URL links to their about pages to learn more about them."
#    prompt3 = "What are some companies in this location," + city + " for " + job1 + "? Provide direct URL links to their about pages to learn more about them."
    st.write(get_completion(system_role3, prompt3))

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(":violet[*Next, learn how to customize your resume for specific job applications here: ➜*]")
with col2:
    st.page_link("pages/3_💼_Resume_Help.py", label=":violet[**Tailor Your Resume**]", icon="💼")