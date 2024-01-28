import streamlit as st
from googletrans import Translator, LANGUAGES

def lang_trans():
    st.title("Language Translator App")
    translator = Translator()

    st.sidebar.header("Supported Languages")
    for code, language in LANGUAGES.items():
        st.sidebar.write(f"{code}: {language}")

    source_lang = st.sidebar.selectbox("Select your language code", list(LANGUAGES.keys()))
    target_lang = st.sidebar.selectbox("Select target language code", list(LANGUAGES.keys()))
    text_to_translate = st.text_area("Enter the text to translate")

    if st.button("Translate"):
        try:
            translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
            st.success(f"Original Text ({LANGUAGES[source_lang]}): {text_to_translate}")
            st.success(f"Translation ({LANGUAGES[target_lang]}): {translation.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    lang_trans()
