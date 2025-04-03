import streamlit as st
import pandas as pd

st.title("My Streamlit App")
st.write("Hello, world!")

st.button("click me")

if st.button("Load Data"):
    # Load data from a CSV file
    df = pd.read_csv("data.csv")
    st.write(df)