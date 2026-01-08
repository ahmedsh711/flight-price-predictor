import pandas as pd
import joblib
import os


from src.data_pipeline import clean_data, engineer_features

def load_model():
    # Use join to avoid path issues on different Windows/Linux setups
    model = joblib.load(os.path.join('models', 'flight_price_model.pkl'))
    metadata = joblib.load(os.path.join('models', 'metadata.pkl'))
    return model, metadata

def prepare_input(data_dict, metadata):
    # Convert dictionary to DataFrame
    df = pd.DataFrame([data_dict])
    
    df = clean_data(df)
    df = engineer_features(df)
    
    # Apply the saved metadata for route features
    df['Airline'] = df['Airline'].replace(metadata['rare_airlines'], 'Others')
    df['Route_Frequency'] = df.apply(lambda row: metadata['route_counts'].get((row['Source'], row['Destination']), 0), axis=1)
    df['Route_Competition'] = df.apply(lambda row: metadata['route_competition'].get((row['Source'], row['Destination']), 1), axis=1)
    df['Airline_Route_Dominance'] = df.apply(lambda row: metadata['airline_route_freq'].get((row['Airline'], row['Source'], row['Destination']), 0), axis=1)
    
    # Ensure columns match what the model expects
    return df

def predict_price(data_dict):
    model, metadata = load_model()
    input_df = prepare_input(data_dict, metadata)
    prediction = model.predict(input_df)[0]
    return prediction