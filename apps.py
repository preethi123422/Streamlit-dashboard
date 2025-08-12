import streamlit as st
import snowflake.connector
import pandas as pd

# Connect to Snowflake
def get_connection():
    return snowflake.connector.connect(
        user='PreethiRajesh',
        password='Geethapriya@123',
        account='on21616.yvoslui',  
        warehouse='COMPUTE_WH',
        database='SNOWFLAKE_LEARNING_DB',
        schema='PUBLIC'
    )

# Fetch data from EMPLOYEES table
def fetch_employees(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM EMPLOYEES;")
        df = pd.DataFrame(cursor.fetchall(), columns=[col[0] for col in cursor.description])
        return df
    finally:
        cursor.close()

# Streamlit UI
st.title("Employee Dashboard")

try:
    conn = get_connection()
    df = fetch_employees(conn)

    if df.empty:
        st.warning("No data found in EMPLOYEES table.")
    else:
        st.success("Data loaded successfully!")
        st.dataframe(df)

except Exception as e:
    st.error(f"Error: {e}")
