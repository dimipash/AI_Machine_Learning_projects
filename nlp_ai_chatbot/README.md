# AI Chatbot with NLTK and Transformers

This project implements a versatile chatbot application in Python. It offers two distinct conversational modes: a straightforward rule-based chatbot for common queries and an advanced AI-powered chatbot leveraging the `microsoft/DialoGPT-medium` model from the Hugging Face Transformers library. The application also includes text preprocessing capabilities using NLTK.

## Features

*   **Rule-Based Chatbot**: Provides quick, predefined responses to common greetings and questions.
*   **AI-Powered Chatbot**: Utilizes a pre-trained transformer model (`microsoft/DialoGPT-medium`) for more dynamic and context-aware conversations.
*   **Text Cleaning**: Includes functions to clean and preprocess text, such as lowercasing, removing punctuation, and removing stop words using NLTK.
*   **Interactive CLI**: A simple command-line interface for seamless user interaction.

## Technologies Used

*   **Python**: The primary programming language.
*   **NLTK**: For natural language processing tasks like tokenization and stop word removal.
*   **Transformers (Hugging Face)**: For accessing and utilizing advanced pre-trained language models.
*   **uv**: For efficient dependency management.

## Installation

1.  **Clone the repository**
2.  **Install dependencies** using `uv`. Navigate to the project directory in your terminal and run:
    ```bash
    uv sync .
    ```
    This command will install all necessary packages as defined in `pyproject.toml`.
3.  **NLTK Data**: The script automatically downloads required NLTK data (`punkt_tab` and `stopwords`) on the first run if they are not already present.

## Usage

1.  **Run the application**:
    ```bash
    uv run main.py
    ```
2.  **Interact with the chatbot**: Follow the prompts in your terminal. You can type your messages and press Enter.
3.  **To exit**: Type `exit` and press Enter.

## Example Interaction

```
Welcome to the Chatbot System!
Type 'exit' to quit.
You: hello
Chatbot: Hi there!
You: tell me about yourself
Chatbot: I'm a simple chatbot.
You: what is the weather like today?
Chatbot: I'm sorry, I didn't understand that.
You: bye
Chatbot: Goodbye!
```
*(Note: The AI chatbot's responses may vary as it generates text dynamically.)*
