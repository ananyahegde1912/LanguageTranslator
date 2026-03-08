# LanguageTranslator

## **Description**

I created a Language Translator app that lets users type a sentence and translate it into multiple languages. It’s simple to use and helps practice understanding different languages quickly.

## **Features**

- Users can type any text into a large input box.
- Users can select the language they want to translate into from a dropdown menu.
- Translated text appears instantly when the user clicks the “Translate” button.
- Supports multiple languages including English, Hindi, Bangla, French, Spanish, German, Japanese, Korean, and Arabic.

  
<img width="453" height="410" alt="Screenshot 2026-03-07 204124" src="https://github.com/user-attachments/assets/cbe08e31-186e-4f73-8f07-fbff53edf9fa" />

## **How It Works**
- I used Tkinter to create the input box, dropdown menu, and button.
- Users can type freely into the Text widget, which I customized to be large and easy to use.
- When a language is selected, the program internally converts the language name (like “English”) into a language code (like “en”) that the translator library can understand.
- Clicking the “Translate” button runs the GoogleTranslator from the deep_translator library, which translates the input text and displays it in an output label.


## **Future Improvements**

- Add more languages for translation.
- Save translation history so users can refer back to previous translations.

## **To Take Note**

- Install the deep_translator library in your computer in order to run the programme
