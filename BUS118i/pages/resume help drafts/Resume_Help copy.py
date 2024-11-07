import streamlit as st
import os
st.set_page_config(
    page_title="Resume Help",
    page_icon="🚀",
)

from openai import OpenAI
client = os.environ["OPENAI_API_KEY"]
openai.api_key = st.secrets["OPENAI_API_KEY"]
def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ]
    )
   return completion.choices[0].message.content

st.title(":red[Career Pathways] 🚀")


input_resume = st.text_area("Input your resume here", height=200)
input_job_description = st.text_area("Input the job description here", height=200)

system_role = """You are AspireAI, a professional business career advisor.
Your job is to directly revise students' resumes to match the job description for higher probability of being selected.
Make the revised text usable in my resume."""

if st.button("Generate Career Paths"):
    prompt = "The resume content is " + input_resume + " and the job description is " + input_job_description
    st.write(get_completion(system_role, prompt))

