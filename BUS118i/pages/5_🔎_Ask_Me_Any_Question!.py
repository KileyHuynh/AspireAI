import streamlit as st 
import os
st.set_page_config(
    page_title="Ask AspireAI",
    page_icon="🔎",
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

st.header(":gray[Ask me Anything] 👨🏻‍💻 :violet[-AspireAI]", divider="rainbow")

system_role = """You are AspireAI, a professional business career advisor.
Provide advice and practical tips for business college students."""

with st.form(key = "chat"):
    prompt = st.text_input("🔎 Ask me any career-related question!")    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(get_completion(system_role, prompt))
