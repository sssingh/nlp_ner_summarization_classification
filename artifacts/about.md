# Common NLP Tasks  
***This app demonstrates common NLP techniques and use cases.***
>This app demonstrate typical NLP techniques used in real-world use cases, such as NER & POS Recognition, Text Summarization, and Text Classification.  

* **`NER`** has applications in various industries for example in `finance` it can extract essential information from earnings reports, financial statements, news articles, and product mentions for automated analysis, fraud detection, and investment opportunities. In `media and entertainment`, it analyzes text for content creation and personalized content creation. In `e-commerce`, it extracts product information from reviews, customer feedback, and descriptions, enabling automated analysis and personalized recommendations.

* **`POS`** tagging is an essential NLP technique used in machine translation, word meaning disambiguation, question answering parsing, and so on.

* **`Text Summarization`** has plethora of use-cases in real world. For example `Media monitoring` for sensitive and  objectional content, `Helping disabled people` in presenting only short and relevant content, producing succinct summary of `Meetings and video-conferencing`, Summarization of financial documents like earning reports and financial news to quickly derive market signals etc.

* **`Text Classification`** has multitude of applications such as `Categorizing customer support tickets` (billing, feedback, questions complaints etc), `sentiment analysis` (customer feedback, tweets etc), `Content moderation` (hate speech, obscene language, NSFW etc).


# App UI Details
The app has four tabs: "ABOUT", "NER & POS", "TEXT SUMMARIZATION", and "TEXT CLASSIFICATION". 

## ABOUT Tab 
This page
    
## NER & POS Tab
Given a text fragment, named entities (NER) and parts of speech (POS) in the text can be extracted with a click of button:

<img src="https://github.com/sssingh/nlp_ner_summarization_classification/blob/main/assets/ner.png?raw=true"/><br>

<img src="https://github.com/sssingh/nlp_ner_summarization_classification/blob/main/assets/pos.png?raw=true"/>


Because of hardware resource constraints on public cloud hosting, the app uses a "small" language model to illustrate functionality that is far from ideal. A bigger model running on more capable hardware will yield much better results.

## TEXT SUMMARIZATION Tab
A brief text summary is generated from a specified text. The summation technique (TextRankSummarizer, LexRankSummarizer, LsaSummarizer) and the length of the summary text may be selected by the user.

<img src="https://github.com/sssingh/nlp_ner_summarization_classification/blob/main/assets/summ1.png?raw=true"/>

<img src="https://github.com/sssingh/nlp_ner_summarization_classification/blob/main/assets/summ2.png?raw=true"/>

## TEXT CLASSIFICATION Tab
The text classifier can determine the `emotion` portrayed by a sentence or paragraph given a sentence or paragraph. The `LogisticRegression` classifier is used to detect emotions in this app. The classifier was trained using labeled data from 34,000 samples. 

<img src="https://github.com/sssingh/nlp_ner_summarization_classification/blob/main/assets/emotion.png?raw=true"/>

Please keep in mind that this is far from flawless. Given the training and inference hardware restrictions, the corpus utilized for training is tiny, and the model employed is basic. Training on a much bigger text corpus and employing a model capable of classifying non-linear data (e.g., XGBoost, RandomForest, or a Neural Network) would provide significantly superior results.


# Project Source
[👉 Visit GitHub Repo](https://github.com/sssingh/nlp_ner_summarization_classification)

# Contact Me
[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sunil@sunilssingh.me)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/@thesssingh)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sssingh/)
[![website](https://img.shields.io/badge/web_site-8B5BE8?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sunilssingh.me)

# Appendix

## Local Installation and Run
To run the app locally...
1. Create a conda or virtual environment and activate it
2. install python 3.11.0 or above
3. execute below commands from terminal/command-prompt
```
git clone https://github.com/sssingh/nlp_ner_summarization_classification
cd nlp_ner_summarization_classification
pip install -r requirements.txt
streamlit run src/app.py
```
4. Open any browser and then visit `localhost:8501`

NOTE: The trained text classifier is kept in `artifacts` folder as `logistic_regression_model.joblib` file. If you wish to re-train the model again and make changes to its hyperparameter (or use another classifier) then... 
* Modify `src/logistic_regression_model.py` script
* execute below commands from terminal/command-prompt
```
pip install -r requirements.txt
streamlit run src/app.py
``` 
