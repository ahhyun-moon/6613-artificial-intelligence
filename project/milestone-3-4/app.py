import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset

dataset = load_dataset('HUPD/hupd',
    name='sample',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    icpr_label=None,
    train_filing_start_date='2016-01-01',
    train_filing_end_date='2016-01-01',
    val_filing_start_date='2016-01-30',
    val_filing_end_date='2016-01-31',
)
exclude_pending = dataset.filter(lambda example: example["decision"] != "PENDING")
data = exclude_pending["validation"]
p_number = data["patent_number"]
p_abstract = data["abstract"]
p_claims = data["claims"]
p_decision = data["decision"]
abstract = ""
claims = ""
decision = ""
# Streamlit app
st.title("Patentability Score")
st.write("Select a patent ID and click submit to get patentability score.")
selected_id = st.selectbox("Patent ID:", p_number, index=len(p_number)-1)
selected_index = p_number.index(selected_id)
abstract = p_abstract[selected_index]
claims = p_claims[selected_index]
decision = p_decision[selected_index]

st.text_area("Abstract:", abstract)
st.text_area("Claims:", claims)

def get_pipeline():
    model = AutoModelForSequenceClassification.from_pretrained("moonahhyun/project-uspto")
    tokenizer = AutoTokenizer.from_pretrained("moonahhyun/project-uspto")
    pl = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return pl

# Load the model and perform sentiment analysis
if st.button("Submit"):
    with st.spinner("Analyzing the patent claims..."):
        pl = get_pipeline()
        result = pl(abstract)
        label = result[0]['label']
        score = result[0]['score']
        if label == "ACCEPTED":
            st.write(f"Patentability Score: {score}")
            st.write(f"Higher % of being: {label}")
        else: 
            score = 1 - score
            st.write(f"Patentability Score: {score}")
            st.write(f"Higher % of being: {label}")
        st.write(f"Actual Decision: {decision}")
else:
    st.write("Click 'Submit' for patentability score.")