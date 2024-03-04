import subprocess
import streamlit as st
from PIL import Image

st.title("Project - Open Ended Analysis")
st.title("Investigating National Parks")

st.subheader('Data')
with st.expander('See code'):
  code1 = '''
# Load packages and import data
library(tidyverse)
library(dplyr)
library(ggplot2)
library(purrr)
national_park <- read.csv("national_park_trails.csv")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "data2.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)
st.write("The dataset analyzed is the collection of all of the national parks in the United States, including the state in which each park is located, the date when it was established, its total area, the number of recreation visitors it receives each year, and a description of its key features.")

st.subheader('Start Exploration')
st.write("What is the length in miles of the fourth longest trail in California?")
with st.expander('See code'):
  code2 = '''
national_park|>
  filter(state_name == "California")|>
  mutate(length_mi = length*0.000621371) |>
  slice_max(n = 4, order_by = length_mi)|>
  slice(4)|>
  select(name, length_mi)
  '''
  st.code(code2, language='R')
process2 = subprocess.Popen(["Rscript", "parks1.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process1.communicate()
image1 = Image.open('plot11.png')
st.image(image1)

st.write("Consider an “easy” trail to be one that has an elevation gain of less than 500 meters, a distance of less than 5 kilometers, and a difficulty rating below 4.")
st.write("Which California National Park has most “easy” trails?")
with st.expander('See code'):
  code3 = '''
national_park|>
  mutate(length_km = length*0.001)|>
  filter(elevation_gain < 500, difficulty_rating < 4, length_km < 5)|>
  group_by(area_name)|>
  summarise(easy_trail_num = n())|>
  slice_max(n=1, order_by = easy_trail_num)
  '''
  st.code(code3, language='R')
process3 = subprocess.Popen(["Rscript", "parks2.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process1.communicate()
image2 = Image.open('plot12.png')
st.image(image2)

st.write("How many National Parks contain the word “Mountain” somewhere in their name?")
st.write("(If it is an abbreviation, like “Mount” or “Mt”, that counts too.)")
with st.expander('See code'):
  code4 = '''
national_park|>
  filter(str_detect(area_name, "Mount|Mt|Mountain"))|>
  count()
  '''
  st.code(code4, language='R')
process4 = subprocess.Popen(["Rscript", "parks3.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result4 = process1.communicate()
image3 = Image.open('plot13.png')
st.image(image3)

st.write("Write code to create the np_trails_new object to follow specific criteria.")
with st.expander('See code'):
  code5 = '''
np_trails_new <- national_park |>
  pivot_longer(
    cols = c(avg_rating, difficulty_rating, popularity, visitor_usage),
    names_to = "measure",
    values_to = "score")

np_trails_new %>%
  ggplot(aes(x=score)) +
  geom_density() +
  facet_wrap(~ measure, scales = 'free') +
  ggtitle("Overall distribution of various trail scores in National parks")
  '''
  st.code(code5, language='R')
process5 = subprocess.Popen(["Rscript", "parks4.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result5 = process1.communicate()
image4 = Image.open('plot14.png')
st.image(image4)

st.subheader('Write a functions to help recommend trails to a user')
st.write("""
The function will have as its input the dataset and the name of a National Park, and the following optional arguments:

    - A minimum trail elevation gain (in meters)
    - A maximum trail elevation gain (in meters)
    - A minimum trail rating
    - The type of trail
""")
with st.expander('See code'):
  code6 = '''
#Returns all the trails that fit the supplied criteria
recommend_trails <- function(data, park_name, min_elev = 0, max_elev = Inf, min_rating = 0, trl_type = NULL){

  stopifnot(is.data.frame(data),
            is.numeric(min_elev),
            is.numeric(max_elev),
            is.numeric(min_rating))
  
  recommended_trails <- data |>
    filter(area_name == park_name,
           elevation_gain >= min_elev,
           elevation_gain <= max_elev,
           avg_rating >= min_rating)

  if (!missing(trl_type)) {
    recommended_trails <- recommended_trails |>
      filter(route_type %in% trl_type)
  }
  
  recommended_trails <- recommended_trails |>
    select(name)
  
  return(recommended_trails)
}
  '''
  st.code(code6, language='R')
process6 = subprocess.Popen(["Rscript", "parks5.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result6 = process1.communicate()

st.write("Test the function with the code below")
with st.expander('See code'):
  code7 = '''
national_park |> 
  recommend_trails("Haleakala National Park", 
                   min_elev = 1000, 
                   min_rating = 4
                   )
  '''
  st.code(code7, language='R')
process7 = subprocess.Popen(["Rscript", "parks6.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result7 = process1.communicate()
image5 = Image.open('plot15.png')
st.image(image5)