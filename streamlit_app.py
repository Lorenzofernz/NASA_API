import streamlit as st
import requests
import json


st.title("NASA API")
st.header("Learning Streamlit")

nasa_api = open("nasa_api.json")
nasa_api = json.load(nasa_api) # dictionary
api_key = nasa_api["api_key"] # string

apod_url = "https://api.nasa.gov/planetary/apod?api_key="+api_key

response = requests.get(apod_url).json()

st.subheader("Astronomy Picture of the Day: "+response["title"])
st.text("Today is "+response["date"])

st.image(response["url"],
         # caption="Image credit: "+response["copyright"],
         width=360)

explanation=st.checkbox("Click here for an explanation")
if explanation:
    st.write(response["explanation"])

st.subheader("Mars Rover Photos")

mars_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&api_key="+api_key
response2 = requests.get(mars_url).json()

# st.write(response2) # temporarily

cameraChoice = st.selectbox("Please select a camera:",
                            options=["",
                                     "Front Hazard Avoidance Camera",
                                     "Rear Hazard Avoidance Camera",
                                     "Mast Camera",
                                     "Chemistry and Camera Complex",
                                     "Navigation Camera"])

if cameraChoice:
    for i in response2["photos"]:
        if i["camera"]["full_name"]==cameraChoice:
            st.image(i["img_src"],width=360)