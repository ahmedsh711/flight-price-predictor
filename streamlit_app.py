import streamlit as st
from datetime import date
import sys
sys.path.append('.')
from src.inference import predict_price

st.title('Flight Price Predictor')

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox('Airline', ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 
                                       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])
    
    source = st.selectbox('Source', ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    
    destination = st.selectbox('Destination', ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 
                                                'Delhi', 'Hyderabad'])
    
    journey_date = st.date_input('Journey Date', min_value=date.today())

with col2:
    total_stops = st.selectbox('Total Stops', [0, 1, 2, 3, 4])
    
    dep_time = st.time_input('Departure Time')
    
    duration = st.text_input('Duration (e.g., 2h 50m)', '2h 50m')

if st.button('Predict Price'):
    try:
        input_data = {
            'Airline': airline,
            'Date_of_Journey': journey_date.strftime('%d/%m/%Y'),
            'Source': source,
            'Destination': destination,
            'Total_Stops': total_stops,
            'Dep_Time': dep_time.strftime('%H:%M'),
            'Duration': duration
        }
        
        predicted_price = predict_price(input_data)
        
        st.success(f'Predicted Price: {predicted_price:,.2f}')
        
    except Exception as e:
        st.error(f'Error: {str(e)}')