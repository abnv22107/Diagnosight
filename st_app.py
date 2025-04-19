import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
from api_key import api_key  # Your existing import

# Configure Gemini
genai.configure(api_key=api_key)

# Convert image to byte data
def get_image_bytes(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    return image_bytes.getvalue()

# Generate report using Gemini
def generate_report(image_bytes):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")  # Corrected model name
    
    response = model.generate_content(
        [
            "You are a medical imaging specialist. Analyze this medical image and provide a professional diagnostic report "
            "including observations, potential findings, and clinical recommendations if any abnormalities are detected.",
            {"mime_type": "image/png", "data": image_bytes}  # Properly structured image data
        ],
        stream=True
    )

    response.resolve()  # Important to handle potential errors
    return response.text

# Streamlit UI
st.set_page_config(page_title="Medical Image Report Generator", page_icon="🩺")
st.title("🩺 Medical Image Analysis Report Generator")
st.write("Upload a medical image (X-ray, MRI, CT scan, etc.) to generate a diagnostic report.")

upload_file = st.file_uploader("Upload Medical Image", type=["png", "jpg", "jpeg"])

if upload_file is not None:
    st.image(upload_file, caption="Uploaded Medical Image", use_container_width=True)
    st.write("")  # Spacer

if st.button("Generate Report", type="primary"):
    if upload_file is not None:
        with st.spinner("Analyzing image and generating report..."):
            try:
                image_bytes = get_image_bytes(upload_file)
                report = generate_report(image_bytes)
                
                st.success("Analysis Complete!")
                st.subheader("📝 Diagnostic Report")
                st.markdown(report)  # Using markdown for better formatting
                
                # Add download button for the report
                st.download_button(
                    label="Download Report",
                    data=report,
                    file_name="medical_report.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try again with a clearer image or check your API key permissions.")
    else:
        st.warning("Please upload a medical image first.")