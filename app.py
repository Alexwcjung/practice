import streamlit as st
from gtts import gTTS
import io

st.subheader("Text-to-Speech Converter (using Google TTS)")

text_input = st.text_area("Enter the text you want to convert to speech:")

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

st.markdown("---")
st.caption("🇺🇸 English text: Teacher-designed coding applications create tailored learning experiences, making complex concepts easier to understand through interactive and adaptive tools. They enhance engagement, provide immediate feedback, and support active learning.")
st.caption("🇰🇷 Korean text: 교사가 직접 만든 코딩 기반 애플리케이션은 학습자의 필요에 맞춘 학습 경험을 제공하고, 복잡한 개념을 쉽게 이해하도록 돕습니다. 또한 학습 몰입도를 높이고 즉각적인 피드백을 제공하며, 능동적인 학습을 지원합니다.")
