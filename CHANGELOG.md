# 📑 Changelog – AutoEDA

All notable changes to this project will be documented here.  
This project follows a **phase-wise learning journey** rather than strict semantic versioning.  

---

## [Phase 1] – MVP Auto-EDA Script ✅
### Added
- `eda_mvp.py`: Minimal auto-EDA script that:
  - Reads CSV file and generates dataset summary
  - Handles missing values reporting
  - Outputs numerical & categorical summaries
  - Saves histograms, bar plots, and correlation heatmap
- `requirements.txt`: Initial dependencies (pandas, numpy, seaborn, matplotlib)
- `.gitignore`: Ignore venv, caches, and outputs folder

---

## [Phase 1] – Documentation & Repo Setup ✅
### Added
- `README.md`: Project description, usage guide, roadmap, and structure
- `LICENSE`: MIT License
- `CONTRIBUTING.md`: Contribution guidelines
- `CODE_OF_CONDUCT.md`: Community guidelines
- Badges (Python, License, Contributions, Stars, Forks) in README
- Project folder structure diagram in README

---

## [Phase 2] – Automated Reports (Planned)
### Planned
- Generate HTML reports using **ydata-profiling / Sweetviz**
- Export EDA summary as **PDF** (with charts)
- Add command-line option `--report` to generate reports

---

## [Phase 3] – Interactive Dashboard (Planned)
### Planned
- Build **Streamlit dashboard** for dataset uploads
- Add interactive charts & filters
- Preview and download reports directly from UI

---

## [Phase 4] – AI-Powered Insights (Planned)
### Planned
- Integrate **OpenAI / Hugging Face LLM** for natural language summaries
- Enable prompt-based queries (e.g., *“Find correlations in dataset”*)
- Provide feature engineering suggestions

---

## [Phase 5] – Advanced Features (Planned)
### Planned
- ML Readiness report (class imbalance, leakage, skewness, etc.)
- Feature engineering recommendations
- API support via Flask/FastAPI
- Deployment on **Streamlit Cloud / Hugging Face Spaces**
