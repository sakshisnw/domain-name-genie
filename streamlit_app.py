import streamlit as st
from generator.name_generator import generate_name

st.set_page_config(page_title="Domain Name Genie")
st.title("Domain Name Genie")

if st.button("Generate Name"):
    st.subheader(generate_name())
