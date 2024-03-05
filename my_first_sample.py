import streamlit as st
from snowflake.snowpark import Session

st.title(":snowflake: WELCOME TO PROJECT :snowflake:")
st.markdown("---")
st.markdown("THIS PAGE WILL PROVIDE INFO OF OUR STAGE")
# Establish Snowflake session
conn = st.connection("snowflake")
@st.cache_resource



def load_data(table_name):
   session = conn.session()
   st.write("Here's some example data from `{table_name}`:")
   return session.table(table_name).to_pandas()


table_name = "SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER"
df = load_data(table_name)
st.dataframe(df)
st.write(df)
st.button("SHOW STAGES",on_click=st.write(df))
