import streamlit as st 
import os
st.set_page_config(
    page_title="Jobs and Internships",
    page_icon="🤝",
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

st.header(":blue[Land a Job or Internship] 🤝", divider="rainbow")
st.markdown(":violet[**AspireAI**] is here to guide you through your career development! This page offers insights into various job roles, industry trends, and leading companies in your field.")
