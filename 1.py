import streamlit as st
import google.generativeai as genai
import os
from gtts import gTTS
import tempfile

st.title("TransformAI")

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Change environment variable name

lang_codes = {
    "English": "en", "हिंदी": "hi", "Español": "es", "Français": "fr", "Deutsch": "de",
    "中文": "zh", "日本語": "ja", "한국어": "ko", "Русский": "ru", "اردو": "ur",
    "বাংলা": "bn", "తెలుగు": "te", "தமிழ்": "ta", "ગુજરાતી": "gu", "मराठी": "mr",
    "ਪੰਜਾਬੀ": "pa", "ಕನ್ನಡ": "kn", "मारवाड़ी": "rwr", "O‘zbekcha": "uz", "ქართული": "ka",
    "العربية": "ar", "Türkçe": "tr", "ภาษาไทย": "th", "فارسی": "fa", "Shqip": "sq",
    "Nederlands": "nl", "Svenska": "sv", "Italiano": "it", "Việt": "vi", "ລາວ": "lo"
}

lang = st.selectbox("Choose language:", list(lang_codes.keys()))
txt = st.text_area("Paste your text here")
outpt = st.selectbox(
    "Choose output type:",
    ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"]
)

# Initialize session states
if "sp_state" not in st.session_state:
    st.session_state.sp_state = False
if "result" not in st.session_state:
    st.session_state.result = ""

# Generate output
if st.button("Generate"):
    if txt.strip() == "":
        st.warning("Please enter some text to generate output.")
    else:
        # Check if API key is available
        if not os.getenv("GEMINI_API_KEY"):
            st.error("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
        else:
            try:
                prompt = f"Please generate a {outpt} of the following text in {lang}:\n\n{txt}"
                
                # Initialize Gemini model
                model = genai.GenerativeModel('gemini-pro')
                
                # Generate content
                response = model.generate_content(prompt)
                
                st.session_state.result = response.text
                st.subheader("Output:")
                st.subheader("Try clicking the speaker as given above")
                st.write(st.session_state.result)
            except Exception as e:
                st.error(f"Error generating output: {str(e)}")

if st.button("🔊 Listen") and st.session_state.result != "":
    st.session_state.sp_state = True

if st.session_state.sp_state:
    speech = st.selectbox("Choose speech language:", list(lang_codes.keys()), key="speech_lang")
    try:
        tts = gTTS(text=st.session_state.result, lang=lang_codes[speech])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            st.audio(tmp.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")
