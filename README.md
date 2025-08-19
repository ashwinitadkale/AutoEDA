![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)
![GitHub stars](https://img.shields.io/github/stars/ashwinitadkale/eda-ai-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/ashwinitadkale/eda-ai-tool?style=social)

# 🧠 AutoEDA – AI-powered Exploratory Data Analysis Tool

AutoEDA is a step-by-step project where we are building an **AI-powered Exploratory Data Analysis (EDA) assistant**.  
This repo documents the journey from a **basic EDA script (Phase 1)** to a **full-fledged interactive AI EDA tool** 🚀  

---

## ✅ Features (Phase 1 MVP)
- Upload any CSV file and instantly get:
  - Dataset summary (rows, columns, dtypes, missing values)
  - Basic statistics for numeric columns
  - Preview of first 20 rows
  - Histograms for numeric columns
  - Bar plots for categorical columns
  - Correlation heatmap for numeric features
- Outputs are saved in the `outputs/` folder

---

## 📂 Project Structure

```bash
eda-ai-tool/
│── .gitignore          # Ignore venv, cache, outputs, etc.
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
│── eda_mvp.py          # Phase 1: Minimal Auto-EDA script
│
├── outputs/            # Generated reports & plots (created at runtime)
│   ├── summary.txt
│   ├── sample_head.csv
│   ├── hist_column.png
│   ├── bar_column.png
│   └── correlation_heatmap.png
│
└── .venv/              # Virtual environment (ignored in Git)

## 🛠 Installation

Clone the repo:
```bash
git clone https://github.com/ashwinitadkale/AutoEDA.git
cd eda-ai-tool
