import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider , selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days= st.slider("Forecast Days", min_value= 1, max_value= 5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place :
    # Get the temperature/sky data
    filtered_data= get_data(place, days)

    if option =="Temperature":
        temperatures = [entry["main"]["temp"] for entry in filtered_data]
        dates = [entry["dt_txt"] for entry in filtered_data]
        # Plot the data in the site
        figure = px.line(x=dates, y=temperatures, labels= {"x":"Date", "y":"temperature (C)"})
        st.plotly_chart(figure)

    if option=="Sky":
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        images=  {"Clear": "images/clear.png","Clouds": "images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
        image_paths = [images[condition] for condition in sky_condition]
        st.image(image_paths, width=115)