import streamlit as st 
import os
st.set_page_config(
    page_title="Explore MIS Courses",
    page_icon="💻",
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

st.header(":blue[SJSU MIS Courses] 📚", divider="rainbow")
#st.markdown(":violet[**AspireAI**] is here to help you understand how your courses translate into career opportunities, giving you the insights you need to plan your future with confidence.")   
st.markdown("These course descriptions are available on [SJSU](https://www.sjsu.edu/isystems/resume_course_descriptions.php), and you're welcome to include them on your resume!")
st.subheader("👩🏻‍💻 :violet[Explore MIS Courses]")
#st.markdown("*Select a course number(s) to get the description.*")

courses = {
    "BUS4 092 - Introduction to Business Programming": "Employed Python programming (loops, branching, file access, and error handling) and teamwork skills to develop a notebook-based project to access and analyze data from the web.",
    "BUS4 110A - Fundamentals of Management Information Systems": "Leveraged Google Colab and Python data analytics libraries to analyze 10,000 sales records and make value-added business recommendations. Designed an AI-powered solution for a social problem and developed a pitch presentation for industry professionals.",
    "BUS4 110B - Systems Analysis & Design": "Conducted an analysis and design of a web store project. Created a baseline project plan and analyzed client requirements. Developed data flow and use case diagrams in LucidChart. Completed the logical design of the database, studied the UI/UX aspect of the web design and proposed an AWS cloud system architecture.",
    "BUS4 111 - Networking & Data Communications": "Applied TCP-IP Hybrid/OSI framework, critical thinking, and problem-solving skills to design wifi and physical networks using a wifi-inspector, Archiplain and Lucidchart. Visualized and tracked network packets using Wireshark. Encrypted files using AES 512-bit using Veracrypt to enhance file security. Learned how to navigate the dark web and safeguard against online fraud and phishing attacks. Completed the Juniper Networks Certification training program.",
    "BUS4 112 - Database Management Systems": "Designed efficient relational database models that meet business needs by applying entity-relationship diagrams, data modeling, and data normalization. Developed database schema, SQL queries, and stored procedures using MySQL Workbench, data warehousing, business intelligence, and data mining. Familiar with business applications of NoSQL database, big data, MongoDB and the need for transaction management, concurrency control, back-up, disaster recovery, and database security.",
    "BUS4 119A - Practicum in MIS": "Employed Agile / Scrum methodologies to develop a value-added information systems solution for a real-world client while effectively managing project scope, risk, time, cost, quality, human resources, procurement, and client expectations.",
    "BUS4 119B - Business Strategy & Information Systems": "Leveraged research, problem solving, team management, and communication skills to develop a Digital Transformation business case analysis and technology solution plan to help drive profitable revenue growth for a non-tech savvy SMB challenged by larger competitors.",
    "BUS4 118A - Cloud Computing for Data Professionals": "Created a Microsoft (MS) Azure cloud virtual machine (VM) including a web server, applications, and Internet-accessible blob storage container. Established a network security group (NSG) to securely access VMs through a command line interface (CLI) and browser. Provisioned an Azure SQL (relational) Database, Data Lake Storage Gen 2 account, Azure Files and Tables, and an Azure Cosmos DB database for non-relational data, secured with Microsoft Defender for Cloud. Trained, evaluated, deployed, and tested an Azure Machine Learning model. Prepared for the MS Azure Fundamentals (AZ-900) and Data Fundamentals (DP-900) exams.",
    "BUS4 118B - Business Intelligence": "Developed visual analytics business performance management (BPM) interactive dashboards with Tableau to track performance against planned goals. Performed Python predictive analytics applying supervised and unsupervised learning techniques, including simple and multiple linear regression; logistic regression; cluster analysis; association rules mining (market basket analysis); decision trees; and sentiment analysis using text mining to various business use cases.",
    "BUS4 118D - Big Data": "Wrangled and analyzed data using Apache Spark, SQL, Jupyter notebooks, and visualized the results using Tableau. Leveraged teamwork skills and Jupyter notebooks to tell the data story that our analysis revealed regarding a realistic business question based on a large dataset from a social media company.",
    "BUS4 118I - AI for Social Good": "Qualitatively analyzed ethnographic user interviews to identify a local social problem. Designed a conversational agent solution employing IBM Watson Assistant and other IBM services. Evaluated system usefulness and effectiveness via user interviews and presented the final project to industry judges.",
    "BUS4 118W - Web Based Computing": "Programmed client and server-side business applications using HTML, CSS, and JavaScript. Developed a business website by applying UI design principles and wireframes."
}

def get_course_description(course_number):
    """Return the course description based on the course number."""
    return courses.get(course_number, "Course not found.")

user_input = st.multiselect(
    "What courses have you taken before and are currently taking?",
    ["BUS4 092 - Introduction to Business Programming",
     "BUS4 110A - Fundamentals of Management Information Systems",
     "BUS4 110B - Systems Analysis & Design", "BUS4 111 - Networking & Data Communications",
     "BUS4 112 - Database Management Systems",
     "BUS4 119A - Practicum in MIS",
     "BUS4 119B - Business Strategy & Information Systems",
     "BUS4 118A - Cloud Computing for Data Professionals",
     "BUS4 118B - Business Intelligence",
     "BUS4 118D - Big Data",
     "BUS4 118I - AI for Social Good",
     "BUS4 118W - Web Based Computing"
     ],
)

if st.button("Show Course Descriptions"):
    if user_input:
        for course in user_input:
            description = get_course_description(course)
            st.write(f"**{course}:**")
            st.write(description)
    else:
        st.write("Please select at least one course.")

st.subheader("💻 :green[Career Opportunities based on Courses Taken]")

descriptions = []
for course in user_input:
    descriptions.append(f"{course}: {get_course_description(course)}")

if st.button("Explore Career Opportunities"):
    c_string = ', '.join(user_input)
    description_string = "\n".join(descriptions)
    system_role = f"""Provide career opportunities based on courses that the students have taken or are
    currently taking with consideration of the following course descriptions:\n{description_string}.
    Be detailed and format it as a list of [bolded job position]: [detailed relevant skills].
    Also, in a new line under each job, briefly show the corresponding inputted college course(s) that are relevant to those jobs based on the course description.
    Format it as 'Relevant Courses:' [course numbers and names].
    Separate each job with lines."""
    prompt = f"The courses I have or am currently taking are: {c_string}.\nHere are the descriptions of each course:\n{description_string}"
    st.write(get_completion(system_role, prompt))

col1, col2 = st.columns([4,1])
with col1:
    st.markdown(":violet[*Afterward, take a closer look into job insights, skills, and companies on this page:  ➜*]")
with col2:
    st.page_link("pages/2_🚀_Career_Pathways.py", label=":red[**Career Pathways**]", icon="🚀")