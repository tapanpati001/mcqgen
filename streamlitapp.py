# import os
# import json
# import traceback
# import pandas as pd
# from dotenv import load_dotenv
# from src.mcqgen.utils import read_file,get_table_data
# import streamlit as st
# from langchain.callbacks import get_openai_callback
# from src.mcqgen.mcqgenerator import generate_evaluate_chain
# from src.mcqgen.logger import logging

# #loading json file

# with open('response.json', 'r') as file:
#     RESPONSE_JSON = json.load(file)

# #creating a title for the app
# st.title("MCQs Creator Application with LangChain 🦜⛓️")

# #Create a form using st.form
# with st.form("user_inputs"):
#     #File Upload
#     uploaded_file=st.file_uploader("Uplaod a PDF or txt file")

#     #Input Fields
#     mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

#     #Subject
#     subject=st.text_input("Insert Subject",max_chars=20)

#     # Quiz Tone
#     tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

#     #Add Button
#     button=st.form_submit_button("Create MCQs")

#     # Check if the button is clicked and all fields have input

#     if button and uploaded_file is not None and mcq_count and subject and tone:
#         with st.spinner("loading..."):
#             try:
#                 text=read_file(uploaded_file)
#                 #Count tokens and the cost of API call
#                 with get_openai_callback() as cb:
#                     response=generate_evaluate_chain(
#                         {
#                         "text": text,
#                         "number": mcq_count,
#                         "subject":subject,
#                         "tone": tone,
#                         "response_json": json.dumps(RESPONSE_JSON)
#                             }
#                     )
#                 #st.write(response)

#             except Exception as e:
#                 traceback.print_exception(type(e), e, e.__traceback__)
#                 st.error("Error")

#             else:
#                 print(f"Total Tokens:{cb.total_tokens}")
#                 print(f"Prompt Tokens:{cb.prompt_tokens}")
#                 print(f"Completion Tokens:{cb.completion_tokens}")
#                 print(f"Total Cost:{cb.total_cost}")
#                 if isinstance(response,(list, dict)):
#                     #Extract the quiz data from the response
#                     quiz=response.get("quiz", None)
#                     if quiz is not None:
#                         table_data=get_table_data(quiz)
#                         #print(type(table_data))
                        
#                         if table_data is not None:
#                             df=pd.DataFrame(table_data)
#                             df.index=df.index+1
#                             st.table(df)
#                             #Display the review in atext box as well
#                             st.text_area(label="Review", value=response["review"])
#                         else:
#                             st.error("Error in the table data")

#                 else:
#                     st.write(response)


# import os
# import json
# import traceback
# import pandas as pd
# import streamlit as st
# from langchain.callbacks import get_openai_callback
# from src.mcqgen.utils import read_file, get_table_data
# from src.mcqgen.mcqgenerator import generate_evaluate_chain

# # loading json file
# with open('response.json', 'r') as file:
#     RESPONSE_JSON = json.load(file)

# # creating a title for the app
# st.title("MCQs Creator Application with LangChain 🦜⛓️")

# # Create a form using st.form
# with st.form("user_inputs"):
#     # File Upload
#     uploaded_file = st.file_uploader("Upload a PDF or txt file")

#     # Input Fields
#     mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
#     subject = st.text_input("Insert Subject", max_chars=20)
#     tone = st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

#     # Add Button
#     button = st.form_submit_button("Create MCQs")

#     # Check if the button is clicked and all fields have input
#     if button and uploaded_file is not None and mcq_count and subject and tone:
#         with st.spinner("loading..."):
#             try:
#                 text = read_file(uploaded_file)
#                 # Count tokens and the cost of API call
#                 with get_openai_callback() as cb:
#                     response = generate_evaluate_chain({
#                         "text": text,
#                         "number": mcq_count,
#                         "subject": subject,
#                         "tone": tone,
#                         "response_json": json.dumps(RESPONSE_JSON)
#                     })

#                 if isinstance(response, dict):
#                     # Extract the quiz data from the response
#                     quiz = response.get("quiz", None)
#                     print("Quiz String:", quiz) 
#                     if quiz is not None:
#                         table_data = get_table_data(quiz)
#                         print("Type of table_data:", type(table_data))
#                         print("Content of table_data:", table_data)
#                         if isinstance(table_data, (list, dict)):
#                             try:
#                                 df = pd.DataFrame(table_data)
#                                 df.index = df.index + 1
#                                 st.table(df)
#                                 # Display the review in a text box as well
#                                 st.text_area(label="Review", value=response["review"])
#                             except Exception as e:
#                                 st.error(f"Error creating DataFrame: {e}")
#                         else:
#                             st.error("Error: table_data is not in the correct format.")
#                             st.write(table_data)  # Debugging: Output the content of table_data
#                     else:
#                         st.error("Error: No quiz data found in the response.")
#                 else:
#                     st.write(response)

#             except Exception as e:
#                 traceback.print_exception(type(e), e, e.__traceback__)
#                 st.error("Error: An unexpected error occurred.")

#             finally:
#                 if 'cb' in locals():
#                     print(f"Total Tokens: {cb.total_tokens}")
#                     print(f"Prompt Tokens: {cb.prompt_tokens}")
#                     print(f"Completion Tokens: {cb.completion_tokens}")
#                     print(f"Total Cost: {cb.total_cost}")

import os
import json
import traceback
import pandas as pd
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgen.utils import read_file, get_table_data
from src.mcqgen.mcqgenerator import generate_evaluate_chain

# loading json file
with open('response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# creating a title for the app
st.title("MCQs Creator Application with LangChain 🦜⛓️")

# Create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # Input Fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                # Count tokens and the cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    })

                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        # Remove prefix "### RESPONSE_JSON" if present
                        quiz_str = quiz.strip().lstrip('# RESPONSE_JSON').strip()
                        print("Quiz String:", quiz_str)  # Debugging: Print quiz string
                        table_data = get_table_data(quiz_str)
                        print("Table Data:", table_data)  # Debugging: Print table data
                        if isinstance(table_data, (list, dict)):
                            try:
                                df = pd.DataFrame(table_data)
                                df.index = df.index + 1
                                st.table(df)
                                # Display the review in a text box as well
                                st.text_area(label="Review", value=response["review"])
                            except Exception as e:
                                st.error(f"Error creating DataFrame: {e}")
                        else:
                            st.error("Error: table_data is not in the correct format.")
                    else:
                        st.error("Error: No quiz data found in the response.")
                else:
                    st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error: An unexpected error occurred.")

            finally:
                if 'cb' in locals():
                    print(f"Total Tokens: {cb.total_tokens}")
                    print(f"Prompt Tokens: {cb.prompt_tokens}")
                    print(f"Completion Tokens: {cb.completion_tokens}")
                    print(f"Total Cost: {cb.total_cost}")
