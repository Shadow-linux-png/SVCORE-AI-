import requests
import streamlit as st

FASTAPI_URL = "https://svcore-ai-translation-api.onrender.com/docs"

st.set_page_config(page_title="Multilingual Translator", layout="wide")

st.title("Hindi Translation App")


# --- Character Counter ---
def character_counter(text):
    return len(text)


# --- Input Area ---
hindi_text = st.text_area(
    "Enter Hindi text here:", height=150, help="Type or paste your Hindi text below."
)

col1, col2, col3 = st.columns(3)
with col1:
    translate_button = st.button("Translate")
with col2:
    clear_button = st.button("Clear")
with col3:
    char_count = character_counter(hindi_text)
    st.write(f"Characters: {char_count}")

# --- Output Area ---
st.subheader("Translations")

# Initialize session state for output cards
if "translations" not in st.session_state:
    st.session_state.translations = {"english": "", "tamil": "", "bengali": ""}

# --- Translation Logic ---
if translate_button and hindi_text:
    with st.spinner("Translating..."):
        try:
            response = requests.post(
                f"{FASTAPI_URL}/translate", json={"text": hindi_text}
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            st.session_state.translations = response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error during translation: {e}")
            st.session_state.translations = {
                "english": "Error",
                "tamil": "Error",
                "bengali": "Error",
            }
elif clear_button:
    hindi_text = ""  # Clear the input text
    st.session_state.translations = {"english": "", "tamil": "", "bengali": ""}
    st.experimental_rerun()  # Rerun to clear the display

# --- Display Translations ---
col_en, col_ta, col_bn = st.columns(3)

with col_en:
    st.card("English", styles={"card": {"background-color": "#f0f0f0"}})
    st.write(st.session_state.translations.get("english", ""))

with col_ta:
    st.card("Tamil", styles={"card": {"background-color": "#f0f0f0"}})
    st.write(st.session_state.translations.get("tamil", ""))

with col_bn:
    st.card("Bengali", styles={"card": {"background-color": "#f0f0f0"}})
    st.write(st.session_state.translations.get("bengali", ""))
