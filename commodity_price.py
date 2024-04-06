import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv('commodities_data.csv')


list_of_states = df['State'].unique().tolist()

selected_state = st.selectbox('Select a State', list_of_states)

filtered_df = df[df['State'] == selected_state]
state_district_map = {}


for index, row in df.iterrows():
    state = row['State']
    district = row['District']
    
    
    if state in state_district_map:
        state_district_map[state].append(district)
   
    else:
        state_district_map[state] = [district]
st.write(filtered_df)
