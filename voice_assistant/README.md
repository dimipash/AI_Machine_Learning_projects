# Voice Assistant

A simple voice assistant built in Python that can perform basic tasks based on voice commands.

## Features

- **Voice Recognition:** Listens for voice commands and converts them to text.
- **Text-to-Speech:** Provides spoken responses.
- **Tells Time:** Can tell you the current time.
- **Wikipedia Search:** Can search for topics on Wikipedia and read a summary of the results.
- **Exit:** Can be terminated with a "goodbye" message.

## Requirements

The following Python libraries are required to run this project:

- `pyttsx3`
- `SpeechRecognition`
- `wikipedia`

You can install them using uv:

```bash
uv add pyttsx3 SpeechRecognition wikipedia
```

## Usage

To start the voice assistant, run the `main.py` file:

```bash
uv run main.py
```

The assistant will greet you and then start listening for your commands.

## Commands

The following voice commands are supported:

- **"time"**: The assistant will tell you the current time.
- **"wikipedia"**: The assistant will ask you what to search for, and then provide a summary from Wikipedia.
- **"exit"** or **"quit"**: The assistant will say goodbye and terminate the program.
