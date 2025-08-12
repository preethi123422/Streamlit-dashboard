import streamlit as st
import pandas as pd

# Mock data
storage_data = pd.DataFrame({
    'TABLE_NAME': ['users', 'transactions', 'logs', 'archive_data', 'events'],
    'ACTIVE_BYTES': [500_000_000, 2_000_000_000, 3_000_000_000, 4_500_000_000, 1_000_000_000],
    'TIME_TRAVEL_BYTES': [50_000_000, 200_000_000, 300_000_000, 450_000_000, 100_000_000],
    'FAILSAFE_BYTES': [25_000_000, 100_000_000, 150_000_000, 225_000_000, 50_000_000],
    'QUERY_COUNT': [100, 10, 2, 1, 50]
})

# Identify large tables with low query frequency
size_threshold = 1_000_000_000  # 1 GB
query_threshold = 5
candidates = storage_data[
    (storage_data['ACTIVE_BYTES'] > size_threshold) &
    (storage_data['QUERY_COUNT'] < query_threshold)
].copy()

candidates['SUGGESTED_RETENTION_DAYS'] = 1
candidates['ARCHIVAL_CANDIDATE'] = True

st.title("Snowflake Storage Analysis Dashboard")

st.subheader("Storage Breakdown")
st.dataframe(storage_data)

st.subheader("Archival and Retention Suggestions")
st.dataframe(candidates[['TABLE_NAME', 'ACTIVE_BYTES', 'QUERY_COUNT', 'SUGGESTED_RETENTION_DAYS', 'ARCHIVAL_CANDIDATE']])
