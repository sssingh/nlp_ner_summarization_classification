"""Application entry point, global configuration, application structure"""

from config import app_config
import data
import utils
import tab_about
import tab_ner
import tab_emotions as tab_emotions
import tab_summarization
import streamlit as st


def init():
    ### setup app-wide configuration
    utils.setup_app(app_config)

    ### load data only once and cache it
    nlp = data.load_lang_model(app_config.spacy_lang_model)
    data.load_nltk_punkt()
    df = data.load_emotions_data(app_config.emotions_data_file)

    ### initialize session state

    ### setup app tab structure
    about, ner, summarization, sentiment = utils.create_tabs(
        ["ABOUT 👋", "NER & POS 🔍", "TEXT SUMMARIZATION 📝", "TEXT CLASSIFICATION 📑"]
    )
    with about:
        tab_about.render()
    with ner:
        tab_ner.render(nlp)
    with summarization:
        tab_summarization.render()
    with sentiment:
        tab_emotions.render(df)


if __name__ == "__main__":
    init()
