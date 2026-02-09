# 🔍 VerifiAI — The Research Integrity Auditor

**VerifiAI** is a forensic data auditing system designed to detect **"Scientific Friction"**—the gap between *what a research paper claims* and *what its underlying dataset actually supports*. Built for the **AI & Data Science** ecosystem, VerifiAI combines **LLMs**, **automated statistical profiling**, and **forensic cross-referencing** to promote transparency, reproducibility, and trust in research.

---

## 📊 Project Badges

<!-- Replace links and usernames as needed -->

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-purple)

---

## 🖼️ Visual Overview

![VerifiAI Dashboard](https://github.com/Karthih2/verifiai-audit/blob/main/results/Result%201.png)
*Streamlit-based dashboard showing manuscript upload, dataset profiling, and integrity score.*

![Audit Flow](https://github.com/Karthih2/verifiai-audit/blob/main/results/Result%202.png) 
*End-to-end forensic auditing pipeline: Manuscript → Dataset → Integrity Report.*
![Audit Flow](https://github.com/Karthih2/verifiai-audit/blob/main/results/Result%203.png) 

---

## 🚀 Key Features

### 🧪 Forensic Cross-Referencing

Automatically compares **claims in research PDFs** against **ground-truth dataset statistics** to identify inconsistencies.

### 🧠 Chain-of-Thought Auditing

Uses advanced prompt engineering to reason through:

* Methodological gaps
* Data leakage risks
* Metric misuse or deception

### ⚡ Turbo-Optimized Pipeline

Efficient document parsing that focuses on **Abstract**, **Methods**, and **Results**, delivering audits in seconds.

### 📈 Automated Statistical Profiling

Real-time dataset analysis including:

* Class distribution checks
* Duplicate & leakage detection
* Feature presence and transformation analysis

### 🧮 Integrity Scoring

Assigns a **0–100 Integrity Score** quantifying detected *Scientific Friction*.

---

## 🧠 Design Thinking Approach

### 1️⃣ Empathy Mapping

| Stakeholder           | Pain Point                                                   | VerifiAI Solution                   |
| --------------------- | ------------------------------------------------------------ | ----------------------------------- |
| **Journal Reviewers** | Overwhelmed by submissions; limited time for data validation | Automated first-pass forensic audit |
| **Researchers**       | Unintentional reporting errors or hidden leakage             | Pre-submission integrity check      |
| **Public / Industry** | Reliance on irreproducible or p-hacked results               | Transparent integrity scoring       |

---

### 2️⃣ Problem Statement

> **How might we instantly detect logical contradictions between a research manuscript and its raw data to prevent scientific misinformation?**

---

## 🛠️ Technical Stack

* **Frontend**: Streamlit (clean, modern UI)
* **AI Engine**: Google Gemini 1.5 Flash (fast inference, large context window)
* **Processing**: Python (Pandas, NumPy)
* **Document Parsing**: PyPDF2
* **Prompt Engineering**: Chain-of-Thought (CoT) with XML delimiters

---

## 📂 Project Structure

```
VerifiAI-Audit/
├── src/
│   ├── app.py              # Main Streamlit application
│   └── prompts.txt         # Chain-of-Thought forensic prompts
├── assets/                 # Images & diagrams (placeholders)
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/YourUsername/VerifiAI-Audit.git
cd VerifiAI-Audit
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_actual_key_here
```

### 4️⃣ Run the Application

```
streamlit run src/app.py
```

---

## 🤖 Advanced Prompting Logic

VerifiAI goes beyond surface-level analysis by applying **forensic reasoning**:

1. **Extraction**
   Identifies claims related to features, preprocessing, and evaluation metrics.

2. **Conflict Detection**
   Cross-checks claims against dataset statistics (e.g., flags *accuracy* on highly imbalanced data).

3. **Validation**
   Verifies whether reported features actually exist or are obscured (e.g., PCA-transformed variables).

---

## 📌 Use Cases

* Pre-submission paper audits
* Journal and conference reviewer assistance
* Research reproducibility checks
* AI ethics and integrity assessments

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## ⭐ Acknowledgements

Inspired by the growing need for **transparent, reproducible, and trustworthy AI research**.

> *“Science advances fastest when claims and data speak the same truth.”*

