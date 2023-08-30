#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re
import streamlit as st
import pandas as pd

text = st.text_input("Paste text")

rows = re.findall(r'([^\d]+ [\d\w]+ [^\d]+)\s(\d+)', text)

data = []

for row in rows:
  spokesperson = row[0].strip()
  spokespeople = spokesperson.split('|')
  spokespeople = [name.strip() for name in spokespeople]
  
  frequency = int(row[1])
  
  for spokesperson in spokespeople:
    data.append([spokesperson, frequency])
    
df = pd.DataFrame(data, columns=['Spokesperson', 'Frequency'])

top_spokespeople = df.groupby('Spokesperson')['Frequency'].sum().reset_index()

top_spokespeople = top_spokespeople.sort_values(by='Frequency', ascending=False) 

# Display dataframe  
st.write(top_spokespeople)

top_spokespeople.to_csv('top_spokespeople.csv', index=False)


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




