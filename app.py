import streamlit as st
import nbformat
from evaluator import evaluate_notebook

# Streamlit configuration
st.set_page_config(page_title="Notebook Evaluator", layout="centered")

# Custom styling for the app
st.markdown("""
    <style>
    .stApp { background-color: #ffe5b4; }
    .main-card {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("📓 Notebook Evaluator")
st.write("Upload your `.ipynb` file to get instant feedback on its structure and code quality.")

# File upload for Jupyter Notebook
uploaded_file = st.file_uploader("Upload your Jupyter Notebook", type=["ipynb"])

# Process the notebook on upload
if uploaded_file is not None:
    with st.spinner("⏳ Evaluating notebook..."):
        try:
            # Read the notebook content
            notebook = nbformat.read(uploaded_file, as_version=4)
            
            # Evaluate the notebook
            result = evaluate_notebook(notebook)

            # Display evaluation result
            st.subheader("📊 Evaluation Result")
            st.json(result)
        except Exception as e:
            st.error(f"❌ Error reading notebook: {e}")

st.markdown('</div>', unsafe_allow_html=True)
