"""Summary tab rendering functionality"""
import pandas as pd
import streamlit as st
import spacy
from spacy import displacy


###
### INTERNAL FUNCTIONS
###
def __analyse(text, analysis_type, nlp):
    """Analyse and return the named-entity for the given text"""
    doc = nlp(text)
    ### analyse based on type
    if analysis_type == "NER":
        heading = "Named Entity Recognition (NER)"
        result = displacy.render(docs=doc, style="ent", jupyter=False)
        label, desc = [], []
        for ent in doc.ents:
            label.append(ent.label_)
            desc.append(spacy.explain(ent.label_))
        df = pd.DataFrame(data={"Codes": label, "Description": desc})
        df = df.drop_duplicates().reset_index()
    elif analysis_type == "POS":
        result = ""
        word, tag, pos, desc = [], [], [], []
        for token in doc:
            if token.is_stop or token.is_punct:
                continue
            word.append(str(token))
            tag.append(str(token.tag_))
            pos.append(token.pos_)
            desc.append(spacy.explain(token.tag_))
            df = pd.DataFrame(data=dict(Token=word, Tag=tag, Pos=pos, Description=desc))
            heading = "Parts of speech tagging (POS)"
    return result, df, heading


def __section(header, nlp):
    """Build page UI elements"""
    st.header(header)
    st.write(
        "Choose the analysis-type (NER/POS) to be performed, "
        + "enter the text in the text area and then click Analyse"
    )
    analysis_type = st.radio(label="Type:", options=["NER", "POS"])
    text = st.text_area("Enter text:", height=300)
    ### analyse the entered text and show the results
    if st.button("Analyse"):
        result, df, heading = __analyse(text, analysis_type, nlp)
        st.subheader(heading)
        st.divider()
        st.write(result, unsafe_allow_html=True)
        st.write(" ")
        st.dataframe(df, use_container_width=True)
        st.divider()


###
### MAIN FLOW, entry point
###
def render(nlp):
    """NER tab page"""
    __section("Named Entity & Parts Of Speech Recognition", nlp)
