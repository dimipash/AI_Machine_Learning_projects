from googletrans import Translator

# translator = Translator()

# text = "Hello, how are you?"
# translated_text = translator.translate(text, src='en', dest='it')
# print(f"Original: {text}")
# print(f"Translated: {translated_text.text}")

def translate_text():
    translator = Translator()
    text = input("Enter text to translate: ")
    source_lang = input("Enter source language code (e.g., 'en', 'fr', 'de'): ")
    target_lang = input("Enter target language code (e.g., 'en', 'fr', 'de'): ")

    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    print(f"Translated Text: {translated_text.text}")

translate_text()
