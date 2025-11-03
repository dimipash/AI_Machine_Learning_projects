# Fake News Detector

## Overview

This project is a machine learning-based application to detect fake news. It uses Natural Language Processing (NLP) techniques to process and classify news articles as either "REAL" or "FAKE". The model is trained on a labeled dataset of news articles and utilizes a Logistic Regression classifier.

## Features

- Text cleaning and preprocessing using NLTK.
- Feature extraction using TF-IDF vectorization.
- Fake news prediction using a trained Logistic Regression model.
- Model evaluation with accuracy and classification reports.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- `uv` package manager

### Installation

1. **Clone this repository.** 

2. **Create a virtual environment and install dependencies:**

   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

   *(Note: You may need to create a `requirements.txt` file from `pyproject.toml` or have `uv` handle it directly if it supports `pyproject.toml`.)*

## Usage

To run the fake news detection script:

```bash
python main.py
```

This will train the model, print the accuracy and classification report, and make a prediction on a sample news text.

## Dataset

The dataset used for training is in the `data.csv` file. It contains two columns:

- `text`: The text of the news article.
- `label`: The label of the news article, which is either "REAL" or "FAKE".

## Model

- **Model:** Logistic Regression
- **Feature Extraction:** TF-IDF Vectorizer (with a maximum of 5000 features)
- **Accuracy:** The accuracy of the model is printed to the console when you run `main.py`.

