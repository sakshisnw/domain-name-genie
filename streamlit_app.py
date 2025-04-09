import streamlit as st
from generator.tagline_generator import generate_tagline
from generator.name_generator import generate_name

# Page config must come BEFORE any UI elements
st.set_page_config(
    page_title="Domain Name Genie",
    page_icon="🧞‍♂️",
    layout="centered"
)


if st.button("Generate Name and Tagline"):
    name = generate_name()
    tagline = generate_tagline()
    st.subheader(name)
    st.caption(tagline)
