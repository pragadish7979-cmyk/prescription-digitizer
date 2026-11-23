import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(
    page_title="MedScan",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MedScan")
st.subheader("Prescription & Lab Report Digitizer")

st.write(
    "Upload a medical document to begin digitization."
)

st.warning(
    "Educational prototype only. Always verify medical "
    "information with a qualified healthcare professional."
)

# Select the type of document
document_type = st.radio(
    "Select document type",
    ["Prescription", "Lab Report"],
    horizontal=True
)

# Upload an image
uploaded_file = st.file_uploader(
    "Upload your document image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    try:
        # Read and correct image orientation
        image = Image.open(uploaded_file)
        image = ImageOps.exif_transpose(image).convert("RGB")

        st.success("Image uploaded successfully!")

        # Display the document
        st.subheader("Uploaded Document")

        st.image(
            image,
            caption=f"Document type: {document_type}",
            width=500
        )

        # Display basic file information
        st.subheader("File Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Document type:**", document_type)

        with col2:
            st.write(
                "**Image dimensions:**",
                f"{image.width} × {image.height} pixels"
            )

        # Placeholder for the next development stage
        st.info(
            "Upload complete! Text extraction will be added "
            "in a future development step."
        )

    except Exception:
        st.error(
            "Unable to open this image. Please upload a valid "
            "PNG or JPEG image."
        )

else:
    st.info("No document uploaded yet. Choose an image above.")