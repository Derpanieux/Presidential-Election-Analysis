import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Presidential Election Maps", layout="wide")
st.title("Presidential Election Analysis")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


STATES_DIR = "states"
MAPS_DIR = "maps"

# Get available years from map files
years = sorted(
    int(f.replace(".png", ""))
    for f in os.listdir(MAPS_DIR)
    if f.endswith(".png")
)

year = st.slider(
    "Select Election Year",
    min_value=min(years),
    max_value=max(years),
    value=max(years),
    step=4
)

# Load table for selected year
df = pd.read_csv(f"{STATES_DIR}/{year}.csv")

# Layout: table on left, map on right
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(f"Results: {year}")
    st.dataframe(df, height=600)

with col2:
    st.subheader("Electoral Map")
    st.image(f"{MAPS_DIR}/{year}.png", use_container_width=True)
