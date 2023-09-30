"""All app-specific user defined configurations are defined here"""

import os
from dataclasses import dataclass
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import plotly.express as px


### define all plotting configuration here,
### should not be accessed and changed directly hence leading "__"
@dataclass
class __PlotConfig:
    """All plotting configurations are defined here"""

    # Available themes (templates):
    # ['ggplot2', 'seaborn', 'simple_white', 'plotly',
    #  'plotly_white', 'plotly_dark', 'presentation',
    #  'xgridoff', 'ygridoff', 'gridon', 'none']
    theme = "plotly_dark"
    cat_color_map = px.colors.qualitative.T10
    cat_color_map_r = px.colors.qualitative.T10_r
    cont_color_map = px.colors.sequential.amp
    cont_color_map_r = px.colors.sequential.amp_r


### define all app-wide configuration here,
### should not be accessed and changed directly hence leading "__"
@dataclass
class __AppConfig:
    """app-wide configurations"""

    # get current working directory
    cwd = os.getcwd()
    banner_image_file = f"{cwd}/"
    logo_image_file = f"{cwd}/assets/logo.png"
    app_icon_file = f"{cwd}/assets/NLP.png"
    app_title = "Applications"
    readme_file_path = f"{cwd}/artifacts/about.md"
    app_short_desc = "For common NLP use cases"
    emotions_data_file = f"{cwd}/data/emotions.csv"
    emoji_map = {
        "joy": "😃",
        "anger": "😡",
        "disgust": "🤮",
        "fear": "😨",
        "neutral": "😐",
        "sadness": "😔",
        "shame": "🫣",
        "surprise": "😲",
    }
    model_file = f"{cwd}/artifacts/lr_model.joblib"
    sidebar_state = "expanded"  # collapsed
    layout = "centered"  # wide
    icon_question = "❓"
    icon_important = "🎯"
    icon_info = "ℹ️"
    icon_stop = "⛔"
    icon_about = "👋"
    spacy_lang_model = "en_core_web_sm"
    # sumy summarizers
    summarizers = dict(
        TextRankSummarizer={
            "module": "sumy.summarizers.text_rank",
            "desc": (
                "**`TextRank`** is a graph based ranking algorithm. Read this article"
                + " https://blogs.cornell.edu/info2040/2018/10/22/40068/"
                + " to get a good intuition behind it"
            ),
        },
        LexRankSummarizer={
            "module": "sumy.summarizers.lex_rank",
            "desc": (
                "**`LexRank`** is another graph based ranking algorithm. Read this"
                + " https://github.com/crabcamp/lexrank"
                + " to get a good intuition behind it"
            ),
        },
        LsaSummarizer={
            "module": "sumy.summarizers.lsa",
            "desc": (
                "**`LSA`** or Latent Semantic Analysis uses word frequency and Singular"
                + " Value Decomposition (SVD). Read this"
                + " https://www.analyticsvidhya.com/blog/2021/09/latent-semantic-analysis-and-its-uses-in-natural-language-processing/ article"
                + " to get a good intuition behind it"
            ),
        },
    )


### make configs available to any module that imports this module
app_config = __AppConfig()
plot_config = __PlotConfig
