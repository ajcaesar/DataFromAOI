import numpy as np
import math 
import pandas as pd
import streamlit as st
from io import StringIO

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-2.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted', 'Complete'])

i = 0
while i < 111:
  x = 0
  numCompleted = 0
  Finished = True
  while x < 37:
    y = df.iloc[37 * i + x, 7]
    if not pd.isna(y):
      numCompleted += 1
    else:
      Finished = False
    x += 1
  dfcheck.at[i, 0] = i
  dfcheck.at[i, 1] = numCompleted
  dfcheck.at[i, 2] = Finished
  i += 1
st.write(dfcheck)
    
