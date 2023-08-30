#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re
import pandas as pd
import streamlit as st

text = "NAME1 NAME2 10 \nNAME3|NAME4|NAME5 15"

# Phase 1 - split rows on '|'
rows = []
for line in text.split('\n'):
    if '|' in line:
        names = line.split('|')
        for name in names:
            rows.append(name)
    else:
        rows.append(line)

# Phase 2 - extract names and numbers
pattern = '(.+?) (\d+)'

data = []
for row in rows:
    matches = re.findall(pattern, row)
    for match in matches:
        name = match[0]
        number = int(match[1])  # Convert the frequency to an integer
        data.append([name, number])

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




