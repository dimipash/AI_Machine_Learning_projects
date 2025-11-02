import tkinter as tk
from googletrans import Translator

translator = Translator()

def translate():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = target_lang_var.get()
    if text:
        translated_text = translator.translate(text, dest=target_lang)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text.text)
        output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Text Translator")
root.geometry("400x400")

input_text = tk.Text(root, height=10, width=40)
input_text.pack(pady=10)

target_lang_var = tk.StringVar(root)
target_lang_var.set("es")  
lang_dropdown = tk.OptionMenu(root, target_lang_var, "es", "fr", "de", "it", "ru")
lang_dropdown.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=5)

output_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
output_text.pack(pady=10)

root.mainloop()
