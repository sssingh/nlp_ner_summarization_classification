import data
import config
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def __train_model(df, full=False):
    ### train on full data for final model else split the data and then train
    if full:
        X_train = df["Clean_Text"]
        y_train = df["Emotion"]
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            df["Clean_Text"], df["Emotion"], test_size=0.2, random_state=42
        )
    ### build model pipeline
    lr_pipeline = Pipeline(
        steps=[("cv", CountVectorizer()), ("lr", LogisticRegression(max_iter=300))]
    )
    ### train and test the model
    print(f"\nTraining LogisticRegression with {X_train.shape[0]} samples...")
    lr_pipeline.fit(X_train, y_train)
    if not full:
        print(f"Testing LogisticRegression with {X_test.shape[0]} samples...")
        score = lr_pipeline.score(X_test, y_test)
        print(f"Accuracy achieved: [{score*100:.2f}%].")
    return lr_pipeline


if __name__ == "__main__":
    emotions_df = data.load_emotions_data(config.app_config.emotions_data_file)
    emotions_df = data.preprocess_data(emotions_df)
    model = __train_model(emotions_df, full=True)
    data.save_model(model, config.app_config.model_file)
    print(f"Saved model to: [{config.app_config.model_file}]")

    ### Test code
    # model = data.load_model(config.app_config.model_file)
    # test_text = "I am loving NLP and it makes me feel so good"
    # print(f"\nTesting model with sample text '{test_text}'\nPrediction:")
    # print(model.predict([test_text]))
    # print(model.classes_)
    # print(model.predict_proba([test_text]))
