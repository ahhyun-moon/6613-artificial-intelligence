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
        st.write(f"Sentiment: {result[0]['label']}")
        if(selected_model == "cardiffnlp/twitter-roberta-base-sentiment"):
            st.write("(LABEL_0: *Negative*,  LABEL_1: *Neutral*,  LABEL_2: *Positive*)")
        elif(selected_model == "textattack/bert-base-uncased-SST-2"):
            st.write("(LABEL_0: *Negative*,  LABEL_1: *Positive*)")
        st.write(f"Confidence Score: {result[0]['score']:.2f}")
else:
    st.write("Click 'Submit' for sentiment analysis.")