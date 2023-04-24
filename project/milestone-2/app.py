import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Streamlit app
st.title("Sentiment Analysis")
st.write("Enter a text and select a pre-trained model to get the sentiment analysis.")
text = st.text_input("Text:", "I love you!")
model_options = {
    "distilbert-base-uncased-finetuned-sst-2-english",
    "finiteautomata/bertweet-base-sentiment-analysis",
    "siebert/sentiment-roberta-large-english",
    "textattack/bert-base-uncased-SST-2",
    "cardiffnlp/twitter-roberta-base-sentiment"
}
selected_model = st.selectbox("Model:", model_options)

# Prepare analysis model, tokenizer and pipeline
def get_pipeline(selected_model):
    model = AutoModelForSequenceClassification.from_pretrained(selected_model)
    tokenizer = AutoTokenizer.from_pretrained(selected_model)
    pl = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return pl

# Load the model and perform sentiment analysis
if st.button("Submit"):
    with st.spinner("Analyzing sentiment..."):
        pl = get_pipeline(selected_model)
        result = pl(text)
        label = result[0]['label']
        if(selected_model == "cardiffnlp/twitter-roberta-base-sentiment"):
            if label == "LABEL_0": st.write("Sentiment: Negative")
            elif label == "LABEL_1": st.write("Sentiment: Neutral")
            elif label == "LABEL_2": st.write("Sentiment: Positive")
        elif(selected_model == "textattack/bert-base-uncased-SST-2"):
            if label == "LABEL_0": st.write("Sentiment: Negative")
            elif label == "LABEL_1": st.write("Sentiment: Positive")
        else:
            st.write(f"Sentiment: {label}")
        st.write(f"Confidence Score: {result[0]['score']:.2f}")
else:
    st.write("Click 'Submit' for sentiment analysis.")