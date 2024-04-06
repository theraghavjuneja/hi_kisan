import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv('commodities_data.csv')


list_of_states = df['State'].unique().tolist()

selected_state = st.selectbox('Select a State', list_of_states)

filtered_df = df[df['State'] == selected_state]


st.write(filtered_df)
