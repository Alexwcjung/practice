import streamlit as st
from gtts import gTTS
import io

st.subheader("Text-to-Speech Converter (using Google TTS)")

default_text = """"""

text_input = st.text_area(
    "Enter the text you want to convert to speech:",
    value=default_text,
    height=200
)

language = st.selectbox(
    "Choose a language: 🇰🇷 🇺🇸 🇬🇧",
    [
        "Korean",
        "English (American)",
        "English (British)"
    ]
)

tts_button = st.button("Convert Text to Speech")

if tts_button and text_input:
    lang_codes = {
        "Korean": ("ko", None),
        "English (American)": ("en", "com"),
        "English (British)": ("en", "co.uk")
    }

    language_code, tld = lang_codes[language]

    if tld:
        tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
    else:
        tts = gTTS(text=text_input, lang=language_code, slow=False)

    speech = io.BytesIO()
    tts.write_to_fp(speech)
    speech.seek(0)

    st.audio(speech.getvalue(), format="audio/mp3")
