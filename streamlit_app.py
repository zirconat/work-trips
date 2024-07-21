import streamlit as st
import pandas as pd
# import random
import plotly.express as px
st.set_page_config(
    page_title = "Trips & Visits",
    page_icon = ":airplane:",
    layout = "wide"
)

st.title("✈️ Trips & Visits Outlook")
st.write(
    "An overview of the trips and visits for WY2024/25."
)

# Upload file function
@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

# Store uploaded file
uploaded_file = st.file_uploader("Choose a file to begin")

# Check if file uploaded, prevent error message
if uploaded_file is None:
    st.info("Please upload a file", icon = "⚠️")
    st.stop() # stop processes

# Assign uploaded file to dataframe
df = load_data(uploaded_file)

# Preview data in expanded window
with st.expander("Data preview"):
    st.dataframe(df)