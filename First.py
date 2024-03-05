import streamlit as st
from snowflake.snowpark import Session

st.title('❄️ Connect Streamlit to a Snowflake database & Visualizing Predictions')

# Establish Snowflake session
conn = st.connection("snowflake")
@st.cache_resource
##def create_session():
   ## return Session.builder.configs(st.secrets.snowflake).create()





# Load data table
@st.cache_data

def load_data(table_name):
   session = conn.session()
   st.write("Here's some example data from `{table_name}`:")
   return session.table(table_name).to_pandas()
 
    ## Do some computation on it
    #table = table.limit(20)
       
    ## Collect the results. This will run the query and download the data
    #table = table.collect()
    #return table


# Select and display data table
table_name = "SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER"
df = load_data(table_name)
st.dataframe(df)
st.write(df)
## Display data table
##with st.expander("See Table"):
  