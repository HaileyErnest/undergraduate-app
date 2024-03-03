
from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume2024.pdf"
profile_pic = current_dir / "assets" / "profile_picture.png"

PAGE_TITLE = "Hailey Ernest's Portfolio"
PAGE_ICON = ":wave:"
NAME = "Hailey Ernest"
DESCRIPTION = """
Data Scientist
"""
EMAIL = "hailey.ernest@icloud.com"

# st.set_page_config(
#     page_title="Hailey Ernest\'s Portfolio",
#     layout="wide",
#     page_icon="👨‍🔬"
# )

# st.title("Hailey Ernest\'s Portfolio")

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

st.sidebar.success("Select a demo above.")

st.header('Background')
st.subheader('About me')
st.write(
    """
- Education: Cal Poly University - B.S. Statistics, Data Science
- Location: Woodinville, Washington
- Languages: English, Hebrew, French
"""
)

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)