import streamlit as st
from generator.tagline_generator import generate_tagline
from generator.name_generator import generate_name
from generator.moodboard import generate_moodboard_keywords
from generator.app_logic import generate_brand_package

# Initialize session state before any UI elements
if "generated" not in st.session_state:
    st.session_state["generated"] = False
    
# Page config must come BEFORE any UI elements
st.set_page_config(
    page_title="Domain Name Genie",
    page_icon="assets/favicon.ico",
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
        name, tagline, keywords = generate_brand_package()
        
        # Update session state
        st.session_state["generated"] = True

        st.markdown("### 🔮 Your Magical Domain Name is Ready!")
        st.subheader(name)
        st.caption(tagline)
        
        st.markdown("**Moodboard Keywords:**")
        st.write(", ".join(keywords))
    
# Moodboard placeholder image
st.image("assets/sample_moodboard.png", caption="Moodboard (Coming Soon)", use_container_width=True)


st.markdown("---")
st.markdown("© 2025 Domain Name Genie — Built with ❤️ by Sakshi")

