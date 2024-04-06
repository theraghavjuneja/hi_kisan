import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = pd.read_csv("commodities_data.csv")
df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['State', 'District', 'Market','Commodity'])


dynamic_filters.display_filters()


dynamic_filters.display_df()
