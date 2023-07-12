import streamlit as st
from gtts import gTTS
import io
import base64
import tempfile

def synthesize_text(text, language="en"):
    speech = gTTS(text=text, lang=language)
    audio_data = io.BytesIO()
    speech.save("output.mp3")
    audio_data.seek(0)
    return audio_data


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

            st.header("Download")
            temp_file = save_temp_file(audio_file, file_name='output.mp3')
            st.markdown(get_file_downloader_html(temp_file, file_label='Download Audio', file_name='output.mp3'), unsafe_allow_html=True)

            st.info("Click the 'Download Audio' link to download the synthesized speech as an MP3 file.")
    elif uploaded_file is not None and not uploaded_file:
        st.warning("Please select a valid .txt file.")

def save_temp_file(bin_file, file_name):
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = temp_dir.name + '/' + file_name
    with open(temp_file_path, 'wb') as f:
        f.write(bin_file.read())
    return temp_file_path

def get_file_downloader_html(file_path, file_label='File', file_name='output.bin'):
    href = f'<a href="data:file/txt;base64,{base64.b64encode(file_path.encode()).decode()}" download="{file_name}">{file_label}</a>'
    return href

if __name__ == "__main__":
    main()
