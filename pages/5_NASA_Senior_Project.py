import streamlit as st
from PIL import Image
import base64

st.title("Data Science Senior Project with NASA")

pdf_path = "assets/NasaMid-ProjectReport.pdf"

with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

st.download_button(
    label="Download the report",
    data=pdf_bytes,
    file_name="NasaMid-ProjectReport.pdf",
    mime="application/pdf"
)

st.markdown("### View Report")
pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
pdf_display = f"""
<iframe
    src="data:application/pdf;base64,{pdf_base64}"
    width="100%"
    height="800"
    type="application/pdf">
</iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)


st.subheader("Description")
st.write("""
This project analyzes acoustic sensor data to identify early-stage boiling patterns in cryogenic fuel systems for space applications.

Key features:
- Feature engineering of time and frequency-domain signals from accelerometer data
- Application of unsupervised machine learning to detect distinct boiling behaviors
- Use of dimensionality reduction and clustering to uncover meaningful patterns
- Visualization of signal groupings to support interpretability

This work demonstrates how data-driven methods can improve early detection of critical system behaviors, supporting more reliable and efficient space operations.
""")

image1 = Image.open("plot21.png")
st.image(image1, caption="NASA project visualization 1", use_container_width=True)

image2 = Image.open("plot22.png")
st.image(image2, caption="NASA project visualization 2", use_container_width=True)