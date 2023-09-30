"""All app-specific data and disk-IO related functionality implemented here"""

import subprocess
import joblib
import pandas as pd
import neattext.functions as nfx
import nltk
import spacy
import streamlit as st


@st.cache_resource
def load_lang_model(model):
    """Download and then instantiate then language model"""
    # subprocess.run(["python", "-m", "spacy", "download", model])
    nlp = spacy.load(model)
    return nlp


@st.cache_resource
def load_nltk_punkt():
    """Downloads NLTK tokenizers"""
    nltk.download("punkt")


@st.cache_resource
def load_emotions_data(data_file_path):
    """Reads a given data-file and returns a DataFrame"""
    return pd.read_csv(data_file_path)


def preprocess_data(df):
    """Cleans and transforms data"""
    df["Clean_Text"] = df["Text"].apply(nfx.remove_userhandles)
    df["Clean_Text"] = df["Clean_Text"].apply(nfx.remove_stopwords)
    df["Clean_Text"] = df["Clean_Text"].apply(nfx.remove_urls)
    df["Clean_Text"] = df["Clean_Text"].apply(nfx.remove_punctuations)
    return df


def preprocess_pred_data(input_data):
    input_data = nfx.remove_userhandles(input_data)
    input_data = nfx.remove_stopwords(input_data)
    input_data = nfx.remove_urls(input_data)
    input_data = nfx.remove_punctuations(input_data)
    return [input_data]


def save_model(model_obj, model_file_path):
    joblib.dump(value=model_obj, filename=model_file_path)


@st.cache_resource
def load_model(model_file_path):
    return joblib.load(model_file_path)
