import streamlit as st

st.title("Data Science Senior Project with NASA")
with open("assets/NasaMid-ProjectReport.pdf", "rb") as f:
    st.download_button(
        label="Click here to view/download the report",
        data=f,
        file_name="report.pdf",
        mime="application/pdf"
    )

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