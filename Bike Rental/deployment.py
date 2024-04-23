import streamlit as st
import pandas as pd
import pickle

# Load the model from the pickle file
with open('bike_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_count(input_data):
    # Function to take input data and return the prediction
    prediction = model.predict([input_data])
    return prediction[0]

# Streamlit application interface
st.title('Bike Rental Prediction')

# Input fields
season = st.selectbox('Season', options=[0, 1, 2, 3], format_func=lambda x: ['Winter', 'Spring', 'Summer', 'Fall'][x])
year = st.selectbox('Year', options=[0, 1], format_func=lambda x: ['2011', '2012'][x])
month = st.selectbox('Month', options=list(range(1, 13)))
hour = st.selectbox('Hour', options=list(range(0, 24)))
holiday = st.selectbox('Holiday', options=[0, 1], format_func=lambda x: ['No', 'Yes'][x])
weekday = st.selectbox('Weekday', options=list(range(0, 7)))
workingday = st.selectbox('Working Day', options=[0, 1], format_func=lambda x: ['No', 'Yes'][x])
weather = st.selectbox('Weather', options=[0, 1, 2, 3], format_func=lambda x: ['Clear', 'Mist', 'Light Snow', 'Heavy Rain'][x])
temp = st.text_input('Temperature', value="0.00")
temp_feel = st.text_input('Temperature Feeling', value="0.0000")
humidity = st.text_input('Humidity', value="0.000")
windspeed = st.text_input('Wind Speed', value="0.0000")
casual = st.number_input('Casual Users', min_value=0)
registered = st.number_input('Registered Users', min_value=0)

# Predict button
if st.button('Predict Bike Rentals'):
    # Collecting all the input data into a list
    input_data = [
        int(season), int(year), int(month), int(hour), int(holiday),
        int(weekday), int(workingday), int(weather), float(temp),
        float(temp_feel), float(humidity), float(windspeed), int(casual), int(registered)
    ]
    
    # Getting the prediction
    prediction = predict_count(input_data)
    
    # Display the prediction
    st.success(f'Estimated Bike Rentals: {int(prediction)}')

# To run the Streamlit app, save this script and run it from your terminal:
# streamlit run app.py
