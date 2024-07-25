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

# @st.cache_resource # returns the cached object itself
@st.cache_data # creates new copy of data each time it is called

# Load excel file
# for fixed file use below
def load_data(path:str):
    data = pd.read_excel(path)
    return data
df = pd.read_excel("./Trip and visit WY24_25 Database.xlsx")

# for file upload use below
#def load_data(file):
#    data = pd.read_excel(file)
#    return data

# Upload file function
#uploaded_file = st.file_uploader("Choose a file to begin",accept_multiple_files= False)

# Check if file uploaded, prevent error message
#if uploaded_file is None:
#    st.info("Please upload a file", icon = "⚠️")
#    st.stop() # stop processes

# Assign uploaded file to dataframe
#df = load_data(uploaded_file)

# Basic data cleaning
df.dropna(inplace=True) # remove blanks

# Sidebar filter options
with st.sidebar:
    st.header("Filter:")
    country = st.sidebar.multiselect(
        "Country:",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )
    #service = st.sidebar.multiselect(
     #   "Service:",
     #   options=df["Service"].unique(),
     #   default=df["Service"].unique()
    #)
    status = st.sidebar.multiselect(
        "Status:",
        options=df["Status"].unique(),
        default=df["Status"].unique()
    )
    level = st.sidebar.multiselect(
        "Level:",
        options=df["Del Lead"].unique(),
        default=df["Del Lead"].unique()
    )

df_selection = df.query(
   "Country == @country & Status == @status & Del Lead == @level"
)
# Preview data in expanded window
with st.expander("Data preview"):
    #st.dataframe(df)
    #st.dataframe(df_selection) # use when filter is on
    
    # Specify editable columns in df_selection
    #editable_columns = ['Service', 'Departure Date', 'Return Date', 'Status']
     
    edited_df = st.data_editor(
        df_selection,
        use_container_width=True,
        num_rows= "dynamic",
        #disabled=~df_selection.columns.isin(editable_columns)
    )
    # Check if df is edited
    #if edited_df is not None:
      #  st.write("Edited dataframe:")
      #  st.dataframe(edited_df)
    #st.dataframe(df_selection) # use when filter is on

# Key Stats
total_trips = edited_df[edited_df['Type'] == 'Trip (Outgoing)'].shape[0]
total_visits = edited_df[edited_df['Type'] == 'Visit (Incoming)'].shape[0]

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.header(f"{total_trips}")
    #st.markdown()
    st.subheader("Total Trips")

with middle_column:
    st.header(f"{total_visits}")
    st.subheader("Total Visits")

st.markdown("###")
left_column, middle_column = st.columns(2)
with left_column:
    # Convert 'Departure date' column to datetime
    df_selection['Date'] = pd.to_datetime(df_selection['Departure Date'])

    # Extract month
    df_selection['Month'] = df_selection['Date'].dt.month_name()

    # Count occurrences of each month
    df_grouped = df_selection['Month'].value_counts().reset_index(name= 'Count')
    df_grouped.rename(columns={'index': 'Month'}, inplace= True)

    # Create line chart
    fig1 = px.line(df_grouped, x = 'Month', y = 'Count', title = 'Monthly Breakdown')

    # Display chart
    st.plotly_chart(fig1)


with middle_column:
    st.header(f"{total_visits}")
    st.subheader("Total Visits")