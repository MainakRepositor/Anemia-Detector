"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Anaemia Detector")

    # Add image to the home page
    st.image("./images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
    A condition in which the blood doesn't have enough healthy red blood cells.
Anaemia results from a lack of red blood cells or dysfunctional red blood cells in the body. This leads to reduced oxygen flow to the body's organs.
Symptoms may include fatigue, skin pallor, shortness of breath, light-headedness, dizziness or a fast heartbeat.Treatment depends on the underlying diagnosis. Iron supplements can be used for iron deficiency. Vitamin B supplements may be used for low vitamin levels. Blood transfusions can be used for blood loss. Medication to induce blood formation may be used if the body’s blood production is reduced.
    """, unsafe_allow_html=True)