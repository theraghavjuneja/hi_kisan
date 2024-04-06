import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv('commodities_data.csv')

# Get unique states
list_of_states = df['State'].unique().tolist()

# Create a dictionary to map states to their corresponding districts
state_district_map = {}
for state in list_of_states:
    state_district_map[state] = df[df['State'] == state]['District'].unique().tolist()

# Get user input for state selection
selected_state = st.selectbox('Select a State', list_of_states)
st.info("ALL THE PRICES ARE PER QUINTAL OF THE COMMODITY")
# Display the corresponding districts for the selected state
if selected_state in state_district_map:
    selected_district = st.selectbox('Select a District', state_district_map[selected_state])
else:
    st.write("No districts available for the selected state.")

# Filter data based on user selection
filtered_df = df[(df['State'] == selected_state) & (df['District'] == selected_district)]

# Display filtered data
st.write(filtered_df)
