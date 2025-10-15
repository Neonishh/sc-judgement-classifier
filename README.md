# Automated Classification of Indian Supreme Court Legal Judgments Using NLP

## **Team**

**Team Number:** 30

**Collaborators:**

* Nidhi K – SRN: PES2UG23CS383
* Navya G N – SRN: PES2UG23CS372

---

## **Project Overview**

Indian Supreme Court judgments are lengthy and written in specialized legal language, making manual classification into categories like constitutional law, criminal law, civil rights, and taxation slow and expertise-intensive.

This project automates classification using **unsupervised NLP techniques**:

* **LDA (Latent Dirichlet Allocation)** – topic modeling
* **Doc2Vec** – document embeddings
* **BERT/Longformer** – embeddings for capturing semantic information in long texts

Challenges addressed:

* Multiple overlapping legal themes per judgment
* Long-form documents
* Improving unsupervised classification accuracy in the Indian legal domain

---

## **Workflow**

1. **Dataset Preparation**

   * Cleaned judgments dataset uploaded to Google Drive: [Link](https://drive.google.com/drive/folders/1Ig2TMrXHS4uqzA3UQ0nKWckgiXURY9v1)

2. **LDA Model**

   * Preprocessing: PDF text extraction, chunking
   * Unsupervised topic modeling
   * Visualization of topic distributions

3. **Doc2Vec Model**

   * Preprocessing: PDF text extraction, chunking
   * Document embeddings for unsupervised classification
   * Visualization of embedding-based clusters

4. **BERT/Longformer Embeddings**

   * Extracted embeddings from long legal texts
   * Used for semantic representation and unsupervised similarity analysis

5. **UI Application (`app.py`)**

   * Streamlit-based interface
   * Enter a **diary number** → returns predicted judgment category

---

## **How to Use**

1. pip install -r requirements.txt
2. Upload cleaned dataset to the model directories.
3. Run preprocessing and training scripts.
4. Launch UI:

   ```bash
   streamlit run app.py
   ```
5. Input a **diary number** to get the predicted judgment category.

---

## **Key Features**

* Fully unsupervised approach: LDA, Doc2Vec, embeddings
* Handles long legal documents
* Interactive Streamlit UI
* Visualizations for classification insights
