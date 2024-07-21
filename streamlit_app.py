import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

st.set_page_config(
    page_title = "Trips & Visits",
    page_icon = ":airplane:",
    layout = "wide"
)

st.title("✈️ Trips & Visits Outlook")
st.write(
    "An overview of the trips and visits for WY2024/25."
)

# Generate random data into existing excel
def gen_rand_data(num_rows):
    data = []
    for i in range(num_rows):
        row = [
            random.randint(1,100)
            
        ]
        data.append(row)
    return data

def append_2_excel(filename, data, sheet_name='Sheet1'):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook[sheet_name]

    # Get the last row number
    last_row = worksheet.max_row + 1

    # Append data to the worksheet
    for row_data in data:
        worksheet.append(row_data)

    workbook.save(filename)

# Example
filename = 'Trip and visit WY24_25 Database.xlsx'
num_rows_to_gen = 80

random_data = gen_rand_data(num_rows_to_gen)
append_2_excel(filename,random_data)