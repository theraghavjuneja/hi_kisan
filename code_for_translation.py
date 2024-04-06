from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


# english_text = "Hello World Friend"
# translated_text = translate_text(english_text, 'hi')  # 'hi' is the language code for Hindi
# print(translated_text)
