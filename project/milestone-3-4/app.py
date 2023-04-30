import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
### Load HUPD dataset
# Sample a small subset of the dataset that corresponds to all patent applications submitted in Jan 2016.
dataset = load_dataset('HUPD/hupd',
    name='sample',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    icpr_label=None,
    train_filing_start_date='2016-01-01',
    train_filing_end_date='2016-01-01',
    val_filing_start_date='2016-01-30',
    val_filing_end_date='2016-01-31',
)
### Exclude pending applications (also removed in finetuned model)
exclude_pending = dataset.filter(lambda example: example["decision"] != "PENDING")
### Extract necessary data lists
data = exclude_pending["validation"]
p_number = data["patent_number"]
p_abstract = data["abstract"]
p_claims = data["claims"]
p_decision = data["decision"]
abstract = ""
claims = ""
decision = ""
### Streamlit app
st.title("Patentability Score")
st.write("Select a patent ID and click submit to get patentability score.")
selected_id = st.selectbox("Patent ID:", p_number, index=len(p_number)-1)
selected_index = p_number.index(selected_id)
abstract = p_abstract[selected_index]
claims = p_claims[selected_index]
decision = p_decision[selected_index]
st.text_area("Abstract:", abstract)
st.text_area("Claims:", claims)
### Load model and tokenizer
def get_pipeline():
    model = AutoModelForSequenceClassification.from_pretrained("moonahhyun/project-uspto")
    tokenizer = AutoTokenizer.from_pretrained("moonahhyun/project-uspto")
    pl = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    return pl
### Perform patentability analysis
if st.button("Submit"):
    with st.spinner("Analyzing the patentability..."):
        pl = get_pipeline()
        result = pl(abstract)
        label = result[0]['label']
        score = result[0]['score']
        # Print score when label = accepted
        if label == "ACCEPTED":
            st.write(f"Patentability Score: {score}")
            st.write(f"Higher % of being: {label}")
        # Print 1 - score when label = rejected
        else: 
            score = 1 - score
            st.write(f"Patentability Score: {score}")
            st.write(f"Higher % of being: {label}")
        st.write(f"Actual Decision: {decision}")
else:
    st.write("Click 'Submit' for patentability score.")
