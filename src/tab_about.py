"""About tab rendering functionality"""

import streamlit as st
from config import app_config


###
### INTERNAL FUNCTIONS
###
def __section(header):
    """Render the section on this page"""
    st.header(header)
    with open(app_config.readme_file_path, "r") as f:
        about = f.read()
    st.markdown(about, unsafe_allow_html=True)


###
### MAIN FLOW, entry point
###
def render():
    __section("About The App")
