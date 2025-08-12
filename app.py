import snowflake.connector
import pandas as pd
 
def get_connection():
    return snowflake.connector.connect(
        user='PreethiRajesh',
        password='Geethapriya@123',
        account='on21616',
        warehouse='COMPUTE_WH',
        database='SNOWFLAKE_LEARNING_DB'
        schema='PUBLIC'
    )
 
def fetch_storage_metrics(conn):
    query = """
    SELECT TABLE_NAME, ACTIVE_BYTES, TIME_TRAVEL_BYTES, FAILSAFE_BYTES
    FROM INFORMATION_SCHEMA.TABLE_STORAGE_METRICS;
    """
    return pd.read_sql(query, conn)
 
def fetch_query_history(conn):
    query = """
    SELECT QUERY_TEXT, START_TIME
    FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
    WHERE START_TIME >= DATEADD(day, -30, CURRENT_TIMESTAMP());
    """
    return pd.read_sql(query, conn)
