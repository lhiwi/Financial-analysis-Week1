# Financial News Sentiment Analysis

![CI Status](https://github.com/lhiwi/Financial-analysis-Week1/workflows/Python%20CI/CD/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue)

> Week 1 challenge solution for 10 Academy AI Mastery program analyzing correlations between financial news sentiment and stock movements.

## Features
- NLP sentiment analysis of financial headlines
- Technical indicators (RSI, MACD) with TA-Lib
- Correlation analysis between news sentiment and stock returns
- Automated CI/CD pipeline with GitHub Actions
- Comprehensive exploratory data analysis

## Project Structure
├── .github/workflows/ # CI/CD pipelines
├── data/ # Financial datasets
├── notebooks/ # Jupyter notebooks
│ └── eda.ipynb # EDA implementation
├── plots/ # Generated visualizations
├── reports/ # Documentation
├── src/ # Source code
├── tests/ # Test cases
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## Setup
```bash
# 1. Clone repository
git clone https://github.com/lhiwi/Financial-analysis-Week1.git
cd Financial-analysis-Week1

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run EDA
jupyter notebook notebooks/eda.ipynb

```
Key Analyses
- Headline length statistics
- Top publishers by volume
- Publication time patterns
- Keyword extraction from headlines
- Daily publication frequency
