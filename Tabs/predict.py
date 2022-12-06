"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Anaemia.
            </p>
        """, unsafe_allow_html=True)

   
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Gender", int(df["Sex"].min()), int(df["Sex"].max()))
    B = st.slider("Red Pixels", int(df["Red_pixel"].min()), int(df["Red_pixel"].max()))
    C = st.slider("Green Pixels", int(df["Green_pixel"].min()), int(df["Green_pixel"].max()))
    D = st.slider("Blue Pixels", int(df["Blue_pixel"].min()), int(df["Blue_pixel"].max()))
    E = st.slider("Haemoglobin", int(df["Hb"].min()), int(df["Hb"].max()))
    
    # Create a list to store all the features
    features = [A,B,C,D,E]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to experience Anaemia!!")
        else:
            st.success("The person has relatively less chances of Anaemia")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
