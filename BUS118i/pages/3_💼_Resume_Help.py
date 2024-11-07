import streamlit as st 
import os
st.set_page_config(
    page_title="Resume Help",
    page_icon="📑",
)

from openai import OpenAI
client = os.environ["OPENAI_API_KEY"]
client = st.secrets["OPENAI_API_KEY"]
def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ]
    )
   return completion.choices[0].message.content

st.header(":violet[Resume Help] 💼", divider="rainbow")
st.markdown("Whether you’re starting from scratch or refining an existing document, :violet[**AspireAI**] provides tips to make your resume shine. Get ready to make a lasting impression and boost your job search success!")

#st.subheader("Craft your Resume", divider="gray")
#document = st.radio(
#    "Get started by selecting your document:",
#    ("Resume", "Cover Letter", "Thank You Letter"),
#)
#system_role1 = """As AspireAI, you help students build their resume, cover letter or thank you letter.
#Give general tips for students crafting their document"""
#if st.button("Submit"):
#    prompt1 = "I am a business student building a " + document
#    st.write(get_completion(system_role1, prompt1))
#input_skills = st.text_area("List any relevant experience.", height=200)

st.subheader("📑 Tailor your Resume")

input_resume = st.text_area("Copy and paste your resume here. :red[(Please leave out any personal information.)]", height=200)
input_job_description = st.text_area("Copy and paste the job description here.", height=200)

# system_role2 = """You are AspireAI, a resume editor.
# Change action words in my resume content to better align with the job description and
# highlight relevant skills and experience that would help me secure an interview.
# Also, give advice on what I can add to increase my chance of getting the job.
# Format it into bullet points."""

resume_content = """
[Insert your resume content here]
"""

system_role2 = f"""
You are AspireAI, a resume editor.

- Revise the action words in the following resume content to align better with the job description and emphasize relevant skills and experiences that would enhance my chances of securing an interview.
- Format the output in a professional resume style, including the following sections:
  - Contact Information
  - Summary or Objective
  - Skills
  - Experience
  - Education
  - Certifications (if applicable)

Here is my resume content:
{resume_content}

Additionally, provide bullet-point advice on what I can add or improve to increase my chances of getting the job.
"""

if st.button("Generate Updated Resume"):
    prompt2 = "Here is my current resume content: " + input_resume + " and here is the job description: " + input_job_description
    st.write(get_completion(system_role2, prompt2))

st.caption(":red[NOTE: These results are AI-generated and may not fully reflect your professional experience. Please proofread and make any changes to fit your background.]")