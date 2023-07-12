import streamlit as st
from gtts import gTTS
import io
import base64

def synthesize_text(text, language="en"):
    speech = gTTS(text=text, lang=language)
    audio_data = io.BytesIO()
    speech.save(audio_data)
    audio_data.seek(0)
    return audio_data

def save_audio_file(audio_file, file_name):
    with open(file_name, "wb") as file:
        file.write(audio_file.read())

def main():
    st.title("Text-to-Speech App")

    st.header("Upload a .txt File")
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

    if uploaded_file is not None and uploaded_file:
        text = uploaded_file.read().decode("utf-8")

        st.header("Text Preview")
        st.text(text)

        st.header("Speech Synthesis")
        language = st.selectbox("Select Language", ["en", "es", "fr", "de"])
        if st.button("Synthesize Speech"):
            audio_file = synthesize_text(text, language)

            # Save the audio file
            save_audio_file(audio_file, "output.mp3")

            st.header("Download")
            st.markdown(get_binary_file_downloader_html("output.mp3", file_label='Download Audio', file_name='output.mp3'), unsafe_allow_html=True)

            st.info("Click the 'Download Audio' link to download the synthesized speech as an MP3 file.")
    elif uploaded_file is not None and not uploaded_file:
        st.warning("Please select a valid .txt file.")

def get_binary_file_downloader_html(file_path, file_label='File', file_name='output.bin'):
    with open(file_path, "rb") as file:
        data = file.read()

    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">{file_label}</a>'
    return href

if __name__ == "__main__":
    main()
