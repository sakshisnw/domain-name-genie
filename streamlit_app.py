import streamlit as st
from generator.tagline_generator import generate_tagline
from generator.name_generator import generate_name

# Page config must come BEFORE any UI elements
st.set_page_config(
    page_title="Domain Name Genie",
    page_icon="🧞‍♂️",
    layout="centered"
)

# UI starts here
st.title("Domain Name Genie")
st.markdown("## Your Brand Identity Starts Here")
st.markdown("---")

if st.button("Generate Name and Tagline"):
    name = generate_name()
    tagline = generate_tagline()
    st.subheader(name)
    st.caption(tagline)
    
# Moodboard placeholder image
st.image("assets/sample_moodboard.png", caption="Moodboard (Coming Soon)", use_column_width=True)
