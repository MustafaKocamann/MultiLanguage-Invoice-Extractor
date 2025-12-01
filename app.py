from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

# .env yükle
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(user_input, image_parts, system_prompt):
    response = model.generate_content([system_prompt, image_parts[0], user_input])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

user_input = st.text_input("Input Prompt:", key="user_input")
uploaded_file = st.file_uploader(
    "Choose an Image of the invoice...",
    type=["png", "jpg", "jpeg"]
)

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Tell me about the invoice")

system_prompt = """
You are an expert in understanding invoices. 
We will upload an invoice image and you must answer any questions 
based on the uploaded invoice image.
"""

if submit:
    if uploaded_file is None:
        st.warning("Please upload an invoice image first.")
    else:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(user_input, image_data, system_prompt)
        st.subheader("The response is")
        st.write(response)
