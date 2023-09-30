"""Summary tab rendering functionality"""

from config import app_config
import utils
import sys
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.evaluation import rouge_n


###
### INTERNAL FUNCTIONS
###
def __get_summarizer(summarizer_type):
    """Helper to get summarizer object given its name as string"""
    summarizer_dict = app_config.summarizers.get(summarizer_type)
    module = sys.modules[summarizer_dict["module"]]
    summarizer = utils.get_class_from_name(module, summarizer_type)
    desc = summarizer_dict["desc"]
    return summarizer(), desc


def __summarize(text, summarizer, n_sentences):
    ### instantiate the text parser, summarize text and return the summary text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary_tuple = summarizer(parser.document, n_sentences)
    summary_text = ""
    for sentence in summary_tuple:
        summary_text += str(sentence)
    ### compute length of sentences are ROUGE score for summary text
    rouge = rouge_n(
        evaluated_sentences=summary_tuple,
        reference_sentences=parser.document.sentences,
        n=2,
    )
    stats = f"""
    Number of sentences in original text: **{len(parser.document.sentences)}**  
    Number of sentences in summary text: **{len(summary_tuple)}**  
    ROUGE (bi-gram) score: **{rouge}**
    """
    return summary_text, stats


def __section(header):
    """Build page UI elements"""
    st.header(header)
    st.write(
        "Choose the `Summarization Method`, `Enter Text` in the text "
        + "area, choose the `Number Of Sentences` required in summary text "
        + "and then click `Summarize`"
    )
    summarizer_type = st.radio(
        "Summarization Method:",
        options=[
            # "WordFrequency",
            "TextRankSummarizer",
            "LexRankSummarizer",
            "LsaSummarizer",
        ],
    )
    ### Based on type selected, fetch the summarizer object and show short description
    summarizer, desc = __get_summarizer(summarizer_type)
    st.info(body=f"{desc}", icon=app_config.icon_info)
    text = st.text_area("Enter text:", height=300, key="summarization")
    n_sentences = st.slider(
        label="Number Of Sentences", min_value=1, max_value=10, value=3
    )
    ### summarize the entered text and show the results
    if st.button("Summarize"):
        summary, stats = __summarize(text, summarizer, n_sentences)
        st.divider()
        st.subheader("Summary")
        st.success(stats)
        st.write(summary)
        st.divider()


###
### MAIN FLOW, entry point
###
def render():
    __section("Text Summarization")
