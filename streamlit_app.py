import streamlit as st
from generator.tagline_generator import generate_tagline
from generator.name_generator import generate_name
from generator.moodboard import generate_moodboard_keywords

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

# Use Streamlit Form for cleaner UX
with st.form("gen_form"):
    submitted = st.form_submit_button("Generate Brand Package")
    if submitted:
        name = generate_name()
        tagline = generate_tagline()
        keywords = generate_moodboard_keywords(name)

        st.subheader(name)
        st.caption(tagline)
        st.markdown("**Moodboard Keywords:**")
        st.write(", ".join(keywords))
    
# Moodboard placeholder image
st.image("assets/sample_moodboard.png", caption="Moodboard (Coming Soon)", use_column_width=True)
