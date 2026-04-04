import streamlit as st
from PIL import Image
import base64

st.title("Data Science Senior Project with NASA")

pdf_path = "assets/NasaTeamDocument.pdf"
with open(pdf_path, "rb") as f:
    pdf_data = f.read()

st.download_button(
    label="Download Full Report",
    data=pdf_data,
    file_name="NasaTeamDocument.pdf",
    mime="application/pdf"
)

image1 = Image.open("plot21.png")
st.image(image1, caption="NASA project visualization 1", use_container_width=True)

image2 = Image.open("plot22.png")
st.image(image2, caption="NASA project visualization 2", use_container_width=True)

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

pages = [
    "assets/nasa_page1.png",
    "assets/nasa_page2.png",
    "assets/nasa_page3.png",
    "assets/nasa_page4.png",
    "assets/nasa_page5.png",
    "assets/nasa_page6.png",
    "assets/nasa_page7.png",
    "assets/nasa_page8.png",
]

if "page_num" not in st.session_state:
    st.session_state.page_num = 0

st.markdown("### Report Preview")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("Previous") and st.session_state.page_num > 0:
        st.session_state.page_num -= 1

with col3:
    if st.button("Next") and st.session_state.page_num < len(pages) - 1:
        st.session_state.page_num += 1

st.write(f"Page {st.session_state.page_num + 1} of {len(pages)}")

image = Image.open(pages[st.session_state.page_num])
st.image(image, use_container_width=True)