#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re
import pandas as pd
import streamlit as st

text = "NAME1 NAME2 10 \nNAME3|NAME4|NAME5 15\nNAME NAME 10\nNAME NAME NAME NAME 15"

# Phase 1 - split rows on '\n'
rows = text.split('\n')

# Phase 2 - extract names and numbers
pattern = '(.+?) (\d+)'

data = []

for row in rows:
    if '|' in row:
        match = re.search(pattern, row)
        if match:
            name = match.group(1)
            number = int(match.group(2))
            data.append([name, number])
    else:
        names = row.split()
        for name in names[:-1]:
            data.append([name, int(names[-1])])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Spokesperson', 'Frequency'])

# Group and aggregate the data
top_spokespeople = df.groupby('Spokesperson')['Frequency'].sum().reset_index()

# Sort the data by frequency in descending order
top_spokespeople = top_spokespeople.sort_values(by='Frequency', ascending=False)

# Display the DataFrame using Streamlit
st.write(top_spokespeople)

# Download button for CSV
@st.cache
def convert_df_to_csv(result):
    return result.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(top_spokespeople)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='top_spokespeople.csv',
    mime='text/csv',
)
# In[ ]:




