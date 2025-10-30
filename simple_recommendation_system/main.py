import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
data = {
    "Book": ["Python Basics", "Deep Learning for beginners", "Data Science with Python", "Machine Learning for beginners", "AI Fundamentals"],
    "Category": ["Programming", "Deep Learning", "Data Science", "Machine Learning", "Artificial Intelligence"],
}
df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
category_vectors = vectorizer.fit_transform(df["Category"])
similarity_matrix = cosine_similarity(category_vectors)

def recommend_books(book_name):
    if book_name not in df["Book"].values:
        return "Book not found in the dataset."

    index = df[df["Book"] == book_name].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = [df["Book"][i] for i,_ in scores[1:3]]
    return recommendations

user_ratings = {
    "User": ["Alice", "Bob", "Charlie", "David"],
    "Python Basics": [5, 3, 0, 4],
    "Deep Learning for beginners": [4, 0, 5, 2],
    "Data Science with Python": [0, 5, 4, 3],
    "Machine Learning for beginners": [2, 4, 5, 5],
    "AI Fundamentals": [5, 3, 4, 0],
}

ratings_df = pd.DataFrame(user_ratings).set_index("User")
user_similarity = cosine_similarity(ratings_df.fillna(0))
np.fill_diagonal(user_similarity, 0)
user_sim_df = pd.DataFrame(user_similarity, index=ratings_df.index, columns=ratings_df.index)

def recommend_for_user(user):
    if user not in user_sim_df.index:
        return "User not found in the dataset."

    similar_users = user_sim_df[user].sort_values(ascending=False).index[0]
    recommended_books = ratings_df.loc[similar_users][ratings_df.loc[similar_users] == 5].index.tolist()
    
    return recommended_books

print("Content-Based Recommendation for 'Python Basics':", recommend_books("Python Basics"))
print("User-Based Recommendation for 'Charlie':", recommend_for_user("Charlie"))

