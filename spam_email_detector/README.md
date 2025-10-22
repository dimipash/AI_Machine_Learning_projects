# Spam Email Detector

This project is a simple spam email detector built in Python using natural language processing (NLP) and machine learning techniques. It uses a logistic regression model to classify emails as either "spam" or "ham" (not spam).

## Features

-   Text preprocessing using NLTK for cleaning and normalization.
-   TF-IDF vectorization to convert text data into numerical features.
-   Logistic Regression model for classification.
-   A function to predict whether a new email is spam or ham.

## Requirements

-   Python >= 3.13
-   nltk >= 3.9.2
-   numpy >= 2.3.4
-   pandas >= 2.3.3
-   scikit-learn >= 1.7.2

## Usage

1.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run the `main.py` script:

    ```bash
    python main.py
    ```

The script will train the model, print the accuracy and a classification report, and then predict whether a sample email is spam or ham.

## Dataset

The model is trained on the `spam.csv` dataset, which contains a collection of labeled emails.

## Model

The logistic regression model is trained on a TF-IDF vectorized representation of the email messages. The model achieves an accuracy of over 95% on the test set.
