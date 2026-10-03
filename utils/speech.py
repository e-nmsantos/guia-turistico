"""
Audio and Pronunciation Engine using gTTS and Streamlit Audio Player
Provides offline cached natural text-to-speech in Portuguese, English, and Spanish
"""

import os
import hashlib
import streamlit as st
from gtts import gTTS
import base64

# Cache directory for audio files
AUDIO_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "audio_cache")
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

LANG_MAP = {
    "pt": "pt",
    "pt-pt": "pt",
    "pt-br": "pt",
    "en": "en",
    "en-gb": "co.uk",
    "en-us": "com",
    "es": "es",
    "es-es": "es"
}

def get_audio_file(text: str, lang: str = "en") -> str:
    """
    Generates and caches an MP3 audio file for a given text and language.
    Returns the absolute path to the MP3 file.
    """
    cleaned_text = text.strip()
    if not cleaned_text:
        return ""
        
    tld = "co.uk" if lang.lower().startswith("en") else "com"
    gtts_lang = "pt" if lang.lower().startswith("pt") else ("es" if lang.lower().startswith("es") else "en")
    
    # Hash for caching
    cache_key = hashlib.md5(f"{cleaned_text}_{gtts_lang}_{tld}".encode("utf-8")).hexdigest()
    file_path = os.path.join(AUDIO_CACHE_DIR, f"{cache_key}.mp3")
    
    if not os.path.exists(file_path):
        try:
            tts = gTTS(text=cleaned_text, lang=gtts_lang, tld=tld, slow=False)
            tts.save(file_path)
        except Exception as e:
            # If offline or network issue, fallback
            return ""
            
    return file_path

def play_audio_button(text: str, lang: str = "en", label: str = "🔊 Ouvir Pronúncia", key: str = None):
    """
    Renders an audio player in Streamlit with generated audio.
    """
    clean_key = key if key else f"aud_{hash(text + lang) % 1000000}"
    audio_path = get_audio_file(text, lang)
    
    if audio_path and os.path.exists(audio_path):
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        # Fallback to interactive Web Speech JS button
        render_web_speech_button(text, lang, label)

def render_web_speech_button(text: str, lang: str = "en", label: str = "🔊 Ouvir"):
    """
    Fallback interactive HTML5 speech synthesis button via Streamlit components
    """
    lang_code = "pt-PT" if lang.lower().startswith("pt") else ("es-ES" if lang.lower().startswith("es") else "en-GB")
    safe_text = text.replace('"', '\\"').replace("'", "\\'").replace("\n", " ")
    
    html_code = f"""
    <div style="margin: 4px 0;">
        <button onclick="window.speechSynthesis.cancel(); var u = new SpeechSynthesisUtterance('{safe_text}'); u.lang = '{lang_code}'; window.speechSynthesis.speak(u);" 
                style="background: #1e3a8a; color: white; border: none; padding: 6px 12px; border-radius: 6px; font-weight: 600; cursor: pointer;">
            {label}
        </button>
    </div>
    """
    import streamlit.components.v1 as components
    components.html(html_code, height=45)
