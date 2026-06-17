import requests
import streamlit as st

FASTAPI_URL = "https://svcore-ai-translation-api.onrender.com"

st.set_page_config(
    page_title="Multilingual Translator",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Hindi Multilingual Translator")
st.write("Translate Hindi text into English, Tamil and Bengali.")

# Session state
if "translations" not in st.session_state:
    st.session_state.translations = {
        "english": "",
        "tamil": "",
        "bengali": ""
    }


# Input box
hindi_text = st.text_area(
    "Enter Hindi text here:",
    height=180,
    placeholder="Type something in Hindi..."
)

# Buttons row
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    translate_button = st.button("🚀 Translate")

with col2:
    clear_button = st.button("🗑️ Clear")

with col3:
    st.write(f"Characters: {len(hindi_text)}")


# Translate
if translate_button:

    if not hindi_text.strip():
        st.warning("Please enter some Hindi text.")
    else:
        with st.spinner("Translating..."):
            try:
                response = requests.post(
                    f"{FASTAPI_URL}/translate",
                    json={"text": hindi_text},
                    timeout=60
                )

                response.raise_for_status()

                st.session_state.translations = response.json()

            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {e}")


# Clear
if clear_button:
    st.session_state.translations = {
        "english": "",
        "tamil": "",
        "bengali": ""
    }
    st.rerun()


# Output section
st.divider()
st.subheader("Translations")

col_en, col_ta, col_bn = st.columns(3)

with col_en:
    st.markdown("### 🇬🇧 English")
    st.text_area(
        "English Output",
        value=st.session_state.translations.get("english", ""),
        height=150,
        disabled=True,
        label_visibility="collapsed"
    )

with col_ta:
    st.markdown("### 🇮🇳 Tamil")
    st.text_area(
        "Tamil Output",
        value=st.session_state.translations.get("tamil", ""),
        height=150,
        disabled=True,
        label_visibility="collapsed"
    )

with col_bn:
    st.markdown("### 🇧🇩 Bengali")
    st.text_area(
        "Bengali Output",
        value=st.session_state.translations.get("bengali", ""),
        height=150,
        disabled=True,
        label_visibility="collapsed"
    )
