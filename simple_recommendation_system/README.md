# Simple Recommendation System

This project implements a simple recommendation system in Python using content-based and user-based collaborative filtering techniques.

## Project Overview

The recommendation system provides two main functionalities:

1.  **Content-Based Recommendation:** Recommends books based on their category.
2.  **User-Based Collaborative Filtering:** Recommends books to a user based on the ratings of similar users.

The project is implemented in a single Python script, `main.py`, and uses the following libraries:

*   **pandas:** For data manipulation and analysis.
*   **numpy:** For numerical operations.
*   **scikit-learn:** For building the recommendation models.

## Getting Started

### Prerequisites

*   Python 3.6+
*   pip

### Installation

1.  Clone this repository.
  
2.  Navigate to the project directory:
    ```bash
    cd simple_recommendation_system
    ```
3.  Install the required dependencies:
    ```bash
    uv add -r requirements.txt
    ```

### Running the Project

To run the recommendation system, execute the `main.py` script:

```bash
uv run main.py
```

This will output the following recommendations:

```
Content-Based Recommendation for 'Python Basics': ['Data Science with Python', 'Machine Learning for beginners']
User-Based Recommendation for 'Charlie': ['Deep Learning for beginners', 'Machine Learning for beginners']
```

## Recommendation Systems

### Content-Based Filtering

The content-based filtering approach recommends items similar to those a user has liked in the past. In this project, it recommends books based on their categories. The `TfidfVectorizer` from scikit-learn is used to convert the book categories into a matrix of TF-IDF features. The cosine similarity is then calculated between the books to find the most similar ones.

### User-Based Collaborative Filtering

The user-based collaborative filtering approach recommends items to a user based on the preferences of similar users. In this project, it recommends books to a user based on the ratings of other users. The cosine similarity is calculated between the users to find the most similar ones. The books rated highly by the most similar user are then recommended.


