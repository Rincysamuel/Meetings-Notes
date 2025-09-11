import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process-audio/"

st.set_page_config(page_title="Meeting Notes Extractor", layout="wide")
st.title("📋 Meeting Notes & Action Item Extractor")

uploaded_file = st.file_uploader("Upload Meeting Audio", type=["mp3", "wav"])

if uploaded_file:
    with st.spinner("Processing audio..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files={"file": (uploaded_file.name, uploaded_file, "audio/mpeg")})
        if response.status_code == 200:
            data = response.json()
            st.subheader("Transcript")
            st.text_area("Transcript", data['transcript'], height=200)

            st.subheader("Summary")
            st.write(data['summary'])

            st.subheader("Action Items")
            if data['action_items']:
                for idx, item in enumerate(data['action_items'], 1):
                    st.write(f"✅ {idx}. {item}")
            else:
                st.write("No action items found.")
        else:
            st.error("Error processing audio.")
