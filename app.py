import streamlit as st
import pandas as pd

st.title("My Streamlit App")
st.write("Hello, Maya!")


if st.button("Load Data"):
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write("Data loaded successfully!")
        st.dataframe(df)

reddit_username = 'maya'
st.write(f"Reddit username: {reddit_username}")