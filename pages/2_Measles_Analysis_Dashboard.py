import streamlit as st
from PIL import Image

st.title("Dashboard - Measles Analysis")
link= "Click on this link to view [link](https://019e572c-1ca9-4706-e827-a598ce59bd01.share.connect.posit.cloud/)"
st.markdown(link,unsafe_allow_html=True)

st.subheader("Description")

st.write("This dashboard is an interactive data visualization platform analyzing worldwide measles cases and their relationship with GDP per capita across countries and regions.")

st.write("""
- Built using **R, Shiny, and Quarto Dashboard**
- Uses WHO measles data and World Bank GDP data
- Interactive maps, graphs, and tables update based on user selections
- Leaflet maps display worldwide measles and GDP patterns
- Plotly and ggplot visualizations show trends over time
- Focuses on how economic conditions may relate to measles outbreaks globally
- Includes a case study on Ethiopia’s increase in measles cases and temperature patterns
""")

st.write("This analysis helps users better understand global public health trends, economic inequality, and disease outbreaks through interactive visualizations and data exploration.")

image1 = Image.open("plot25.png")
st.image(image1, caption="Interactive Dashboard Preview", use_column_width=True)