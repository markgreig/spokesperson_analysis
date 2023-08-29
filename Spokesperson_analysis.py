#!/usr/bin/env python
# coding: utf-8

# In[2]:
import subprocess
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

st.title('My App') 

import pyperclip
import pandas as pd

# Get the text from the clipboard
clipboard_data = pyperclip.paste()

# Split the clipboard data into rows based on newline character ('\n')
rows = clipboard_data.strip().split('\n')

# Split each row into columns based on tabs ('\t')
data = [row.split('\t') for row in rows]

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Spokesperson', 'Frequency'])

# Convert the 'Frequency' column to integers
df['Frequency'] = df['Frequency'].astype(int)

# Split and explode the Spokesperson column
df['Spokesperson'] = df['Spokesperson'].str.split('|')

# Explode the Spokesperson column to create one row per Spokesperson
df = df.explode('Spokesperson')

# Group by Spokesperson and calculate the sum of Frequency
result = df.groupby('Spokesperson')['Frequency'].sum().reset_index()

# Sort by Frequency in descending order
result = result.sort_values(by='Frequency', ascending=False)

result.to_csv('top_spokespeople.csv')


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

if __name__ == '__main__':
    main()
# In[ ]:




