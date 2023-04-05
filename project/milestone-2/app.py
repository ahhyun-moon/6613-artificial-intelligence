import streamlit as st
import torch
# from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification

first_model = "distilbert-base-uncased-finetuned-sst-2-english"
second_model = "twitter-xlm-roberta-base-sentiment"
third_model = "bertweet-base-sentiment-analysis"

st.title('Text Sentiment Analysis')
st.markdown('Type a sentence in the below text box and select a pretrained model in the menu.')
text = st.text_input("Enter the sentence", "I love you!")
model = st.selectbox("Select a model below", (first_model, second_model, third_model))

def distilbert(text):
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]

def run():
    if st.button('Submit'):
        if model == first_model:
            st.write(text)
            st.write(distilbert(text))
