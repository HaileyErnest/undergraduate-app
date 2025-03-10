import streamlit as st

st.title("Project - Creat Shiny App")
link= "Click on this link to view [link](https://haileyerneststatistician.shinyapps.io/obesity/)"
st.markdown(link,unsafe_allow_html=True)

st.subheader("Description")
st.write("This app is an extremely in depth interactive platform analyzing Obesity Rates across the United States. Details:")
st.write("""
    - Using code, the statistics are chosen by the user
    - Selection of Ethnicity, Years, and Percentage intervals affect the graphics
    - A density graph of the United states changes colors of states by the criteria
    - A time-series graph of the top 3 and bottom 3 states changes by specified criteria
         """)
st.write("This analysis is a very eye-opening topic about the health of people in the United States and taking further action is apparent through interacting with ethnicities and years from the data set.")