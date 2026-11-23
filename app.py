from PIL import Image, ImageOps, ImageFilter
import streamlit as st

st.set_page_config(
    page_title="MedScan",
    page_icon="🩺"
)

st.title("🩺 MedScan")
st.subheader("Prescription & Lab Report Digitizer")

st.write(
    "Welcome! This application will help digitize "
    "medical documents using OCR and AI."
)

st.info(
    "Day 1: Project setup completed. "
    "Document scanning will be added next."
)