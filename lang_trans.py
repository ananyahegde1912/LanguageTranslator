import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Language options
languages = {
    "English": "en",
    "Bangla": "bn",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

def translate_text():
    text = input_text.get("1.0", tk.END)
    lang_name = lang_combo.get()
    lang_code = languages[lang_name]

    translated = GoogleTranslator(
        source="auto",
        target=lang_code
    ).translate(text)

    output_label.config(text=translated)

# Window
window = tk.Tk()
window.title("Language Translator")
window.geometry("500x500")
window.configure(bg="#E3FCEA")

# Input
tk.Label(window, text="Enter text:", font=("Arial", 12, "bold"), fg="black", bg="#E3FCEA").pack(pady=20)
input_text = tk.Text(window, width=50, height=5)
input_text.pack(pady=10)

# Language dropdown
tk.Label(window, text="Select language:", font=("Arial",12, "bold"),fg="black", bg="#E3FCEA").pack(pady=20)
lang_combo = ttk.Combobox(window, values=list(languages.keys()), width=18,font=("Arial",10))
lang_combo.set("English")
lang_combo.pack(pady=10)

# Button
tk.Button(window, text="Translate", command=translate_text, width=8, height=1, font=("Arial",10), fg="black").pack(pady=25)

# Output
output_label = tk.Label(window, text="", fg="#000502", bg="#E3FCEA", wraplength=350, font=("Arial",12))
output_label.pack(pady=15)

window.mainloop()

