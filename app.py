import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import pytesseract

st.set_page_config(
    page_title="MedScan",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MedScan")
st.subheader("Prescription & Lab Report Digitizer")

st.write("Upload a medical document to extract its text.")

st.warning(
    "Educational prototype only. Extracted medical information "
    "may be incorrect. Verify it with a qualified healthcare "
    "professional. Do not use it to make treatment decisions."
)

document_type = st.radio(
    "Select document type",
    ["Prescription", "Lab Report"],
    horizontal=True
)

uploaded_file = st.file_uploader(
    "Upload your document image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        image = ImageOps.exif_transpose(image).convert("RGB")

        st.success("Image uploaded successfully!")

        st.subheader("Uploaded Document")
        st.image(image, caption=document_type, width=500)

        st.write(
            "**Image dimensions:**",
            f"{image.width} × {image.height} pixels"
        )

        if st.button("Extract Text"):
            with st.spinner("Reading text from your document..."):
                try:
                    processed_image = ImageOps.grayscale(image)
                    processed_image = ImageOps.autocontrast(
                        processed_image
                    )
                    processed_image = processed_image.filter(
                        ImageFilter.SHARPEN
                    )

                    extracted_text = pytesseract.image_to_string(
                        processed_image,
                        lang="eng"
                    )

                    st.session_state["extracted_text"] = extracted_text
                    st.session_state["last_document"] = uploaded_file.name

                except Exception as error:
                    st.error(
                        "Text extraction failed. Check that Tesseract "
                        "is installed correctly."
                    )
                    st.caption(str(error))

        if (
            st.session_state.get("last_document") == uploaded_file.name
            and "extracted_text" in st.session_state
        ):
            st.subheader("Extracted Text")
            st.caption(
                "Review and correct this text manually. OCR can "
                "misread medicine names, doses, and lab values."
            )

            st.text_area(
                "You can edit the extracted text below",
                key="extracted_text",
                height=250
            )

            st.info(
                "This version extracts text only. It does not verify "
                "medicines, dosages, or lab results."
            )

            if not st.session_state["extracted_text"].strip():
                st.warning(
                    "No text was detected. Try a clearer, well-lit "
                    "image with larger, readable text."
                )

    except Exception:
        st.error(
            "Unable to open this image. Please upload a valid PNG or JPEG."
        )
else:
    st.info("No document uploaded yet. Choose an image above.")