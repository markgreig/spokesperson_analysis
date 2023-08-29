#!/usr/bin/env python
# coding: utf-8

# In[2]:
import re
import streamlit as st

st.title('My App') 


import pandas as pd

text = st.text_input("Paste text here")

# Extract rows
rows = re.findall(r'([^\d]+ [\d\w]+ [^\d]+)\s(\d+)', text)

# Split spokesperson column 
data = []
for row in rows:
  spokesperson = row[0].strip()
  spokespeople = spokesperson.split('|')
  spokespeople = [name.strip() for name in spokespeople]
  frequency = int(row[1])
  
  for spokesperson in spokespeople:
    data.append([spokesperson, frequency])

# Create dataframe  
df = pd.DataFrame(data, columns=['Spokesperson', 'Frequency'])

# Group by Spokesperson and calculate the sum of Frequency
result = df.groupby('Spokesperson')['Frequency'].sum().reset_index()

# Sort by Frequency in descending order
result = result.sort_values(by='Frequency', ascending=False)

result.to_csv('top_spokespeople.csv', index=False)


@st.cache
def convert_df(result):
     return result.to_csv().encode('utf-8')

csv = convert_df(result)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='top_spokespeople.csv',
     mime='text/csv',
 )

# In[ ]:




