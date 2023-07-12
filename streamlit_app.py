import streamlit as st
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

def synthesize_text(text, language="en"):
    speech = gTTS(text=text, lang=language)
    temp_file = NamedTemporaryFile(delete=True)
    speech.save(temp_file.name)
    return temp_file.name

def main():
    st.title("Text-to-Speech App")

    st.header("Upload a .txt File")
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")

        st.header("Text Preview")
        st.text(text)

        st.header("Speech Synthesis")
        language = st.selectbox("Select Language", ["en", "es", "fr", "de"])
        if st.button("Synthesize Speech"):
            audio_file = synthesize_text(text, language)
            st.audio(audio_file, format="audio/mp3")

            st.header("Playback")
            st.audio(audio_file, format="audio/mp3", start_time=0)

            st.info("You can click the play button above to listen to the generated speech.")

if __name__ == "__main__":
    main()

