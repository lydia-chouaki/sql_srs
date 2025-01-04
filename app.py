import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System for SQL practice
""")

option = st.selectbox(
    "How would you like to review?",
    ["Joins", "GroupBy", "Window Functions"],
    index=None,
    placeholder="Select a theme...",
)

st.write("You selected: ", option)

data= {"a": (1, 2, 3), "b":[4, 5, 6]}
df= pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["Cat","Dog","Owl"])
with tab1:
    st.header("A cat")
    st.write(f"nos données: ")
    st.write(duckdb.sql("select * from df").df())
    query=st.text_area(label="Entrez votre requete ")
    st.write(f"Vous avez rentré cette requete: {query}")
    st.write(duckdb.sql(query).df())

with tab2:
    st.header("A dog")

with tab3:
    st.header("An owl")