from config import plot_config
import pandas as pd
import plotly.express as px
import plotly.io as io

# setup app-wide plotly theme
io.templates.default = plot_config.theme


def plot_proba(classes, proba):
    df_proba = pd.DataFrame({"Emotions": classes, "Probability": proba})
    df_proba["Emotions"] = df_proba["Emotions"].str.upper()
    df_proba = df_proba.sort_values(by="Probability", ascending=False)
    fig = px.bar(
        data_frame=df_proba,
        x="Probability",
        y="Emotions",
        color="Emotions",
        title="Prediction Probabilities",
        color_discrete_sequence=plot_config.cat_color_map,
    )
    return fig


def plot_class_dist(df):
    df_count = pd.DataFrame(df["Emotion"].value_counts()).reset_index()
    df_count.columns = ["Emotions", "Count"]
    df_count["Emotions"] = df_count["Emotions"].str.upper()
    fig = px.bar(
        data_frame=df_count,
        x="Emotions",
        y="Count",
        color="Emotions",
        title="Class Distribution",
        color_discrete_sequence=plot_config.cat_color_map,
    )
    return fig
