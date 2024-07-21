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

@st.cache_data # cache data
# Upload file function
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


# Sidebar filter options
with st.sidebar:
    st.header("Filter:")
    country = st.sidebar.multiselect(
        "Select the country:",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )
    service = st.sidebar.multiselect(
        "Select the service:",
        options=df["Service"].unique(),
        default=df["Service"].unique()
    )
    status = st.sidebar.multiselect(
        "Select the status:",
        options=df["Status"].unique(),
        default=df["Status"].unique()
    )
    level = st.sidebar.multiselect(
        "Select the level:",
        options=df["Level"].unique(),
        default=df["Level"].unique()
    )

df_selection = df.query(
    "Country == @country & Service == @service & Status == @status & Level == @level"
)


# Preview data in expanded window
with st.expander("Data preview"):
    #st.dataframe(df)
    st.dataframe(df_selection) # use when filter is on