import streamlit as st
import google.generativeai as genai
import pandas as pd
from PyPDF2 import PdfReader
import os
import time
import random
from dotenv import load_dotenv
from google.api_core import exceptions

# --- 1. CONFIGURATION ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found! Add GEMINI_API_KEY to your .env file.")
    st.stop()

genai.configure(api_key=API_KEY)
MODEL_ID = "gemini-3-flash-preview"

def load_prompts(filepath="prompts.txt"):
    """Reads logic from external file with UTF-8 support."""
    if not os.path.exists(filepath):
        return "You are a Research Auditor.", "Identify discrepancies."
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if "SYSTEM_INSTRUCTION:" in content and "AUDIT_LOGIC:" in content:
            sys_instr = content.split("SYSTEM_INSTRUCTION:")[1].split("AUDIT_LOGIC:")[0].strip()
            audit_logic = content.split("AUDIT_LOGIC:")[1].strip()
            return sys_instr, audit_logic
        return "You are a Research Auditor.", content
    except Exception:
        return "You are a Research Auditor.", "Analyze the data."

# --- 2. OPTIMIZED DOCUMENT PROCESSING (FAST) ---
def extract_pdf_text_fast(file, max_pages=6):
    """
    Optimized: Reads key pages to prevent UI hanging.
    """
    try:
        reader = PdfReader(file)
        text = ""
        pages_to_process = min(max_pages, len(reader.pages))
        
        # Progress bar for visual feedback
        progress_bar = st.progress(0, text="Reading PDF...")
        for i in range(pages_to_process):
            content = reader.pages[i].extract_text()
            if content:
                text += content + "\n"
            progress_bar.progress((i + 1) / pages_to_process, text=f"Processing page {i+1}...")
        
        time.sleep(0.3) 
        progress_bar.empty()
        return text
    except Exception as e:
        st.error(f"PDF Error: {e}")
        return ""

def get_data_summary_fast(df):
    """
    Optimized: Summary statistics for the Auditor.
    """
    row_count = len(df)
    # Sample if the dataset is massive to keep the app fast
    if row_count > 10000:
        sample_df = df.sample(2000)
        duplicates = f"~{int(sample_df.duplicated().sum() * (row_count/2000))} (estimated)"
    else:
        duplicates = int(df.duplicated().sum())

    return {
        "total_rows": row_count,
        "columns": df.columns.tolist(),
        "duplicates": duplicates,
        "class_balance": df.iloc[:, -1].value_counts(normalize=True).head(5).to_dict()
    }

# --- 3. API WRAPPER (Corrected Keyword Mappings) ---
def safe_audit_call(sys_instr, prompt_body):
    """Handles Rate Limiting (429) gracefully."""
    model = genai.GenerativeModel(model_name=MODEL_ID, system_instruction=sys_instr)
    for attempt in range(3):
        try:
            return model.generate_content(prompt_body)
        except exceptions.ResourceExhausted:
            wait = (attempt * 2) + 3
            st.warning(f"⚠️ API Busy. Retrying in {wait}s...")
            time.sleep(wait)
    return None

# --- 4. STREAMLIT UI ---
st.set_page_config(page_title="VerifiAI Auditor", layout="wide", page_icon="🕵️")

st.title("🕵️ VerifiAI: Forensic Research Auditor")
st.write("Detecting 'Scientific Friction' between Manuscript claims and Raw Data.")

col1, col2 = st.columns(2)
with col1:
    uploaded_pdf = st.file_uploader("1. Research Manuscript (PDF)", type="pdf")
with col2:
    uploaded_csv = st.file_uploader("2. Raw Dataset (CSV)", type="csv")

if st.button("🚀 EXECUTE FORENSIC AUDIT", use_container_width=True):
    if uploaded_pdf and uploaded_csv:
        # Step 1: Document Processing
        with st.status("⚡ Processing Inputs...", expanded=True) as status:
            st.write("Reading Manuscript (Fast Mode)...")
            paper_content = extract_pdf_text_fast(uploaded_pdf, max_pages=6)
            
            st.write("Summarizing Dataset...")
            df = pd.read_csv(uploaded_csv)
            data_stats = get_data_summary_fast(df)
            
            st.write("Fetching Audit Logic...")
            sys_msg, audit_logic = load_prompts()
            status.update(label="✅ Pre-processing Done!", state="complete", expanded=False)

        # Step 2: AI Audit
        if paper_content:
            with st.spinner("🤖 Gemini is performing the Forensic Audit..."):
                final_prompt = f"{audit_logic}\n\n[DATA STATS]: {data_stats}\n\n[PAPER TEXT]: {paper_content[:8000]}"
                
                # FIXED: Arguments match the definition in safe_audit_call
                response = safe_audit_call(sys_instr=sys_msg, prompt_body=final_prompt)

                if response:
                    st.divider()
                    
                    # UI Score Display
                    try:
                        score_raw = response.text.split("Integrity Score:")[1].strip()
                        score = "".join(filter(str.isdigit, score_raw.split("/")[0]))
                        st.metric("Integrity Score", f"{score}/100")
                    except:
                        pass
                    
                    st.markdown("### 📋 Forensic Audit Report")
                    st.markdown(response.text)
                    
                    # Visualization for presentation
                    st.subheader("📊 Target Variable Distribution")
                    st.bar_chart(df.iloc[:, -1].value_counts())
    else:
        st.warning("Please upload both a PDF and a CSV to begin.")