import streamlit as st
import pandas as pd
import json
from snowflake.snowpark import Session

# connect to Snowflake
with open('creds.json') as f:
    connection_parameters = json.load(f)  
session = Session.builder.configs(connection_parameters).create()

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
file_df = pd.read_csv(file)
snowparkDf=session.write_pandas(file_df,file.name,auto_create_table = True, overwrite=True)