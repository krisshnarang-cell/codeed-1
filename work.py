import streamlit as st

lang_codes = {"English": "en", "हिंदी": "hi", "Español": "es"}
translations = {
    "en": {"title": "TransformAI", "choose_lang": "Choose language:"},
    "hi": {"title": "ट्रांसफॉर्मAI", "choose_lang": "भाषा चुनें:"},
    "es": {"title": "TransformAI", "choose_lang": "Elige idioma:"}
}

lang = st.selectbox("Choose language:", list(lang_codes.keys()))
selected_lang = lang_codes[lang]
ui_texts = translations.get(selected_lang, translations["en"])

st.title(ui_texts["title"])
st.write(ui_texts["choose_lang"])

