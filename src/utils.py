"""App agnostic reusable utility functionality"""

from config import app_config
import data
from typing import List
from PIL import Image
import streamlit as st


def setup_app(config):
    """Sets up all application icon, banner, title"""
    st.set_page_config(
        page_title=config.app_title,
        page_icon=app_config.app_icon_file,
        initial_sidebar_state=config.sidebar_state,
        layout=config.layout,
    )
    ### Logo and App title, description
    with st.container():
        app_icon, app_title, logo = st.columns([0.2, 0.9, 0.3])
        app_icon.image(image=app_config.app_icon_file, width=80)
        app_title.markdown(
            f"<h1 style='text-align: left; color: #03989e;'>{app_config.app_title}</h1> ",
            unsafe_allow_html=True,
        )
        app_title.markdown(
            f"<p style='text-align: left;'>{app_config.app_short_desc}</p>",
            unsafe_allow_html=True,
        )
        logo.image(image=app_config.logo_image_file, width=100)


def create_tabs(tabs: List[str]):
    """Creates streamlit tabs"""
    return st.tabs(tabs)


def download_file(btn_label, data, file_name, mime_type):
    """Creates a download button for data download"""
    st.download_button(label=btn_label, data=data, file_name=file_name, mime=mime_type)


def get_class_from_name(module: str, class_name: str):
    """Instantiates and return the class given the class name and its module as str"""
    return getattr(module, class_name)


def make_prediction(model, input_data, proba=False):
    """
    prediction pipeline for the model, model must have predict method and predict_proba
    method if prediction probabilities to be returned
    """
    ### preprocess the input and return it in a shape suitable for this model
    processed_input_data = data.preprocess_pred_data(input_data)
    ### call model's predict method
    pred = model.predict(processed_input_data)
    ### call model's predict_proba method if required
    pred_proba = []
    if proba:
        pred_proba = model.predict_proba(processed_input_data)
    return pred, pred_proba.squeeze()
