import streamlit as st
import requests
import os
from bs4 import BeautifulSoup

def get_url_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the page title
            title = soup.title.string if soup.title else "No title found"

            # Extract all the text content from the page
            page_text = soup.get_text()

            # Return the title and the text content
            return {
                'title': title,
                'content': page_text
            }
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"
    
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(
    page_title="Resume Help",
    page_icon="🚀",
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

st.title(":red[Career Pathways] 🚀")



st.subheader(":gray[Careers based on your Interests 🎮]", divider="blue")


input_resume = st.text_area("Input your resume here", height=200)
#input_job_description = st.text_area("Input the job description here", height=200)
job_post_url = st.text_input("Insert the URL of the job post")

system_role = """You are AspireAI, a professional business career advisor.
Your job is to directly revise students' resumes to match the job description for higher probability of being selected.
Make the revised text usable in my resume."""

if st.button("Generate Career Paths"):
#    prompt = "The resume content is " + input_resume + " and the job description is " + input_job_description
#    st.write(get_completion(system_role, prompt))
    st.write(get_url_content(job_post_url))