"""Summary tab rendering functionality"""

from config import app_config
import plot
import streamlit as st
import data
import utils
from config import app_config


###
### INTERNAL FUNCTIONS
###
def __section(header, df):
    """Build page UI elements"""
    st.header(header)
    ### accept text input, make prediction and show results
    st.write(
        "`Enter the text` to be classified in the text area and then click `Detect`"
    )
    text = st.text_area("Enter Text:", height=200)
    if st.button("Predict"):
        model = data.load_model(app_config.model_file)
        pred, pred_proba = utils.make_prediction(model, text, proba=True)
        pred_col, conf_col = st.columns(2)
        with pred_col:
            emotion = pred[0]
            st.success(
                f"Detected Emotion: {emotion.upper()} {app_config.emoji_map[emotion]}"
            )

        with conf_col:
            st.success(f"Confidence: {pred_proba.max():.2f}%")
        fig = plot.plot_proba(model.classes_, pred_proba)
        st.plotly_chart(fig, use_container_width=True)

    ### Supplementary details about the model used
    st.divider()
    with st.expander("Supplementary under-the-hood details:"):
        st.info(
            body="""
        A trained LogisticRegression model is used here for emotion detection. The model
        has been trained on a labeled data of 34,000 samples. Sample data and class
        distribution is shown below.
        """,
            icon=app_config.icon_info,
        )
        st.dataframe(df.loc[:15, ["Clean_Text", "Emotion"]])
        fig = plot.plot_class_dist(df)
        st.plotly_chart(fig, use_container_width=True)


###
### MAIN FLOW, entry point
###
def render(df):
    __section("Emotions Detection", df)
