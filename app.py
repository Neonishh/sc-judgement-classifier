import streamlit as st
import pandas as pd

# --- Load CSVs ---
lda_path = 'judgment_law_category_mapped.csv'
doc2vec_path = 'doc2vec_output_predictions.csv'

df_lda = pd.read_csv(lda_path, dtype=str)       # read as string to handle hyphens
df_doc2vec = pd.read_csv(doc2vec_path, dtype=str)

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
    color: #0f4c81;  /* make text visible */
}
</style>
""", unsafe_allow_html=True)

# --- App UI ---
st.title("⚖️ Supreme Court Judgment Category Lookup")

st.markdown("""
This tool predicts the **law category** of Indian Supreme Court judgments.
- Select the **model** (LDA or Doc2Vec).
- Enter a **diary number**.
- See the predicted law category.
""")

# --- Model selection ---
model = st.selectbox("Select Model:", ["LDA", "Doc2Vec"])

# --- Diary number input ---
diary_input = st.text_input("Enter Diary Number:")

if st.button("Lookup Category"):
    if not diary_input.strip():
        st.error("⚠️ Please enter a diary number.")
    else:
        diary_no = diary_input.strip()  # keep as string, your CSVs have hyphens
        
        if model == "LDA":
            row = df_lda[df_lda['diary_no'] == diary_no]
            category = row.iloc[0]['law_category'] if not row.empty else "❌ Not found"
            card_color = "#99ccff"  # blue-ish for LDA
        else:  # Doc2Vec
            row = df_doc2vec[df_doc2vec['diary_no'] == diary_no]
            category = row.iloc[0]['category_name'] if not row.empty else "❌ Not found"
            card_color = "#99ff99"  # green-ish for Doc2Vec
        
        # Display result in a colored card
        st.markdown(f"""
        <div class="card" style="background-color:{card_color}">
        <h3>📘 {model} Prediction</h3>
        <p style="font-size:18px">{category}</p>
        </div>
        """, unsafe_allow_html=True)
