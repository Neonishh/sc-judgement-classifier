import streamlit as st
import pandas as pd

# --- Load CSVs ---
lda_path = 'judgment_law_category_mapped.csv'
doc2vec_path = 'doc2vec_output_predictions.csv'
bert_path = 'bert_judgment_predictions.csv'   # new file for BERT predictions

df_lda = pd.read_csv(lda_path, dtype=str)
df_doc2vec = pd.read_csv(doc2vec_path, dtype=str)
df_bert = pd.read_csv(bert_path, dtype=str)

# --- Custom CSS for nicer UI ---
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
}
h1 {
    color: #0f4c81;
    text-align: center;
}
.stButton>button {
    background-color: #0f4c81;
    color: white;
    font-size: 16px;
    padding: 10px 20px;
}
.stTextInput>div>input, .stSelectbox>div>div>div>select {
    padding: 8px;
    font-size: 16px;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.card h3, .card p {
    color: #0f4c81;
}
</style>
""", unsafe_allow_html=True)

# --- App UI ---
st.title("⚖️ Indian Supreme Court Judgment Category Lookup")

st.markdown("""
This tool predicts the **law category** of Indian Supreme Court judgments.
- Select the **model** (LDA, Doc2Vec, or BERT).
- Enter a **diary number**.
- See the predicted law category.
""")

# --- Model selection ---
model = st.selectbox("Select Model:", ["LDA", "Doc2Vec", "BERT"])

# --- Diary number input ---
diary_input = st.text_input("Enter Diary Number:")

if st.button("Lookup Category"):
    if not diary_input.strip():
        st.error("⚠️ Please enter a diary number.")
    else:
        diary_no = diary_input.strip()
        
        if model == "LDA":
            row = df_lda[df_lda['diary_no'] == diary_no]
            category = row.iloc[0]['law_category'] if not row.empty else "❌ Not found"
            card_color = "#99ccff"  # blue for LDA

        elif model == "Doc2Vec":
            row = df_doc2vec[df_doc2vec['diary_no'] == diary_no]
            category = row.iloc[0]['category_name'] if not row.empty else "❌ Not found"
            card_color = "#99ff99"  # green for Doc2Vec

        else:  # BERT
            row = df_bert[df_bert['diary_no'] == diary_no]
            # adjust column name if different, e.g., 'bert_predicted_category'
            category = row.iloc[0]['predicted_category'] if not row.empty else "❌ Not found"
            card_color = "#ffcc99"  # orange for BERT
        
        # --- Display result card ---
        st.markdown(f"""
        <div class="card" style="background-color:{card_color}">
        <h3>📘 {model} Prediction</h3>
        <p style="font-size:18px">{category}</p>
        </div>
        """, unsafe_allow_html=True)
