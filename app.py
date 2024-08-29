from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=api_key)

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from Gemini
def get_gemini_response(prompt_text, image_data, user_input):
    response = model.generate_content([prompt_text, image_data[0], user_input])
    return response.text

# Function to extract image details
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Streamlit UI configuration
st.set_page_config(page_title="Multilingual Invoice Querying")
st.header("Multilingual Invoice Extractor")

# Get user input
user_input = st.text_input("Input:", key="user_input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image = None

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Prompt setup
input_prompt = """
You are an expert in understanding invoices. We will upload an image of invoices,
and you have to provide precise and accurate answers to any question based on the invoice.
"""

# Handle submit button
if st.button("Tell me about the invoice") and image:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, user_input)
    st.subheader("The Response is:")
    st.write(response)


# from dotenv import load_dotenv

# load_dotenv()

# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel("gemini-pro-vision")

# def get_gemini_response(input,image,prompt):
#     response=model.generate_content([input,image[0],prompt])
#     return response.text

# def input_image_details(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         image_parts=[
#             {
#                 "mime_type":uploaded_file.type,
#                 "data":bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No File Uploaded")
     

# st.set_page_config(page_title="MutiLingual Invoice Quering")
# st.header("Multi Lingual Invoice extractor")
# input=st.text_input("Input :",key="input")
# uploaded_file=st.file_uploader("Choose an image of the Invoice ...",type=["jpg","jpeg","png"])
# image=""
# if(uploaded_file) is not None:
#     image=Image.open(uploaded_file)
#     st.image(image,caption="Uploaded Image..",use_column_width=True)

# submit=st.button("Tell me about the invoice")

# input_prompt="""
# You are an expert in understanding invoices. We will upload an image of Invoices 
# and you have to give precise and accurate answer any question based on the invoice.

# """

# if submit:
#     image_data=input_image_details(image)
#     response=get_gemini_response(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)


