#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re
import pandas as pd

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

print(rows)
# ['NAME1 NAME2 10', 'NAME3', 'NAME4', 'NAME5 15']

# Phase 2 - extract names and number 
pattern = '(\w+ \w+) (\d+)'

data = []
for row in rows:
  match = re.search(pattern, row)
  if match:
    name = match.group(1)
    number = match.group(2)  
    data.append([name, number])

    
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




